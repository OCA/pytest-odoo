from odoo import fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    pytest_odoo_custom_field = fields.PytestOdooCustomField(
        compute="_compute_pytest_odoo_custom_field",
        store=False,
    )

    def _compute_pytest_odoo_custom_field(self):
        for partner in self:
            partner.pytest_odoo_custom_field = "ok"

    def res_partner_test_method(self):
        return True
