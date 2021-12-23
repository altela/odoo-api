import xmlrpc.client
from endpoint import models
from establish import *
from datetime import datetime

# Search Product
searchByID = models.execute_kw(db, uid, password,
    'product.product', 'search',
    [[['id', '=', yourProductID]]],
    {'limit': 1})

# Read Product from table product.product
read = models.execute_kw(db, uid, password,'product.product', 'read',
        [searchByID], {'fields': 
        ['name',
        'type',
        'sale_ok',
        'purchase_ok',
        'can_be_expensed',
        'categ_id',
        'default_code',
        'barcode',
        'list_price',
        'standard_price',
        'uom_id',
        'uom_po_id',
        'description',
        'available_in_pos',
]})

print(read)

# Description
# id                = your product ID
# name              = product name
# type              = product type
# sale_ok           = this product can be sold (boolean checkbox status in odoo)
# purchase_ok       = this product can be purchased (boolean checkbox status)
# can_be_expensed   = this product can be expensed (boolean checkbox status)
# categ_id          = category ID
# default_code      = internal reference of the product
# barcode           = product barcode
# list_price        = Sales Price
# standard_price    = Cost
# uom_id            = Unit of Measure ID
# uom_po_id         = purchase uom ID
# description       = internal notes of your product
# available_in_pos  = this product can be sold via point of sales (cashier)
