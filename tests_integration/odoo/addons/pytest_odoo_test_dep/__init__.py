from odoo import fields


class PytestOdooCustomField(fields.Char):
    type = "pytest_odoo_custom"


fields.PytestOdooCustomField = PytestOdooCustomField
