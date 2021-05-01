import time


def start():
    """
    Starts or resets your timer
    :return start_value: needed in other functions
    """
    return time.time()


def get_timer_value(_start_value, _round=None, _formatted=False):
    """
    :param _formatted: if True return value is beautifully formatted (must be rounded)
    :param _start_value: start() function return value
    :param _round: size of round (decimal digits amount) - don't fill if you don't want rounded number
    :return: actual timer value
    """
    if _formatted:
        return format_timer(round(time.time() - _start_value, _round))
    if _round is None:
        return time.time() - _start_value
    else:
        return round(time.time() - _start_value, _round)


def format_timer(_seconds):
    """
    Beautifully formatting time (used in get_timer_value)
    :param _seconds: seconds amount
    :return: beautifully formatted time ({hours}hr {minutes}min {seconds}sec)
    """
    _minutes = round(_seconds / 60)
    _seconds = _seconds % 60
    _hours = round(_minutes / 60)
    _minutes = _minutes % 60
    return '{}hr {}min {}sec'.format(_hours, _minutes, _seconds)


def pause(_start_value):
    """
        Pausing your timer
        :param _start_value: start() function return value
        :return pause_value: needed in unpause() function
        """
    return time.time() - _start_value


def unpause(_pause_value):
    """
    Unpausing your timer
    :param _pause_value: pause() function return value
    :return _start_value: unpaused value needed in other functions
    """
    return time.time() - _pause_value
