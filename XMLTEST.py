#!/usr/bin/python
#Erstellt von Gerhard ZEISLER 24.08.2014
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
	cursor = cx_Oracle.Cursor(connection)
	logging.info("Erfolgreich Verbunden")
except cx_Oracle.Error as e:
	logging.critical(e)
	exit(-1)
except:
	logging.critical("ERROR beim Verbinden!")
	exit(-2)
######################################


#########SQL MAGIE####################
try:
	sql = "SELECT * FROM STPL_FACH_V ORDER BY SKZ_UNI,SKZ_KEY,SKZKEY,VERSION,ABSCHNITT,KENNUNG,NAME,NAME_ENGL,SWS,CREDITS"
	cursor.execute(sql)
	inhalt_STPL_FACH_V = cursor.fetchall()
	sql = "SELECT * FROM STPL_GHK_V ORDER BY NR,SKZ_UNI,SKZ_KEY,SKZKEY,VERSION,ABSCHNITT,KENNUNG,STP_LV_NR,KURZBEZEICHNUNG,TITEL,SWS,CREDITS"
	cursor.execute(sql)
	inhalt_STPL_GHK_V = cursor.fetchall()
	sql = "SELECT * FROM STPL_V ORDER BY SKZ_UNI,SKZ_KEY,SKZKEY,SKZBEZ,VERSION,GUELTIG_AB,GUELTIG_BIS,STUDIERBAR_BIS,ABSCHNITT,SWS,SEMESTER,CREDITS"
	cursor.execute(sql)
	inhalt_STPL_V = cursor.fetchall()
	logging.info("Erfolgreich alle SQL Befehle ausgefuehrt")
except cx_Oracle.Error as e:
	logging.critical(e)
	exit(-1)
except:
	logging.critical("ERROR beim fetchen!")
	exit(-2)
	

######################################


#####XML STRUKTUR#####################
STPL = ET.Element("STPL")
######################################


########XML VERSCHACHTELN#############
logging.info("Erstelle XML Struktur...")
for liste_STPL_V in inhalt_STPL_V:
	field1 = ET.SubElement(STPL, "STPL_V")
	field1.set('SKZ_UNI',bytes(liste_STPL_V[0]))
	field1.set("SKZ_KEY",bytes(liste_STPL_V[1]))
	field1.set("SKZKEY",liste_STPL_V[2])
	field1.set("SKZBEZ",liste_STPL_V[3])
	field1.set("VERSION",bytes(liste_STPL_V[4]))
	field1.set("GUELTIG_AB",bytes(liste_STPL_V[5]))
	field1.set("GUELTIG_BIS",bytes(liste_STPL_V[6]))
	field1.set("STUDIERBAR_BIS",bytes(liste_STPL_V[7]))
	field1.set("ABSCHNITT",bytes(liste_STPL_V[8]))
	field1.set("SEMESTER",bytes(liste_STPL_V[9]))
	field1.set("SWS",bytes(liste_STPL_V[10]))
	field1.set("CREDITS",bytes(liste_STPL_V[11]))
	for liste_STPL_FACH_V in inhalt_STPL_FACH_V:
		if liste_STPL_V[0] in liste_STPL_FACH_V:
			field2 = ET.SubElement(field1, "STPL_FACH_V")
			field2.set("KENNUNG",bytes(liste_STPL_FACH_V[5]))
			field2.set("NAME",liste_STPL_FACH_V[6])
			field2.set("NAME-ENGL",liste_STPL_FACH_V[7])
			field2.set("SWS",bytes(liste_STPL_FACH_V[8]))
			field2.set("CREDITS",bytes(liste_STPL_FACH_V[9]))
			for liste_STPL_GHK_V in inhalt_STPL_GHK_V:
				if liste_STPL_FACH_V[0] in liste_STPL_GHK_V and liste_STPL_FACH_V[5] in liste_STPL_GHK_V:
					field3 = ET.SubElement(field2, "STPL_GHK_V")
					field3.set("NR",bytes(liste_STPL_GHK_V[0]))
					field3.set("KENNUNG",bytes(liste_STPL_GHK_V[6]))
					field3.set("STP_LV_NR",bytes(liste_STPL_GHK_V[7]))
					field3.set("KURZBEZEICHNUNG",liste_STPL_GHK_V[8])
					field3.set("TITEL",liste_STPL_GHK_V[9])
					field3.set("SWS",bytes(liste_STPL_GHK_V[10]))
					field3.set("CREDITS",bytes(liste_STPL_GHK_V[11]))
#######################################
cursor.close()
connection.close()
logging.info("Verbindungen geschlossen")
tree = ET.ElementTree(STPL)
tree.write("DB_expo.xml",pretty_print=True)
logging.info("XML geschrieben")
exit(0)
