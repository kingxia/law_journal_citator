# law_journal_citator
Pull secondary cites from CAP to find where legal journals are cited in case law.

Journal data courtesy of the Gallagher Law Library of the University of Washington School of Law. You can find this data here: https://lib.law.uw.edu/cilp/abbrev.html.

## Set up

1. clone the repo
2. if journals.py needs updating:
  a. cd scripts
  b. python3 build_journals.py
  c. cp output/journals.py ../lib/journals.py
3. python3 build_database.py
4. export FLASK_APP=server.py
5. flask run
