#!/usr/bin/env python
import os
import inspect
import shutil
import json

import settings


###################################################
#
###################################################
def reset():
    print "%s%s %s%s" % (settings.color.RED, __name__, inspect.stack()[0][3], settings.color.ENDC)
    try:
        shutil.rmtree(logsPath)
        os.makedirs(logsPath)
    except OSError:
        os.makedirs(logsPath)
    with open(listFile, 'w') as f:
        json.dump([], f)


###################################################
#
###################################################
def createEntry(list):
    print "%s%s %s%s" % (settings.color.RED, __name__, inspect.stack()[0][3], settings.color.ENDC)
    with open(listFile, 'r') as f:
        entries = json.load(f)

    entries.append(list)

    with open(listFile, 'w') as f:
        json.dump(entries, f)

    print '%sreturn: %s%s' % (settings.color.YELLOW, list, settings.color.ENDC)
    return list


###################################################
#
###################################################
def getAll():
    print "%s%s %s%s" % (settings.color.RED, __name__, inspect.stack()[0][3], settings.color.ENDC)
    with open(listFile, 'r') as f:
        entries = json.load(f)

    entries.sort(key=lambda x: x[3], reverse=True)
#    entries.sort(key=lambda x: x[1])

    print '%sreturn: %s%s' % (settings.color.YELLOW, entries, settings.color.ENDC)
    return entries


logsPath = settings.app + 'logs'
listFile = '%s/%s' % (logsPath, 'list.json')
