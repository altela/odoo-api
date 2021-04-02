# Creating Quotation
models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))
new_quotation = models.execute_kw(db, uid, password, 'sale.order', 'create', [{
    'partner_id': 4444, #Customer ID
    'client_order_ref': "000000", #Order Reference Number
    'picking_policy': "direct", #select either "direct" or "one"    
 #   'commitment_date': 
    'order_line' : [
        (0, 0, {    
            'product_id': productID, #insert product ID
            'product_uom_qty': qty #insert product qty
            }
        )
    ]
}])

 # Fill in partner_id with your partner ID
 # Fill in product_id with your product ID
 # Fill in product_uom_qty your desired qty
 # IDs can be acquired from exporting through odoo. IE, you want to get partner ID then go to Sales > Order > Customer > Check desired customer > Action > Export > Select ID