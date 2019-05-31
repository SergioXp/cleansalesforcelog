#!/usr/bin/env python
# -*- coding: utf-8 -*-

from os import listdir, walk
from os.path import isfile, join
from datetime import datetime
import time
import re
import json

ficheros_log = []

for (path, ficheros, archivos) in walk("."):
    for archivo in archivos:
        name = join(path, archivo)
        # print (name)
        if '.log' in name and '_new_' not in name:
            ficheros_log.append(name)

for fichero_log in ficheros_log:

    num_tabs = 0

    nameFileNoExt = fichero_log[:-4]
    ts = time.time().__str__()[:-3]
    newLog = open(nameFileNoExt+'_new_'+ts+'.log', 'w')
    newLogDebug = open(nameFileNoExt+'_new_debug_'+ts+'.log', 'w')

    log = open(fichero_log, 'r')

    line = log.readline()
    while line:
        tabs = ''

        if 'CODE_UNIT_STARTED' in line:
            lineJson = re.findall(r'\{[\W\d\w]*\}', line)
            line = re.sub(r'\{[\W\d\w]*\}', '', line)
            lineClean = re.sub(r'(\d\d:\d\d:\d\d.(\d*) \(\d*\)\|)', '', line)
            for x in xrange(0, num_tabs):
                tabs += '\t'

            newLog.write(tabs + lineClean)
            if lineJson and lineJson[0] != '{}':
                try:
                    parsed = json.loads(lineJson[0])
                    newLog.write(
                        tabs + json.dumps(parsed, sort_keys=True, indent=4, separators=(',', ': ')))
                    newLog.write('\n')
                except:
                    print ('error')

        if 'METHOD_ENTRY' in line and 'SYSTEM_METHOD_ENTRY' not in line and 'System.debug(ANY)' not in line:
            lineJson = re.findall(r'\{[\W\d\w]*\}', line)
            line = re.sub(r'\{[\W\d\w]*\}', '', line)
            lineClean = re.sub(r'(\d\d:\d\d:\d\d.(\d*) \(\d*\)\|)', '', line)
            for x in xrange(0, num_tabs):
                tabs += '\t'

            newLog.write(tabs + lineClean)
            if lineJson and lineJson[0] != '{}':
                try:
                    parsed = json.loads(lineJson[0])
                    newLog.write(
                        tabs + json.dumps(parsed, sort_keys=True, indent=4, separators=(',', ': ')))
                    newLog.write('\n')
                except:
                    print ('error')
            num_tabs += 1

        if 'METHOD_EXIT' in line and 'SgitYSTEM_METHOD_EXIT' not in line and 'System.debug(ANY)' not in line:
            num_tabs -= 1
            lineJson = re.findall(r'\{[\W\d\w]*\}', line)
            line = re.sub(r'\{[\W\d\w]*\}', '', line)
            lineClean = re.sub(r'(\d\d:\d\d:\d\d.(\d*) \(\d*\)\|)', '', line)
            for x in xrange(0, num_tabs):
                tabs += '\t'

            newLog.write(tabs + lineClean)
            if lineJson and lineJson[0] != '{}':
                try:
                    parsed = json.loads(lineJson[0])
                    newLog.write(
                        tabs + json.dumps(parsed, sort_keys=True, indent=4, separators=(',', ': ')))
                    newLog.write('\n')
                except:
                    print ('error')

        if 'USER_DEBUG' in line:
            lineJson = re.findall(r'\{[\W\d\w]*\}', line)
            line = re.sub(r'\{[\W\d\w]*\}', '', line)
            lineClean = re.sub(r'(\d\d:\d\d:\d\d.(\d*) \(\d*\)\|)', '', line)
            for x in xrange(0, num_tabs):
                tabs += '\t'
            newLog.write(tabs + lineClean)
            if lineJson and lineJson[0] != '{}':
                try:
                    parsed = json.loads(lineJson[0])
                    newLog.write(
                        tabs + json.dumps(parsed, sort_keys=True, indent=4, separators=(',', ': ')))
                    newLog.write('\n')
                except:
                    print ('error')

            newLogDebug.write(lineClean)
            if lineJson and lineJson[0] != '{}':
                try:
                    parsed = json.loads(lineJson[0])
                    newLogDebug.write(
                        tabs + json.dumps(parsed, sort_keys=True, indent=4, separators=(',', ': ')))
                    newLog.write('\n')
                except:
                    print ('error')

        if 'VARIABLE_ASSIGNMENT' in line:
            lineJson = re.findall(r'\{[\W\d\w]*\}', line)
            line = re.sub(r'\{[\W\d\w]*\}', '', line)
            lineClean = re.sub(r'(\d\d:\d\d:\d\d.(\d*) \(\d*\)\|)', '', line)
            for x in xrange(0, num_tabs):
                tabs += '\t'

            newLog.write(tabs + lineClean)
            if lineJson and lineJson[0] != '{}':
                try:
                    parsed = json.loads(lineJson[0])
                    newLog.write(
                        tabs + json.dumps(parsed, sort_keys=True, indent=4, separators=(',', ': ')))
                    newLog.write('\n')
                except:
                    print ('error')

        if 'VARIABLE_SCOPE_BEGIN' in line:
            lineJson = re.findall(r'\{[\W\d\w]*\}', line)
            line = re.sub(r'\{[\W\d\w]*\}', '', line)
            lineClean = re.sub(r'(\d\d:\d\d:\d\d.(\d*) \(\d*\)\|)', '', line)
            for x in xrange(0, num_tabs):
                tabs += '\t'

            newLog.write(tabs + lineClean)
            if lineJson and lineJson[0] != '{}':
                try:
                    parsed = json.loads(lineJson[0])
                    newLog.write(
                        tabs + json.dumps(parsed, sort_keys=True, indent=4, separators=(',', ': ')))
                    newLog.write('\n')
                except:
                    print ('error')

        if 'SOQL_EXECUTE_BEGIN' in line:
            lineJson = re.findall(r'\{[\W\d\w]*\}', line)
            line = re.sub(r'\{[\W\d\w]*\}', '', line)
            lineClean = re.sub(r'(\d\d:\d\d:\d\d.(\d*) \(\d*\)\|)', '', line)
            for x in xrange(0, num_tabs):
                tabs += '\t'

            newLog.write(tabs + lineClean)
            if lineJson and lineJson[0] != '{}':
                try:
                    parsed = json.loads(lineJson[0])
                    newLog.write(
                        tabs + json.dumps(parsed, sort_keys=True, indent=4, separators=(',', ': ')))
                    newLog.write('\n')
                except:
                    print ('error')

        if 'SOQL_EXECUTE_END' in line:
            lineJson = re.findall(r'\{[\W\d\w]*\}', line)
            line = re.sub(r'\{[\W\d\w]*\}', '', line)
            lineClean = re.sub(r'(\d\d:\d\d:\d\d.(\d*) \(\d*\)\|)', '', line)
            for x in xrange(0, num_tabs):
                tabs += '\t'

            newLog.write(tabs + lineClean)
            if lineJson and lineJson[0] != '{}':
                try:
                    parsed = json.loads(lineJson[0])
                    newLog.write(
                        tabs + json.dumps(parsed, sort_keys=True, indent=4, separators=(',', ': ')))
                    newLog.write('\n')
                except:
                    print ('error')

        if 'DML_BEGIN' in line:
            lineJson = re.findall(r'\{[\W\d\w]*\}', line)
            line = re.sub(r'\{[\W\d\w]*\}', '', line)
            lineClean = re.sub(r'(\d\d:\d\d:\d\d.(\d*) \(\d*\)\|)', '', line)
            for x in xrange(0, num_tabs):
                tabs += '\t'

            newLog.write(tabs + lineClean)
            if lineJson and lineJson[0] != '{}':
                try:
                    parsed = json.loads(lineJson[0])
                    newLog.write(
                        tabs + json.dumps(parsed, sort_keys=True, indent=4, separators=(',', ': ')))
                    newLog.write('\n')
                except:
                    print ('error')

        line = log.readline()

    log.close()
    newLog.close()
    newLogDebug.close()