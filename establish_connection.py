import xmlrpc.client

# Establishing Connection
url = 'http://yourDomain-or-yourIP'
db = 'yourDatabaseName'
username = 'yourOdooInternalUser'
password = 'yourPassword'

# Fill url with your domain or your IP.
# Fill db with your database name
# Fill username with your odoo internal user. Make sure that this username has authotrity needed to do certain job like creating quotation, cancelling invoice, etc.
# Fill password with password

# Logging in Connection
models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))
common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
uid = common.authenticate(db, username, password, {})