# Check that ticket owners are in EMAIL_TO_GITHUB.txt map
import sqlite3

email_map = dict([s.strip().split(" ") for s in open("EMAIL_TO_GITHUB.txt")])

def check_ticket_owners(dbfile):
    conn = sqlite3.connect(dbfile)
    c = conn.cursor()
    for (owner,) in c.execute("SELECT owner FROM ticket").fetchall():
        if owner in ["somebody", "anonymous", "spammer"]:
            print owner, "None"
            continue
        email = c.execute('SELECT value FROM session_attribute WHERE sid=? AND name="email"', (owner,)).fetchone()
        if email is None:
            email = owner
        else:
            email = email[0]
        if email in email_map:
            print email, email_map[email]
        else:
            print "MISSING", email

if __name__ == '__main__':
    check_ticket_owners("numpy-trac.db")

