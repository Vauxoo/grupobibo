# -*- coding: utf-8 -*-
from odoo import http

# class BiboCalculationPieces(http.Controller):
#     @http.route('/bibo_calculation_pieces/bibo_calculation_pieces/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/bibo_calculation_pieces/bibo_calculation_pieces/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('bibo_calculation_pieces.listing', {
#             'root': '/bibo_calculation_pieces/bibo_calculation_pieces',
#             'objects': http.request.env['bibo_calculation_pieces.bibo_calculation_pieces'].search([]),
#         })

#     @http.route('/bibo_calculation_pieces/bibo_calculation_pieces/objects/<model("bibo_calculation_pieces.bibo_calculation_pieces"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('bibo_calculation_pieces.object', {
#             'object': obj
#         })