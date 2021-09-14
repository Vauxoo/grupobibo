# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Customer Based Discount on Sales and Invoice',
    'version': '12.0.0.0',
    'sequence': 4,
    'summary': 'This module helps to allow customer based discount on sales order and invoice.',
    'category': 'sales',
    'description': """Used to specify discount on the customer that will be apply in sales orders and invoices.
BrowseInfo developed a new odoo/OpenERP module apps
Manage sales orders and Invoice  Discount
=========================================
Manages the Discount in Sale order , Purchase Order and in whole Sale order/Purchase order basis on Fix
and Percentage wise as well as calculate tax before discount and after
discount and same for the Invoice.
This module also have following separated features.
    -Global Discount on Invoice, Discount on purchase order, Global Discount on Sales order
    -Discount on sale order line, Discount on purchase order line, Discount on Invoice line
    -Discount purchase, Discount sale,Discount Invoice, Discount POS, Disount Order,Order Discount, Point of Sale Discount,Discont on pricelist, Fixed Discount, Percentage Discount, Commission, Discount Tax.
    -All in One Discount, All discount, Sales Discount, Purchase Discount,Sales Invoice Discount, Purchase Invoice Discount,Odoo Discount, OpenERP Discount, Sale Order Discount, Purchase order discount, Invoice line Discount,Discount with Taxes, Order line Discount, sale line discount, purchase line discount,Discount on line.Discount Feature, Discount for all.
	customer based discount on sales order
	customer based discount on invoice
	customer discount on sales order
	customer discount on invoice
	discount on customer form
	customer specific discount on sales order
	customer specific discount on invoice
	specific customer discount on sale order
	specific customer discount on invoice
	

   """,
    'author': 'BrowseInfo',
    'price': '15',
    'currency': "EUR",
    'author': 'BrowseInfo',
    'website': 'http://www.browseinfo.in',
    'depends': ['base','product','sale','account'],
    'data': [
        "security/ir.model.access.csv",
        "views/res_partner.xml",
    ],
    'qweb': [
    ],
    'demo': [],
    'test': [],
    'installable': True,
    'auto_install': False,
    "images":['static/description/Banner.png'],
}
