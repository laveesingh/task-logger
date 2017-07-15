import sys
import datetime


original_pipe = sys.stdout
new_pipe = open("task.log", "a+")

def dump_to_file(task_title, start_time, end_time):
    sys.stdout = new_pipe  # This goes to file
    duration = end_time - start_time
    time_stamp = datetime.datetime.strftime(datetime.datetime.now(), "%H:%M:%S %d/%m/%Y")
    print 'Title="%s" Start="%s" End="%s" Duration="%s" timestamp=%s' % (task_title, start_time, end_time, str(duration), time_stamp)
    sys.stdout.flush()
    sys.stdout = original_pipe


while 1:
    task_title = raw_input("Enter title to your new task: ")
    start = datetime.datetime.now()
    ends = raw_input("Hit enter to end this task and start a new one")
    end = datetime.datetime.now()
    dump_to_file(task_title, start, end)
