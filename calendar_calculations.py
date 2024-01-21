#!/usr/bin/env python3
"""
This module provides functions for converting dates between the Gregorian and Julian calendars.
It includes methods for calculating the Julian Day Number (JDN) for both calendars,
as well as functions for converting a date from one calendar to another
and from JDN to Julian and Gregorian.

The formulas used for these calculations are derived from the algorithms
described on the Wikipedia: https://en.wikipedia.org/wiki/Julian_day
and descriptions on the Alexander Krutov's site: http://krutov.org/algorithms/julianday.

The formulas used for these calculations are derived from the algorithms
described on the Wikipedia:
[Julian Day](https://en.wikipedia.org/wiki/Julian_day) and
[Юлианская дата](https://ru.wikipedia.org/wiki/Юлианская_дата).

Also, the descriptions of the algorithms are available on
Alexander Krutov's site: [Юлианский день](http://krutov.org/algorithms/julianday).

Do 'chmod +x calendar_calculations.py' for making the script executable.
Then, you can run the script using './calendar_calculations.py'.

:Author: Valery Tropin
:Website: https://tropin.one

"""

# TODO: Include type(float) for JDN and days

import argparse


def calculate_gregorian_to_JDN(year: int, month: int, day: int) -> int:
    """Calculate Julian Day Number (JDN) for the given Gregorian calendar date.

    Args:
        year (int): Year in Gregorian calendar.
        month (int): Month in Gregorian calendar.
        day (int): Day in Gregorian calendar.

    Returns:
        int: JDN
    """

    _a = (14 - month) // 12
    _y = year + 4800 - _a
    _m = month + 12 * _a - 3

    JDN = day + (153 * _m + 2) // 5 + 365 * _y + _y // 4 - _y // 100 + _y // 400 - 32045

    return JDN


def calculate_julian_to_JDN(year: int, month: int, day: int) -> int:
    """Calculate Julian Day Number (JDN) for the given Julian calendar date.

    Args:
        year (int): Year in Julian calendar.
        month (int): Month in Julian calendar.
        day (int): Day in Julian calendar.

    Returns:
        int: JDN
    """

    _a = (14 - month) // 12
    _y = year + 4800 - _a
    _m = month + 12 * _a - 3

    JDN = day + (153 * _m + 2) // 5 + 365 * _y + _y // 4 - 32083

    return JDN


def get_weekday(JDN: int) -> str | None:
    """Get the Julian Day Number (JDN) and calculate it's weekday.

    Returns:
        str or None: Weekday corresponding to the Julian Day Number (JDN).
        If the JDN does not correspond to a valid weekday, returns None.
    """

    days = {
        0: "Sunday",
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
    }

    day_number = int((JDN + 1.5) % 7)

    return days.get(day_number)


