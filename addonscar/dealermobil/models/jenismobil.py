from odoo import api, fields, models


class JenisMobil(models.Model):
    _name = 'dealermobil.jenismobil'
    _description = 'New Description'

    name = fields.Selection([
        ('toyota', 'TOYOTA'),
        ('mitsubishi', 'MITSUBISHI'),
        ('lexus', 'LEXUS'),
        ('daihatsu', 'DAIHATSU'),
        ('marcedes benz', 'MARCEDES BENZ'),
        ('bmw', 'BMW'),
        ('datsun', 'DATSUN'),
        ('lamborghini', 'LAMBORGHINI'),
        ('audi', 'AUDI'),
        ('ferrari', 'FERRARI'),
        ('honda', 'HONDA'),
        ('nissan', 'NISSAN'),
        ('kia', 'KIA'),
        ('suzuki', 'SUZUKI'),
        ('hyundai', 'HYUNDAI')
    ], string='Nama Jenis Mobil')
    model_mobil = fields.Char(string='Tipe Jenis Mobil')

    @api.onchange('name')
    def _onchange_model_mobil(self):
        if self.name == 'toyota':
            self.model_mobil = 'TYT'
        elif self.name == 'audi':
            self.model_mobil = 'Audi'
        elif self.name == 'suzuki':
            self.model_mobil = 'SZK'
    model_tipe = fields.Char(string='Model Mobil')
    mobil_ids = fields.One2many(comodel_name='dealermobil.mobil',
                                inverse_name='jenismobil_id',
                                string='Daftar Mobil')
    jml_mobil = fields.Char(compute='_compute_jml_mobil', string='Jml Mobil')
    
    @api.depends('mobil_ids')
    def _compute_jml_mobil(self):
        for record in self:
            a = self.env['dealermobil.mobil'].search([('jenismobil_id', '=', record.id)]).mapped('name')
            b = len(a)
            record.jml_mobil = b
            record.daftar = a
    
    daftar = fields.Char(string='Daftar isi')