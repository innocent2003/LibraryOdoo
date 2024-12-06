from odoo import models, fields

class LibraryBook(models.Model):
    _name = 'library.book'
    _description = 'Library Book'

    name = fields.Char(string='Title', required=True)
    author_id = fields.Many2one('library.author', string='Author')
    description = fields.Text(string='Description')
    isbn = fields.Char(string='ISBN')
    copies_available = fields.Integer(string='Copies Available', default=1)
