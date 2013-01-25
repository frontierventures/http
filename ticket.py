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
        ticketId = request.args.get('id')
        ticketSignature = request.args.get('sig')

        try:
            ticketId = ticketId[0]
        except TypeError:
            ticketId = ''

        try:
            ticketSignature = ticketSignature[0]
        except TypeError:
            ticketSignature = ''
        ticket = ticketsModule.getById(ticketId)

        if ticket:
            ticketAuthorId = str(ticket[2])
            ticketAuthorName = quickAccess.lookupName(ticketAuthorId)
            ticketTimestamp = settings.convertTimestamp(float(ticket[3]))
            html += '<table>'
            html += '<tr>'
            html += '<td align="center"><a href = "%s">%s</a></td>' % ('./', 'home')
            html += '</tr>'
            html += '</table>'
            html += '<table>'
            html += '<tr>'
            html += '<td align="center"><h1>Ticket %s</h1></td>' % (ticketId)
            html += '</tr>'
            html += '<tr>'
            html += '<td align="center"><b>Details<b></td>'
            html += '</tr>'
            html += '<tr>'
            html += '<td align="center">Author: <a href ="%s">%s</a></td>' % ('user?id=%s' % ticketAuthorId, ticketAuthorName)
            html += '</tr>'
            html += '<tr>'
            html += '<td align="center">Date created: %s</td>' % ticketTimestamp
            html += '</tr>'

            if ticket[1] == 0:
                html += '<tr bgcolor="#00FF00">'
                html += '<td align="center">Status: Closed</td>'
                html += '</tr>'

            if ticket[1] == 1:
                html += '<tr bgcolor="#FF0000">'
                html += '<td align="center">Status: Open</td>'
                html += '</tr>'

            html += '<tr>'
            html += '<td align="center"><h2>Register and start receiving feedback today!</h2></td>'
            html += '</tr>'
            html += '</table>'
            if ticketSignature:
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
