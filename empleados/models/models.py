# -*- coding: utf-8 -*-

from odoo import models, fields, api


class empleados(models.Model):
     _name = 'empleados.empleados'
     _description = 'empleados.empleados'
     name = fields.Char(string="Nombre")
     edad = fields.Integer(string="Edad")
     numero_tlf = fields.Char(string="Numero de telefono")
     n_departamento = fields.Many2one('empleados.departamentos',  string="Departamentos", required=True)
     

     
     
     
     

