#!/usr/bin/env python
import re

import sessions
 #import quickAccess

import settings
import encryptor

import ticketsModule
import usersModule


class Login:
    def __init__(self):
        print "Login class created"
        self.reset()

    def reset(self):
        self.html = ''

    def makeHtml(self):
        self.html += '<form style="margin-bottom:0;" action="" method="POST" enctype="application/x-www-form-urlencoded">'
        self.html += '<table>'
        self.html += '<tr>'
        self.html += '<td>Username</td><td><input type="TEXT" name="username" size="16"></td><td><input type="SUBMIT" name="button" value="Login"></td>'
        self.html += '</tr>'
        self.html += '<tr>'
        self.html += '<td>Password</td><td><input type="PASSWORD" name="password" size="16"></td><td><input type="SUBMIT" name="button" value="Register"></td>'
        self.html += '</tr>'
        self.html += '</table>'
        self.html += '</form>'

    def processInput(self, request):
        stop = False
        response = []

        try:
            print '%s%s%s' % (settings.color.RED, request.args, settings.color.ENDC)
            button = request.args.get('button')
            username = request.args.get('username')
            password = request.args.get('password')

            button = button[0]
            username = username[0]
            password = password[0]

            if not username:
                stop = True
                response.append('Username not entered')

            elif not re.match('^[\w-]+$', username):
                stop = True
                response.append('Non-alphanumeric username entered')

            if not password:
                stop = True
                response.append('Password not entered')

            elif not re.match('^[\w-]+$', password):
                stop = True
                response.append('Non-alphanumeric password entered')

            if not stop:
                user = usersModule.getOne(username)
                if button == 'Register':
                    if user:
                        stop = True
                        response.append('Username taken')

                    else:
                        usersModule.create(username, password)
                        response.append('Registration successful')
                        print '%snew_user created%s' % (settings.color.YELLOW, settings.color.ENDC)

                if button == 'Login':
                    if user:
                        if encryptor.checkPassword(user[2], password):
                            sessions.manager.setUserId(request, user[0])
                            response.append('Login sussessful')
                            print '%s%s: logged in from %s%s' % (settings.color.YELLOW, user[0], request.getClientIP(), settings.color.ENDC)

                        else:
                            stop = True
                            response.append('Invalid password entered')
                            print '%s%s: invalid password entered%s' % (settings.color.YELLOW, user[0], settings.color.ENDC)

                    else:
                        stop = True
                        response.append('Invalid username entered')
        except:
            pass

        if response:
            self.html += '<table>'
            if stop:
                self.html += '<tr bgcolor="#FF0000"><td>%s</td></tr>' % response
            else:
                self.html += '<tr bgcolor="#00FF00"><td>%s</td></tr>' % response
            self.html += '</table>'


class Search:
    def __init__(self):
        print "Search class created"
        self.reset()

    def reset(self):
        self.html = ''

    def makeHtml(self):
        self.html += '<form style="margin-bottom:0;" action="" method="POST" enctype="application/x-www-form-urlencoded">'
        self.html += '<table>'
        self.html += '<tr>'
        self.html += '<td>Query</td><td><input type = "TEXT" name = "query" size="16"></td><td><input type="SUBMIT" name="button" value="Search"></td>'
        self.html += '</tr>'
        self.html += '</table>'
        self.html += '</form>'

    def processInput(self, request):
        stop = False
        response = []

        print '%s%s%s' % (settings.color.RED, request.args, settings.color.ENDC)
        button = request.args.get('button')
        query = request.args.get('query')

        try:
            button = button[0]
            query = query[0]
        except:
            button = ''
            query = ''

        self.htmlResult = ''
        if button == 'Search':
            if not re.match('^[\w-]*$', query):
                stop = True
                response.append('Non-alphanumeric query entered')

            if not stop:
                count = 0
                users = [x for x in usersModule.getAll() if query in x[1]]

                if users:
                    response.append('Search sussessful')
                    self.htmlResult += '<table>'
                    self.htmlResult += '<tr bgcolor = "#00FF00">'
                    self.htmlResult += '<td align = "center">id</td>'
                    self.htmlResult += '<td align = "center">username</td>'
                    self.htmlResult += '<td align = "center">timestamp</td>'
                    self.htmlResult += '</tr>'
                    for user in users:
                        count += 1
                        if count % 2 == 0:
                            bgcolor = '#E0E0E0'
                        else:
                            bgcolor = '#FFFFFF'

                        self.htmlResult += '<tr bgcolor = "%s">' % bgcolor
                        self.htmlResult += '<td align = "center">%s</td>' % str(user[0])
                        self.htmlResult += '<td align = "center"><a href = "user?id=%s">%s</a></td>' % (str(user[0]), str(user[1]))
                        self.htmlResult += '<td align = "center">%s</td>' % str(user[3])
                        self.htmlResult += '</tr>'
                    self.htmlResult += '</table>'
                else:
                    response.append('No matches found')
                    self.htmlResult = ''
                    stop = True

        if response:
            self.html += '<table>'
            if stop:
                self.html += '<tr bgcolor="#FF0000"><td>%s</td></tr>' % response
            else:
                self.html += '<tr bgcolor="#00FF00"><td>%s</td></tr>' % response
            self.html += '</table>'
            self.html += self.htmlResult


