from odoo import fields, models


class ResCompany(models.Model):
    _inherit = 'res.company'

    name_ar = fields.Char(string='Company Name (Arabic)')
    street_ar = fields.Char(string='Street (Arabic)')
    street2_ar = fields.Char(string='Street 2 (Arabic)')
    city_ar = fields.Char(string='City (Arabic)')
    state_ar = fields.Char(string='State (Arabic)')
    country_ar = fields.Char(string='Country (Arabic)')
    zip_ar = fields.Char(string='ZIP (Arabic)')
    header_bilingual_enabled = fields.Boolean(
        string='Use Bilingual Report Header',
        default=True,
        help='Show English and Arabic company identity blocks in report headers.',
    )
