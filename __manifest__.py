{
    'name': 'Library Management',
    'version': '1.0',
    'summary': 'Manage books and authors',
    'category': 'Tools',
    'author': 'Mitchell Admin',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/library_book_views.xml',
        'views/library_author_views.xml',
    ],
    'installable': True,
    'application': True,
}
