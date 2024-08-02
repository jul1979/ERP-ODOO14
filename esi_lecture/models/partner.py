from odoo import models, fields


class ResPartner(models.Model):
    _name = 'res.partner'
    _inherit = 'res.partner'

    is_author = fields.Boolean(string='Est auteur', default=False)
    livre_ids = fields.Many2many('esi.lecture.livre', string="Livres")
