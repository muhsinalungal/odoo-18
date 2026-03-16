from odoo import fields, models


class BaseDocumentLayout(models.TransientModel):
    _inherit = 'base.document.layout'

    name_ar = fields.Char(related='company_id.name_ar', readonly=False)
    street_ar = fields.Char(related='company_id.street_ar', readonly=False)
    street2_ar = fields.Char(related='company_id.street2_ar', readonly=False)
    city_ar = fields.Char(related='company_id.city_ar', readonly=False)
    state_ar = fields.Char(related='company_id.state_ar', readonly=False)
    country_ar = fields.Char(related='company_id.country_ar', readonly=False)
    zip_ar = fields.Char(related='company_id.zip_ar', readonly=False)
    header_bilingual_enabled = fields.Boolean(
        related='company_id.header_bilingual_enabled',
        readonly=False,
    )
