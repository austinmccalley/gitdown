import os


def checkGitFile():
    return os.path.isdir('.git')


def getGitLog():
    return os.popen('git log --decorate=short').read()


def getRemoteURL():
    origin_url = os.popen('git config --get remote.origin.url').read()

    url = ''

    # SSH remote url
    if(origin_url.startswith('git@')):
        splits = origin_url.split(':')

        post = splits[-1]
        post = post.rstrip()[:-4]

        pre = splits[0].split('@')[-1]
        return ('https://{}/{}/commit/'.format(pre, post))
    else:
      return origin_url[:-5]  + '/commit/'