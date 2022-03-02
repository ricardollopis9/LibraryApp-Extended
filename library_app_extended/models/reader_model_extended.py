from odoo.exceptions import ValidationError
from odoo import models, fields, api


class Reader_model_extended(models.Model):
    _name = "library_app_extended.reader_model_extended"
    _inherit = 'library_app.reader_model'

    personaldescription = fields.Char(string="Personal Description", help="Describe yourself")
    