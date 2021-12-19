# Odoo XML-RPC Connection With Python
XML-RPC connection for External API to create, read, write, delete (CRUD) record of Odoo through your own external third-party app or module using python programming language. If you willing to develop and add more option, please refer to [Odoo API Documentation](https://www.odoo.com/documentation/12.0/webservices/odoo.html) & [Odoo ORM API Documentation](https://www.odoo.com/documentation/12.0/reference/orm.html)

Please read this README file thoroughly. All files in `main` are using the same var and if you put everything into one .py file it should be work (tested using python 3.9). In order to work, you should add [main configuration](#Main-Configuration) below to your .py files first. Then, you can add [additional configuration](#Additional-configuration) based on what you need.

To run the scripts, type `python3 -m your_file.py`

## MAIN CONFIGURATION
1. [Establisihing Connection & Login from your third party to odoo](https://github.com/Altela/odooExternalAPI/blob/main/establish_connection.py)

## ADDITIONAL CONFIGURATION
1. [Create Quotation](https://github.com/Altela/odooExternalAPI/blob/main/create_quotation.py)
2. [Create Partner](https://github.com/Altela/odooExternalAPI/blob/main/create_partner.py)
3. [Create Memo](https://github.com/Altela/odooExternalAPI/blob/main/create_memo.py)
4. [Create Product](https://github.com/Altela/odooExternalAPI/blob/main/create_product.py)
5. [Create Helpdesk Ticket](https://github.com/Altela/odooExternalAPI/blob/main/create_ticket_helpdesk.py)
6. [List Partner](https://github.com/Altela/odooExternalAPI/blob/main/list_partner.py)
7. [Printing Product](https://github.com/Altela/odooExternalAPI/blob/main/printing_product.py)
