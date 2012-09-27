import issue
import util

fields = "id,type,time,component,severity,priority,owner,reporter,cc,version,milestone,status,resolution,summary,description,keywords"

def issues(dbfile):
    c = util.cursor(dbfile)
    for (id,) in c.execute("SELECT id FROM ticket").fetchall():
        vals = c.execute("SELECT %s FROM ticket where id=%d" % \
                             (fields, id)).fetchone()
        changes = issue_changes_and_attachments(id)
        yield issue.issue(**dict(zip(fields.split(","), vals) + \
                                     [('_changes_and_attachments', changes)]))

def single_issue(dbfile, id):
    c = util.cursor(dbfile)
    vals = c.execute("SELECT %s FROM ticket where id=%d" % \
                         (fields, id)).fetchone()
    changes = issue_changes_and_attachments(id)
    return issue.issue(**dict(zip(fields.split(","), vals) + \
                                  [('_changes_and_attachments', changes)]))

def issue_changes_and_attachments(id):
    c = util.cursor()
    for vals in c.execute("SELECT time, author, field, oldvalue, newvalue FROM ticket_change WHERE ticket=?", (id,)).fetchall():
        yield vals
    for vals in c.execute("SELECT time, author, description, filename FROM attachment WHERE id=?", (id,)).fetchall():
        yield vals
