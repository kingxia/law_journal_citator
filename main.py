import lzma, json, os

from lib.constants import *
from lib.extract import *
from lib.journals import *
from lib.logic import *

def get_all_bulk_data_folders():
    '''Return all the folders stored as data.
    Download folders directly to data/jurisdiction, and extract.
    e.g. data/jurisdiction/Alabama-20181204-xml.zip.'''
    return [filename for filename in os.listdir(BULK_DATA_PATH) \
                if os.path.isdir(os.path.join(BULK_DATA_PATH, filename))]

def folder_to_xz_path(path):
    return '%s%s/%s' % (BULK_DATA_PATH, path, XZ_FILE_FROM_JD_FOLDER)

def extract_cases(f):
    with lzma.open(f) as in_file:
        for line in in_file:
            case = json.loads(str(line, 'utf8'))
            cites = extract_cites(case)
            return case

def main():
    folders = get_all_bulk_data_folders()
    for folder in folders:
        log('Extracting cases from %s.' % folder, to_console=True)
        extract_cases(folder_to_xz_path(folder))

if __name__ == '__main__':
    main()
