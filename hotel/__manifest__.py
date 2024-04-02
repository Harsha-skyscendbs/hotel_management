{
    'name':'Hotel Management System',
    'description':'This module is used for booking hotel rooms',
    'author':'Harsha Yadav',
    'website':'https://www.stardivine.com',
    'version':'1.0',
    'depends':['base'],
    'data': [
        'security/hotel_security.xml',
             'security/ir.model.access.csv',
             'views/booking_view.xml'],
    'auto_install': False,
    'installable':True,
    'application': True,
    'license':'OEEL-1',
}