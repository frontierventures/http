from twisted.web import resource
from twisted.web.util import redirectTo

import sessions

class Main(resource.Resource):
    isLeaf = True
    def render_GET(self, request):
        sessions.manager.setUserId(request, 0)
	sessions.manager.remove(request)

        return redirectTo("./",request)
#        html = ''
#        html += '<html>'
#        html += '<body>'
#        html += '<center>'
#        html += header.main(request)     
#        html += '<table>'
#        html += '<tr>'
#        html += '<td bgcolor="#FF0000">'
#        html += 'user logged out' 
#        html += '</td>'
#        html += '</tr>'
#        html += '</table>'
#        html += footer.main()
#        html += '</center>'
#        html += '</body>'
#        html += '</html>'
#        return html


