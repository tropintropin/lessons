"""
This module provides functions for converting dates between the Gregorian and Julian calendars.
It includes methods for calculating the Julian Day Number (JDN) for both calendars,
as well as functions for converting a date from one calendar to another.

The formulas used for these calculations are derived from the algorithms
described on the Wikipedia: https://en.wikipedia.org/wiki/Julian_day.

Please note that the functions in this module do not perform any error handling.
They assume that the user will always provide input in the correct format (yyyy.mm.dd),
and that this input represents a valid date. If the user enters invalid data,
the functions may behave unpredictably or raise exceptions.
"""


def calculate_JDN_gregorian(year: int, month: int, day: int) -> int:
    """Calculate Julian Day Number (JDN) for the given Gregorian calendar date.

    Returns:
        int
    """
    _a = (14 - month) // 12
    _y = year + 4800 - _a
    _m = month + 12 * _a - 3

    JDN = day + (153 * _m + 2) // 5 + 365 * _y + _y // 4 - _y // 100 + _y // 400 - 32045

    return JDN


def calculate_JDN_julian(year: int, month: int, day: int) -> int:
    """Calculate Julian Day Number (JDN) for the given Julian calendar date.

    Returns:
        int
    """
    _a = (14 - month) // 12
    _y = year + 4800 - _a
    _m = month + 12 * _a - 3

    JDN = day + (153 * _m + 2) // 5 + 365 * _y + _y // 4 - 32083

    return JDN


def convert_gregorian_to_julian() -> None:
    """Convert date in Gregorian calendar to date in Julian calendar.

    Returns:
        None
    """
    yyyymmdd = input(
        "Enter your Gregorian date in the next format: Year.Month.Day in numbers:\n"
    )
    year: int
    month: int
    day: int
    year, month, day = [int(v) for v in yyyymmdd.split(".")]

    JDN = calculate_JDN_gregorian(year=year, month=month, day=day)

    _c = JDN + 32082
    _d = (4 * _c + 3) // 1461
    _e = _c - ((1461 * _d) // 4)
    _m = (5 * _e + 2) // 153

    day_julian = _e - (153 * _m + 2) // 5 + 1
    month_julian = _m + 3 - 12 * (_m // 10)
    year_julian = _d - 4800 + _m // 10

    print(
        f"""
For your Gregorian date {day}.{month}.{year}:
Julian Day Number (JDN) = {JDN}
Julian Date = {day_julian}.{month_julian}.{year_julian}
"""
    )


def convert_julian_to_gregorian() -> None:
    """Convert date in Julian calendar to date in Gregorian calendar.

    Returns:
        None
    """
    yyyymmdd = input(
        "Enter your Julian date in the next format: Year.Month.Day in numbers:\n"
    )
    year: int
    month: int
    day: int
    year, month, day = [int(v) for v in yyyymmdd.split(".")]

    JDN = calculate_JDN_julian(year=year, month=month, day=day)

    _a = JDN + 32044
    _b = (4 * _a + 3) // 146097
    _c = _a - (146097 * _b) // 4
    _d = (4 * _c + 3) // 1461
    _e = _c - (1461 * _d) // 4
    _m = (5 * _e + 2) // 153

    day_gredorian = _e - (153 * _m + 2) // 5 + 1
    month_gredorian = _m + 3 - 12 * (_m // 10)
    year_gredorian = 100 * _b + _d - 4800 + _m // 10

    print(
        f"""
For your Julian date {day}.{month}.{year}:
Julian Day Number (JDN) = {JDN}
Gregorian date = {day_gredorian}.{month_gredorian}.{year_gredorian}
    """
    )


def choose_conversion() -> None:
    """Choose conversion direction between Gregorian and Julian calendars.

    Returns:
        None
    """

    def _direction() -> str:
        """Prompt the user to enter a direction for conversion between Gregorian and Julian calendars.

        Prompts the user to enter either "j" for conversion from Gregorian to Julian,
        or "g" for conversion from Julian to Gregorian.

        Returns:
            str: The user's input.
        """
        return input(
            'Enter "j" to convert Gregorian date into Julian\nEnter "g" to convert Julian date into Gregorian:\n'
        )

    conversion_direction = _direction()
    if conversion_direction == "j":
        return convert_gregorian_to_julian()
    elif conversion_direction == "g":
        return convert_julian_to_gregorian()
    else:
        print('Enter only "g" or "j" letters!')
        conversion_direction = _direction()


if __name__ == "__main__":
    choose_conversion()
