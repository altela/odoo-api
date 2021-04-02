models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))
new_contact = models.execute_kw(db, uid, password, 'res.partner', 'create', [{
'company_type': "company", # select either "company" or "person"
'name': "partnerName",
'street': "partnerAddress",
'street2': "partnerAddress",
'vat': "00.000.000.0.000.000",
'phone': "123456789098",
'mobile': "partneremail@email.com",
'website': "website.com",
'customer': "True",
'lang': "en_US",
#'tags': "yourTags",

# Sales
#'customer': "True",
#'user_id': "salesPersonID",
#'property_delivery_carrier_id': "deliveryMethodID",
#'message_bounce': "numberOfBouncedEmail",
#'property_payment_term_id': "salesPaymentTermID",
#'property_product_pricelist': "productPricelistID",

# Purchase
#'vendor': "True",
#'property_supplier_payment_term_id': "purchasePaymentTermID",
#'property_purchase_currency_id': "supplierCurrencyID",

# Fiscal Information
#'property_account_position_id': "fiscalAccountID",

# Misc
#'ref': "internalReferenceNumber",
#'barcode': "partnerBarcode",
#'industry_id': "IndustryID",

#Warehouse
#'property_stock_customer': "warehouseCustomerLocation",
#'property_stock_supplier': "warehouseVendorLocation"

}])