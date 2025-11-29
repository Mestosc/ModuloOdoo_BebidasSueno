# -*- coding: utf-8 -*-
from odoo import http

class BebidasSueno(http.Controller):
     @http.route('/bebidas_sueno/bebidas_sueno', auth='public')
     def index(self, **kw):
         return "Hello, world"

     @http.route('/bebidas_sueno/bebidas_sueno/objects', auth='public')
     def list(self, **kw):
         return http.request.render('bebidas_sueno.listing', {
             'root': '/bebidas_sueno/bebidas_sueno',
             'objects': http.request.env['bebidas_sueno.alumnos_sueno'].search([]),
         })

     @http.route('/bebidas_sueno/bebidas_sueno/objects/<model("bebidas_sueno.alumnos_sueno"):obj>', auth='public')
     def object(self, obj, **kw):
         return http.request.render('bebidas_sueno.object', {
             'object': obj
         })