# -*- coding: utf-8 -*-
{
    'name': "Bebidas Sueño",

    'summary': """
        Es un modulo para ver bebidas para estudiantes segun su nivel de sueño""",

    'description': """
        Modulo para ver que bebidas darle a los alumnos de un centro educativo que se duermen en clase según su nivel
        de sueño, las bebidas van de cosas tan diversas como un cafe hasta una inyeccion de adrenalina
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv', # Acordarme siempre descomentar esta cosa
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}