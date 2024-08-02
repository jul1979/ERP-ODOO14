from odoo import models, fields


class LivreLike(models.Model):
    _name = 'esi.lecture.livrelike'
    _description = 'Like de livre'

    livre_id = fields.Many2one('esi.lecture.livre', string="Livre", required=True, ondelete='cascade')
    user_id = fields.Many2one('res.users', string="Utilisateur", required=True, ondelete='cascade')

    _sql_constraints = [
        ('livre_user_unique', 'UNIQUE(livre_id, user_id)', "Un utilisateur ne peut liker un livre qu'une seule fois.")
    ]
