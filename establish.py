import xmlrpc
from connection import db, username, password
from endpoint import common

# Authenticating Connection
uid = common.authenticate(db, username, password, {})