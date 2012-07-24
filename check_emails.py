# Check that ticket owners are in EMAIL_TO_GITHUB.txt map
import util

def get_ticket_owners():
    c = util.cursor()
    return [v[0] for v in c.execute("SELECT owner FROM ticket").fetchall()]

def get_ticket_reporters():
    c = util.cursor()
    return [v[0] for v in c.execute("SELECT reporter FROM ticket").fetchall()]

def get_ticket_ccs():
    c = util.cursor()
    return [s.strip() for v in c.execute("SELECT cc FROM ticket").fetchall() for s in v[0].split(",") if s != ""]

if __name__ == '__main__':
    names = get_ticket_owners() + get_ticket_reporters() + get_ticket_ccs()
    import collections
    counts = collections.Counter(names)
    cn = [(c, n) for n, c in counts.iteritems()]
    cn.sort()
    cn.reverse()
    for c, n in cn:
        if c > 1:
            if util.trac_email_to_github(util.trac_user_email(n)) is None and util.trac_user_to_github(n) is None:
                print "MISSING", n, util.trac_user_email(n), c
