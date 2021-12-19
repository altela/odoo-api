# Logging in Connection
import xmlrpc.client
from datetime import datetime
common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
uid = common.authenticate(db, username, password, {})

# Search Product
models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))
searchByID = models.execute_kw(db, uid, password,
    'product.product', 'search',
    [[['id', '=', yourDesiredID]]], #Put Your Product ID here
    {'limit': 1})

# Reading Product from table product.product
read = models.execute_kw(db, uid, password,'product.product', 'read',
        [searchByID], {'fields': 
        ['name', #Product Name
        'type', #Product Type
        'sale_ok', #Can Be Sold (Boolean checkbox status)
        'purchase_ok', #Can Be Purchased (Boolean checkbox status)
        'can_be_expensed', #Can Be Expensed (Boolean checkbox status)
        'categ_id', #Product Category
        'default_code', #Print Internal Reference
        'barcode', #Product Barcode
        'list_price', #Sales Price
        'standard_price', #Cost
        'uom_id', #Unit of Measure ID
        'uom_po_id', #Purchase Unit of Measure ID
        'description', #Internal Notes
        'available_in_pos',
]})

print(read)
