{
    'name': 'CTH',
    'version': '1.0',
    'sequence': 14,
    'summary': 'customize view',
    'description': """
            Need to add province & district in partner address \n
            The master data can see in \n
            menu : Sales -> Configuration -> Address Book -> Provinces | Districts
    """,
    'depends': ['base'],
    'installable': True,
    'data': [
        'view.xml',
        'security/ir.model.access.csv',
        ],
    'demo': [
        'data/cth.province.csv',
        'data/cth.district.csv',
    ]
}
