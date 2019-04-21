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

def extract_citations(f):
    cases = {}
    to_process = 100
    with lzma.open(f) as in_file:
        for line in in_file:
            to_process += 1
            case = json.loads(str(line, 'utf8'))
            cites = extract_cites(case)
            ## Change this to ID later
            cases[case['name']] = cites
    return cases

def main():
    folders = get_all_bulk_data_folders()
    for folder in folders:
        log('Extracting cases from %s.' % folder, to_console=True)
        cases = extract_citations(folder_to_xz_path(folder))
    for case in cases:
        if len(cases[case]) > 0:
            print('\t%s:\t%s' % (case, cases[case]))

if __name__ == '__main__':
    main()
