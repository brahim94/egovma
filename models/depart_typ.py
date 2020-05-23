from odoo import models, fields, api


class depart_typ(models.Model):
    _inherit = "hr.department"

    type_un =  fields.Selection([ ('type1', 'Sommet'),('type2', 'Intermédiaire'),('type3', 'Feuille'),],'Type', default='type2')
    nom_un = fields.Char(string="الاسم")


