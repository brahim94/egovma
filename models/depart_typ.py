from odoo import api, fields, models
from odoo.exceptions import AccessError, UserError, ValidationError


class depart_typ(models.Model):
    _inherit = "hr.department"

    depart_typ_fiel = fields.Many2one('department.type', 'Type')
    type_test = fields.Selection(related='depart_typ_fiel.niveau')
    nom_un = fields.Char(string="الاسم")

    
class depart_line(models.Model):
    _name = "department.type"
    _description = "Type Hierarchie"

    name = fields.Char(string="Nom", store=True, readonly=False)
    _sql_constraints = [        
    ('name_uniq',
        'UNIQUE (name)',
        'type must be unique.')
    ]
    niveau =  fields.Selection([ ('type1', 'Sommet'),('type2', 'Intermédiaire'),('type3', 'Feuille'),], string="Niveau", default='type2')
    #depa = fields.One2many('hr.department','depart_typ', string="Departement")
       
class concat_name(models.Model):
#    _name = "sample.model"
    _inherit = "hr.employee"

    corp = fields.Many2one('employee.corp', 'Corps')
    grad = fields.Many2one('employee.grad', 'Grade')
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

class hr_corp(models.Model):
    _name = "employee.corp"
    _description = "Corp"

    name = fields.Char(string="Nom", store=True, readonly=False)
    _sql_constraints = [        
    ('name_uniq',
        'UNIQUE (name)',
        'name corp must be unique.')
    ]
    nom_corp_ar = fields.Char(string="الاسم")
    
class hr_grade(models.Model):
    _name = "employee.grad"
    _description = "Grade Employé"

    name = fields.Char(string="Nom", store=True, readonly=False)
    _sql_constraints = [        
    ('name_uniq',
        'UNIQUE (name)',
        'name grade must be unique.')
    ]
    nom_grade_ar = fields.Char(string="الاسم")

class event_emplacement(models.Model):
    _name = "event.emplacement"

    name = fields.Char(string="Nom")

class event_emplacement_arrive(models.Model):
    _name = "event.emplacement.arrive"

    name = fields.Char(string="Nom")

class event_trajet_line(models.Model):
    _inherit = "event.event"

    trajet = fields.One2many('event.trajet','trajet_id', string="Trajets")
    name_test = fields.Char(related='trajet.name_id')
    conducteur = fields.Many2many('hr.employee', string="Conducteur")
    vehicule = fields.Many2many('fleet.vehicle', string="Vehicule")

class event_trajets(models.Model):
    _name = "event.trajet"
    _description = "Trajet de la mission"

    name_id = fields.Char(string='Trajet Reference', required=True, copy=False, readonly=True, index=True, default=lambda self: ('New'))
    _sql_constraints = [        
    ('name_uniq',
        'UNIQUE (name)',
       'name trajet must be unique.')
    ]

    @api.model 
    def create(self, vals):
        if vals.get('name_id', ('New')) == ('New'):
            vals['name_id'] = self.env['ir.sequence'].next_by_code('trajet.order') or ('New')
        result = super(event_trajets, self).create(vals)
        return result 

    type_tr = fields.Selection([ ('type1', 'Route Nationale'),('type2', 'Route Autoroute'),],'Type Route', default='type2')
    trajet_id = fields.Many2one('event.event', string="Trajet ID")
    point_dpart_ids = fields.Many2many('event.emplacement', string="Point de départ")
    point_arriv_ids = fields.Many2many('event.emplacement.arrive', string="Point d'arrivé")

