# -*- coding: utf-8 -*-
# from odoo import http


# class Dealermobil(http.Controller):
#     @http.route('/dealermobil/dealermobil', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/dealermobil/dealermobil/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('dealermobil.listing', {
#             'root': '/dealermobil/dealermobil',
#             'objects': http.request.env['dealermobil.dealermobil'].search([]),
#         })

#     @http.route('/dealermobil/dealermobil/objects/<model("dealermobil.dealermobil"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('dealermobil.object', {
#             'object': obj
#         })

from crypt import methods
import json


import json

from odoo import http, models, fields
from odoo.http import request


class Dikimart(http.Controller):
    @http.route('/dealermobil/getmobil', auth='public', method=['GET'])
    def getMobil(self, **kw):
        # Mengambil semua mobil dari table mobil
        mobil = request.env['dealermobil.mobil'].search([])
        items = []

        for item in mobil:
            items.append({
                'nama_mobil': item.name,
                'harga_jual': item.harga_jual,
                'stok': item.stok
            })
        
        return json.dumps(items)

    @http.route('/dealermobil/getsupplier', auth='public', method=['GET'])
    def getSupplier(self, **kw):
        supplier = request.env['dealermobil.supplier'].search([])
        items = []

        for item in supplier:
            items.append({
                'nama_perusahaan': item.name,
                'alamat': item.alamat,
                'no_telepon': item.no_telp,
                'barang_id': item.mobil_id[0].name
            })
        
        return json.dumps(items)