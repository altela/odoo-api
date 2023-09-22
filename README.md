# Odoo API XML-RPC Connection With Python
XML-RPC connection for External API to create, read, write, delete (CRUD) record of Odoo through your own external third-party app or module using python programming language. 

[View Changelog](https://github.com/Altela/odoo-api/blob/main/changelog.md)

### Clone The Project

    git clone https://github.com/Altela/odoo-api.git

### Modify `connection.py`
    url = 'https://yourDomain-or-yourIP'
    db = 'yourDatabaseName'
    username = 'yourOdooInternalUser'
    password = 'yourPassword'

### Get Into The Project
    cd odoo-api

### Run The Script
    python3 -m your_file.py

# Files Information

There are two kind of files, it's `Mandatory Files` and `Query Files`. 

### Mandatory Files
This three files will be used to establish connection between your Odoo server and app you build. You just have to edit the `connection.py` files as previous instruction tells you. 

The `connection.py` will pass the information to `endpoint.py`. When you run the `Query Files`, `establish.py` will be triggered and requesting information from `connection,py` and `endpoint.py`. This will gives you credential to log into Odoo and execute the Queries.

- [Connection File](https://github.com/Altela/odoo-api/blob/main/connection.py)
- [Endpoint File](https://github.com/Altela/odoo-api/blob/main/endpoint.py)
- [Establish Connection File](https://github.com/Altela/odoo-api/blob/main/establish.py)

### Query Files
This is the files that has queries to CRUD.

  Contact App
  - [Search Partner](https://github.com/Altela/odoo-api/blob/main/partner_list.py)
  - [Create Partner](https://github.com/Altela/odoo-api/blob/main/partner_create.py)


  Sales App
  - [Create Quotation](https://github.com/Altela/odoo-api/blob/main/quotation_create.py)

  Inventory App
  - [Search Master Product](https://github.com/Altela/odoo-api/blob/main/product_list.py)
  - [Create Master Product](https://github.com/Altela/odoo-api/blob/main/product_create.py)

  Purchase App
  - [Create RFQ](https://github.com/Altela/odoo-api/blob/main/rfq_create.py)

  Memo App
  - [Create Memo](https://github.com/Altela/odoo-api/blob/main/memo_create.py)

  Helpdesk App
  - [Create Helpdesk Ticket](https://github.com/Altela/odoo-api/blob/main/ticket_helpdesk_create.py)

  Attendance App
  - [Create Attendance](https://github.com/altela/odoo-api/blob/main/attendance_create.py)

# Contribution
If you wish to contribute, you can fork this repository, and please see this [to-do lists](https://github.com/Altela/odoo-api/issues/15).

For reference, here's the [Odoo API Documentation](https://www.odoo.com/documentation/12.0/webservices/odoo.html) & [Odoo ORM API Documentation](https://www.odoo.com/documentation/12.0/reference/orm.html).

Create your script file and make a pull request.
