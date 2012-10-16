import sqlite3

def trac_email_to_github(email, email_map={}):
    if len(email_map) == 0:
        email_map.update(dict([s.strip().rsplit(" ", 1) for s in open("EMAIL_TO_GITHUB.txt")]))
    return email_map.get(email, None)

def trac_user_to_github(user, user_map={}):
    if len(user_map) == 0:
        user_map.update(dict([s.strip().rsplit(" ", 1) for s in open("TRAC_TO_GITHUB_USERS.txt")]))
    return user_map.get(user, None)

def trac_user_email(user):
    email = cursor().execute('SELECT value FROM session_attribute WHERE sid=? AND name="email"', (user,)).fetchone()
    if email is None:
        email = user
    else:
        email = email[0]
    return email

def cursor(dbfile="numpy-trac.db", c=[]):
    if len(c) == 0:
        conn = sqlite3.connect(dbfile)
        c.append(conn.cursor())
    return c[0]

all_users = []

def mention_trac_user(user):
    ghuser = trac_user_to_github(user)
    if ghuser:
        all_users.append("@" + ghuser)
        return "atmention:" + ghuser
    if user in ['', 'somebody', 'anonymous', None]:
        return 'unknown'
    return "trac user " + user
