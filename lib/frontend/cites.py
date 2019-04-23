import sqlite3
from lib.logic import list_to_csv

REQUEST_KEYWORDS = ['journalId', 'jurisdiction']
YEAR_KEYWORDS = ['yearMin', 'yearMax']

def build_options(request):
    options = {}

    for kw in REQUEST_KEYWORDS:
        if kw in request:
            options[kw] = request[kw]

    for kw in YEAR_KEYWORDS:
        if kw in request:
            options[kw] = request[kw]

    return options

def get_cites(dst, options={}):
    db = sqlite3.connect(dst)
    cursor = db.cursor()

    query = 'SELECT * FROM citations'
    query += ' WHERE ' if len(options) > 0 else ''

    where_query = map(lambda x: '%s IN (%s)' % (x, list_to_csv(options[x])),
                      filter(lambda x: x in REQUEST_KEYWORDS, options))
    if 'yearMin' in options:
        where_query.append('year >= %d' % options['yearMin'])
    if 'yearMax' in options:
        where_query.append('year <= %d' % options['yearMax'])

    query += ' and '.join(where_query)
    query += ';'

    cursor.execute(query)
    results = cursor.fetchall()
    
    db.close()

    return results
