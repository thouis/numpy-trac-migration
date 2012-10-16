import trac
import time
import traceback

for issue in trac.issues('Numpy-snapshot-2012-10-8/numpy-trac.db'):
    issue.githubify()
    try:
        if not issue.in_github():
            issue.push()
            print "PUSHED", issue.github.title
        else:
            print "EXISTS", issue.github.title
    except Exception, e:
        print "Could not push", issue.trac.id
        traceback.print_exc()
        raise

