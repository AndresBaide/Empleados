# -*- coding: utf-8 -*-

from odoo import models, fields, api


class departamentos(models.Model):
     _name = 'empleados.departamentos'
     _description = 'empleados.departamentos'
     n_departamento = fields.Char(string="Nombre del departamento")
     
     
     
     
     

