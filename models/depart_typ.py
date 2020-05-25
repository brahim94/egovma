from odoo import models, fields, api
from odoo.osv import osv
from odoo.exceptions import ValidationError, AccessError


class depart_typ(models.Model):
    _inherit = "hr.department"

    type_un =  fields.Selection([ ('type1', 'Sommet'),('type2', 'Intermédiaire'),('type3', 'Feuille'),],'Type', default='type2')
    nom_un = fields.Char(string="الاسم")

class concat_name(models.Model):
#    _name = "sample.model"
    _inherit = "hr.employee"

    full_name_ar = fields.Char(string="الاسم الكامل")

    @api.onchange("preno_emp", "nom_emp")
    def _onchange_firstname_lastname(self):
        if self.preno_emp or self.nom_emp:
            self.name = str(self['preno_emp'] or '') + ' ' +str(self['nom_emp'] or '')

    preno_emp = fields.Char(string="Prénom", required=True)
    nom_emp = fields.Char(string="Nom", required=True)

    @api.constrains("preno_emp", "nom_emp")
    def _check_name(self):
        """Ensure at least one name is set."""
        for record in self:
            if not (record.preno_emp or record.nom_emp):
                raise ValidationError(("No name set."))

    @api.onchange("preno_emp_ar", "nom_emp_ar")
    def _onchange_firstname_lastname_ar(self):
        if self.preno_emp_ar or self.nom_emp_ar:
            self.full_name_ar = str(self['preno_emp_ar'] or '') + ' ' +str(self['nom_emp_ar'] or '')

    preno_emp_ar = fields.Char(string="الاسم", required=True)
    nom_emp_ar = fields.Char(string="النسب", required=True)

    @api.constrains("preno_emp_ar", "nom_emp_ar")
    def _check_name_ar(self):
        """Ensure at least one name is set."""
        for record in self:
            if not (record.preno_emp_ar or record.nom_emp_ar):
                raise ValidationError(("No name set."))

    
    




