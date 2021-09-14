{
    'name': 'Bibo Reporte Cotizacion',
    'version': '1.0',
    'summary': 'Personalizacion de bibo',
    'description': 'Modificacion del reporte de operaciones de Picking',
    'category': 'Personalizacion',
    'author': 'Xmarts',
    'website': 'www.xmarts.com',
    'depends': [
        'stock',
                ],
    'data': [
        'reports/report_cotizacion_parcialidad.xml',
        'reports/reports_menu.xml',

    ],
    'installable': True,
    'auto_install': False,
}
