from odoo import fields, models, api


class PenjualanReport(models.TransientModel):
    _name = 'dealermobil.penjualanreport'
    _description = 'Description'

    pelanggan_id = fields.Many2one(
        comodel_name='res.partner',
        string='Pelanggan',
        required=False)
    dari_tgl = fields.Date(
        string='Dari Tanggal',
        required=False)
    ke_tgl = fields.Date(
        string='Ke tanggal',
        required=False)

    def action_penjualan_report(self):
        filter = []
        pelanggan_id = self.pelanggan_id
        dari_tgl = self.dari_tgl
        ke_tgl = self.ke_tgl
        if pelanggan_id:
            filter += [('nama_pembeli', '=', pelanggan_id.id)]
        if dari_tgl:
            filter += [('tgl_penjualan', '>=', dari_tgl)]
        if ke_tgl:
            filter += [('tgl_penjualan', '<=', ke_tgl)]
        print(filter)
        penjualan = self.env['dealermobil.penjualan'].search_read(filter)
        print(penjualan)
        data = {
            'form': self.read()[0],
            'penjualanxx': penjualan,
        }
        print(data)
        return self.env.ref('dealermobil.wizard_penjualanreport_pdf').report_action(self, data=data)