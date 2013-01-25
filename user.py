#!/usr/bin/env python

import settings
import header
import footer

import ticketsModule

from twisted.web.resource import Resource

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

        html += header.Main(request)
        try:
            userId = request.args.get('id')
            userId = userId[0]
        except:
            userId = 0

        if userId == 0:
            html += '<table>'
            html += '<tr bgcolor = "#FF0000">'
            html += '<td align = "center">No user id specified</td>'
            html += '</tr>'
            html += '</table>'
        else:

            tickets = ticketsModule.getByAuthor(userId)

            if tickets:
                html += '<table>'
                html += '<tr bgcolor = "#00FF00">'
                html += '<td align = "center">id</td>'
                html += '<td align = "center">status</td>'
                html += '<td align = "center">timestamp</td>'
                html += '</tr>'

                count = 0

                for ticket in tickets:
                    transactionId = str(ticket[0])
                    ticketStatus = ticket[1]
                    ticketTimestamp = float(ticket[3])

                    ticketTimestamp = settings.convertTimestamp(ticketTimestamp)

                    count += 1
                    if count % 2 == 0:
                        bgcolor = '#E0E0E0'
                    else:
                        bgcolor = '#FFFFFF'

                    html += '<tr bgcolor = "%s">' % bgcolor
                    html += '<td align = "center">%s</td>' % transactionId
                    html += '<td align = "center">%s</td>' % ticketStatus
                    html += '<td align = "center">%s</td>' % ticketTimestamp
                    html += '</tr>'
                html += '</table>'
            else:
                html += '<table>'
                html += '<tr bgcolor = "#FF0000">'
                html += '<td align = "center">User has no transactions recorded</td>'
                html += '</tr>'

        html += footer.Main()
        html += '</center>'
        html += '</body>'
        html += '</html>'
        return html
