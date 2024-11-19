# -*- coding: utf-8 -*-
{
    'name': "Course Management",
    'summary': """Manage courses and sessions""",
    'description': """Module for managing courses and sessions with date validations and computed fields.""",
    'author': "Your Name/Company",
    'website': "http://www.yourwebsite.com",
    'category': 'Education',
    'version': '0.1',
    'depends': ['base', 'sale'],
    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/course_views.xml',
        'views/session_views.xml',
        'views/coupon_views.xml',
        'wizard/sale_coupon_wizard_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}