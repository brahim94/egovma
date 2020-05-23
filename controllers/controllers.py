# -*- coding: utf-8 -*-
# from odoo import http


# class Egovma(http.Controller):
#     @http.route('/egovma/egovma/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/egovma/egovma/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('egovma.listing', {
#             'root': '/egovma/egovma',
#             'objects': http.request.env['egovma.egovma'].search([]),
#         })

#     @http.route('/egovma/egovma/objects/<model("egovma.egovma"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('egovma.object', {
#             'object': obj
#         })
