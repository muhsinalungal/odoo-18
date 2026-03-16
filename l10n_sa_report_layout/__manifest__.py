{
    'name': 'Saudi Report Layout',
    'summary': 'Bilingual English and Arabic company headers for Saudi commercial documents.',
    'version': '18.0.1.0.0',
    'category': 'Accounting/Localizations',
    'author': 'Custom',
    'website': 'https://www.odoo.com',
    'license': 'LGPL-3',
    'depends': [
        'web',
        'account',
        'sale',
        'l10n_sa',
    ],
    'data': [
        'views/res_company_views.xml',
        'views/base_document_layout_views.xml',
        'report/report_templates.xml',
    ],
    'assets': {
        'web.report_assets_common': [
            'l10n_sa_report_layout/static/src/scss/report_layout.scss',
        ],
    },
    'installable': True,
    'application': False,
}
