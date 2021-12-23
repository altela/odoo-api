import xmlrpc.client
from endpoint import models
from establish import *

list_partners = models.execute_kw(db, uid, password, 'res.partner', 'search', [[
    ['is_company', '=', True], #Input False for person
    ['customer', '=', True], #Input False for Vendor
]])
print(list_partners)
