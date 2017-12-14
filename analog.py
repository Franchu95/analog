#!/usr/bin/env python
#-*- coding: utf-8 -*-

#procesar el fichero auth.log y guardar la fecha en un 
#formato procesable (si el sumas un dia a la fecha te de la fecha correcta)[datetime]
#y ver si determinada ip ha intentado logearse en un determinado tiempo
#enunciado completo en analog.pdf

from datetime import datetime

fallo = 'authentication failure;'
log = open ('auth.log', 'r')
li=[]
for linea in log.readlines():
	if fallo in linea:
		cats = linea[:15]
		ts = datetime.strptime(cats, '%b %d %H:%M:%S')
		li.append(cats)
		
log.close()
print li

#pillar desde la 129 hasta la 144 
