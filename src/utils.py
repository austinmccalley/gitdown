import os

def checkGitFile():
    return os.path.isdir('.git')


def getGitLog():
  return os.popen('git log --decorate=short').read()