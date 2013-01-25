import json
import shutil
import os
import inspect
import settings
import encryptor


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
    with open(listFile, 'w') as f:
        json.dump([], f)


###################################################
#
###################################################
def create(username, password):
    print "%s%s %s%s" % (settings.color.RED, __name__, inspect.stack()[0][3], settings.color.ENDC)
    with open(listFile, 'r') as f:
        users = json.load(f)

    userId = len(users)
    timestamp = settings.timestamp()
    password = encryptor.hashPassword(password)
    userId = str(userId)
    user = [userId, username, password, timestamp]
    users.append(user)

    with open(listFile, 'w') as f:
        json.dump(users, f)

    userFile = '%s/%s.json' % (usersPath, userId)

    with open(userFile, 'w') as f:
        json.dump([], f)

    print '%sreturn: %s%s' % (settings.color.YELLOW, user, settings.color.ENDC)
    return user


###################################################
#
###################################################
def getOne(username):
    print "%s%s %s%s" % (settings.color.RED, __name__, inspect.stack()[0][3], settings.color.ENDC)
    with open(listFile, 'r') as f:
        users = json.load(f)

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
    with open(listFile, 'r') as f:
        users = json.load(f)
    print '%sreturn: %s%s' % (settings.color.YELLOW, users, settings.color.ENDC)
    return users


###################################################
#
###################################################
def getInfo(userId):
    print "%s%s %s%s" % (settings.color.RED, __name__, inspect.stack()[0][3], settings.color.ENDC)
    with open(listFile, 'r') as f:
        users = json.load(f)
    users = [x for x in users if x[0] == userId]
    user = []
    if users:
        user = users[0]

    print '%sreturn: %s%s' % (settings.color.YELLOW, user, settings.color.ENDC)
    return user


usersPath = settings.app + 'users'
listFile = '%s/%s' % (usersPath, 'list.json')