def calculate_JDN_to_gregorian(JDN: int) -> dict[str, int]:
    """Convert Julian Day Number (JDN) to date in Gregorian calendar.

    Returns:
        dict[str, int]: Dictionary containing the year, month, and day
        in Gregorian calendar corresponding to the Julian Day Number (JDN).
    """

    _a = JDN + 32044
    _b = (4 * _a + 3) // 146097
    _c = _a - (146097 * _b) // 4
    _d = (4 * _c + 3) // 1461
    _e = _c - (1461 * _d) // 4
    _m = (5 * _e + 2) // 153

    day_gredorian = _e - (153 * _m + 2) // 5 + 1
    month_gredorian = _m + 3 - 12 * (_m // 10)
    year_gredorian = 100 * _b + _d - 4800 + _m // 10

    return {
        "year_gredorian": year_gredorian,
        "month_gredorian": month_gredorian,
        "day_gredorian": day_gredorian,
    }


def calculate_JDN_to_julian(JDN: int) -> dict[str, int]:
    """Convert Julian Day Number (JDN) to date in Julian calendar.

    Returns:
        dict[str, int]: Dictionary containing the year, month, and day
        in Julian calendar corresponding to the Julian Day Number (JDN).
    """

    _c = JDN + 32082
    _d = (4 * _c + 3) // 1461
    _e = _c - ((1461 * _d) // 4)
    _m = (5 * _e + 2) // 153

    day_julian = _e - (153 * _m + 2) // 5 + 1
    month_julian = _m + 3 - 12 * (_m // 10)
    year_julian = _d - 4800 + _m // 10

    return {
        "year_julian": year_julian,
        "month_julian": month_julian,
        "day_julian": day_julian,
    }


def get_julian_gregorian_from_JDN(args: argparse.Namespace) -> None:
    """Convert Julian Day Number (JDN) to the dates in Gregorian and Julian calendars.

    If the user enters invalid data, the function will print
    an error message and terminate without raising an exception.

    Args:
        args (argparse.Namespace): Arguments parsed from the command line.

    Raises:
        ValueError: If the input JDN is not in the correct type int.

    Returns:
        None: Prints the Julian and Gregorian dates corresponding
        to the Julian Day Number (JDN) and the weekday.
    """

    try:
        JDN: int = int(args.date)
    except ValueError:
        print("Invalid input. Please enter a valid Julian Day Number (JDN).")
        return

    weekday = get_weekday(JDN=JDN)

    date_julian = calculate_JDN_to_julian(JDN=JDN)
    day_julian = date_julian.get("day_julian")
    month_julian = date_julian.get("month_julian")
    year_julian = date_julian.get("year_julian")

    date_gregorian = calculate_JDN_to_gregorian(JDN=JDN)
    day_gredorian = date_gregorian.get("day_gredorian")
    month_gredorian = date_gregorian.get("month_gredorian")
    year_gredorian = date_gregorian.get("year_gredorian")

    print(
        f"""
For your Julian Day Number (JDN) = {JDN}:
Julian Date = {day_julian}.{month_julian}.{year_julian}
Gregorian date = {day_gredorian}.{month_gredorian}.{year_gredorian}
Weekday: {weekday}
"""
    )


def convert_gregorian_to_julian(args: argparse.Namespace) -> None:
    """Convert date in Gregorian calendar to date in Julian calendar.

    If the user enters invalid data, the function will print
    an error message and terminate without raising an exception.

    Args:
        args (argparse.Namespace): Arguments parsed from the command line.

    Raises:
        ValueError: If the input date is not in the correct format (YYYY.MM.DD).

    Returns:
        None: Prints the Julian Day Number (JDN), Julian date,
        and weekday corresponding to the input Gregorian date.
    """

    try:
        yyyymmdd = args.date
        year: int
        month: int
        day: int
        year, month, day = [int(v) for v in yyyymmdd.split(".")]
    except ValueError:
        print("Invalid input. Please enter a valid date in the format YYYY.MM.DD.")
        return

    JDN = calculate_gregorian_to_JDN(year=year, month=month, day=day)

    weekday = get_weekday(JDN=JDN)

    date_julian = calculate_JDN_to_julian(JDN=JDN)
    day_julian = date_julian.get("day_julian")
    month_julian = date_julian.get("month_julian")
    year_julian = date_julian.get("year_julian")

    print(
        f"""
For your Gregorian date {day}.{month}.{year}:
Julian Day Number (JDN) = {JDN}
Julian Date = {day_julian}.{month_julian}.{year_julian}
Weekday: {weekday}
"""
    )


def convert_julian_to_gregorian(args: argparse.Namespace) -> None:
    """Convert date in Julian calendar to date in Gregorian calendar.

    If the user enters invalid data, the function will print
    an error message and terminate without raising an exception.

    Args:
        args (argparse.Namespace): Arguments parsed from the command line.

    Raises:
        ValueError: If the input date is not in the correct format (YYYY.MM.DD).

    Returns:
        None: Prints the Julian Day Number (JDN), Gregorian date,
        and weekday corresponding to the input Julian date.
    """

    try:
        yyyymmdd = args.date
        year: int
        month: int
        day: int

        year, month, day = [int(v) for v in yyyymmdd.split(".")]
    except ValueError:
        print("Invalid input. Please enter a valid date in the format YYYY.MM.DD.")
        return

    JDN = calculate_julian_to_JDN(year=year, month=month, day=day)

    weekday = get_weekday(JDN=JDN)

    date_gregorian = calculate_JDN_to_gregorian(JDN=JDN)
    day_gredorian = date_gregorian.get("day_gredorian")
    month_gredorian = date_gregorian.get("month_gredorian")
    year_gredorian = date_gregorian.get("year_gredorian")

    print(
        f"""
For your Julian date {day}.{month}.{year}:
Julian Day Number (JDN) = {JDN}
Gregorian date = {day_gredorian}.{month_gredorian}.{year_gredorian}
Weekday: {weekday}
"""
    )


def choose_conversion(args: argparse.Namespace) -> None:
    """Choose the conversion direction between Gregorian and
    Julian calendars based on the flags passed by the user.

    The function expects one of three flags to be passed:
        '-j': for converting a Gregorian date to Julian
        '-g': for converting a Julian date to Gregorian
        '-n': for converting a Julian Day Number (JDN) to Julian and Gregorian date

    If no flag or an incorrect flag is passed, the function prints an error message.

    Args:
        args (argparse.Namespace): Arguments parsed from the command line.

    Returns:
        None: The function doesn't return any value.
        Instead, it either calls the appropriate conversion function
        or prints an error message.
    """

    if args.j:
        return convert_gregorian_to_julian(args)
    elif args.g:
        return convert_julian_to_gregorian(args)
    elif args.n:
        return get_julian_gregorian_from_JDN(args)
    else:
        print("Enter only '-j', '-g' or '-n' flags!")


if __name__ == "__main__":
    parser: argparse.ArgumentParser = argparse.ArgumentParser(
        prog="JDN Calculator",
        description="Convert dates between the Gregorian and Julian calendars and calculate Julian Day Number (JDN)",
    )
    parser.add_argument("date", help="User date in format YYYY.MM.DD", type=str)
    parser.add_argument(
        "-j", action="store_true", help="Convert Gregorian date to Julian"
    )
    parser.add_argument(
        "-g", action="store_true", help="Convert Julian date to Gregorian"
    )
    parser.add_argument(
        "-n",
        action="store_true",
        help="Convert Julian Day Number (JDN) to Julian and Gregorian date",
    )

    args = parser.parse_args()
    choose_conversion(args)
