import github
import getpass

def gh_repo(r=[]):
    if len(r) == 0:
        u = raw_input("Github username: ")
        p = getpass.getpass("Password: ")
        g = github.Github(u, p)
        del p
        r += [g.get_user().get_repo("numpy-trac-migration")]
    return r[0]

def lookup(issue):
    '''update the issue with the remove issue number and other information'''
    pass

def find_milestone(trac_milestone, milestones=[]):
    if len(milestones) == 0:
        milestones += [m for m in gh_repo().get_milestones()]
    if trac_milestone in ['1.7.0', '1.8.0', '2.0.0']:
        for m in milestones:
            if m.title.endswith(trac_milestone[:3]):
                return m.number
    return None
