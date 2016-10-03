# -*- coding: utf-8 -*-

{
    'name': 'Payment: Lipisha Website Integration',
    'category': 'Website',
    'summary': 'Payment: Lipisha Websiet Integration',
    'version': '0.0.1',
    'description': 'Website integration for POS that allows cart checkout to be paid using Airtel and M-Pesa',
    'depends': ['website', 'payment', 'portal'],
    'data': [
        'views/website_payment_view.xml',
        'views/website_payment_templates.xml',
        'views/res_config_view.xml',
    ],
    'installable': True,
}