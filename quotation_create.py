import xmlrpc.client
from endpoint import models
from establish import *
from datetime import datetime

new_quotation = models.execute_kw(db, uid, password, 'sale.order', 'create', [{
    'state': "draft", #Select either "sent", "sale", "done", "cancel"
    'partner_id': yourPartnerID, #Customer ID
    'client_order_ref': "000000", #Order Reference Number
    'picking_policy': "direct", #select either "direct" or "one"  
    'order_line' : [
        # First line of Order Lines
        (0, 0, {    
            'product_id': product_id, #insert product ID
            'product_uom_qty': 20, #insert product qty
            #'price_unit': desiredPrice,
            #'discount' : desiredDisc,
            #'tax_id': taxID,
            }
        ),
        
        # Second line of Order Lines
        (0, 0, {    
            'product_id': product_id, #insert product ID
            'product_uom_qty': 50, #insert product qty
            #'price_unit': desiredPrice,
            #'discount' : desiredDisc,
            #'tax_id': taxID,
            }
        )
    ],
    
    #Optional Products
    #Every record you want to put into Optional Products is mandatory so you cannot skip one of these dictionary below.
    #
    #'sale_order_option_ids':[
    #    (0, 0, {
    #        'product_id': 2285, #insert product ID
    #        'product_uom_qty': 100, #insert product qty
    #        'price_unit': 100000,
    #        'name': , #in case you want to put name here, you must do some SEARCH and READ the ID then you can pull the name of product here.
    #        'uom_id' : 31,
    #    })
    #]

   # 'commitment_date': 21-12-31,
    'date_order': "06/05/2021 15:28:55",
    'validity_date': "2021-10-10",
#    'pricelist_id': pricelistID,
#    'fiscal_position_id': fiscalID,
#    'payment_term_id: paymentTermID,
#    'user_id': salesPersonID,
#    'team_id': salesTeamID,
#    'carrier_id' : deliveryMethodID,
#    'require_signature': True,
#    'require_payment': True,
#    'analytic_account_id': analyticAccountID,
#    'origin': "sourceDocumentNumber"
}])

 # Fill in partner_id with your partner ID
 # Fill in product_id with your product ID
 # Fill in product_uom_qty your desired qty
 # IDs can be acquired from exporting through odoo. IE, you want to get partner ID then go to Sales > Order > Customer > Check desired customer > Action > Export > Select ID