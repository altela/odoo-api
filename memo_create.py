from establish_con import url, db, password, username, common, uid, xmlrpc

models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))
new_memo = models.execute_kw(db, uid, password, 'note.note', 'create', [{

    'memo' : "what",
    #'stage_id' : #insert note id 

}])