import calendar_data


def format_tamrielic_date(date):
    """
    Returns current date in Tamrielic format.

    Args:
        date    (datetime.date.today()): Current date derived from date object.

    Returns:
        string: A string representing the current date in Tamrielic format.

    Example #1:
        Given that the date is Monday, January 8th 2017.

        month   = 1
        day     = 8
        weekday = 0
        year    = 2017

        Return value:
            Morndas, the 8th day of Morning Star, 20E 17.

    Example #2:
        Given that the date is Monday, January 15th 2017.

        month   = 1
        day     = 15
        weekday = 0
        year    = 2017

        Return value:
            Morndas, the 15th day of Morning Star, 20E 17. The South Wind's Prayer.

    :param
        date: Datetime.date object.
    :return:
        string: String representation of the given date in Tamrielic format
    """
    month = date.month
    day = date.day
    weekday = date.weekday()
    year = date.year

    # Get suffix for day
    if (4 <= day <= 20) or (24 <= day <= 30):
        suffix = "th"
    else:
        suffix = ["st", "nd", "rd"][day % 10 - 1]

    tamrielic_weekday = calendar_data.WEEKDAY_DICT[weekday]
    tamrielic_day = str(day) + suffix
    tamrielic_month = calendar_data.MONTH_DICT[month]
    tamrielic_year = "{}E {}".format(str(year)[:2], str(year)[2:])

    try:
        holiday_text = calendar_data.HOLIDAY_DICT[month][day] + ". "
    except KeyError:
        holiday_text = ""

    tamrielic_date = "{}, the {} day of {}, {}. {}"

    return tamrielic_date.format(tamrielic_weekday, tamrielic_day, tamrielic_month, tamrielic_year, holiday_text)
