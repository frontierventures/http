#!/usr/bin/env python
import os
import inspect
import shutil
import json

import settings
import logsModule


###################################################
#
###################################################
def reset():
    shutil.rmtree(path)
    os.makedirs(path)
    with open(listFile, 'w') as f:
        json.dump([], f)

    print "%s%s %s%s" % (settings.color.RED, __name__, inspect.stack()[0][3], settings.color.ENDC)


###################################################
#
###################################################
def create(transactionId, status, author):
    transactionId = transactionId.decode('utf8')
    with open(listFile, 'r') as f:
        tickets = json.load(f)

    timestamp = settings.timestamp()
    ticket = [transactionId, status, author, timestamp]
    tickets.append(ticket)

    with open(listFile, 'w') as f:
        json.dump(tickets, f)

    userFile = '%s/%s.json' % (usersPath, author)

    with open(userFile, 'r') as f:
        tickets = json.load(f)

    tickets.append(ticket)

    with open(userFile, 'w') as f:
        json.dump(tickets, f)

    print "%s%s %s%s" % (settings.color.RED, __name__, inspect.stack()[0][3], settings.color.ENDC)
    print '%sreturn: %s%s' % (settings.color.YELLOW, ticket, settings.color.ENDC)

    logsModule.createEntry(ticket)

    return ticket


###################################################
#
###################################################
def remove(transactionId):
    with open(listFile, 'r') as f:
        tickets = json.load(f)

    ticket = getByTransactionId(transactionId)
    tickets.remove(ticket)

    with open(listFile, 'w') as f:
        json.dump(tickets, f)

    print "%s%s %s%s" % (settings.color.RED, __name__, inspect.stack()[0][3], settings.color.ENDC)
    print '%sreturn: %s%s' % (settings.color.YELLOW, ticket, settings.color.ENDC)
    return ticket


###################################################
#
###################################################
def getAll():
    with open(listFile, 'r') as f:
        tickets = json.load(f)

    print "%s%s %s%s" % (settings.color.RED, __name__, inspect.stack()[0][3], settings.color.ENDC)
    print '%sreturn: %s%s' % (settings.color.YELLOW, tickets, settings.color.ENDC)
    return tickets


###################################################
#
###################################################
def getByTransactionId(transactionId):
    with open(listFile, 'r') as f:
        tickets = json.load(f)

    tickets = [x for x in tickets if x[0] == transactionId]
    ticket = []
    if tickets:
        ticket = tickets[0]
#    print ticket
#    ticket = [s.encode('utf-8') for s in ticket]

    print "%s%s %s%s" % (settings.color.RED, __name__, inspect.stack()[0][3], settings.color.ENDC)
    print '%sreturn: %s%s' % (settings.color.YELLOW, ticket, settings.color.ENDC)
    return ticket


###################################################
#
###################################################
def getByAuthor(author):
    with open(listFile, 'r') as f:
        tickets = json.load(f)

    tickets = [x for x in tickets if x[2] == author]

    print "%s%s %s%s" % (settings.color.RED, __name__, inspect.stack()[0][3], settings.color.ENDC)
    print '%sreturn: %s%s' % (settings.color.YELLOW, tickets, settings.color.ENDC)
    return tickets

path = settings.app + 'tickets'
usersPath = settings.app + 'users'
listFile = '%s/%s' % (path, 'list.json')
