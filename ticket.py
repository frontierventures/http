from twisted.web.resource import Resource

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
        transactionId = request.args.get('id')

        try:
            transactionId = transactionId[0]
        except:
            transactionId = ''

        ticket = ticketsModule.getByTransactionId(transactionId)

        if ticket:
            if ticket[1] == 0:
                html += '<table>'
                html += '<tr>'
                html += '<td bgcolor="#FF0000">'
                html += 'Ticket closed'
                html += '</td>'
                html += '</tr>'
                html += '</table>'

            if ticket[1] == 1:
                author = ticket[2]
                author = str(author)
                html += '<table>'
                html += '<tr>'
                html += '<td align="center"><a href = "%s">%s</a></td>' % ('./', 'home')
                html += '</tr>'
                html += '<td align="center"><b>%s</b> is asking you to provide feedback on transaction <b>%s</b> opened on %s.</td>' % (author, transactionId, ticket[3])
                html += '</tr>'
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
                html += '<tr>'
                html += '<td align="center"><b>Register and start receiving feedback today!</b></td>'
                html += '</tr>'
                html += '</table>'
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
