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
    print "%s%s %s%s" % (settings.color.RED, __name__, inspect.stack()[0][3], settings.color.ENDC)
    try:
        shutil.rmtree(ticketsPath)
        os.makedirs(ticketsPath)
    except OSError:
        os.makedirs(ticketsPath)
    with open(listFile, 'w') as f:
        json.dump([], f)


###################################################
#
###################################################
def create(ticketId, status, author):
    print "%s%s %s%s" % (settings.color.RED, __name__, inspect.stack()[0][3], settings.color.ENDC)
    with open(listFile, 'r') as f:
        tickets = json.load(f)

    timestamp = settings.timestamp()
    ticket = [ticketId, status, author, timestamp]
    tickets.append(ticket)

    with open(listFile, 'w') as f:
        json.dump(tickets, f)

    userFile = '%s/%s.json' % (usersPath, author)

    with open(userFile, 'r') as f:
        tickets = json.load(f)

    tickets.append(ticket)

    with open(userFile, 'w') as f:
        json.dump(tickets, f)

    print '%sreturn: %s%s' % (settings.color.YELLOW, ticket, settings.color.ENDC)

    logsModule.createEntry(ticket)

    return ticket


###################################################
#
###################################################
def remove(ticketId):
    print "%s%s %s%s" % (settings.color.RED, __name__, inspect.stack()[0][3], settings.color.ENDC)
    with open(listFile, 'r') as f:
        tickets = json.load(f)

    ticket = getById(ticketId)
    tickets.remove(ticket)

    with open(listFile, 'w') as f:
        json.dump(tickets, f)

    print '%sreturn: %s%s' % (settings.color.YELLOW, ticket, settings.color.ENDC)
    return ticket


###################################################
#
###################################################
def getAll():
    print "%s%s %s%s" % (settings.color.RED, __name__, inspect.stack()[0][3], settings.color.ENDC)
    with open(listFile, 'r') as f:
        tickets = json.load(f)

    print '%sreturn: %s%s' % (settings.color.YELLOW, tickets, settings.color.ENDC)
    return tickets


###################################################
#
###################################################
def getById(ticketId):
    print "%s%s %s%s" % (settings.color.RED, __name__, inspect.stack()[0][3], settings.color.ENDC)
    with open(listFile, 'r') as f:
        tickets = json.load(f)

    tickets = [x for x in tickets if x[0] == ticketId]
    ticket = []
    if tickets:
        ticket = tickets[0]

    print '%sreturn: %s%s' % (settings.color.YELLOW, ticket, settings.color.ENDC)
    return ticket


###################################################
#
###################################################
def getByAuthor(author):
    print "%s%s %s%s" % (settings.color.RED, __name__, inspect.stack()[0][3], settings.color.ENDC)
    with open(listFile, 'r') as f:
        tickets = json.load(f)

    tickets = [x for x in tickets if x[2] == author]

    print '%sreturn: %s%s' % (settings.color.YELLOW, tickets, settings.color.ENDC)
    return tickets

ticketsPath = settings.app + 'tickets'
usersPath = settings.app + 'users'
listFile = '%s/%s' % (ticketsPath, 'list.json')
