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

def ensure_guard_exists() -> None:
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

sample = '''[1518-07-03 23:58] Guard #2437 begins shift
[1518-09-23 00:54] falls asleep
[1518-05-08 00:02] Guard #659 begins shift
[1518-06-09 00:52] falls asleep
[1518-07-27 00:59] wakes up
[1518-03-04 00:14] falls asleep
[1518-10-28 00:45] falls asleep
[1518-11-14 00:02] Guard #3011 begins shift
[1518-05-15 23:58] Guard #1447 begins shift
[1518-07-29 00:07] falls asleep
[1518-05-20 00:14] falls asleep
[1518-10-18 00:50] wakes up
[1518-09-24 00:02] Guard #1901 begins shift
[1518-10-31 00:20] falls asleep
[1518-08-23 23:49] Guard #3307 begins shift
[1518-09-19 23:52] Guard #2083 begins shift
[1518-02-25 00:51] wakes up
[1518-02-28 00:34] wakes up
[1518-04-29 00:54] wakes up
[1518-07-10 23:59] Guard #1901 begins shift
[1518-10-01 00:52] wakes up
[1518-08-01 00:49] falls asleep
[1518-03-14 00:12] falls asleep
[1518-09-03 00:15] falls asleep
[1518-07-19 00:06] falls asleep
[1518-07-22 00:03] Guard #1307 begins shift
[1518-03-22 00:15] wakes up
[1518-07-08 00:02] falls asleep
[1518-07-06 00:42] wakes up
[1518-03-26 00:58] wakes up
[1518-05-06 00:21] wakes up
[1518-06-07 00:55] wakes up
[1518-10-14 00:37] wakes up
[1518-10-18 00:00] Guard #1009 begins shift
[1518-08-05 00:01] Guard #3307 begins shift
[1518-10-27 00:58] wakes up
[1518-05-27 00:42] falls asleep
[1518-10-05 00:51] wakes up
[1518-06-04 00:39] falls asleep
[1518-06-13 00:21] falls asleep
[1518-09-03 00:01] Guard #991 begins shift
[1518-05-20 00:55] wakes up
[1518-04-19 00:58] wakes up
[1518-10-24 00:02] Guard #991 begins shift
[1518-10-31 00:00] Guard #2269 begins shift
[1518-05-02 00:00] Guard #2437 begins shift
[1518-08-15 00:59] wakes up
[1518-09-12 00:33] wakes up
[1518-08-08 23:56] Guard #3323 begins shift
[1518-11-04 00:16] falls asleep
[1518-07-14 00:57] wakes up
[1518-06-11 00:19] falls asleep
[1518-04-06 23:58] Guard #1307 begins shift
[1518-05-04 00:33] wakes up
[1518-06-30 00:19] falls asleep
[1518-09-14 00:00] Guard #3251 begins shift
[1518-05-13 00:37] wakes up
[1518-08-12 23:50] Guard #3307 begins shift
[1518-07-14 00:18] wakes up
[1518-05-26 00:20] falls asleep
[1518-07-17 00:48] wakes up
[1518-06-15 00:58] wakes up
[1518-07-22 00:29] wakes up
[1518-10-20 00:39] wakes up
[1518-07-12 00:27] falls asleep
[1518-03-17 00:14] falls asleep
[1518-04-28 00:33] falls asleep
[1518-06-12 00:55] falls asleep
[1518-03-08 00:39] falls asleep
[1518-09-05 00:28] wakes up
[1518-05-23 00:49] falls asleep
[1518-07-07 00:02] Guard #1447 begins shift
[1518-11-18 00:56] falls asleep
[1518-09-03 00:40] wakes up
[1518-11-10 00:54] falls asleep
[1518-02-23 00:00] Guard #3323 begins shift
[1518-07-01 00:46] wakes up
[1518-04-24 00:44] wakes up
[1518-09-27 00:14] falls asleep
[1518-09-26 00:04] Guard #2083 begins shift
[1518-05-08 00:31] falls asleep
[1518-05-03 00:19] falls asleep
[1518-07-15 00:01] Guard #991 begins shift
[1518-07-09 00:00] Guard #2437 begins shift
[1518-10-10 00:20] falls asleep
[1518-05-06 00:55] wakes up
[1518-06-13 00:54] falls asleep
[1518-11-06 00:26] falls asleep
[1518-07-16 00:51] wakes up
[1518-08-28 00:10] falls asleep
[1518-06-07 00:35] falls asleep
[1518-07-13 00:41] wakes up
[1518-11-01 00:38] falls asleep
[1518-07-15 00:14] falls asleep
[1518-08-18 00:44] falls asleep
[1518-09-21 23:57] Guard #991 begins shift
[1518-05-30 00:50] wakes up
[1518-09-30 00:47] wakes up
[1518-09-07 00:05] falls asleep
[1518-06-08 00:35] falls asleep
[1518-03-12 23:53] Guard #1901 begins shift
[1518-05-05 00:55] falls asleep
[1518-07-21 00:48] falls asleep
[1518-09-11 00:44] falls asleep
[1518-10-24 23:53] Guard #1307 begins shift
[1518-11-19 00:58] wakes up
[1518-04-03 00:57] wakes up
[1518-04-06 00:54] wakes up
[1518-10-09 23:57] Guard #1447 begins shift
[1518-09-19 00:54] wakes up
[1518-11-10 00:58] wakes up
[1518-08-26 00:42] wakes up
[1518-09-11 00:53] wakes up
[1518-03-18 23:56] Guard #2083 begins shift
[1518-08-01 00:57] wakes up
[1518-07-12 00:01] Guard #1447 begins shift
[1518-10-12 00:34] wakes up
[1518-05-23 00:59] wakes up
[1518-04-16 00:51] wakes up
[1518-03-11 00:04] Guard #1901 begins shift
[1518-08-17 00:40] falls asleep
[1518-10-21 00:17] falls asleep
[1518-07-09 00:15] falls asleep
[1518-08-01 00:01] falls asleep
[1518-03-01 00:45] wakes up
[1518-05-26 00:09] falls asleep
[1518-06-03 00:04] Guard #3307 begins shift
[1518-10-27 00:02] Guard #3307 begins shift
[1518-10-13 00:01] Guard #991 begins shift
[1518-05-04 00:26] falls asleep
[1518-09-10 00:55] wakes up
[1518-07-21 00:25] falls asleep
[1518-07-02 00:45] falls asleep
[1518-04-03 00:17] falls asleep
[1518-10-14 00:32] falls asleep
[1518-07-28 00:03] Guard #127 begins shift
[1518-11-11 00:39] wakes up
[1518-07-16 00:00] Guard #659 begins shift
[1518-06-17 00:01] Guard #2269 begins shift
[1518-05-17 23:53] Guard #3307 begins shift
[1518-07-31 23:49] Guard #1831 begins shift
[1518-03-30 23:59] Guard #467 begins shift
[1518-10-23 00:40] wakes up
[1518-06-25 00:35] wakes up
[1518-04-27 00:44] falls asleep
[1518-08-10 00:22] falls asleep
[1518-05-29 00:50] wakes up
[1518-10-09 00:11] falls asleep
[1518-02-23 23:59] Guard #1303 begins shift
[1518-06-12 00:58] wakes up
[1518-10-12 00:28] falls asleep
[1518-03-07 00:55] wakes up
[1518-10-19 00:50] wakes up
[1518-06-13 00:01] Guard #1307 begins shift
[1518-10-16 00:52] wakes up
[1518-04-26 00:23] falls asleep
[1518-08-08 00:04] falls asleep
[1518-09-14 00:42] falls asleep
[1518-10-12 00:13] falls asleep
[1518-09-20 00:20] wakes up
[1518-09-14 00:57] falls asleep
[1518-07-25 00:02] Guard #2437 begins shift
[1518-07-08 00:56] wakes up
[1518-09-02 00:04] Guard #3307 begins shift
[1518-09-18 00:06] falls asleep
[1518-10-22 00:01] Guard #3011 begins shift
[1518-04-25 00:42] falls asleep
[1518-09-02 00:57] falls asleep
[1518-02-21 23:56] Guard #2239 begins shift
[1518-05-10 00:29] falls asleep
[1518-04-04 23:56] Guard #127 begins shift
[1518-09-28 00:59] wakes up
[1518-10-17 00:12] falls asleep
[1518-04-24 00:01] Guard #1901 begins shift
[1518-09-08 00:16] falls asleep
[1518-11-03 00:47] wakes up
[1518-11-04 00:55] falls asleep
[1518-03-03 00:40] falls asleep
[1518-10-08 00:57] wakes up
[1518-09-14 00:32] falls asleep
[1518-06-25 00:58] wakes up
[1518-09-15 00:33] wakes up
[1518-06-24 00:04] falls asleep
[1518-03-15 00:36] falls asleep
[1518-06-24 23:52] Guard #1447 begins shift
[1518-06-11 00:36] falls asleep
[1518-10-21 00:58] wakes up
[1518-06-17 00:29] wakes up
[1518-08-21 23:59] Guard #467 begins shift
[1518-05-16 00:40] wakes up
[1518-10-07 00:24] falls asleep
[1518-11-04 00:00] Guard #2239 begins shift
[1518-08-30 00:03] Guard #127 begins shift
[1518-05-26 00:04] Guard #2239 begins shift
[1518-05-08 00:52] wakes up
[1518-07-31 00:04] Guard #991 begins shift
[1518-10-11 00:00] Guard #353 begins shift
[1518-09-29 00:38] falls asleep
[1518-04-05 00:48] wakes up
[1518-09-19 00:52] falls asleep
[1518-07-18 00:02] Guard #3323 begins shift
[1518-08-11 23:57] Guard #3011 begins shift
[1518-08-07 23:46] Guard #1307 begins shift
[1518-07-20 23:58] Guard #2083 begins shift
[1518-06-25 00:12] wakes up
[1518-06-12 00:17] falls asleep
[1518-07-23 23:56] Guard #467 begins shift
[1518-03-09 00:17] falls asleep
[1518-07-20 00:35] falls asleep
[1518-05-25 00:22] wakes up
[1518-09-27 00:52] falls asleep
[1518-09-21 00:54] falls asleep
[1518-09-10 00:42] falls asleep
[1518-05-02 00:19] falls asleep
[1518-10-09 00:43] wakes up
[1518-07-11 00:46] wakes up
[1518-06-16 00:51] wakes up
[1518-10-28 00:00] Guard #1303 begins shift
[1518-06-30 00:39] wakes up
[1518-10-14 00:48] wakes up
[1518-11-06 00:37] wakes up
[1518-03-17 00:00] Guard #1831 begins shift
[1518-04-04 00:26] falls asleep
[1518-06-08 00:18] wakes up
[1518-04-23 00:25] falls asleep
[1518-03-25 00:52] wakes up
[1518-09-19 00:01] Guard #659 begins shift
[1518-11-09 00:48] wakes up
[1518-09-17 23:59] Guard #1979 begins shift
[1518-06-01 23:50] Guard #2617 begins shift
[1518-07-22 00:46] falls asleep
[1518-08-06 23:58] Guard #1901 begins shift
[1518-11-23 00:56] wakes up
[1518-05-10 00:37] wakes up
[1518-04-29 00:35] falls asleep
[1518-11-13 00:02] Guard #1307 begins shift
[1518-07-29 00:01] Guard #3323 begins shift
[1518-10-30 00:02] Guard #3251 begins shift
[1518-10-25 00:34] wakes up
[1518-07-08 00:27] falls asleep
[1518-10-16 00:30] falls asleep
[1518-07-03 00:03] Guard #1307 begins shift
[1518-10-16 23:56] Guard #2437 begins shift
[1518-02-22 00:44] falls asleep
[1518-07-25 23:59] Guard #1901 begins shift
[1518-03-15 00:00] Guard #2617 begins shift
[1518-07-07 00:58] wakes up
[1518-02-24 00:59] wakes up
[1518-09-06 23:48] Guard #3251 begins shift
[1518-10-07 00:02] Guard #1979 begins shift
[1518-06-05 00:10] falls asleep
[1518-05-08 23:52] Guard #2269 begins shift
[1518-06-19 23:57] Guard #3307 begins shift
[1518-07-18 00:51] falls asleep
[1518-02-25 00:10] falls asleep
[1518-06-02 00:41] wakes up
[1518-08-27 00:44] wakes up
[1518-07-26 00:08] falls asleep
[1518-10-15 00:10] falls asleep
[1518-04-13 00:17] wakes up
[1518-09-29 23:59] Guard #2437 begins shift
[1518-11-05 00:37] falls asleep
[1518-09-04 00:03] falls asleep
[1518-09-26 23:59] Guard #523 begins shift
[1518-11-09 00:30] falls asleep
[1518-10-28 00:41] wakes up
[1518-03-14 00:53] falls asleep
[1518-05-29 00:08] falls asleep
[1518-04-16 00:32] falls asleep
[1518-11-21 00:16] falls asleep
[1518-11-15 00:01] falls asleep
[1518-08-23 00:52] falls asleep
[1518-03-04 23:59] Guard #2269 begins shift
[1518-05-16 00:19] falls asleep
[1518-07-31 00:53] wakes up
[1518-05-05 00:48] wakes up
[1518-09-27 00:46] wakes up
[1518-05-23 00:44] falls asleep
[1518-09-11 00:03] Guard #2617 begins shift
[1518-05-10 00:02] falls asleep
[1518-03-30 00:37] wakes up
[1518-04-24 00:58] wakes up
[1518-06-20 00:57] wakes up
[1518-11-02 00:34] wakes up
[1518-04-21 00:55] wakes up
[1518-08-30 00:34] falls asleep
[1518-10-09 00:20] wakes up
[1518-03-02 00:19] wakes up
[1518-08-18 00:29] falls asleep
[1518-11-16 00:42] falls asleep
[1518-06-16 00:00] Guard #523 begins shift
[1518-05-18 00:44] falls asleep
[1518-09-05 23:59] Guard #2083 begins shift
[1518-09-19 00:46] falls asleep
[1518-11-16 00:00] Guard #1303 begins shift
[1518-04-27 00:33] wakes up
[1518-07-30 00:04] Guard #2437 begins shift
[1518-08-24 00:54] wakes up
[1518-03-10 00:43] falls asleep
[1518-10-06 00:03] Guard #1979 begins shift
[1518-08-10 00:02] Guard #2437 begins shift
[1518-09-10 00:07] falls asleep
[1518-07-31 00:29] falls asleep
[1518-05-19 00:31] wakes up
[1518-02-28 00:00] Guard #991 begins shift
[1518-03-14 00:50] wakes up
[1518-09-20 23:46] Guard #1901 begins shift
[1518-06-26 00:17] falls asleep
[1518-07-04 00:49] wakes up
[1518-07-04 23:58] Guard #2437 begins shift
[1518-04-11 00:55] wakes up
[1518-08-05 00:49] wakes up
[1518-11-01 00:49] falls asleep
[1518-04-25 23:59] Guard #2437 begins shift
[1518-04-28 00:27] falls asleep
[1518-05-27 00:21] falls asleep
[1518-03-14 00:58] wakes up
[1518-07-04 00:39] falls asleep
[1518-10-22 00:53] wakes up
[1518-05-19 00:57] wakes up
[1518-11-12 00:57] wakes up
[1518-07-21 00:58] wakes up
[1518-04-28 00:42] wakes up
[1518-08-04 00:15] falls asleep
[1518-10-24 00:27] falls asleep
[1518-09-18 00:53] falls asleep
[1518-03-19 00:44] falls asleep
[1518-11-11 00:54] wakes up
[1518-03-10 00:57] wakes up
[1518-08-01 00:20] wakes up
[1518-03-07 00:08] falls asleep
[1518-03-09 00:53] wakes up
[1518-06-13 00:22] wakes up
[1518-06-29 00:54] wakes up
[1518-09-21 00:05] falls asleep
[1518-08-26 00:14] falls asleep
[1518-04-23 00:54] falls asleep
[1518-07-22 00:58] wakes up
[1518-07-03 00:46] falls asleep
[1518-04-17 00:29] wakes up
[1518-06-22 00:34] falls asleep
[1518-03-13 00:01] falls asleep
[1518-08-11 00:58] wakes up
[1518-09-01 00:25] falls asleep
[1518-09-01 00:53] wakes up
[1518-06-12 00:02] Guard #3307 begins shift
[1518-05-01 00:56] wakes up
[1518-04-11 00:04] Guard #127 begins shift
[1518-05-29 23:59] Guard #2083 begins shift
[1518-03-18 00:03] falls asleep
[1518-10-05 00:04] Guard #991 begins shift
[1518-06-14 23:57] Guard #659 begins shift
[1518-10-28 00:15] falls asleep
[1518-03-10 00:02] Guard #1307 begins shift
[1518-04-15 00:21] falls asleep
[1518-08-31 23:56] Guard #1447 begins shift
[1518-06-22 00:57] wakes up
[1518-08-24 00:59] wakes up
[1518-09-08 00:46] falls asleep
[1518-08-24 00:05] falls asleep
[1518-09-09 23:56] Guard #1447 begins shift
[1518-10-02 00:59] wakes up
[1518-11-17 00:33] falls asleep
[1518-04-19 00:34] wakes up
[1518-04-30 00:45] falls asleep
[1518-08-02 00:27] wakes up
[1518-11-05 00:47] wakes up
[1518-05-24 00:43] wakes up
[1518-06-25 00:25] wakes up
[1518-10-09 00:23] falls asleep
[1518-09-16 00:51] wakes up
[1518-06-29 00:57] falls asleep
[1518-11-12 00:03] Guard #3011 begins shift
[1518-07-14 00:00] Guard #3251 begins shift
[1518-06-20 00:51] falls asleep
[1518-11-04 00:32] wakes up
[1518-05-19 00:00] Guard #3323 begins shift
[1518-04-19 00:15] falls asleep
[1518-07-21 00:44] wakes up
[1518-05-30 00:23] falls asleep
[1518-05-15 00:00] Guard #353 begins shift
[1518-08-05 23:58] Guard #2269 begins shift
[1518-09-15 00:52] wakes up
[1518-07-01 00:18] falls asleep
[1518-05-18 00:38] wakes up
[1518-03-02 23:58] Guard #3307 begins shift
[1518-09-23 00:58] wakes up
[1518-05-20 00:35] falls asleep
[1518-05-05 00:30] falls asleep
[1518-09-23 00:44] wakes up
[1518-08-25 00:03] Guard #3011 begins shift
[1518-04-22 00:00] falls asleep
[1518-05-10 00:24] wakes up
[1518-06-27 00:43] wakes up
[1518-03-05 00:45] wakes up
[1518-11-19 00:18] falls asleep
[1518-09-24 00:08] falls asleep
[1518-06-29 00:10] falls asleep
[1518-04-11 00:29] wakes up
[1518-06-23 23:52] Guard #1303 begins shift
[1518-04-20 00:13] wakes up
[1518-06-03 00:40] falls asleep
[1518-03-23 00:59] wakes up
[1518-05-03 00:04] Guard #2437 begins shift
[1518-11-11 00:19] falls asleep
[1518-09-21 00:50] wakes up
[1518-07-12 00:47] wakes up
[1518-06-01 00:37] wakes up
[1518-06-03 00:58] wakes up
[1518-07-18 00:47] wakes up
[1518-07-02 00:39] wakes up
[1518-11-06 00:02] Guard #3323 begins shift
[1518-03-02 00:02] falls asleep
[1518-07-03 00:53] wakes up
[1518-06-06 00:38] wakes up
[1518-04-27 23:56] Guard #2437 begins shift
[1518-06-28 00:23] falls asleep
[1518-11-06 00:42] falls asleep
[1518-03-27 00:30] falls asleep
[1518-11-11 00:31] falls asleep
[1518-04-20 00:24] falls asleep
[1518-06-26 00:49] wakes up
[1518-08-01 00:54] falls asleep
[1518-05-03 00:40] wakes up
[1518-08-23 00:57] wakes up
[1518-10-07 00:44] wakes up
[1518-09-20 00:04] falls asleep
[1518-09-04 00:48] wakes up
[1518-07-18 00:59] wakes up
[1518-06-18 00:56] wakes up
[1518-11-01 00:46] wakes up
[1518-10-28 00:28] falls asleep
[1518-05-04 00:01] Guard #2239 begins shift
[1518-02-24 00:27] falls asleep
[1518-04-30 00:02] Guard #127 begins shift
[1518-09-22 00:45] falls asleep
[1518-06-15 00:44] falls asleep
[1518-08-16 00:45] falls asleep
[1518-07-02 00:50] wakes up
[1518-05-31 00:24] wakes up
[1518-02-27 00:24] falls asleep
[1518-07-30 00:20] falls asleep
[1518-05-16 00:46] falls asleep
[1518-05-25 00:00] falls asleep
[1518-11-13 00:23] falls asleep
[1518-05-22 00:00] Guard #467 begins shift
[1518-04-08 23:50] Guard #1901 begins shift
[1518-05-06 00:42] falls asleep
[1518-03-25 00:43] falls asleep
[1518-04-07 00:56] wakes up
[1518-11-19 00:00] Guard #991 begins shift
[1518-05-20 23:51] Guard #1901 begins shift
[1518-03-10 00:51] wakes up
[1518-10-12 00:38] falls asleep
[1518-06-26 00:02] Guard #3011 begins shift
[1518-09-11 00:17] falls asleep
[1518-05-18 00:55] wakes up
[1518-10-02 00:08] falls asleep
[1518-11-05 00:00] Guard #3251 begins shift
[1518-05-09 00:46] wakes up
[1518-06-26 23:59] Guard #1009 begins shift
[1518-06-27 00:14] falls asleep
[1518-06-29 00:23] wakes up
[1518-04-13 23:58] Guard #1307 begins shift
[1518-09-13 00:00] Guard #467 begins shift
[1518-08-04 00:35] falls asleep
[1518-04-08 00:54] wakes up
[1518-05-24 23:52] Guard #523 begins shift
[1518-02-24 00:35] wakes up
[1518-08-08 00:51] wakes up
[1518-05-28 00:59] wakes up
[1518-11-14 00:18] falls asleep
[1518-04-09 00:32] wakes up
[1518-05-17 00:46] wakes up
[1518-11-03 00:28] falls asleep
[1518-09-27 00:57] wakes up
[1518-08-24 00:16] wakes up
[1518-03-20 00:01] falls asleep
[1518-06-16 00:42] wakes up
[1518-08-14 00:22] falls asleep
[1518-08-18 00:53] wakes up
[1518-04-27 00:01] Guard #2437 begins shift
[1518-03-29 00:00] Guard #3251 begins shift
[1518-08-02 00:08] falls asleep
[1518-06-21 00:26] falls asleep
[1518-03-22 00:12] falls asleep
[1518-11-10 23:58] Guard #1447 begins shift
[1518-03-29 23:59] Guard #2617 begins shift
[1518-06-09 00:18] falls asleep
[1518-04-25 00:59] wakes up
[1518-03-29 00:32] falls asleep
[1518-03-17 00:25] wakes up
[1518-04-10 00:07] falls asleep
[1518-08-03 00:57] wakes up
[1518-08-12 00:48] wakes up
[1518-07-29 00:56] wakes up
[1518-05-27 00:11] falls asleep
[1518-06-21 00:22] wakes up
[1518-04-28 00:30] wakes up
[1518-06-08 00:39] wakes up
[1518-11-01 00:56] wakes up
[1518-08-18 00:36] wakes up
[1518-08-17 00:51] wakes up
[1518-06-22 00:01] Guard #523 begins shift
[1518-04-13 00:13] falls asleep
[1518-07-28 00:53] falls asleep
[1518-05-14 00:01] Guard #1831 begins shift
[1518-10-02 00:34] wakes up
[1518-05-19 00:25] falls asleep
[1518-07-14 00:36] falls asleep
[1518-04-17 23:46] Guard #2269 begins shift
[1518-09-20 00:33] falls asleep
[1518-04-22 00:41] wakes up
[1518-03-17 23:53] Guard #2083 begins shift
[1518-08-13 00:03] falls asleep
[1518-03-10 00:23] falls asleep
[1518-03-30 00:08] falls asleep
[1518-08-31 00:42] wakes up
[1518-11-18 00:00] Guard #3307 begins shift
[1518-03-14 00:49] falls asleep
[1518-08-17 23:58] Guard #2083 begins shift
[1518-11-14 23:48] Guard #1307 begins shift
[1518-05-18 00:12] wakes up
[1518-07-13 00:18] falls asleep
[1518-08-23 00:04] Guard #3307 begins shift
[1518-08-20 00:32] falls asleep
[1518-06-14 00:16] falls asleep
[1518-09-21 00:56] wakes up
[1518-06-22 23:50] Guard #2437 begins shift
[1518-09-23 00:39] falls asleep
[1518-10-04 00:08] falls asleep
[1518-04-17 00:27] falls asleep
[1518-09-14 00:52] wakes up
[1518-06-13 00:47] wakes up
[1518-08-17 00:04] Guard #127 begins shift
[1518-07-22 00:24] falls asleep
[1518-09-09 00:57] wakes up
[1518-07-13 00:01] Guard #2083 begins shift
[1518-03-27 00:45] wakes up
[1518-04-04 00:16] falls asleep
[1518-11-11 00:53] falls asleep
[1518-06-30 23:56] Guard #523 begins shift
[1518-04-18 00:02] falls asleep
[1518-10-25 00:01] falls asleep
[1518-09-14 00:39] wakes up
[1518-04-09 00:02] falls asleep
[1518-03-10 00:54] falls asleep
[1518-10-23 00:13] falls asleep
[1518-04-22 23:57] Guard #1307 begins shift
[1518-06-17 00:12] falls asleep
[1518-04-15 00:47] wakes up
[1518-09-05 00:50] wakes up
[1518-10-31 00:45] wakes up
[1518-06-21 00:58] wakes up
[1518-03-16 00:51] wakes up
[1518-07-25 00:43] falls asleep
[1518-08-29 00:51] falls asleep
[1518-06-28 23:58] Guard #1979 begins shift
[1518-08-16 00:53] wakes up
[1518-09-12 00:20] falls asleep
[1518-06-29 00:48] falls asleep
[1518-09-19 00:48] wakes up
[1518-09-15 00:24] falls asleep
[1518-03-01 00:26] wakes up
[1518-08-24 00:57] falls asleep
[1518-03-01 00:21] wakes up
[1518-04-07 00:25] falls asleep
[1518-11-23 00:49] falls asleep
[1518-07-16 23:59] Guard #2083 begins shift
[1518-07-08 00:24] wakes up
[1518-05-13 00:19] falls asleep
[1518-10-20 00:47] falls asleep
[1518-05-27 00:26] wakes up
[1518-09-03 23:46] Guard #1901 begins shift
[1518-05-24 00:20] falls asleep
[1518-03-06 00:17] falls asleep
[1518-10-12 00:51] wakes up
[1518-03-20 00:31] falls asleep
[1518-08-02 00:48] wakes up
[1518-05-12 23:58] Guard #523 begins shift
[1518-09-17 00:06] falls asleep
[1518-07-02 00:33] falls asleep
[1518-06-06 00:16] falls asleep
[1518-02-28 23:57] Guard #2239 begins shift
[1518-04-13 00:22] falls asleep
[1518-08-31 00:03] falls asleep
[1518-03-06 00:00] Guard #1979 begins shift
[1518-05-21 00:41] falls asleep
[1518-11-07 00:12] falls asleep
[1518-07-25 00:17] falls asleep
[1518-06-09 00:53] wakes up
[1518-10-30 00:06] falls asleep
[1518-06-25 00:44] falls asleep
[1518-10-22 23:56] Guard #2239 begins shift
[1518-08-21 00:54] wakes up
[1518-04-15 23:58] Guard #659 begins shift
[1518-08-29 00:53] wakes up
[1518-09-29 00:01] Guard #1901 begins shift
[1518-03-18 00:56] wakes up
[1518-06-11 00:31] wakes up
[1518-11-20 23:59] Guard #1831 begins shift
[1518-04-16 23:58] Guard #1447 begins shift
[1518-02-28 00:15] falls asleep
[1518-06-04 00:54] wakes up
[1518-04-18 00:53] falls asleep
[1518-11-16 00:59] wakes up
[1518-04-08 00:03] Guard #2617 begins shift
[1518-06-17 23:56] Guard #1447 begins shift
[1518-05-06 00:04] Guard #1979 begins shift
[1518-08-13 00:53] wakes up
[1518-04-03 23:57] Guard #1447 begins shift
[1518-10-12 00:00] Guard #3323 begins shift
[1518-11-09 23:48] Guard #2269 begins shift
[1518-07-09 00:51] wakes up
[1518-11-02 00:27] falls asleep
[1518-03-13 00:22] wakes up
[1518-09-05 00:45] falls asleep
[1518-11-17 00:00] Guard #2239 begins shift
[1518-10-14 00:44] falls asleep
[1518-09-25 00:06] falls asleep
[1518-05-31 23:59] Guard #2083 begins shift
[1518-05-10 23:57] Guard #127 begins shift
[1518-07-31 00:58] wakes up
[1518-03-23 00:04] Guard #2269 begins shift
[1518-11-21 23:56] Guard #1901 begins shift
[1518-08-27 00:17] falls asleep
[1518-08-07 00:48] wakes up
[1518-05-23 00:45] wakes up
[1518-06-09 00:49] wakes up
[1518-05-02 00:53] falls asleep
[1518-03-05 00:37] falls asleep
[1518-06-18 00:21] falls asleep
[1518-05-31 00:45] wakes up
[1518-09-06 00:38] falls asleep
[1518-11-16 00:52] wakes up
[1518-03-16 00:03] Guard #991 begins shift
[1518-05-12 00:32] falls asleep
[1518-10-07 23:58] Guard #2239 begins shift
[1518-07-03 00:26] falls asleep
[1518-07-28 00:48] wakes up
[1518-05-28 00:14] falls asleep
[1518-10-31 00:42] falls asleep
[1518-09-11 23:59] Guard #991 begins shift
[1518-07-17 00:20] falls asleep
[1518-03-19 00:53] wakes up
[1518-04-03 00:00] Guard #991 begins shift
[1518-10-01 00:04] falls asleep
[1518-07-03 00:31] wakes up
[1518-02-25 00:40] falls asleep
[1518-03-04 00:04] Guard #1307 begins shift
[1518-09-18 00:08] wakes up
[1518-11-06 23:58] Guard #3011 begins shift
[1518-08-24 00:46] falls asleep
[1518-06-13 00:39] falls asleep
[1518-05-23 23:58] Guard #3323 begins shift
[1518-05-16 23:57] Guard #3011 begins shift
[1518-08-03 00:24] falls asleep
[1518-05-03 00:58] wakes up
[1518-10-06 00:53] wakes up
[1518-11-01 23:59] Guard #2239 begins shift
[1518-06-02 00:05] falls asleep
[1518-04-28 23:58] Guard #127 begins shift
[1518-07-27 00:02] Guard #1979 begins shift
[1518-04-19 00:53] falls asleep
[1518-08-04 00:00] Guard #1831 begins shift
[1518-04-05 00:36] falls asleep
[1518-03-08 00:49] wakes up
[1518-03-26 00:51] falls asleep
[1518-05-18 00:18] falls asleep
[1518-04-24 23:59] Guard #3251 begins shift
[1518-11-09 00:14] falls asleep
[1518-08-25 00:27] falls asleep
[1518-10-29 00:04] Guard #1979 begins shift
[1518-02-26 00:22] falls asleep
[1518-07-07 23:46] Guard #1307 begins shift
[1518-09-30 23:52] Guard #1901 begins shift
[1518-03-31 23:56] Guard #467 begins shift
[1518-08-06 00:46] falls asleep
[1518-11-19 23:59] Guard #467 begins shift
[1518-04-15 00:03] Guard #991 begins shift
[1518-04-19 23:46] Guard #523 begins shift
[1518-07-10 00:30] falls asleep
[1518-07-31 00:43] falls asleep
[1518-09-07 00:51] wakes up
[1518-06-18 23:46] Guard #127 begins shift
[1518-04-08 00:18] falls asleep
[1518-04-02 00:58] wakes up
[1518-05-19 00:41] falls asleep
[1518-10-18 00:37] falls asleep
[1518-10-22 00:16] falls asleep
[1518-06-26 00:36] falls asleep
[1518-03-20 00:21] wakes up
[1518-03-01 23:48] Guard #3251 begins shift
[1518-09-08 00:55] wakes up
[1518-10-08 00:44] falls asleep
[1518-06-08 00:01] falls asleep
[1518-10-05 00:24] falls asleep
[1518-02-23 00:43] falls asleep
[1518-03-23 00:37] falls asleep
[1518-07-28 00:58] wakes up
[1518-05-17 00:36] falls asleep
[1518-08-11 00:06] falls asleep
[1518-04-13 00:37] wakes up
[1518-03-11 23:59] Guard #353 begins shift
[1518-08-23 00:24] falls asleep
[1518-04-19 00:50] wakes up
[1518-06-05 00:54] wakes up
[1518-07-31 00:57] falls asleep
[1518-07-25 00:58] wakes up
[1518-06-12 00:26] wakes up
[1518-08-19 23:57] Guard #1009 begins shift
[1518-08-15 00:51] wakes up
[1518-02-27 00:01] Guard #1979 begins shift
[1518-09-16 00:31] falls asleep
[1518-06-20 23:46] Guard #991 begins shift
[1518-09-14 00:59] wakes up
[1518-04-21 23:48] Guard #1307 begins shift
[1518-09-16 23:58] Guard #1979 begins shift
[1518-03-11 00:59] wakes up
[1518-04-13 00:02] Guard #3307 begins shift
[1518-09-20 00:59] wakes up
[1518-02-25 23:57] Guard #1901 begins shift
[1518-10-02 00:00] Guard #1009 begins shift
[1518-08-16 00:00] Guard #991 begins shift
[1518-09-17 00:27] wakes up
[1518-06-09 00:58] wakes up
[1518-04-25 00:09] falls asleep
[1518-03-17 00:32] falls asleep
[1518-07-15 00:27] wakes up
[1518-09-10 00:32] wakes up
[1518-05-02 00:58] wakes up
[1518-09-25 00:44] wakes up
[1518-06-01 00:36] falls asleep
[1518-07-16 00:40] falls asleep
[1518-11-18 00:59] wakes up
[1518-11-17 00:09] falls asleep
[1518-05-01 00:30] falls asleep
[1518-08-10 00:53] wakes up
[1518-11-08 00:58] wakes up
[1518-05-31 00:00] falls asleep
[1518-03-15 00:42] wakes up
[1518-07-05 00:58] wakes up
[1518-03-27 00:04] Guard #2239 begins shift
[1518-10-06 00:16] falls asleep
[1518-07-10 00:54] wakes up
[1518-04-12 00:38] wakes up
[1518-07-05 00:23] falls asleep
[1518-11-19 00:37] wakes up
[1518-06-30 00:00] Guard #3011 begins shift
[1518-10-27 00:43] falls asleep
[1518-04-01 23:56] Guard #991 begins shift
[1518-04-04 00:28] wakes up
[1518-05-22 23:59] Guard #3307 begins shift
[1518-05-06 00:06] falls asleep
[1518-04-25 00:35] wakes up
[1518-04-24 00:07] falls asleep
[1518-07-05 00:35] wakes up
[1518-10-26 00:02] Guard #2753 begins shift
[1518-05-31 00:34] falls asleep
[1518-10-17 00:55] wakes up
[1518-04-19 00:49] falls asleep
[1518-03-13 23:57] Guard #2239 begins shift
[1518-11-21 00:46] wakes up
[1518-03-22 00:04] Guard #3307 begins shift
[1518-05-09 23:50] Guard #991 begins shift
[1518-03-03 00:59] wakes up
[1518-03-02 00:59] wakes up
[1518-04-20 00:48] wakes up
[1518-05-18 00:01] falls asleep
[1518-08-02 00:55] falls asleep
[1518-08-30 00:57] wakes up
[1518-05-27 00:52] wakes up
[1518-06-07 23:46] Guard #127 begins shift
[1518-08-02 00:57] wakes up
[1518-10-10 00:55] wakes up
[1518-02-24 00:53] falls asleep
[1518-04-11 23:56] Guard #1979 begins shift
[1518-10-19 00:00] Guard #1979 begins shift
[1518-09-11 00:29] wakes up
[1518-05-27 00:01] Guard #1831 begins shift
[1518-06-19 00:40] falls asleep
[1518-05-28 00:00] Guard #3011 begins shift
[1518-10-15 00:01] Guard #3011 begins shift
[1518-06-07 00:00] Guard #2239 begins shift
[1518-09-29 00:45] wakes up
[1518-06-29 00:58] wakes up
[1518-10-30 00:45] wakes up
[1518-06-10 00:10] falls asleep
[1518-05-09 00:32] wakes up
[1518-05-28 23:57] Guard #3011 begins shift
[1518-05-09 00:35] falls asleep
[1518-10-09 00:01] Guard #1979 begins shift
[1518-06-24 00:36] wakes up
[1518-07-22 23:59] Guard #3323 begins shift
[1518-11-06 00:46] wakes up
[1518-03-16 00:16] falls asleep
[1518-05-14 00:41] falls asleep
[1518-07-06 00:00] Guard #2239 begins shift
[1518-08-17 00:56] falls asleep
[1518-07-02 00:02] Guard #1009 begins shift
[1518-03-17 00:50] wakes up
[1518-09-15 00:04] Guard #1009 begins shift
[1518-06-14 00:03] Guard #3323 begins shift
[1518-05-16 00:24] wakes up
[1518-10-25 00:57] wakes up
[1518-04-10 00:04] Guard #1303 begins shift
[1518-05-05 00:56] wakes up
[1518-06-03 00:46] wakes up
[1518-05-05 00:02] Guard #1901 begins shift
[1518-05-20 00:29] wakes up
[1518-10-21 00:00] Guard #3251 begins shift
[1518-11-17 00:19] wakes up
[1518-02-27 00:48] wakes up
[1518-11-07 23:57] Guard #659 begins shift
[1518-06-11 00:01] Guard #2239 begins shift
[1518-06-28 00:41] wakes up
[1518-04-30 00:57] wakes up
[1518-11-10 00:40] wakes up
[1518-11-22 00:38] falls asleep
[1518-04-12 00:31] falls asleep
[1518-07-27 00:46] falls asleep
[1518-04-07 00:48] falls asleep
[1518-05-03 00:48] falls asleep
[1518-05-07 00:39] wakes up
[1518-06-26 00:30] wakes up
[1518-07-12 00:59] wakes up
[1518-06-03 23:59] Guard #127 begins shift
[1518-10-15 00:41] wakes up
[1518-08-05 00:17] falls asleep
[1518-05-16 00:47] wakes up
[1518-07-06 00:21] falls asleep
[1518-07-26 00:29] wakes up
[1518-07-19 00:48] wakes up
[1518-10-29 00:49] wakes up
[1518-09-22 00:55] wakes up
[1518-07-20 00:57] wakes up
[1518-08-15 00:00] Guard #2269 begins shift
[1518-09-05 00:01] Guard #1307 begins shift
[1518-08-02 00:02] Guard #2437 begins shift
[1518-10-29 00:42] falls asleep
[1518-03-23 23:54] Guard #1303 begins shift
[1518-05-12 00:44] wakes up
[1518-09-24 00:34] wakes up
[1518-08-13 23:57] Guard #1447 begins shift
[1518-06-16 00:48] falls asleep
[1518-06-08 23:58] Guard #127 begins shift
[1518-10-24 00:48] wakes up
[1518-03-26 00:07] falls asleep
[1518-10-28 00:23] wakes up
[1518-07-31 00:38] wakes up
[1518-08-27 23:58] Guard #1307 begins shift
[1518-08-04 00:47] wakes up
[1518-09-02 00:58] wakes up
[1518-09-23 00:02] Guard #2617 begins shift
[1518-02-22 00:19] falls asleep
[1518-05-16 00:35] falls asleep
[1518-10-04 00:51] wakes up
[1518-03-27 23:51] Guard #1009 begins shift
[1518-08-23 00:32] wakes up
[1518-08-11 00:00] Guard #1447 begins shift
[1518-06-25 00:22] falls asleep
[1518-05-11 00:35] wakes up
[1518-07-19 00:02] Guard #1447 begins shift
[1518-09-15 00:42] falls asleep
[1518-05-21 00:29] wakes up
[1518-05-12 00:01] Guard #3011 begins shift
[1518-08-29 00:27] falls asleep
[1518-02-23 00:50] wakes up
[1518-08-30 23:54] Guard #1831 begins shift
[1518-06-28 00:01] Guard #1307 begins shift
[1518-07-19 23:59] Guard #659 begins shift
[1518-04-06 00:04] Guard #523 begins shift
[1518-06-10 00:16] wakes up
[1518-06-09 00:56] falls asleep
[1518-02-26 00:58] wakes up
[1518-02-23 00:31] falls asleep
[1518-08-21 00:16] falls asleep
[1518-04-14 00:58] wakes up
[1518-11-10 00:05] falls asleep
[1518-03-09 00:00] Guard #1447 begins shift
[1518-06-23 00:04] falls asleep
[1518-09-09 00:05] falls asleep
[1518-07-05 00:50] falls asleep
[1518-10-12 00:24] wakes up
[1518-04-06 00:37] falls asleep
[1518-08-02 00:42] falls asleep
[1518-02-25 00:36] wakes up
[1518-03-28 00:00] falls asleep
[1518-09-25 00:00] Guard #2239 begins shift
[1518-11-18 00:52] wakes up
[1518-11-07 00:55] wakes up
[1518-10-20 00:00] Guard #3323 begins shift
[1518-05-21 00:46] wakes up
[1518-08-20 23:59] Guard #2437 begins shift
[1518-11-17 00:34] wakes up
[1518-04-27 00:19] falls asleep
[1518-06-10 00:00] Guard #3307 begins shift
[1518-03-14 00:44] wakes up
[1518-05-25 00:39] wakes up
[1518-10-17 00:36] falls asleep
[1518-11-09 00:02] Guard #523 begins shift
[1518-08-09 00:38] wakes up
[1518-09-26 00:53] wakes up
[1518-03-01 00:25] falls asleep
[1518-03-28 00:44] wakes up
[1518-11-11 00:27] wakes up
[1518-06-19 00:34] wakes up
[1518-05-11 00:33] falls asleep
[1518-05-26 00:39] wakes up
[1518-08-19 00:30] falls asleep
[1518-06-13 00:59] wakes up
[1518-04-11 00:06] falls asleep
[1518-06-05 00:02] Guard #1447 begins shift
[1518-02-22 00:37] wakes up
[1518-07-30 00:57] wakes up
[1518-03-26 00:46] wakes up
[1518-06-23 00:34] wakes up
[1518-08-14 00:57] wakes up
[1518-06-06 00:03] Guard #1979 begins shift
[1518-10-03 00:02] Guard #467 begins shift
[1518-09-15 23:57] Guard #1901 begins shift
[1518-03-24 00:35] wakes up
[1518-04-14 00:24] falls asleep
[1518-07-23 00:45] wakes up
[1518-04-11 00:50] falls asleep
[1518-08-15 00:54] falls asleep
[1518-02-25 00:03] Guard #1307 begins shift
[1518-07-17 00:59] wakes up
[1518-10-04 00:03] Guard #1831 begins shift
[1518-07-11 00:32] falls asleep
[1518-08-25 00:49] wakes up
[1518-03-08 00:00] Guard #1901 begins shift
[1518-11-16 00:56] falls asleep
[1518-08-19 00:03] Guard #1009 begins shift
[1518-08-12 00:27] falls asleep
[1518-11-09 00:27] wakes up
[1518-04-10 00:48] wakes up
[1518-11-14 00:32] wakes up
[1518-10-28 00:50] wakes up
[1518-10-15 23:56] Guard #1901 begins shift
[1518-07-14 00:10] falls asleep
[1518-09-18 00:54] wakes up
[1518-07-10 00:00] Guard #3323 begins shift
[1518-08-28 00:31] wakes up
[1518-06-21 00:05] falls asleep
[1518-04-02 00:27] falls asleep
[1518-10-20 00:33] falls asleep
[1518-05-09 00:01] falls asleep
[1518-03-26 00:02] Guard #1901 begins shift
[1518-10-13 00:41] wakes up
[1518-06-03 00:55] falls asleep
[1518-04-18 00:58] wakes up
[1518-07-25 00:20] wakes up
[1518-08-04 00:30] wakes up
[1518-05-30 23:51] Guard #2617 begins shift
[1518-08-01 00:50] wakes up
[1518-11-12 00:26] falls asleep
[1518-04-21 00:00] Guard #991 begins shift
[1518-11-14 00:55] wakes up
[1518-07-12 00:57] falls asleep
[1518-08-09 00:36] falls asleep
[1518-08-19 00:34] wakes up
[1518-04-23 00:30] wakes up
[1518-02-22 00:54] wakes up
[1518-09-26 00:51] falls asleep
[1518-03-20 00:56] wakes up
[1518-11-08 00:25] falls asleep
[1518-11-19 00:51] falls asleep
[1518-10-13 23:56] Guard #1979 begins shift
[1518-04-07 00:36] wakes up
[1518-05-25 00:28] falls asleep
[1518-04-23 00:58] wakes up
[1518-04-18 00:46] wakes up
[1518-09-11 00:57] falls asleep
[1518-04-27 00:52] wakes up
[1518-11-18 00:35] falls asleep
[1518-09-05 00:26] falls asleep
[1518-11-15 00:58] wakes up
[1518-02-23 00:40] wakes up
[1518-10-02 00:37] falls asleep
[1518-08-27 00:00] Guard #3011 begins shift
[1518-04-13 00:49] falls asleep
[1518-07-28 00:20] falls asleep
[1518-03-04 00:47] wakes up
[1518-03-24 00:04] falls asleep
[1518-03-20 23:58] Guard #2753 begins shift
[1518-11-14 00:45] falls asleep
[1518-09-11 00:59] wakes up
[1518-06-16 00:40] falls asleep
[1518-05-27 00:12] wakes up
[1518-11-01 00:00] Guard #1447 begins shift
[1518-08-28 23:58] Guard #1307 begins shift
[1518-05-21 00:04] falls asleep
[1518-07-23 00:38] falls asleep
[1518-05-02 00:49] wakes up
[1518-03-24 23:57] Guard #2269 begins shift
[1518-06-25 00:30] falls asleep
[1518-08-02 23:56] Guard #3011 begins shift
[1518-05-07 00:00] Guard #2617 begins shift
[1518-04-26 00:57] wakes up
[1518-04-21 00:19] falls asleep
[1518-04-04 00:18] wakes up
[1518-04-18 23:57] Guard #659 begins shift
[1518-07-18 00:41] falls asleep
[1518-09-08 00:40] wakes up
[1518-09-28 00:33] falls asleep
[1518-11-03 00:04] Guard #3323 begins shift
[1518-08-15 00:26] falls asleep
[1518-10-19 00:14] falls asleep
[1518-03-01 00:10] falls asleep
[1518-06-14 00:45] wakes up
[1518-06-19 00:55] wakes up
[1518-06-11 00:41] wakes up
[1518-03-02 00:29] falls asleep
[1518-09-18 00:40] falls asleep
[1518-07-17 00:54] falls asleep
[1518-11-13 00:33] wakes up
[1518-09-30 00:15] falls asleep
[1518-11-04 00:59] wakes up
[1518-04-24 00:57] falls asleep
[1518-09-06 00:40] wakes up
[1518-10-20 00:59] wakes up
[1518-05-26 00:10] wakes up
[1518-08-20 00:56] wakes up
[1518-06-19 00:04] falls asleep
[1518-05-07 00:33] falls asleep
[1518-10-31 00:21] wakes up
[1518-04-13 00:55] wakes up
[1518-11-22 00:42] wakes up
[1518-10-17 00:20] wakes up
[1518-03-19 23:47] Guard #2083 begins shift
[1518-08-26 00:01] Guard #523 begins shift
[1518-04-20 00:01] falls asleep
[1518-11-23 00:00] Guard #3307 begins shift
[1518-03-10 00:28] wakes up
[1518-09-18 00:45] wakes up
[1518-07-07 00:19] falls asleep
[1518-09-23 00:14] falls asleep
[1518-08-17 00:59] wakes up
[1518-10-13 00:32] falls asleep
[1518-03-01 00:31] falls asleep
[1518-10-25 00:49] falls asleep
[1518-08-07 00:27] falls asleep
[1518-03-06 00:58] wakes up
[1518-08-29 00:32] wakes up
[1518-09-23 00:17] wakes up
[1518-03-07 00:01] Guard #3251 begins shift
[1518-08-06 00:53] wakes up
[1518-09-27 23:56] Guard #3011 begins shift
[1518-04-30 23:57] Guard #3323 begins shift
[1518-03-11 00:13] falls asleep
[1518-05-20 00:00] Guard #1979 begins shift
[1518-03-29 00:47] wakes up
[1518-09-08 00:02] Guard #127 begins shift
[1518-09-08 23:47] Guard #2437 begins shift
[1518-05-14 00:53] wakes up
[1518-06-25 00:02] falls asleep'''



sample = sample.splitlines()
sample = [x.replace('[', '').split(']') for x in sample]
sample.sort(key=lambda x:x[0])
guards_infos = {}
for timestamp, action in sample:
    date, time = timestamp.split(' ')
    day = date[5:10]
    if '#' in action:
        guard_number = extract_number_guard_from_str(action)
        ensure_guard_exists()
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