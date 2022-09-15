from odoo import fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'
    _description = 'New Description'

    is_pelanggan = fields.Boolean(string='Is Pelanggan')
    is_direksi = fields.Boolean(string='Is Direksi')
    poin = fields.Integer(string='Poin')
    level = fields.Char(string='Level')