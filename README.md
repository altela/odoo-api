# OdooExternalAPI
External API for create, read, write, delete (CRUD) record of Odoo through your own third-party app or module. 

Please read this README file thoroughly. All files in `main` are using the same var and if you put everything into one .py file it should be work (tested using python 3.9). In order to work, you should add [main configuration](#Main-Configuration) below to your .py files first. Then, you can add [additional configuration](#Additional-configuration) based on what you need.

To run the scripts, type `python3 -m your_file.py`

## MAIN CONFIGURATION
1. [Establisihing Connection & Login from your third party to odoo](https://github.com/Altela/odooExternalAPI/blob/main/establish_connection.py)

## ADDITIONAL CONFIGURATION
1. [Create Quotation](https://github.com/Altela/odooExternalAPI/blob/main/create_quotation.py)
2. [Printing Partner List](https://github.com/Altela/odooExternalAPI/blob/main/printing_partner.py)
3. [Create Partner](https://github.com/Altela/odooExternalAPI/blob/main/create_partner.py)
4. [Printing Product](https://github.com/Altela/odooExternalAPI/blob/main/printing_product.py)
