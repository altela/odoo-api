# Logging in Connection
import xmlrpc.client
common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
uid = common.authenticate(db, username, password, {})

# Listing partner
models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))

list_partners = models.execute_kw(db, uid, password, 'res.partner', 'search', [[
    ['is_company', '=', True], #Input False for person
    ['customer', '=', True], #Input False for Vendor
]])
print(list_partners)
