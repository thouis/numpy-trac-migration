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
    # some milestones were renamed between trac and github before migrating.
    trac_milestone = {'1.7.0': 'NumPy 1.7',
                      '1.8.0': 'NumPy 1.8',
                      '2.0.0': 'NumPy 2.0'}.get(trac_milestone, trac_milestone)
    for m in milestones:
        if m.title == trac_milestone:
            return m.number
    if trac_milestone in ['', None, 'Unscheduled']:
        return None
    print "CREATING NEW MILESTONE", trac_milestone
    new_milestone = gh_repo().create_milestone(trac_milestone)
    milestones += [new_milestone]
    return new_milestone.number
