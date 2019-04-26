import lzma, json, os, sqlite3

from lib.constants import *
from lib.backend.extract import *
from lib.journals import *
from lib.logic import *

def create_database(dst):
    if os.path.exists(dst):
        os.remove(dst)
    db = sqlite3.connect(dst)
    cursor = db.cursor()
    cursor.execute(CREATE_CITES_TABLE)
    cursor.execute(CREATE_NEXT_IDS_TABLE)
    cursor.execute(INSERT_NEXT_ID % (0, 1000))
    db.commit()
    db.close()

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

def decision_to_year(s):
    return int(s.split('-')[0])

def cite_to_article(s):
    parts = s[2:len(s)-1].split(' ')
    return [parts[0], parts[-1]]

def extract_citations(src, dst, case_count=None):
    current = 0
    cases = {}

    db = sqlite3.connect(dst)
    cursor = db.cursor()

    cursor.execute('SELECT * FROM nextIds')
    next_id = cursor.fetchone()[1]
    
    with lzma.open(src) as in_file:
        for line in in_file:
            case = json.loads(str(line, 'utf8'))
            cites = extract_cites(case)

            for cite in cites:
                match = cite[1]
                article = cite_to_article(match.group())
                cursor.execute(INSERT_CITATION % (
                    next_id, cite[0], int(article[0]), int(article[1]),
                    case['id'], case['name'],
                    case['jurisdiction']['id'],
                    decision_to_year(case['decision_date']),
                    match.start()+2, match.end()-1))
                next_id += 1

            current += 1
            if case_count:
                progress = (current * 100) / case_count
                last_progress = ((current - 1) * 100) / case_count
                if round(progress) > round(last_progress) and round(progress) % 5 == 0:
                    log('\t%d%% done.' % round(progress), to_console=True, to_file=False)

    cursor.execute('UPDATE nextIds SET nextId = %d WHERE id = 0' % next_id)
    db.commit()
    db.close()

def main():
    create_database(DATABASE_PATH)
    folders = get_all_bulk_data_folders()
    journal_citations = {}
    for folder in folders:
        log('Extracting cases from %s.' % folder, to_console=True)
        case_count = get_case_count(folder_to_xz_path(folder))
        log('\tParsing %d cases.' % case_count, to_console=True)
        extract_citations(folder_to_xz_path(folder), DATABASE_PATH, case_count=case_count)

if __name__ == '__main__':
    main()
