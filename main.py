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

def get_case_count(f):
    count = 0
    with lzma.open(f) as in_file:
        for line in in_file:
            count += 1
    return count

def extract_citations(f, case_count=None):
    current = 0
    cases = {}
    with lzma.open(f) as in_file:
        for line in in_file:
            case = json.loads(str(line, 'utf8'))
            cites = extract_cites(case)
            ## Change this to ID later
            cases[case['id']] = cites

            current += 1
            if case_count:
                progress = (current * 100) / case_count
                last_progress = ((current - 1) * 100) / case_count
                if round(progress) > round(last_progress) and round(progress) % 5 == 0:
                    log('\t%d%% done.' % round(progress), to_console=True, to_file=False)
    return cases

def count_cites(journal):
    count = 0
    for case in journal:
        count += len(journal[case])
    return count

def main():
    folders = get_all_bulk_data_folders()
    journal_citations = {}
    for folder in folders:
        log('Extracting cases from %s.' % folder, to_console=True)
        case_count = get_case_count(folder_to_xz_path(folder))
        log('\tParsing %d cases.' % case_count, to_console=True)
        cases = extract_citations(folder_to_xz_path(folder), case_count=case_count)

        for case in cases:
            for cite in cases[case]:
                if cite[0] not in journal_citations:
                    journal_citations[cite[0]] = {}
                if case not in journal_citations[cite[0]]:
                    journal_citations[cite[0]][case] = []
                journal_citations[cite[0]][case].append(cite[1])

    for journal in journal_citations:
        log('%s: %d cites.' % (
            JOURNALS[journal].name,
            count_cites(journal_citations[journal])),
            to_console=True)

if __name__ == '__main__':
    main()
