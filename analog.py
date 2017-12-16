#!/usr/bin/env python
#-*- coding: utf-8 -*-

#procesar el fichero auth.log y guardar la fecha en un 
#formato procesable (si el sumas un dia a la fecha te de la fecha correcta)[datetime]
#y ver si determinada ip ha intentado logearse en un determinado tiempo
#enunciado completo en analog.pdf

from datetime import datetime

fallo = 'authentication failure;'
log = open ('auth.log', 'r')
di={}
li=[]
for linea in log.readlines():
	if fallo in linea:
		cadena = linea[linea.find('rhost')+6:]
		li2=(cadena.split())
		if li2[0] in linea:
			li=[]
			cats = linea[:15]
			ts = datetime.strptime(cats, '%b %d %H:%M:%S')
			li.append(cats)
			if li2[0] not in di:
				di[li2[0]]=li
				del(li)
log.close()
print di
