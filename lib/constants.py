import datetime

BULK_DATA_PATH = 'data/jurisdiction/'
XZ_FILE_FROM_JD_FOLDER = 'data/data.jsonl.xz'

TIME_STORAGE_FORMAT = '%Y-%m-%d %H:%M:%S'
COURSE_TIME_STORAGE_FORMAT = '%H:%M'
COURSE_TIME_STORAGE_DELIMITER = '-'

LOG_PATH = 'data/logs/'
LOG_DATE_FORMAT = '%Y-%m-%d_log'

DATABASE_PATH = 'data/citations.db'

class Logger():
    def __init__(self):
        self.current_file = None
    
    def log(self, message, to_console=False, to_file=True, include_date_time=True):
        if to_console:
            print(message)
        if to_file and self.current_file is not None:
            _file = open(self.current_file, 'a')
            if not include_date_time:
                _file.write(message)
            else:
                _file.write('[%s] %s' % (self.get_date_time(), message))
            _file.write('\n')
            _file.close()

    def has_file(self):
        return self.current_file is not None

    def get_current_file_date(self):
        filename = self.current_file.split('/')[-1]
        file_head = filename.split('.')[0]
        return datetime.datetime.strptime(file_head, LOG_DATE_FORMAT)

    def set_file(self, filepath):
        self.current_file = filepath

    def get_date_time(self):
        return datetime.datetime.now().strftime(TIME_STORAGE_FORMAT)

SERVER_LOGGER = Logger()

CREATE_CITES_TABLE = '''
CREATE TABLE citations(
    id INTEGER PRIMARY KEY,
    journalId INTEGER,
    volume INTEGER,
    page INTEGER,
    caseId INTEGER,
    caseName TEXT,
    jurisdiction INTEGER,
    year INTEGER,
    startPos INTEGER,
    endPos INTEGER);'''

CREATE_NEXT_IDS_TABLE = '''
CREATE TABLE nextIds(
    id INTEGER PRIMARY KEY,
    nextId INTEGER);'''

INSERT_NEXT_ID = 'INSERT INTO nextIds (id, nextId) VALUES (%d, %d);'
INSERT_CITATION = 'INSERT INTO citations (id, journalId, volume, page, caseId, caseName, jurisdiction, year, startPos, endPos) VALUES (%d, %d, %d, %d, %d, "%s", %d, %d, %d, %d);'
