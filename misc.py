lstMsgTags = []

def log(msg, tag=None, op=None):
    if op == 'add' and tag not in lstMsgTags:
        lstMsgTags.append(tag)
    strTag = ''.join(lstMsgTags)
    print strTag + " " + msg
    if op == 'remove' and tag in lstMsgTags:
        lstMsgTags.remove(tag)
