#!/usr/bin/env python
from twisted.web.resource import Resource

import quickAccess

import settings
import forms

import ticketsModule
# Ask to login or rate annonymously
# Title
# Go to main site
# Show ticket's author badge
# Show advertisement


class Main(Resource):
    def __init__(self):
        Resource.__init__(self)

    def render(self, request):
        html = ''
        html += '<html>'
        html += '<body>'
        html += '<center>'

        print '%s%s%s' % (settings.color.RED, request.args, settings.color.ENDC)
        getTicketId = request.args.get('id')
        getTicketSignature = request.args.get('sig')

        try:
            getTicketId = getTicketId[0]
        except TypeError:
            getTicketId = ''

        try:
            getTicketSignature = getTicketSignature[0]
        except TypeError:
            getTicketSignature = ''

        ticket = ticketsModule.getById(getTicketId)

        if ticket:
            ticketTimestamp = settings.convertTimestamp(float(ticket[0]))
            ticketId = str(ticket[1])
            ticketSignature = str(ticket[2])
            ticketStatus = ticket[3]
            ticketAuthorId = str(ticket[4])
            ticketAuthorName = quickAccess.lookupName(ticketAuthorId)

            html += '<table>'
            html += '<tr>'
            html += '<td align="center"><a href = "%s">%s</a></td>' % ('./', 'home')
            html += '</tr>'
            html += '</table>'
            html += '<table>'

            if ticketStatus == 0:
                html += '<tr bgcolor="#00FF00">'
                html += '<td align="center"><h1>Closed Ticket</h1></td>'
                html += '</tr>'

            if ticketStatus == 1:
                html += '<tr bgcolor="#FF0000">'
                html += '<td align="center"><h1>Open Ticket</h1></td>'
                html += '</tr>'

            html += '<tr>'
            html += '<td align="center"><b>Details<b></td>'
            html += '</tr>'
            html += '<tr>'
            html += '<td align="center">Date created: %s</td>' % ticketTimestamp
            html += '</tr>'
            html += '<tr>'
            html += '<td align="center">Id: %s</a></td>' % ticketId
            html += '</tr>'
            html += '<tr>'
            html += '<td align="center">Author: <a href ="%s">%s</a></td>' % ('user?id=%s' % ticketAuthorId, ticketAuthorName)
            html += '</tr>'

            if ticketSignature == getTicketSignature:
                html += '<tr>'
                html += '<td align="center">Signature: %s</a></td>' % ticketSignature
                html += '</tr>'

            html += '<tr>'
            html += '<td align="center"><h2>Register and start receiving feedback today!</h2></td>'
            html += '</tr>'
            html += '</table>'
            print ticketSignature, type(ticketSignature)
            print getTicketSignature, type(getTicketSignature)

            if ticketSignature == getTicketSignature:
                html += '<table>'
                html += '<tr>'
                html += '<td align="center"><b>Instructions</b></td>'
                html += '</tr>'
                html += '<tr>'
                html += '<td align="center">Please verify transaction detals</td>'
                html += '</tr>'
                html += '<tr>'
                html += '<td align="center">Please choose one (Good, Neutral, Bad)</td>'
                html += '</tr>'
                html += '<tr>'
                html += '<td align="center">Please report any misconduct</td>'
                html += '</tr>'
                html += '</table>'
                formFeedback.reset()
                formFeedback.processInput(request)
                html += formFeedback.html
        else:
            html += '<table>'
            html += '<tr>'
            html += '<td bgcolor="#FF0000">'
            html += 'Ticket does not exist'
            html += '</td>'
            html += '</tr>'
            html += '</table>'

        html += '</center>'
        html += '</body>'
        html += '</html>'
        return html

formFeedback = forms.Feedback()
