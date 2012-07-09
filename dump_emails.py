# build map of email to github username
import sqlite3
from github import Github
import getpass

u = raw_input("Github username: ")
p = getpass.getpass("Password: ")
g = Github(u, p)
del p

conn = sqlite3.connect("numpy-trac.db")
c = conn.cursor()
outf = open("EMAIL_TO_GITHUB.txt", "w")
badf = open("BAD_EMAILS.txt", "w")
for (email,) in c.execute('SELECT value FROM session_attribute WHERE name="email"').fetchall()[:2]:
    print "Looking up", email
    try:
        user = g.legacy_search_user_by_email("thouis")
        outf.write("%s %s\n" %(email, user.name))
        print "%s %s\n" % (email, user.name)
    except Exception, e:
        print e
        badf.write("%s\n" % email)
