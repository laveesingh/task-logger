import argparse
import datetime
import sys

import colorit
import readchar

parser = argparse.ArgumentParser()
parser.add_argument('-t', '--tty', help="tty name for logs")
args = parser.parse_args()

original_pipe = sys.stdout
new_pipe = open("task.log", "a+")
if args.tty:
    t_pipe = open(args.tty, "w+")


def dump_to_file(task_title, start_time, end_time):
    sys.stdout = new_pipe  # This goes to file
    duration = end_time - start_time
    time_stamp = datetime.datetime.strftime(
        datetime.datetime.now(), "%H:%M:%S %d/%m/%Y")
    title = colorit.color_front('Title="%s"' % task_title, 0, 0, 200)
    start = colorit.color_front('Start="%s"' % start_time, 0, 200, 0)
    end = colorit.color_front('End="%s"' % end_time, 0, 200, 0)
    str_duration = colorit.color_front(
        'Duration="%s"' % str(duration), 200, 0, 0)
    current_log = '%s %s %s %s %s' % (
        title, start, end, str_duration, time_stamp)
    print current_log
    sys.stdout.flush()
    if args.tty:
        sys.stdout = t_pipe
        print current_log
    sys.stdout = original_pipe


while 1:
    task_title = raw_input("Enter title to your new task: ")
    start = datetime.datetime.now()
    print "press q to quit logging, n to quit this log, any other key otherwise"
    ends = readchar.readchar()
    if ends == 'q' or ends == 'Q':
        break
    if ends == 'n' or ends == 'N':
        continue
    end = datetime.datetime.now()
    dump_to_file(task_title, start, end)
