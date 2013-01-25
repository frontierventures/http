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
        shutil.rmtree(descriptionsPath)
        os.makedirs(descriptionsPath)
    except OSError:
        os.makedirs(descriptionsPath)
    quickAccess.unload(listFile, [])


###################################################
#
###################################################
def create(ticketId, description):
    print "%s%s %s%s" % (settings.color.RED, __name__, inspect.stack()[0][3], settings.color.ENDC)
    descriptions = quickAccess.load(listFile)

    timestamp = settings.timestamp()
    description = [ticketId, description, timestamp]
    descriptions.append(description)

    quickAccess.unload(listFile, descriptions)

    print '%sreturn: %s%s' % (settings.color.YELLOW, description, settings.color.ENDC)
    return description


###################################################
#
###################################################
def remove(ticketId):
    print "%s%s %s%s" % (settings.color.RED, __name__, inspect.stack()[0][3], settings.color.ENDC)
    descriptions = quickAccess.load(listFile)

    description = getByTicketId(ticketId)
    descriptions.remove(description)

    quickAccess.unload(listFile, descriptions)

    print '%sreturn: %s%s' % (settings.color.YELLOW, description, settings.color.ENDC)
    return description


###################################################
#
###################################################
def getAll():
    print "%s%s %s%s" % (settings.color.RED, __name__, inspect.stack()[0][3], settings.color.ENDC)
    descriptions = quickAccess.load(listFile)

    print '%sreturn: %s%s' % (settings.color.YELLOW, descriptions, settings.color.ENDC)
    return descriptions


###################################################
#
###################################################
def getByTicketId(ticketId):
    print "%s%s %s%s" % (settings.color.RED, __name__, inspect.stack()[0][3], settings.color.ENDC)
    descriptions = quickAccess.load(listFile)

    descriptions = [x for x in descriptions if x[0] == ticketId]
    description = []
    if descriptions:
        description = descriptions[0]

    print '%sreturn: %s%s' % (settings.color.YELLOW, description, settings.color.ENDC)
    return description

descriptionsPath = settings.app + 'descriptions'
listFile = '%s/%s' % (descriptionsPath, 'list.json')
