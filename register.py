#!/usr/bin/env python
from twisted.web.resource import Resource

import re
import inspect

import settings
import usersModule
import header
import footer
import sessions


class Register:
    def __init__(self):
        print "Login class created"
        self.reset()

    def reset(self):
        self.html = ''
        self.htmlResult = ''
        self.args = ['', '', '']

    def makeHtml(self):
        self.html += '<form style="margin-bottom:0;" action="" method="POST" enctype="application/x-www-form-urlencoded">'
        self.html += '<table>'
        self.html += '<tr>'
        self.html += '<td>Username</td><td><input type="TEXT" value="%s" name="0" size="16"></td>' % self.args[0]
        self.html += '</tr>'
        self.html += '<tr>'
        self.html += '<td>Password</td><td><input type="PASSWORD" value="%s" name="1" size="16"></td><td><input type="SUBMIT" name="2" value="Register"></td>' % self.args[1]
        self.html += '</tr>'
        self.html += '</table>'
        self.html += '</form>'
        self.args = []

    def processInput(self, request):
        print "%s%s %s%s" % (settings.color.RED, __name__, inspect.stack()[0][3], settings.color.ENDC)
        self.makeHtml()
        stop = False
        response = []

        print '%s%s %s%s' % (settings.color.RED, request, type(request), settings.color.ENDC)
        print '%s%s%s' % (settings.color.RED, request.args, settings.color.ENDC)

        if request.args:
            for key in sorted(request.args.iterkeys()):
                print key
                value = request.args.get(key)
                self.args.append(value[0])

        print self.args
        if self.args:
            if not self.args[0]:
                stop = True
                response.append('Username not entered')

            elif not re.match('^[\w-]+$', self.args[0]):
                stop = True
                response.append('Non-alphanumeric username entered')

            if not self.args[1]:
                stop = True
                response.append('Password not entered')

            elif not re.match('^[\w-]+$', self.args[1]):
                stop = True
                response.append('Non-alphanumeric password entered')

        else:
            stop = True

        user = []
        if not stop:
            user = usersModule.getOne(self.args[0])

            if self.args[2] == 'Register':
                if user:
                    stop = True
                    response.append('Username taken')

                else:
                    usersModule.create(self.args[0], self.args[1])
                    response.append('Registration successful')

        self.formResponse = ''
        if response:
            self.formResponse += '<table>'
            if stop:
                self.formResponse += '<tr bgcolor="#FF0000"><td>%s</td></tr>' % response
            else:
                self.formResponse += '<tr bgcolor="#00FF00"><td>%s</td></tr>' % response
            self.formResponse += '</table>'
        self.html = self.formResponse + self.html


class Main(Resource):
    def __init__(self):
        Resource.__init__(self)

    def render(self, request):
        activeUser = sessions.manager.getUserId(request)

        html = ''
        html += '<html>'
        html += '<body>'
        html += '<center>'
        html += header.Main(request)

        if activeUser == 0:
            formRegister.reset()
            formRegister.processInput(request)
            html += formRegister.html
        else:
            html += '<table>'
            html += '<tr>'
            html += '<td>Active user: %s</td>' % activeUser
        html += footer.Main()
        html += '</center>'
        html += '</body>'
        html += '</html>'
        return html
formRegister = Register()
