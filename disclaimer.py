from twisted.web import resource

import header
import footer

class Main(resource.Resource):
    isLeaf = True
    def render(self, request):
        html = ''
        html += '<html>'
        html += '<body>'
        html += '<center>'
        html += header.Main(request)     
        html += '<h2>Disclaimer</h2>'  
        html += '''
        Use this service at your own risk!
        '''
        html += footer.Main()
        html += '</center>'
        html += '</body>'
        html += '</html>'
        return html
