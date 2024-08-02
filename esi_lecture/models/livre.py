from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Livre(models.Model):
    _name = 'esi.lecture.livre'
    _description = 'Livre'

    name = fields.Char(string="Titre", required=True)
    description = fields.Html(string="Description")
    #couverture = fields.Binary(string="Image de couverture")
    couverture = fields.Image(string="Image de couverture")
    date_publication = fields.Date(string="Date de publication", required=True)
    nombre_pages = fields.Integer(string="Nombre de pages", required=True)
    auteur_ids = fields.Many2many('res.partner', string="Auteurs")

    like_ids = fields.One2many('esi.lecture.livrelike', 'livre_id', string="Likes")
    like_count = fields.Integer(string="Nombre de likes", compute='_compute_like_count')

    _sql_constraints = [
        ('name_unique', 'UNIQUE(name)', "Le nom du livre doit être unique.")
    ]

    @api.constrains('date_publication')
    def _check_date_publication(self):
        for record in self:
            if record.date_publication >= fields.Date.today():
                raise ValidationError("La date de publication ne peut pas être dans le futur.")

    @api.constrains('nombre_pages')
    def _check_nombre_pages(self):
        for record in self:
            if record.nombre_pages <= 0:
                raise ValidationError("Le nombre de pages doit être strictement supérieur à 0.")

        # @api.constrains('auteur_ids')
        # def _check_auteurs(self):
        #     for record in self:
        #         if not record.auteur_ids:
        #             raise ValidationError("Un livre doit avoir au moins un auteur.")

    @api.depends('like_ids')
    def _compute_like_count(self):
        for livre in self:
            livre.like_count = len(livre.like_ids)

    def toggle_like(self):
        self.ensure_one()
        user = self.env.user
        like = self.env['esi.lecture.livrelike'].search([
            ('livre_id', '=', self.id),
            ('user_id', '=', user.id)
        ])
        if like:
            like.unlink()
        else:
            self.env['esi.lecture.livrelike'].create({
                'livre_id': self.id,
                'user_id': user.id
            })
        return True

    def action_view_likes(self):
        self.ensure_one()
        return {
            'name': 'Likes',
            'view_mode': 'tree,form',
            'res_model': 'esi.lecture.livrelike',
            'domain': [('livre_id', '=', self.id)],
            'type': 'ir.actions.act_window',
            'context': {'default_livre_id': self.id}
        }
