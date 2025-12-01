# -*- coding: utf-8 -*-

from odoo import models, fields, api

class alumnos_sueno(models.Model):
     _name = 'bebidas_sueno.alumnos_sueno'
     _description = 'bebidas_sueno.alumnos_sueno'

     alumno = fields.Text(string="Nombre del alumno")
     nivel_sueno = fields.Integer(string="Nivel de sueño")
     bebida = fields.Text(compute="_recomendar_bebida", store=True,string="Bebida que hay que darle")
     
     @api.depends('nivel_sueno')
     def _recomendar_bebida(self):
        for record in self:
            if 1 <= record.nivel_sueno <= 3:
                record.bebida = "Café con leche"
            elif 3 < record.nivel_sueno <= 6:
                record.bebida = "Café solo largo"
            elif record.nivel_sueno > 6 and record.nivel_sueno <= 9:
                record.bebida = "Cafe solo largisimo"
            elif record.nivel_sueno == 10:
                record.bebida = "Inyeccion de adrenalina"
            else:
                record.bebida = "Muerto o no tienes sueño"