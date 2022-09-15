from odoo import api, fields, models


'''
Membuat model BarangDarang yang inherit
ke Transient Model, Odoo 14 ke atas harus
di daftarkan di security
'''
class DatangMobil(models.TransientModel):
    _name = 'dealermobil.datangmobil'

    mobil_id = fields.Many2one(comodel_name='dealermobil.mobil', string='Nama Mobil', required=True)
    jumlah = fields.Integer(string='Jumlah', required=False)

    def button_datang_mobil(self):
        for line in self:
            self.env['dealermobil.mobil'].search([('id', '=', line.mobil_id.id)]).write(
                {'stok': line.mobil_id.stok +  line.jumlah}
            )