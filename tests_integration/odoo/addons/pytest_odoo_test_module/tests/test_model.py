from odoo import fields

try:
    from odoo.tests.common import SavepointCase as TransactionCase
except ImportError:
    from odoo.tests.common import TransactionCase


POST_LOAD_FIELD = fields.PytestOdooPostLoadField


class TestModuleCommon(TransactionCase):
    def test_res_partner_test_method(self):
        self.assertTrue(self.env["res.partner"].res_partner_test_method())

    def test_post_load_called_before_collection(self):
        self.assertIs(POST_LOAD_FIELD, fields.Char)

    def test_dependency_custom_field_registered(self):
        partner_model = self.env["res.partner"]
        self.assertIn("pytest_odoo_custom_field", partner_model._fields)
        self.assertEqual(
            partner_model._fields["pytest_odoo_custom_field"].type,
            "pytest_odoo_custom",
        )
        partner = partner_model.create({"name": "Test Custom Field"})
        self.assertEqual(partner.pytest_odoo_custom_field, "ok")
