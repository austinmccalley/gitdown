import os
import sys

import utils

if __name__ == "__main__":
    print("gitdown v0.1.0 by Austin McCalley")

    output = sys.argv[1:][0] if sys.argv[1:] else 'output.md'

    # Check if directory is a git repository
    if not utils.checkGitFile():
        print('This is not a git repository!')
        exit(1)

    logs = utils.getGitLog()

    # Split by commit
    logs = logs.split('\ncommit')

    # Check if there are commits
    if(len(logs) < 1 or logs[0] == ''):
        print('There are no commits to be found')
        exit(1)

    # Remove the commit message from the first one
    logs[0] = logs[0][7:]

    commits = []
    url = utils.getRemoteURL()
    # Create the format string for the output
    for log in logs:
        if(log[0] == ' '):
            log = log[1:]

        lines = log.split('\n')

        commitHashShort = lines[0][:6]
        commitHashLong = lines[0]
        commitMessage = lines[-2][4:]

        commits.append('[{}]({}) - {}'.format(commitHashShort,
                                              url + commitHashLong, commitMessage))
    commits.reverse()

    print('Found {} commits'.format(len(commits)))

    with open(output, 'w') as f:
        f.write('# Git Logs\n\n')
        for commit in commits:
            f.write(commit)
            f.write('\n\n')
        f.write(
            '*Powered by [gitdown](https://github.com/austinmccalley/gitdown)*')
        print('Wrote to {}'.format(output))
        f.close()
