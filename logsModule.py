#!/usr/bin/env python
import os
import inspect
import shutil
import quickAccess

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

    quickAccess.unload(listFile, [])


###################################################
#
###################################################
def createEntry(list):
    print "%s%s %s%s" % (settings.color.RED, __name__, inspect.stack()[0][3], settings.color.ENDC)
    entries = quickAccess.load(listFile)

    entries.append(list)

    quickAccess.unload(listFile, entries)

    print '%sreturn: %s%s' % (settings.color.YELLOW, list, settings.color.ENDC)
    return list


###################################################
#
###################################################
def getAll():
    print "%s%s %s%s" % (settings.color.RED, __name__, inspect.stack()[0][3], settings.color.ENDC)
    entries = quickAccess.load(listFile)

    entries.sort(key=lambda x: x[3], reverse=True)
#    entries.sort(key=lambda x: x[1])

    print '%sreturn: %s%s' % (settings.color.YELLOW, entries, settings.color.ENDC)
    return entries


logsPath = settings.app + 'logs'
listFile = '%s/%s' % (logsPath, 'list.json')
