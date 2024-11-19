# -*- coding: utf-8 -*-
# from odoo import http


# class CourseModule(http.Controller):
#     @http.route('/course_module/course_module', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/course_module/course_module/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('course_module.listing', {
#             'root': '/course_module/course_module',
#             'objects': http.request.env['course_module.course_module'].search([]),
#         })

#     @http.route('/course_module/course_module/objects/<model("course_module.course_module"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('course_module.object', {
#             'object': obj
#         })

