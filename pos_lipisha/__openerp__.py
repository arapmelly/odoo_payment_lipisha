# -*- coding: utf-8 -*-

{
    'name': 'Lipisha Payment Acquirer',
    'category': 'Point Of Sale',
    'summary': 'M-Pesa and Airtel Money POS payment module',
    'version': '0.0.1',
    'depends': ['point_of_sale'],
    'data': [
        'restaurant_view.xml',
        'security/ir.model.access.csv',
        'views/templates.xml',
        'data/lipisha.xml',
    ],
    'qweb': [
        'static/src/xml/multiprint.xml',
        'static/src/xml/splitbill.xml',
        'static/src/xml/printbill.xml',
        'static/src/xml/notes.xml',
        'static/src/xml/floors/xml',
    ],
    'installable': True,
}