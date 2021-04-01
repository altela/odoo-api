models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))
product = models.execute_kw(db, uid, password, 'product.template', 'search',[[
]])
print(product)