def format_duration(seconds):
    if seconds == 0:
        return "now"
    MINUTE = 60
    HOUR = MINUTE*60
    DAY  = HOUR*24
    YEAR = DAY*365

    def pluralising(value, string):
        if value == 1:
            return f"{value} {string}"
        if value > 1:
            return f"{value} {string}" + "s"
        return None

    years, seconds = divmod(seconds, YEAR)
    days, seconds = divmod(seconds, DAY)
    hours, seconds = divmod(seconds, HOUR)
    minutes, seconds = divmod(seconds, MINUTE)

    time_ranges = [(years, "year"), (days, "day"), (hours, "hour"),
                   (minutes, "minute"), (seconds, "second")]

    result = [pluralising(*dt) for dt in time_ranges if dt[0] > 0]

    if len(result) > 2:
        return ', '.join(result[:-1]) + " and " + result[-1]
    if len(result) == 2:
        return ' and '.join(result)

    return result[0]


if __name__ == '__main__':
    print(format_duration(2*60*60*24*365 + 3600*25 + 7200 + 123))
    print(format_duration(1))
    assert format_duration(0) == "now"
    assert format_duration(1) == "1 second"
    assert format_duration(62) == "1 minute and 2 seconds"
    assert format_duration(120) == "2 minutes"
    assert format_duration(3600) == "1 hour"
    assert format_duration(3662) == "1 hour, 1 minute and 2 seconds"