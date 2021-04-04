models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))
new_product = models.execute_kw(db, uid, password, 'product.template', 'create', [{
    'name': "Odol",
    'sale_ok': True, #Can Be Sold (Boolean checkbox status)
    'purchase_ok' : True, #Can Be Purchased (Boolean checkbox status)
    'can_be_expensed' : True, #Can Be Expensed (Boolean checkbox status)
    #'categ_id' : productCategoryID, #Product Category
    'default_code' : "Internal Reference", #Print Internal Reference
    'barcode' : 899777, #Product Barcode
    'list_price' : 50000, #Sales Price
    'standard_price' : 30000, #Cost
    #'uom_id' : uomID, #Unit of Measure ID
    #'uom_po_id' : uomID, #Purchase Unit of Measure ID
    #'taxes_id' : tax_id,
    #'pos_categ_id' : ,
    'to_weight': False,
    'description': "Your Description", #Internal Notes
    'available_in_pos' : True,
    'invoicing_policy' : "order" #Select either "order" or "delivery",
    'expense_policy' : "no" #Select either "no", "cost", or "sales_price", 
    #'optional_product_ids' : productID

    # PURCHASE
    #'supplier_taxes_ids' : taxID
    #'purchase_method' : purchase #Select Either "purchase" or "receive"
    #'description_purchase' : "yourDescription"

    # INVENTORY

}])