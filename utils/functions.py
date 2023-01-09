import datetime

from dateutil.relativedelta import relativedelta


def change_time(time: datetime.datetime, subtract: bool = True, **kwargs) -> datetime.time:
    """
    Change datetime value with relativedelta.
    :param time: datetime value
    :param subtract: action vector
    :param kwargs: args for relativedelta
    :return: datetime result replaced to time
    """
    if not isinstance(time, datetime.datetime):
        raise TypeError(f"{time} is not datetime")

    try:
        if subtract:
            result = time - relativedelta(**kwargs)
        else:
            result = time + relativedelta(**kwargs)

        return result.time()
    except TypeError:
        raise TypeError("Unknown kwargs for relativedelta")
