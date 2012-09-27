import trac
import time
import ghissues

for bad_title in ghissues.search_for_failed_markup():
    print bad_title
    tracnum = int(bad_title.split('#')[-1][:-1])
    issue = trac.single_issue('numpy-trac.db', tracnum)
    issue.githubify()
    issue.push()
