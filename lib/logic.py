from constants import *

def log(message, to_console=False, to_file=True, include_date_time=True):
    today = datetime.datetime.now().date()
    if not SERVER_LOGGER.has_file() or SERVER_LOGGER.get_current_file_date().date() != today:
        SERVER_LOGGER.set_file(LOG_PATH + date_to_log_filename(today))
    SERVER_LOGGER.log(message, to_console=to_console, to_file=to_file, include_date_time=include_date_time)
