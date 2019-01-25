#!/usr/bin/env python

from pprint import pprint
import re

input = []
with open('4_input.txt') as f:
    for line in f:
        input.append(line)

#input = ['[1518-11-05 00:55] wakes up', '[1518-11-01 00:25] wakes up', '[1518-11-01 00:55] wakes up', '[1518-11-04 00:46] wakes up', '[1518-11-05 00:45] falls asleep', '[1518-11-01 23:58] Guard #99 begins shift', '[1518-11-02 00:40] falls asleep', '[1518-11-04 00:36] falls asleep', '[1518-11-02 00:50] wakes up', '[1518-11-03 00:05] Guard #10 begins shift', '[1518-11-03 00:29] wakes up', '[1518-11-04 00:02] Guard #99 begins shift', '[1518-11-01 00:05] falls asleep', '[1518-11-01 00:30] falls asleep', '[1518-11-03 00:24] falls asleep', '[1518-11-01 00:00] Guard #10 begins shift', '[1518-11-05 00:03] Guard #99 begins shift']

def sortList(input):
    input.sort()
    return input

def guardInfo(input):
    guard_dict = {}
    guard_re = re.compile(r'\d+')

    for line in input:
        curr_date = line[6:11]
        curr_time = line[15:17]
        curr_log = line[19:]
        if "Guard" in curr_log:
            curr_guard_id = guard_re.findall(curr_log)[0]
            if not curr_guard_id in guard_dict:
                guard_dict.update( { curr_guard_id : {} } )
        if "falls asleep" in curr_log:
            sleep_time = curr_time
            if curr_date in guard_dict[curr_guard_id]:
                guard_dict[curr_guard_id][curr_date].append(int(curr_time))
            else:
                guard_dict[curr_guard_id][curr_date] = [ int(curr_time) ]
        elif "wakes up" in curr_log:
            for i in range(int(sleep_time) + 1, int(curr_time)):
                guard_dict[curr_guard_id][curr_date].append(i)

    return guard_dict

def findBiggestSleeper(guard_info):
    guards_sleep_time = {}
    for guard_id in guard_info:
        sleep_time = 0
        for date in guard_info[guard_id]:
            sleep_time += len(guard_info[guard_id][date])
        guards_sleep_time[guard_id] = sleep_time
    biggest_sleeper = max(guards_sleep_time, key=lambda i: guards_sleep_time[i])
    return biggest_sleeper

def findMostSleepingMin(guard):
    all_mins = []
    for day in guard:
        all_mins = all_mins + guard[day]
    most_common_min = max(set(all_mins), key=all_mins.count)
    return most_common_min

if __name__ == '__main__':
    input = sortList(input)
    guard_info = guardInfo(input)
    biggest_sleeper_id = findBiggestSleeper(guard_info)
    most_asleep_min = findMostSleepingMin(guard_info[biggest_sleeper_id])
    result = int(biggest_sleeper_id) * most_asleep_min
    print(result)
