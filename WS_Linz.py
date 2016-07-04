#!/usr/bin/python
#Erstellt von ... 24.08.2014
import os

os.environ["NLS_LANG"] = ".UTF8" 

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import cx_Oracle
import argparse
import logging

import exchange

log = logging.getLogger(__name__)
log.addHandler(logging.StreamHandler())

####Argparser#########################
parser = argparse.ArgumentParser()
parser.add_argument('usr',type=str,help='Username fuer die DB')
parser.add_argument('pwd',type=str,help='Passwort fuer die DB')
parser.add_argument('host',type=str,help='DB Host')
parser.add_argument('-v',help='Verbose Mode [Default: none]', action='store_true')
args = parser.parse_args()
######################################
if args.v:
    log.setLevel(logging.DEBUG)
    log.info("Verbose aktiviert")

####DB CONNECT########################
try:
    connection = cx_Oracle.Connection("%s/%s@%s" % (args.usr, args.pwd, args.host))
    log.info("Erfolgreich Verbunden")
except cx_Oracle.Error as e:
    log.critical(e)
    exit(-1)
except:
    log.critical("ERROR beim Verbinden!")
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
pyxb_EXCHANGE = exchange.EXCHANGE()
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

log.info("Erstelle XML Struktur...")

cur_STPL = cx_Oracle.Cursor(connection)
log.debug("Running SQL: %s", "SELECT * FROM STPL_V")
cur_STPL.execute("SELECT * FROM STPL_V")
for row_STPL in fetchdict(cur_STPL):
    log.debug("PyXB node: %s", "STPL")
    pyxb_STPL = exchange.STPLType()
    for name in columns(cur_STPL):
        log.debug(" + DB Column %s", name)
        if hasattr(pyxb_STPL, name) and row_STPL[name]:
            log.debug(" - PyXB attribute %s: %s", name, row_STPL[name])
            setattr(pyxb_STPL, name, row_STPL[name])
    cur_FACH = cx_Oracle.Cursor(connection)
    sql = "SELECT * FROM STPL_FACH_V WHERE {cond}".format(cond=conditions(keys_FACH))
    cur_FACH.execute(sql, dict((key, row_STPL[key]) for key in keys_FACH))
    for row_FACH in fetchdict(cur_FACH):
        log.debug("PyXB node: %s", "FACH")
        pyxb_FACH = exchange.FACHType()
        for name in set(columns(cur_FACH)) - keys_FACH:
            log.debug(" + DB Column %s", name)
            if hasattr(pyxb_FACH, name) and row_FACH[name]:
                log.debug(" - PyXB attribute %s: %s", name, row_FACH[name])
                setattr(pyxb_FACH, name, row_FACH[name])
        cur_GHK = cx_Oracle.Cursor(connection)
        sql = "SELECT * FROM STPL_GHK_V WHERE {cond}".format(cond=conditions(keys_GHK))
        cur_GHK.execute(sql, dict((key, row_FACH[key]) for key in keys_GHK))
        for row_GHK in fetchdict(cur_GHK):
            log.debug("PyXB node: %s", "GHK")
            pyxb_GHK = exchange.GHKType()
            for name in set(columns(cur_GHK)) - keys_GHK:
                log.debug(" + DB Column %s", name)
                if hasattr(pyxb_GHK, name) and row_GHK[name]:
                    log.debug(" - PyXB attribute %s: %s", name, row_GHK[name])
                    setattr(pyxb_GHK, name, row_GHK[name])
            pyxb_FACH.GHK.append(pyxb_GHK)
        cur_GHK.close()
        pyxb_STPL.FACH.append(pyxb_FACH)
    cur_FACH.close()
    pyxb_EXCHANGE.STPL.append(pyxb_STPL)
cur_STPL.close()

cur_LV = cx_Oracle.Cursor(connection)
cur_LV.execute("SELECT * FROM LV_V")
for row_LV in fetchdict(cur_LV):
    log.debug("PyXB node: %s", "LV")
    pyxb_LV = exchange.LVType()
    for name in columns(cur_LV):
        log.debug(" + DB Column %s", name)
        if hasattr(pyxb_LV, name) and row_LV[name]:
            log.debug(" - PyXB attribute %s: %s", name, row_LV[name])
            setattr(pyxb_LV, name, row_LV[name])
    pyxb_EXCHANGE.LV.append(pyxb_LV)
cur_LV.close()

cur_PV = cx_Oracle.Cursor(connection)
cur_PV.execute("SELECT * FROM PV_V")
for row_PV in fetchdict(cur_PV):
    log.debug("PyXB node: %s", "PV")
    pyxb_PV = exchange.PVType()
    for name in columns(cur_PV):
        log.debug(" + DB Column %s", name)
        if hasattr(pyxb_PV, name) and row_PV[name]:
            log.debug(" - PyXB attribute %s: %s", name, row_PV[name])
            setattr(pyxb_PV, name, row_PV[name])
    pyxb_EXCHANGE.PV.append(pyxb_PV)
cur_PV.close()

#######################################
connection.close()
log.info("Verbindungen geschlossen")
print pyxb_EXCHANGE.toxml('utf-8')
log.info("XML geschrieben")
