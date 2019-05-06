# law_journal_citator
Pull secondary cites from CAP to find where legal journals are cited in case law.

Journal data courtesy of the Gallagher Law Library of the University of Washington School of Law. You can find this data here: https://lib.law.uw.edu/cilp/abbrev.html.

Case data courtesy of the Caselaw Access Project. Find out more here: https://case.law.

Find out more about the development process here: https://docs.google.com/document/d/1JVBrXXFXtmdmcxRS-DbBWGpiWvwNdSu5ckQZZuetOIY.

## Set up

1. clone the repo
2. if journals.py needs updating:  
  a. cd scripts  
  b. python build_journals.py  
  c. cp output/journals.py ../lib/journals.py  
3. python build_partial_database.py
4. python merge_partial_databases.py
5. export FLASK_APP=server.py
6. flask run
