from twisted.web.resource import Resource

import sessions
import header
import footer

import forms


class Main(Resource):
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
            formSearch.reset()
            formSearch.processInput(request)

            formSearch.makeHtml()
            html += formSearch.html

        html += footer.Main()
        html += '</center>'
        html += '</body>'
        html += '</html>'
        return html

formSearch = forms.Search()
