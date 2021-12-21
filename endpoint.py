import xmlrpc.client
from connection import url

common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))

# common is an endpoint needed to perform login
# models is an endpoint to call methods of odoo models via execute_kw RPC Function