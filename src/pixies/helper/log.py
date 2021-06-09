def logPixie(type, content):
    print('[Pixie] ' + type + ' '*(10-len(type)) + content)


def logError(content):
    print('[Error] ' + content)


def logEvent(content):
    print('[Event] ' + content)
