import calendar_data


def format_tamriellic_date(date):
    """
    Returns current date in Tamriellic format.
    
    Args:
        date    (datetime.date.today()): Current date derived from date object.
        
    Returns:
        string: A string representing the current date in Tamriellic format.
        
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

    tamriellic_weekday = calendar_data.WEEKDAY_DICT[weekday]
    tamriellic_day = str(day) + suffix
    tamriellic_month = calendar_data.MONTH_DICT[month]
    tamriellic_year = "{}E {}".format(str(year)[:2], str(year)[2:])

    try:
        holiday_text = calendar_data.HOLIDAY_DICT[month][day] + ". "
    except KeyError:
        holiday_text = ""

    tamriellic_date = "{}, the {} day of {}, {}. {}"

    return tamriellic_date.format(tamriellic_weekday, tamriellic_day, tamriellic_month, tamriellic_year, holiday_text)