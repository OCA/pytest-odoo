from . import controllers
from . import models


def post_load():
    from odoo import fields

    fields.PytestOdooPostLoadField = fields.Char
