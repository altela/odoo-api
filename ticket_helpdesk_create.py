import xmlrpc.client
from endpoint import models
from establish import *

new_memo = models.execute_kw(db, uid, password, 'helpdesk.ticket', 'create', [{

     'name' : "User having a problem with their computer",
     'priority' : 0,
#    'user_id' : ,
#    'partner_id' : ,
#    'ticket_type_id' : ,
     'field' : "Your Description Here",
#    'tag_ids' : ,
#    'stage_id' :
}])

# Description
# name                = Is the title of ticket
# priority             = Assign either 0 (All), 1 (low priority), 2 (high priority), 3 (urgent)
# user_id            = Assign this ticket to someone using their id
# partner_id        = The user that reported the problem
# ticket_type_id    = Type of the ticket ID, either it's a "Question", "Issue", etc.
# tag_ids            = Is the ID of tag which will be added to this ticket
# stage_id            = Define stages id, leave blank if you'd like it to be new

# The mandatory "key" to create a new ticket is already uncommented as script above.
# If you decide to uncomment several of those, you'll need to assign "value" to it's "key" (Dictionary).
