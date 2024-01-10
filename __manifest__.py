# custom_addons/hospital_management/__manifest__.py

{
    'name': 'Push Notifications',
    'summary' : "Push notifications for Odoo users",
    'version': '0.1',
    'depends': ['base'],
    'author': 'Saif',
    'category': 'Uncategorized',
    'description': 'Hospital Management System Odoo Module',
    'data': [
        'security/ir.model.access.csv',
        'views/push_notification.xml'
    ],
    'installable': True,
    'application': True,
    'auto_install': False
    
}
