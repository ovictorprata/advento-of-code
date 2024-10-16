from re import search

def extract_number_guard_from_str(timestamps: list) -> int:
    guard_number_regex = search(r'#(\d+)', timestamps)
    if guard_number_regex:
        guard_number = int(guard_number_regex.group(1))
    return guard_number

def print_guards_times(guards_infos: dict) -> None:
    for number, guards_info in guards_infos.items():
        print('*' * 80)
        print(number)
        print('*' * 80)
        for date, schedule in guards_info.items():
            print(date)
            print(''.join(schedule))
sample = '''[1518-11-01 00:05] falls asleep
[1518-11-01 00:25] wakes up
[1518-11-01 00:30] falls asleep
[1518-11-01 00:00] Guard #10 begins shift
[1518-11-01 00:55] wakes up
[1518-11-01 23:58] Guard #99 begins shift
[1518-11-02 00:40] falls asleep
[1518-11-02 00:50] wakes up
[1518-11-03 00:05] Guard #10 begins shift
[1518-11-03 00:24] falls asleep
[1518-11-03 00:29] wakes up
[1518-11-04 00:02] Guard #99 begins shift
[1518-11-04 00:36] falls asleep
[1518-11-04 00:46] wakes up
[1518-11-05 00:45] falls asleep
[1518-11-05 00:03] Guard #99 begins shift
[1518-11-05 00:55] wakes up'''

sample = sample.splitlines()
sample = [x.replace('[', '').split(']') for x in sample]
sample.sort(key=lambda x:x[0])
guards_infos = {}
for timestamp, action in sample:
    date, time = timestamp.split(' ')
    if '#' in action:
        guard_number = extract_number_guard_from_str(action)
        day = date[5:10]
        guards_infos[guard_number] = {}
        guards_infos[guard_number][day] = ['.' for _ in range(60)]
    elif 'asleep' in action:
        date, time = timestamp.split(' ')
        asleep_start = int(time[-2:])
    else:
        asleep_end = int(time[-2:])
        for i in range(asleep_start, asleep_end):
            guards_infos[guard_number][day][i] = '#'
print_guards_times(guards_infos)