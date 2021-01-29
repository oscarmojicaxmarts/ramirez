# -*- coding: utf-8 -*-
{
    'name': "Extend ramirez",

    'summary': """""",

    'description': """
    """,

    'author': "Ramirez Dev",
    'website': "Ramirez Sport",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['purchase','stock','sale','purchase_sale'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/purchase_order.xml',
        'views/stock_picking.xml',
        'views/sale_order.xml',
        'report/report_purchase_order.xml',
        'report/report_sale_order.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
