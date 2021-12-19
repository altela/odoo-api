from establish_con import url, db, password, username, common, uid, xmlrpc

models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))
new_memo = models.execute_kw(db, uid, password, 'helpdesk.ticket', 'create', [{

    'name' : "what",
    'priority' : 0, # Select either 0 (All), 1 (low priority), 2 (high priority)
    #'user_id' : , # Assign to someone using their id 
    #'partner_id' : , # The user that reported the problem
    #'ticket_type_id' : , # Type of the ticket ID, either it's a "Question", "Issue", etc.
    'field' : "Your Description Here", 
    # 'tag_ids' : , # Desired tag id
    # 'stage_id' : # Define stages id, leave blank if you'd like it to be new
}])