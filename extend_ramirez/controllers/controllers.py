# -*- coding: utf-8 -*-
# from odoo import http


# class ExtendRamirez(http.Controller):
#     @http.route('/extend_ramirez/extend_ramirez/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/extend_ramirez/extend_ramirez/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('extend_ramirez.listing', {
#             'root': '/extend_ramirez/extend_ramirez',
#             'objects': http.request.env['extend_ramirez.extend_ramirez'].search([]),
#         })

#     @http.route('/extend_ramirez/extend_ramirez/objects/<model("extend_ramirez.extend_ramirez"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('extend_ramirez.object', {
#             'object': obj
#         })
