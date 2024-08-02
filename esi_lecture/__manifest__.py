# -*- coding: utf-8 -*-
{
    'name': "esi_lecture",

    'summary': """
       module de ventes de livres""",

    'description': """
        module de ventes de livres
    """,

    'author': "HEB-ESI-ERP5",
    'website': "https://he2b.be/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'data/author_data.xml',
        'views/menu.xml',
        'views/book_view.xml',
        'views/author_view.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
