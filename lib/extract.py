from lib.journals import *
import re

def extract_cites(case):
    cites = []

    for i in JOURNALS:
        j_cites = [m.start() for m in re.finditer(JOURNALS[i].short, case['casebody']['data'])]
        for cite in j_cites:
            cites.append((i, cite))

    return cites
