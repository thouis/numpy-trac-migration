# build map of trac to github username
from check_emails import get_ticket_owners, get_ticket_reporters, get_ticket_ccs
import util
from github import Github
import getpass

u = raw_input("Github username: ")
p = getpass.getpass("Password: ")
g = Github(u, p)
del p

if __name__ == '__main__':
    outf = open("TRAC_TO_GITHUB_USERS.txt", "w")
    names = get_ticket_owners() + get_ticket_reporters() + get_ticket_ccs()
    import collections
    counts = collections.Counter(names)
    cn = [(c, n) for n, c in counts.iteritems()]
    cn.sort()
    cn.reverse()
    for c, n in cn:
        if c > 1:
            tracemail = util.trac_user_email(n)
            ghuser = util.trac_email_to_github(tracemail)
            if ghuser is None and '@' in tracemail:
                try:
                    ghuser = g.legacy_search_user_by_email(tracemail).login
                except:
                    pass
            if ghuser is not None:
                outf.write("%s %s\n" % (n, ghuser))
                outf.flush()
            else:
                print "MISSING", n, tracemail, c
