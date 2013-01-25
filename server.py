#!/usr/bin/env python

from twisted.web.resource import Resource
from twisted.internet import reactor
from twisted.python import log
from twisted.web.server import Site
import sys

import sessions
import quickAccess
import settings
import header
import footer
import forms

import descriptionsModule
import commentsModule
import logsModule
import ticketsModule
import usersModule

import account
import disclaimer
import logout
import ticket
import search
import user


def load():
    usersModule.reset()
    usersModule.create('admin', 'admin')
    usersModule.create('alice1', 'pass')
    usersModule.create('alice2', 'pass')
    usersModule.create('alice3', 'pass')
    usersModule.create('bob1', 'pass')
    usersModule.create('bob2', 'pass')
    usersModule.create('bob3', 'pass')
    usersModule.create('carol1', 'pass')
    usersModule.create('carol2', 'pass')
    usersModule.create('carol3', 'pass')

    logsModule.reset()
    descriptionsModule.reset()
    commentsModule.reset()

    ticketsModule.reset()

    ticketsModule.create('a', 1, u'1')
    ticketsModule.create('b', 1, u'1')


class Main(Resource):
    def __init__(self):
        Resource.__init__(self)

    def render(self, request):
        formLogin.reset()
        formLogin.processInput(request)

        formTicket.reset()
        formTicket.processInput(request)

        activeUser = sessions.manager.getUserId(request)

        html = ''
        html += '<html>'
        html += '<body>'
        html += '<center>'
        html += header.Main(request)
        if activeUser == 0:
            formLogin.makeHtml()
            html += formLogin.html
        else:
            formTicket.makeHtml()
            html += formTicket.html

        html += '<table>'
        for entry in logsModule.getAll():
            transactionId = str(entry[0])
            ticketStatus = entry[1]
            ticketAuthorId = str(entry[2])
            ticketAuthorName = quickAccess.lookupName(ticketAuthorId)
            ticketTimestamp = float(entry[3])

            ticketTimestamp = settings.convertTimestamp(ticketTimestamp)

            bgcolor = "#FFFFFF"
            print ticketStatus
            if (ticketStatus == 0):
                bgcolor = "#00FF00"
                html += '<tr bgcolor="%s">' % bgcolor
                html += '<td align = "center">%s Ticket <a href = "ticket?id=%s"><b>%s</b></a> closed</td>' % (ticketTimestamp, transactionId, transactionId)
            if (ticketStatus == 1):
                html += '<tr bgcolor="%s">' % bgcolor
                html += '<td align = "center">%s Ticket <a href = "ticket?id=%s"><b>%s</b></a> opened by <a href = "user?id=%s"><b>%s</b></a></td>' % (ticketTimestamp, transactionId, transactionId, ticketAuthorId, ticketAuthorName)

            html += '</tr>'
        html += '</table>'

        html += footer.Main()
        html += '</center>'
        html += '</body>'
        html += '</html>'
        return html

log.startLogging(sys.stdout)

load()

root = Main()

formLogin = forms.Login()
formTicket = forms.Ticket()

root.putChild('', root)
root.putChild('account', account.Main())
root.putChild('disclaimer', disclaimer.Main())
root.putChild('logout', logout.Main())
root.putChild('search', search.Main())
root.putChild('ticket', ticket.Main())
root.putChild('user', user.Main())

site = Site(root)
reactor.listenTCP(8080, site)
reactor.run()
