import xmlrpc.client
from endpoint import models
from establish import *

new_product = models.execute_kw(db, uid, password, 'product.template', 'create', [{
        'name': "Your Product Name",
        'sale_ok': True,
        'purchase_ok' : True,
        'can_be_expensed' : True,
        #'image_medium' : yourImage,

    # General Information
        'type' : "product",
        #'categ_id' : productCategoryID,
        'default_code' : "Internal Reference",
        'barcode' : 48484848,
        'list_price' : 50000,
        'standard_price' : 30000,
        'description': "Your Description",
        #'uom_id' : uomID,
        #'uom_po_id' : uomID,
        #'taxes_id' : tax_id,

    # Sales
        'available_in_pos' : True,
        #'pos_categ_id' : yourPostCategID
        'to_weight': False,
        'invoicing_policy' : "order",
        'expense_policy' : "no",
        #'optional_product_ids' : productID

    # Purchase
        #'supplier_taxes_ids' : taxID
        #'purchase_method' : purchase
        #'description_purchase' : "yourDescription"

    # INVENTORY
        'route_ids' : "Buy",
        'produce_delay' : 0.20,
        'sale_delay' : 0.30,
        'weight' : 0.40,
        'volume' : 0.50,
        #'responsible_id' : #responsible 
        #'property_stock_production' : 
        #'property_stock_inventory' : 

    # ACCOUNTING
        # 'property_account_income_id' : 
        # 'property_stock_account_input' :
        # 'property_stock_account_output' :
        # 'property_account_expense_id' :    
        # 'asset_category_id' :    
        # 'property_account_creditor_price_difference' :
}])

# Description
# sale_ok                       = This product Can Be Sold (Boolean checkbox status)
# purchase_ok                   = This product Can Be Purchased (Boolean checkbox status)
# can_be_expensed               = This Can Be Expensed (Boolean checkbox status)
# image_medium                  = Insert your product image
# type                          = select either product (Storable), consu (Consumable), service (service)
# categ_id                      = Your Product Category ID
# default_code                  = Product's internal reference
# barcode                       = Product barcode
# list_price                    = Sales Price
# standard_price                = Cost price of the product
# description                   = Internal Notes
# uom_id                        = Unit of Measure ID
# taxes_id                      = tax ID
# available_in_pos              = This product will shown and can be sold in PoS (Boolean checkbox)
# pos_categ_id                  = Category you used in Point of Sale
# to_weight                     = check if the product should be weighted using the hardware scale integration
# invoicing_policy              = Select either "order" or "delivery"
# expense_policy                = Select either "no", "cost", or "sales_price"
# purchase_method               = Select Either "purchase" or "receive"
# uom_po_id                     = Purchase Unit of Measure IDs
# taxes_id                      = Customer taxes ID
# optional_product_ids          = Product id's of related product
# supplier_taxes_ids            = Tax ID of Supplier
# description_purchase          = Description purchase
# route_ids                     = It's "Buy" as default. You can select "Make to Order" or "Manufacture"
# produce_delay                 = Manufacturing lead time
# sale_delay                    = Customer Lead Time
# weight                        = Weight in KG
# volume                        = Volume in m³
# responsible_id                = User that responsible for this product
# property_stock_production     = Production Counterpart Location
# property_stock_inventory      = Inventory Counterpart Location
