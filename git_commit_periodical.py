#!/usr/bin/env python3
"""git commit at regular intervals

https://github.com/mica5/auto-git-commits

Version 0.1
2018-03-21
"""
import argparse
import datetime
from dateutil import parser
import subprocess
from time import sleep

def run_main():
    args = parse_cl_args()

    next_time = subprocess.check_output(
        'date -d"{}"'.format(args.period),
        shell=True
    )
    next_time = parser.parse(next_time, ignoretz=True)
    now = datetime.datetime.now()
    period = next_time - now
    sleep_seconds = period.total_seconds()

    # TODO add option to make it only run a specified number of times
    while True:
        if args.pull_first:
            subprocess.call('git pull', shell=True)

        for pattern in args.patterns:
            # TODO make it possible to make it non-recursive so only specific files are committed
            subprocess.call(
                "find . -name '{pattern}'|xargs git add".format(pattern=pattern),
                shell=True
            )

        subprocess.call(
            'git commit --message="{}"'.format(args.message),
            shell=True
        )

        if args.push_after:
            subprocess.call('git push', shell=True)
        sleep(sleep_seconds)

    success = True
    return success

def parse_cl_args():
    argParser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawTextHelpFormatter,
    )

    argParser.add_argument(
        'period',
        help="anything that can be parsed by the -d option of\n"
             "gnu date utility, e.g. '10minutes'"
    )
    argParser.add_argument(
        'patterns', nargs='+',
        help="anything that can be used by the -name option of the gnu\n"
             "'find' command, e.g. '*.scala' '*.sl1' or 'somefile.txt'"
    )
    argParser.add_argument('--pull-first', default=False, action='store_true')
    argParser.add_argument('--push-after', default=False, action='store_true')
    argParser.add_argument(
        '--message', default='autocommit',
        help='message to use on commit, default "%(default)s"'
    )

    args = argParser.parse_args()
    return args


if __name__ == '__main__':
    success = run_main()
    exit_code = 0 if success else 1
    exit(exit_code)

