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
        shutil.rmtree(commentsPath)
        os.makedirs(commentsPath)
    except OSError:
        os.makedirs(commentsPath)
    with open(listFile, 'w') as f:
        json.dump([], f)


###################################################
#
###################################################
def create(ticketId, comment):
    print "%s%s %s%s" % (settings.color.RED, __name__, inspect.stack()[0][3], settings.color.ENDC)
    with open(listFile, 'r') as f:
        comments = json.load(f)

    timestamp = settings.timestamp()
    comment = [ticketId, comment, timestamp]
    comments.append(comment)

    with open(listFile, 'w') as f:
        json.dump(comments, f)

    print '%sreturn: %s%s' % (settings.color.YELLOW, comment, settings.color.ENDC)
    return comment


###################################################
#
###################################################
def remove(ticketId):
    print "%s%s %s%s" % (settings.color.RED, __name__, inspect.stack()[0][3], settings.color.ENDC)
    with open(listFile, 'r') as f:
        comments = json.load(f)

    comment = getByTicketId(ticketId)
    comments.remove(comment)

    with open(listFile, 'w') as f:
        json.dump(comments, f)

    print '%sreturn: %s%s' % (settings.color.YELLOW, comment, settings.color.ENDC)
    return comment


###################################################
#
###################################################
def getAll():
    print "%s%s %s%s" % (settings.color.RED, __name__, inspect.stack()[0][3], settings.color.ENDC)
    with open(listFile, 'r') as f:
        comments = json.load(f)

    print '%sreturn: %s%s' % (settings.color.YELLOW, comments, settings.color.ENDC)
    return comments


###################################################
#
###################################################
def getByTicketId(ticketId):
    print "%s%s %s%s" % (settings.color.RED, __name__, inspect.stack()[0][3], settings.color.ENDC)
    with open(listFile, 'r') as f:
        comments = json.load(f)

    comments = [x for x in comments if x[0] == ticketId]
    comment = []
    if comments:
        comment = comments[0]

    print '%sreturn: %s%s' % (settings.color.YELLOW, comment, settings.color.ENDC)
    return comment

commentsPath = settings.app + 'comments'
listFile = '%s/%s' % (commentsPath, 'list.json')
