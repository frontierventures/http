import shutil
import os
import inspect
import settings
import encryptor
import quickAccess


###################################################
#
###################################################
def reset():
    print "%s%s %s%s" % (settings.color.RED, __name__, inspect.stack()[0][3], settings.color.ENDC)
    try:
        shutil.rmtree(usersPath)
        os.makedirs(usersPath)
    except OSError:
        os.makedirs(usersPath)

    quickAccess.unload(listFile, [])


###################################################
#
###################################################
def create(username, password):
    print "%s%s %s%s" % (settings.color.RED, __name__, inspect.stack()[0][3], settings.color.ENDC)
    users = quickAccess.load(listFile)

    userId = len(users)
    timestamp = settings.timestamp()
    password = encryptor.hashPassword(password)
    userId = str(userId)
    user = [userId, username, password, timestamp]
    users.append(user)

    quickAccess.unload(listFile, users)

    userFile = '%s/%s.json' % (usersPath, userId)

    quickAccess.unload(userFile, [])

    print '%sreturn: %s%s' % (settings.color.YELLOW, user, settings.color.ENDC)
    return user


###################################################
#
###################################################
def getOne(username):
    print "%s%s %s%s" % (settings.color.RED, __name__, inspect.stack()[0][3], settings.color.ENDC)

    users = quickAccess.load(listFile)
    users = [x for x in users if x[1] == username]
    user = []

    if users:
        user = users[0]

    print '%sreturn: %s%s' % (settings.color.YELLOW, user, settings.color.ENDC)
    return user


###################################################
#
###################################################
def getAll():
    print "%s%s %s%s" % (settings.color.RED, __name__, inspect.stack()[0][3], settings.color.ENDC)

    users = quickAccess.load(listFile)

    print '%sreturn: %s%s' % (settings.color.YELLOW, users, settings.color.ENDC)
    return users


###################################################
#
###################################################
def getInfo(userId):
    print "%s%s %s%s" % (settings.color.RED, __name__, inspect.stack()[0][3], settings.color.ENDC)

    users = quickAccess.load(listFile)
    users = [x for x in users if x[0] == userId]
    user = []

    if users:
        user = users[0]

    print '%sreturn: %s%s' % (settings.color.YELLOW, user, settings.color.ENDC)
    return user


usersPath = settings.app + 'users'
listFile = '%s/%s' % (usersPath, 'list.json')
