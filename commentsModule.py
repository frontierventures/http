#!/usr/bin/env python
import os
import inspect
import shutil

import settings
import quickAccess


###################################################
#
###################################################
def reset():
    print "%s%s %s%s" % (settings.color.RED, __name__, inspect.stack()[0][3], settings.color.ENDC)
    try:
        shutil.rmtree(commentsPath)
        os.makedirs(commentsPath)
    except OSError:
        os.makedirs(commentsPath)

    quickAccess.unload(listFile, [])


###################################################
#
###################################################
def create(ticketId, comment):
    print "%s%s %s%s" % (settings.color.RED, __name__, inspect.stack()[0][3], settings.color.ENDC)
    comments = quickAccess.load(listFile)

    timestamp = settings.timestamp()
    comment = [ticketId, comment, timestamp]
    comments.append(comment)

    quickAccess.unload(listFile, comments)

    print '%sreturn: %s%s' % (settings.color.YELLOW, comment, settings.color.ENDC)
    return comment


###################################################
#
###################################################
def remove(ticketId):
    print "%s%s %s%s" % (settings.color.RED, __name__, inspect.stack()[0][3], settings.color.ENDC)
    comments = quickAccess.load(listFile)

    comment = getByTicketId(ticketId)
    comments.remove(comment)

    quickAccess.unload(listFile, comments)

    print '%sreturn: %s%s' % (settings.color.YELLOW, comment, settings.color.ENDC)
    return comment


###################################################
#
###################################################
def getAll():
    print "%s%s %s%s" % (settings.color.RED, __name__, inspect.stack()[0][3], settings.color.ENDC)
    comments = quickAccess.load(listFile)

    print '%sreturn: %s%s' % (settings.color.YELLOW, comments, settings.color.ENDC)
    return comments


###################################################
#
###################################################
def getByTicketId(ticketId):
    print "%s%s %s%s" % (settings.color.RED, __name__, inspect.stack()[0][3], settings.color.ENDC)
    comments = quickAccess.load(listFile)

    comments = [x for x in comments if x[0] == ticketId]
    comment = []
    if comments:
        comment = comments[0]

    print '%sreturn: %s%s' % (settings.color.YELLOW, comment, settings.color.ENDC)
    return comment

commentsPath = settings.app + 'comments'
listFile = '%s/%s' % (commentsPath, 'list.json')
