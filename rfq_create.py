import xmlrpc.client
from endpoint import models
from establish import *

new_rfq = models.execute_kw(db, uid, password, 'purchase.order', 'create', [{
    'state': "draft", 
    'partner_id': yourPartnerID, 
    'client_order_ref': "000000",
    'picking_policy': "direct",
    'order_line' : [
        # First line of Order Lines
        (0, 0, {    
             'product_id': yourProductOD,
             'name': thisProductNameWillFollowProductIDAbove,
             'product_qty': 10,
             'date_planned': "06/05/2021 15:28:55",
             'product_uom' : "Each"
            }
        ),
    ],  
}])

# Description
# State             = #Select either "sent", "sale", "done", "cancel"
# partner_id        = #Customer ID
# client_order_ref  = Order Reference Number
# picking_policy    = Select either "direct" or "one"
# product_id		= Product ID
# name 				= Product ID name, will automatically follow the product ID
# product_qty		= Quantity
# date_planned		= This is the scheduled date
# product_uom		= Product UoM will also follow product_id
