from zope.interface import Interface, Attribute, implements
from twisted.python.components import registerAdapter
from twisted.web.server import Session
#from twisted.web.resource import Resource


class SessionManager():
    def __init__(self):
        self.uidList = []

    def add(self, request):
        sessionUid = self.getSessionUid(request)
        self.uidList.append(sessionUid)

    def remove(self, request):
        session = request.getSession()
        session.expire()
        self.uidList = [x for x in self.uidList if x != session.uid]

    def getSessionUid(self, request):
        session = request.getSession()
        return session.uid

    def getUserId(self, request):
        session = request.getSession()
        sessionObject = ISessionObject(session)
        return sessionObject.userId

    def setUserId(self, request, userId):
        session = request.getSession()
        sessionObject = ISessionObject(session)
        sessionObject.userId = userId


class ISessionObject(Interface):
    userId = Attribute('')


class SessionObject(object):
    implements(ISessionObject)

    def __init__(self, session):
        self.userId = 0

registerAdapter(SessionObject, Session, ISessionObject)
manager = SessionManager()

#resource = ShowSession()
#resource.putChild("expire", ExpireSession())

#interface = ISessionObject()



#class ShowSession(Resource):
#    def render_GET(self, request):
#        session = request.getSession()
#        counter = ICounter(session)
#        counter.value += 1
#        print "Visit #%d for you!" % (counter.value)
#        return 'session_id: ' + session.uid
#
#class ExpireSession(Resource):
#    def render_GET(self, request):
#        request.getSession().expire()
#        return 'session expired'
#
#class ICounter(Interface):
#    value = Attribute("An int value which counts up once per page view.")
#
#class Counter(object):
#    implements(ICounter)
#    def __init__(self, session):
#        self.value = 0
#
#registerAdapter(Counter, Session, ICounter)
#
#resource = ShowSession()
#resource.user_id = 0
#resource.putChild("expire", ExpireSession())
