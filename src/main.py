import os

import utils

if __name__ == "__main__":
    print("gitdown")

    # Check if directory is a git repository
    if not utils.checkGitFile():
        print('This is not a git repository!')
        exit(1)

    logs = utils.getGitLog()

    logs = logs.split('\ncommit')

    if(len(logs) < 1 or logs[0] == ''):
        print('There are no commits to be found')
        exit(1)

    logs[0] = logs[0][7:]

    for log in logs:
        if(log[0] == ' '):
            log = log[1:]

        lines = log.split('\n')

        commitHash = lines[0][:6]
        commitMessage = lines[-2][4:]
        
        print(commitHash)
        print(commitMessage)
