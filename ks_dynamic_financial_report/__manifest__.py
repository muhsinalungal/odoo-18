# -*- coding: utf-8 -*-
{
    'name': 'Dynamic Financial Report',

    'summary': 'Odoo 18 dynamic financial reports: P&L, Balance Sheet, Tax, GL, Partner Ledger, Aging, Trial Balance, Cash Flow, and Executive Summary',

    'description': """
Dynamic Financial Report for Odoo 18.

This module provides dynamic accounting and financial reports including:
- Profit and Loss
- Balance Sheet
- Cash Flow Statement
- Executive Summary
- Trial Balance
- General Ledger
- Partner Ledger
- Aged Receivable
- Aged Payable
- Consolidate Journal
- Tax Report

Odoo 18 compatibility:
- Ported and validated on Odoo 18
- Backend ORM/report APIs updated for Odoo 18
- Frontend OWL/dropdown behavior updated for Odoo 18
- XLSX, PDF, drilldown, and filter flows verified during migration

See README.md for local migration notes and tested behavior.
    """,
    'author': 'Ksolves India Ltd.',

    'website': 'https://store.ksolves.com/',

    'live_test_url': 'https://dynamicreport15.kappso.in/web/demo_login',
    'category': 'Accounting/Accounting',
    'currency': 'EUR',
    'version': '18.0.1.1.0',
    'price': '119',
    'license': 'OPL-1',
    'maintainer': 'Ksolves India Ltd.',
    'support': 'sales@ksolves.com',
    'images': ['static/description/DFR2.gif'],
    'depends': ['base', 'mail', 'account', 'sale_management'],
    'auto_install': True,
    'data': ['security/ir.model.access.csv', 'data/ks_dfr_account_data.xml', 'data/ks_dynamic_financial_report.xml',
             'security/ks_access_file.xml',
             'views/ks_mail_template.xml', 'views/ks_searchtemplate.xml', 'views/ks_base_template.xml',
             'views/ks_dfr_account_type.xml',
             'views/ks_res_config_settings.xml'],

    'assets': {'web.assets_backend': ['ks_dynamic_financial_report/static/src/scss/ks_dynamic_financial_report.scss',
                                      'ks_dynamic_financial_report/static/src/scss/ks_pdf.scss',
                                      'ks_dynamic_financial_report/static/src/js/ks_dynamic_action_manager.js',
                                      'ks_dynamic_financial_report/static/src/js/ks_dynamic_financial_report.js',
                                      'ks_dynamic_financial_report/static/src/xml/ks_dynamic_financial_report.xml',
                                      ]},
}
