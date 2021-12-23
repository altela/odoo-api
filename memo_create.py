import xmlrpc.client
from endpoint import models
from establish import *

new_memo = models.execute_kw(db, uid, password, 'note.note', 'create', [{

     'memo' : "The title of the memo",
    #'stage_id' : yourMemoID

}])

# Description
# Memo 		= The title of the memo
# stage_id	= The state id of the memo