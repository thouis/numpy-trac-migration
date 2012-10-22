import trac
import time
import traceback

count = 0
for issue in trac.issues('Numpy-snapshot-2012-10-8/numpy-trac.db'):
    if issue.trac.id in [2222, 2223]:  #spam
        continue
    count = count + 1
    issue.githubify()
    try:
        if not issue.in_github():
            issue.push()
            print "PUSHED", issue.github.title
            time.sleep(1)
        else:
            print "EXISTS", issue.github.title
    except Exception, e:
        print "Could not push", issue.trac.id
        traceback.print_exc()
        raise

