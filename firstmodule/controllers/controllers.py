# -*- coding: utf-8 -*-
from odoo import http

# class Firstmodule(http.Controller):
#     @http.route('/firstmodule/firstmodule/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/firstmodule/firstmodule/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('firstmodule.listing', {
#             'root': '/firstmodule/firstmodule',
#             'objects': http.request.env['firstmodule.firstmodule'].search([]),
#         })

#     @http.route('/firstmodule/firstmodule/objects/<model("firstmodule.firstmodule"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('firstmodule.object', {
#             'object': obj
#         })