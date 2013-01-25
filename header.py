#!/usr/bin/env python
import settings
import sessions


def Main(request):
    sessionUid = sessions.manager.getSessionUid(request)

    if sessionUid not in sessions.manager.uidList:
        sessions.manager.add(request)
        sessions.manager.setUserId(request, 0)

    print '%ssessions: %s%s' % (settings.color.RED, sessions.manager.uidList, settings.color.ENDC)
    activeUser = sessions.manager.getUserId(request)

    html = ''
    html += '<table>'
    html += '<tr>'
    html += '<td>%s</td>' % sessionUid
    html += '</tr>'
    html += '</table>'
    if activeUser == 0:
        html += '<table>'
        html += '<tr>'
        html += '<td><a href = "%s">%s</a></td>' % ('./', 'home')
        #html += '<td><a href = "%s">%s</a></td>' % ('', '')
        html += '</tr>'
        html += '</table>'

    if activeUser != 0:
        html += '<table>'
        html += '<tr>'
        html += '<td><a href = "%s">%s</a></td>' % ('./', 'home')
        html += '<td><a href = "%s">%s</a></td>' % ('account', 'account')
        html += '<td><a href = "%s">%s</a></td>' % ('user?id=%s' % str(activeUser), 'history')
        html += '<td><a href = "%s">%s</a></td>' % ('search', 'search')
        html += '<td><a href = "%s">%s</a></td>' % ('logout', 'logout')
        html += '</tr>'
        html += '</table>'
        html += '<table>'
        html += '<tr>'
        html += '<td>Active user: %s</td>' % str(activeUser)
        html += '</tr>'
        html += '</table>'
    return html
