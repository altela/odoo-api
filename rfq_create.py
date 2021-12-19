from establish_con import url, db, username, password, uid
import xmlrpc.client

# Create RFQ

models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))
new_rfq = models.execute_kw(db, uid, password, 'purchase.order', 'create', [{
    'state': "draft", #Select either "sent", "sale", "done", "cancel"
    'partner_id': 19258, #Customer ID
    'client_order_ref': "000000", #Order Reference Number
    'picking_policy': "direct", #select either "direct" or "one"  
    'order_line' : [
        # First line of Order Lines
        (0, 0, {    
            'product_id': 2294, #insert product ID
            # 'name': 2294,
            # 'product_qty': 10,
            # 'date_planned': "06/05/2021 15:28:55",
            # 'product_uom' : "Each"
            }
        ),
    ],  
}])