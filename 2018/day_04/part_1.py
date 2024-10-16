from re import search

def extract_number_guard_from_str(timestamps: list) -> int:
    guard_number_regex = search(r'#(\d+)', timestamps)
    if guard_number_regex:
        guard_number = int(guard_number_regex.group(1))
    return guard_number

def print_guards_times(guards_infos) -> None:
    for number, guards_info in guards_infos.items():
        print('*' * 80)
        print(number)
        print('*' * 80)
        for date, schedule in guards_info.items():
            print(date)
            print(''.join(schedule))

def create_guard_number_if_not_exist() -> None:
    if guard_number not in guards_infos:
        guards_infos[guard_number] = {}

def count_minutes_asleep(days: dict) -> int:
    minutes = 0
    for schedule in days.values():
        minutes += schedule.count('#')
    return minutes

def get_sleepiest_guard(guards: dict) -> int:
    max_minutes_asleep = 0
    sleepiest_guard = None
    for guard, days_schedule in guards.items():  
        minutes_asleep = count_minutes_asleep(days_schedule)
        if minutes_asleep > max_minutes_asleep:
            max_minutes_asleep = minutes_asleep
            sleepiest_guard = guard
    return sleepiest_guard


def get_most_asleep_min(schedule: dict) -> int:
    schedule_list = list(schedule.values())
    most_asleep_minutes = 0
    most_asleep_time = None
    for i in range(len(schedule_list[0])):
        min_asleep = sum(minute[i] == '#' for minute in schedule_list)
        if min_asleep > most_asleep_minutes:
            most_asleep_minutes = min_asleep
            most_asleep_time = i
    return most_asleep_time


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
    day = date[5:10]
    if '#' in action:
        guard_number = extract_number_guard_from_str(action)
        create_guard_number_if_not_exist()
    elif 'asleep' in action:
        if day not in guards_infos[guard_number]:
            guards_infos[guard_number][day] = ['.' for _ in range(60)]
        asleep_start = int(time[-2:])
    else:
        asleep_end = int(time[-2:])

        for i in range(asleep_start, asleep_end):
            guards_infos[guard_number][day][i] = '#'

sleepiest_guard = get_sleepiest_guard(guards_infos)
most_asleep_minute = get_most_asleep_min(guards_infos[sleepiest_guard])
answer = sleepiest_guard * most_asleep_minute
print(answer)