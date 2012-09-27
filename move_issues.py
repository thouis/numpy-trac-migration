import trac
import time
import traceback
import pdb

for issue in trac.issues('numpy-trac.db'):
    issue.githubify()
    try:
        time.sleep(4)
        issue.push()
    except Exception, e:
        print "Could not push", issue.trac.id
        traceback.print_exc()
        raise

