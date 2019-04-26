import sqlite3
from lib.logic import list_to_csv

REQUEST_KEYWORDS = ['journalId', 'jurisdiction']
OPTION_KEYWORDS = ['yearMin', 'yearMax', 'groupBy']
GROUP_BY_TRANSLATE = {
    'case': 'caseId',
    'cite': 'volume, page, journalId',
    'jurisdiction': 'jurisdiction',
    'year': 'year'
}
SELECT_TRANSLATE = {
    'case': 'caseId, caseName, jurisdiction, year, count(id), count(distinct journalId)',
    'cite': 'volume, page, journalId, count(id), count(distinct caseId), count(distinct jurisdiction), count(distinct year)',
    'jurisdiction': 'jurisdiction, count(id), count(distinct journalId), count(distinct caseId), count(distinct year)',
    'year': 'year, count(id), count(distinct journalId), count(distinct caseId), count(distinct jurisdiction)'
}

def build_options(request):
    options = {}

    for kw in REQUEST_KEYWORDS:
        if kw in request:
            options[kw] = request[kw]

    for kw in OPTION_KEYWORDS:
        if kw in request:
            options[kw] = request[kw]

    return options

def get_select(options):
    if 'groupBy' not in options:
        return '*'
    return SELECT_TRANSLATE[options['groupBy']]
        
def get_cites(dst, options={}):
    db = sqlite3.connect(dst)
    cursor = db.cursor()

    query = 'SELECT %s FROM citations' % (get_select(options))
    query += ' WHERE ' if len(options) > 0 else ''

    where_query = map(lambda x: '%s IN (%s)' % (x, list_to_csv(options[x])),
                      filter(lambda x: x in REQUEST_KEYWORDS, options))
    if 'yearMin' in options:
        where_query.append('year >= %d' % options['yearMin'])
    if 'yearMax' in options:
        where_query.append('year <= %d' % options['yearMax'])

    query += ' and '.join(where_query)
    if 'groupBy' in options:
        query += ' GROUP BY %s' % (GROUP_BY_TRANSLATE[options['groupBy']])
        
    query += ';'

    cursor.execute(query)
    results = cursor.fetchall()
    
    db.close()

    return results
