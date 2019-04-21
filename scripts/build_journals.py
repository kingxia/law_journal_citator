import string, re
SOURCE = 'data/journal_data.txt'
OUTPUT = 'scripts/output/journals.py'

STARTER_CODE = '''from enum import IntEnum

class Journal():
    def __init__(self, _id, name, short):
        self.id = _id
        self.name = name
        self.short = short'''

def get_journal_data(src):
    _file = open(src)
    lines = [line.strip() for line in _file.readlines()]
    _file.close()

    return [line.split('\t') for line in lines]

def output_python(dst, text):
    _file = open(dst, 'w')
    _file.write(text)
    _file.close()

def short_cite_to_key(j):
    return re.sub(' +', ' ', j.translate(str.maketrans('', '', string.punctuation))).replace(' ', '_').upper()

def write_safe(s):
    return s.replace('\'', '\\\'')

def build_journal_enum(journals):
    return '''\n\nclass Journals(IntEnum):\n%s''' % (
        '\n'.join(map(lambda x: '    %s = %d' % (
            short_cite_to_key(journals[x][1]), x), range(len(journals)))))

def build_journal_map(journals):
    return '''\n\nJOURNALS = {\n%s\n}''' % (
        ',\n'.join(map(lambda x: '    %d: Journal(%d, \'%s\', \'%s\')' % (
            x, x, write_safe(journals[x][0]), write_safe(journals[x][1])), range(len(journals)))))

def main():
    journals = get_journal_data(SOURCE)
    code = STARTER_CODE
    code += build_journal_enum(journals)
    code += build_journal_map(journals)

    output_python(OUTPUT, code)

if __name__ == '__main__':
    main()
