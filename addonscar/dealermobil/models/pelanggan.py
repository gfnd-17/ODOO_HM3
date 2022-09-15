from odoo import api, fields, models


class Pelanggan(models.Model):
    _inherit = 'res.partner'
    _description = 'Contact'

    poin = fields.Integer(string='Poin')
    level = fields.Char(string='Level')