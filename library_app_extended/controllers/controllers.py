# -*- coding: utf-8 -*-
# from odoo import http


# class LibraryAppExtended(http.Controller):
#     @http.route('/library_app_extended/library_app_extended/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/library_app_extended/library_app_extended/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('library_app_extended.listing', {
#             'root': '/library_app_extended/library_app_extended',
#             'objects': http.request.env['library_app_extended.library_app_extended'].search([]),
#         })

#     @http.route('/library_app_extended/library_app_extended/objects/<model("library_app_extended.library_app_extended"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('library_app_extended.object', {
#             'object': obj
#         })
