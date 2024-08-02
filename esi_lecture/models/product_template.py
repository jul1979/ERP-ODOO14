from odoo import models, fields


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    livre_ids = fields.Many2many('esi.lecture.livre', string="Livres")
