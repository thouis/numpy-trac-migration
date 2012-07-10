import sqlite3

def trac_email_to_github(email, email_map={}):
    if len(email_map) == 0:
        email_map.update(dict([s.strip().rsplit(" ", 1) for s in open("EMAIL_TO_GITHUB.txt")]))
    return email_map.get(email, None)

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
