from odoo import api, fields, models


class Mobil(models.Model):
    _name = 'dealermobil.mobil'
    _description = 'New Description'

    name = fields.Char(string='Nama Mobil')
    harga_beli = fields.Integer(string='Harga Modal', required=True)
    harga_jual = fields.Integer(string='Harga Jual', required=True)
    jenismobil_id = fields.Many2one(comodel_name='dealermobil.jenismobil',
                                        string='Jenis Mobil')
    supplier_id = fields.Many2many(comodel_name='dealermobil.supplier', string='Supplier')
    stok = fields.Integer(string='Stok')