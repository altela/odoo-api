models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))
new_contact = models.execute_kw(db, uid, password, 'res.partner', 'create', [{
'name': "YourPartnerName",
'street': "YourPartnerAddress",
'vat': "00.000.000.0.000.000",
'phone': "123456789098",
'mobile': "yourpartneremail@email.com",
'website': "website.com",
'customer': "True",
'lang': "English",
'ref': "yourInternalReferenceNumber",
'barcode': "yourPartnerBarcode",

#'industry_id': "yourPartnerIndustryID"
#'property_payment_term_id': "yourPaymentTermID",
#'property_delivery_carrier_id': "yourDeliveryMethodID",
#'property_product_pricelist': "yourProductPricelistID"
#'message_bounce': "numberOfYourBouncedEmail",
#'user_id': "yourSalesPersonID",
#'tags': "yourTags",
}])