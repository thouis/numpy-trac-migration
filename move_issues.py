import trac

for issue in trac.issues('numpy-trac.db'):
    if issue.trac.id == 2179:
        issue.githubify()
        issue.push()
        break
