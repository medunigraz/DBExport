#!/usr/bin/python
#Erstellt von ... 24.08.2014
import sys
import lxml.etree as ET
import cx_Oracle
import argparse
import logging
####Argparser#########################
parser = argparse.ArgumentParser()
parser.add_argument('usr',type=str,help='Username fuer die DB')
parser.add_argument('pwd',type=str,help='Passwort fuer die DB')
parser.add_argument('host',type=str,help='DB Host')
parser.add_argument('-v',help='Verbose Mode [Default: none]', action='store_true')
args = parser.parse_args()
######################################
if args.v:
    logging.basicConfig(format = "%(asctime)s [%(levelname)-s] %(message)s",level = logging.DEBUG)
    logging.info("Verbose aktiviert")
else:
    logging.basicConfig(format = "%(asctime)s [%(levelname)-s] %(message)s")

####DB CONNECT########################
try:
    connection = cx_Oracle.Connection("%s/%s@%s" % (args.usr, args.pwd, args.host))
    logging.info("Erfolgreich Verbunden")
except cx_Oracle.Error as e:
    logging.critical(e)
    exit(-1)
except:
    logging.critical("ERROR beim Verbinden!")
    exit(-2)
######################################

def columns(cursor):
    return zip(*cursor.description)[0]

def fetchdict(cursor):
    names = columns(cursor)
    for row in cursor:
        yield dict(zip(names, row))

def conditions(keys):
    return " AND ".join(["{name}=:{name}".format(name=name) for name in keys])

#####XML STRUKTUR#####################
xml_ROOT = ET.Element("EXCHANGE")
######################################


########XML VERSCHACHTELN#############
keys_FACH = set((
    "SKZ_UNI",
    "SKZ_KEY",
    "SKZKEY",
    "VERSION",
    "ABSCHNITT",
    ))

keys_GHK = keys_FACH | set((
    "KENNUNG",
    ))

cur_STPL = cx_Oracle.Cursor(connection)
cur_STPL.execute("SELECT * FROM STPL_V")
logging.info("Erstelle XML Struktur...")
for row_STPL in fetchdict(cur_STPL):
    xml_STPL = ET.SubElement(xml_ROOT, "STPL")
    for name in columns(cur_STPL):
        xml_STPL.set(name, unicode(row_STPL[name]))
    cur_FACH = cx_Oracle.Cursor(connection)
    sql = "SELECT * FROM STPL_FACH_V WHERE {cond}".format(cond=conditions(keys_FACH))
    cur_FACH.execute(sql, dict((key, row_STPL[key]) for key in keys_FACH))
    for row_FACH in fetchdict(cur_FACH):
        xml_FACH = ET.SubElement(xml_STPL, "FACH")
        for name in set(columns(cur_FACH)) - keys_FACH:
            xml_FACH.set(name, unicode(row_FACH[name]))
        cur_GHK = cx_Oracle.Cursor(connection)
        sql = "SELECT * FROM STPL_GHK_V WHERE {cond}".format(cond=conditions(keys_GHK))
        cur_GHK.execute(sql, dict((key, row_FACH[key]) for key in keys_GHK))
        for row_GHK in fetchdict(cur_GHK):
            xml_GHK = ET.SubElement(xml_FACH, "GHK")
            for name in set(columns(cur_GHK)) - keys_GHK:
                xml_GHK.set(name, unicode(row_GHK[name]))
        cur_GHK.close()
    cur_FACH.close()
cur_STPL.close()

#######################################
connection.close()
logging.info("Verbindungen geschlossen")
tree = ET.ElementTree(xml_ROOT)
tree.write(sys.stdout,pretty_print=True)
logging.info("XML geschrieben")
