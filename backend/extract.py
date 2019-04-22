from journals import *
import re

## TODO: add ", %s ," around all journal names for citations, to avoid things like Transactions being cited everywhere.
## TODO: check for journal misspellings?
def all_journals_regex():
    return '(%s)' % (
        '|'.join(map(lambda x: JOURNALS[x].short.replace('.', '\\.'), range(len(JOURNALS)))))

def extract_cites(case):
    cites = []

    if len([m.start() for m in re.finditer(all_journals_regex(), case['casebody']['data'])]) == 0:
        return cites

    for i in JOURNALS:
        j_cites = [m.start() for m in re.finditer(JOURNALS[i].short, case['casebody']['data'])]
        for cite in j_cites:
            cites.append((i, cite))

    return cites
