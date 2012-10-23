import trac
import time
import traceback

count = 0
for issue in trac.issues('Numpy-snapshot-2012-10-8/numpy-trac.db'):
    if issue.trac.id in [2222, 2223]:  #spam
        continue
    count = count + 1
    issue.githubify()
    issue.check_crossrefs()

