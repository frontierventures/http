from twisted.web import resource

import settings
import sessions
import header
import footer

import usersModule

class Main(resource.Resource):
    isLeaf = True
    def render(self, request):
	activeUser = sessions.manager.getUserId(request)
        
	html = ''
        html += '<html>'
        html += '<body>'
	html += '<center>'
        html += header.Main(request)
        if activeUser == 0:
            html += '<table>'
            html += '<tr>'
            html += '<td bgcolor="#FF0000">'
            html += 'User only area' 
            html += '</td>'
            html += '</tr>'
            html += '</table>'
        else:
	    user = usersModule.getInfo(activeUser)
            html += 'Registration timestamp: %s' % str(user[3])
	html += footer.Main()
	html += '</center>'
        html += '</body>'
        html += '</html>'
        return html
