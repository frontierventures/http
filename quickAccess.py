#!/usr/bin/env python
#import descriptionsModule
#import commentsModule
#import logsModule
#import ticketsModule
import json
import inspect
import settings
import usersModule


###################################################
#
###################################################
def load(file):
    print "%s%s %s%s" % (settings.color.RED, __name__, inspect.stack()[0][3], settings.color.ENDC)
    with open(file, 'r') as f:
        list = json.load(f)
    return list


###################################################
#
###################################################
def unload(file, list):
    print "%s%s %s%s" % (settings.color.RED, __name__, inspect.stack()[0][3], settings.color.ENDC)
    with open(file, 'w') as f:
        json.dump(list, f)


###################################################
#
###################################################
def lookupName(id):
    print "%s%s %s%s" % (settings.color.RED, __name__, inspect.stack()[0][3], settings.color.ENDC)
    user = usersModule.getInfo(id)
    return str(user[1])