class Ticket:
    def __init__(self):
        print "Ticket class created"
        self.reset()

    def reset(self):
        self.html = ''

    def makeHtml(self):
        self.html += '<form style="margin-bottom:0;" action="" method="POST" enctype="application/x-www-form-urlencoded">'
        self.html += '<table>'
        self.html += '<tr>'
        self.html += '<td>Broadcast</td><td>Yes<input type = "RADIO" name = "broadcast" checked></td><td>No<input type = "RADIO" name = "broadcast"></td></td>'
        self.html += '</tr>'
        self.html += '<tr>'
        self.html += '<td>Transaction ID</td><td><input type = "TEXT" name = "transactionId" size="16"></td><td><input type="SUBMIT" name="button" value="Create ticket"></td>'
        self.html += '</tr>'
        self.html += '<tr>'
        self.html += '<td>Description</td><td><input type = "TEXT" name = "description" size="40"></td><td></td>'
        self.html += '</tr>'
        self.html += '</table>'
        self.html += '</form>'

    def processInput(self, request):
        stop = False
        response = []

        print '%s%s%s' % (settings.color.RED, request.args, settings.color.ENDC)
        button = request.args.get('button')
        transactionId = request.args.get('transactionId')
        description = request.args.get('description')

        try:
            button = button[0]
            ticketId = transactionId[0]
            description = description[0]
        except:
            button = ''
            ticketId = ''
            description = ''

        self.htmlResult = ''
        if button == 'Create ticket':
            if not re.match('^[\w-]+$', ticketId):
                stop = True
                response.append('Non-alphanumeric transactionId entered')

            if not stop:
                ticket = ticketsModule.getById(ticketId)

                if ticket:
                    stop = True
                    response.append('Ticket already exists')
                else:
                    response.append('Ticket created')
                    activeUser = sessions.manager.getUserId(request)
                    ticket = ticketsModule.create(ticketId, 1, activeUser)
                    ticketSignature = str(ticket[2])

                    self.htmlResult += '<table>'
                    self.htmlResult += '<tr>'
                    self.htmlResult += '<td align = "center">Please ask your customer to rate this transaction at the link below</td>'
                    self.htmlResult += '</tr>'
                    self.htmlResult += '<tr>'
                    self.htmlResult += '<td align = center><a href = "ticket?id=%s&sig=%s">%s</a></td>' % (ticketId, ticketSignature, ticketId)
                    self.htmlResult += '</tr>'
                    self.htmlResult += '</table>'

        if response:
            self.html += '<table>'
            if stop:
                self.html += '<tr bgcolor="#FF0000"><td>%s</td></tr>' % response
            else:
                self.html += '<tr bgcolor="#00FF00"><td>%s</td></tr>' % response
            self.html += '</table>'
            self.html += self.htmlResult


class Feedback:
    def __init__(self):
        print "Feedback class created"
        self.reset()

    def reset(self):
        self.html = ''

    def makeHtml(self):
        html = ''
        html += '<form style="margin-bottom:0;" action="" method="POST" enctype="application/x-www-form-urlencoded">'
        html += '<table>'
        html += '<tr>'
        html += '<td>Grade:</td>'
        html += '<td align="center">'
        html += 'Good<input type="RADIO" name = "grade" value="1" checked>'
        html += 'Bad<input type="RADIO" name = "grade" value="-1">'
        html += 'Neutral<input type="RADIO" name = "grade" value="0">'
        html += '</td>'
        html += '<td></td>'
        html += '</tr>'
        html += '<tr>'
        html += '<td>Comment:</td>'
        html += '<td>'
        html += '<input type="TEXT" name="comment" size="64">'
        html += '</td>'
        html += '<td><input type="SUBMIT" name="button" value="Submit Feedback"></td>'
        html += '</tr>'
        html += '</table>'
        html += '</form>'
        return html

    def processInput(self, request):
        stop = False
        response = []

        print '%s%s%s' % (settings.color.RED, request.args, settings.color.ENDC)
        button = request.args.get('button')
        grade = request.args.get('grade')
        comment = request.args.get('comment')
        ticketId = request.args.get('id')

        try:
            button = button[0]
            grade = grade[0]
            comment = comment[0]
            ticketId = ticketId[0]
        except:
            button = ''
            grade = ''
            comment = ''
            ticketId = ''

        self.html = self.makeHtml()
        if button == 'Submit Feedback':
            if not re.match('^[\w-]+$', comment):
                stop = True
                response.append('Non-alphanumeric comment entered')

            if not stop:
                    ticket = ticketsModule.remove(ticketId)
                    ticketsModule.create(ticketId, 0, ticket[4])
                    response.append('Your feedback has been recorded')

        if response:
            if stop:
                self.html += '<table>'
                self.html += '<tr bgcolor="#FF0000"><td>%s</td></tr>' % response
            else:
                self.html = ''
                self.html += '<table>'
                self.html += '<tr bgcolor="#00FF00"><td>%s</td></tr>' % response
            self.html += '</table>'
