# auto-git-commits
periodically/automatically run git commits

At regular intervals, e.g. '10minutes' or '30seconds', git add any files that match given patterns, and commit.

This was written for taking a coding midterm where the instructor requires commits every 10 minutes (Professor Horstmann at San Jose State University). The purpose of requiring commits every 10 minutes is to prevent and detect cheating. This script is to automate the committing to avoid taking focus away from the midterm.

example usage:

    git_commit_periodical.py 10seconds '*.scala' '*.sl1' --message 'midterm auto-commit'
