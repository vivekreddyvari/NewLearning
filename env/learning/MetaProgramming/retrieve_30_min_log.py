from datetime import datetime
from stat import ST_CTIME
from dateutil.relativedelta import relativedelta
import os.path, time


"""
class RetrieveLog30:
    """ # This procedure return files from giving path modified/added in last 30 mins """
"""
    def __init__(self, path, last_30_min_files):
        self._path = path
        self._savedSet = set()
        self._last_30_min_files = last_30_min_files
"""


def retrieve_log(path):
    """
    This function return last 30 min modified files
    Args:
        path: input the path which has log files

    Returns:log_files

    """
    _name_set = name_the_set(path=path)
    _retrieved_set = retrieved_set(name_set=_name_set, path=path)

    # sort the files
    _retrieved_set = sorted(_retrieved_set, reverse=True)
    _last_30_min_files = ""
    for _ in _retrieved_set: # '_' is the object
        date_time_today = datetime.today()
        last_30_min = date_time_today - relativedelta(minutes=30)
        if _[0] >= last_30_min:
            print(str(_[0]) + ' ' + _[1])


def name_the_set(path):
    """ This function returns names of the files in the given path
        i/p = path
        o/p = List(files)
    """
    _name_set = set()
    for file in os.listdir(path):
        fullpath = os.path.join(path, file)
        if os.path.isfile(fullpath):
            _name_set.add(file)
    return _name_set


def retrieved_set(name_set, path):
    """
    This function assign stat function, to know when the file is modified and
    returns the time and file name
    Args:
        name_set:
        path:
    Returns: Tuple (time, name of the file)
    """
    _retrieved_set_file = set()
    for name in name_set:
        stat = os.stat(os.path.join(path, name))
        _time = datetime.fromtimestamp(stat[ST_CTIME])
        _retrieved_set_file.add((_time, name))
    return _retrieved_set_file

# latest files
if __name__ == "__main__":

    mypath = "../../learning/MetaProgramming"
    print(retrieve_log(path=mypath))







