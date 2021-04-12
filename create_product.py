from establish_con import url, db, password, username, common, uid, xmlrpc

models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))
new_product = models.execute_kw(db, uid, password, 'product.template', 'create', [{
    'name': "Aal",
    'sale_ok': True, #Can Be Sold (Boolean checkbox status)
    'purchase_ok' : True, #Can Be Purchased (Boolean checkbox status)
    'can_be_expensed' : True, #Can Be Expensed (Boolean checkbox status)
    #'image_medium' : #your image

    # General Information
        'type' : "product", #select either product (Storable), consu (Consumable), service (service) 
        #'categ_id' : productCategoryID, #Product Category
        'default_code' : "Internal Reference", #Print Internal Reference
        'barcode' : 48484848, #Product Barcode
        'list_price' : 50000, #Sales Price
        'standard_price' : 30000, #Cost
        'description': "Your Description", #Internal Notes
        #'uom_id' : uomID, #Unit of Measure ID
        #'uom_po_id' : uomID, #Purchase Unit of Measure ID
        #'taxes_id' : tax_id,

    # Sales
        'available_in_pos' : True,
        #'pos_categ_id' : #category you used in Point of Sale,
        'to_weight': False,
        'invoicing_policy' : "order", #Select either "order" or "delivery",
        'expense_policy' : "no", #Select either "no", "cost", or "sales_price", 
        #'optional_product_ids' : productID

    # Purchase
        #'supplier_taxes_ids' : taxID
        #'purchase_method' : purchase #Select Either "purchase" or "receive"
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