# -*- coding: utf-8 -*
import dp

from odoo import models, fields, api


class LibraryBook(models.Model):
    _name = "library.book"
    _description = "Library Book"
    _sql_constraints = [
        ('name_uniq',
         'UNIQUE (name)',
         'Book title must be unique.')
    ]
    name = fields.Char('Title', require=True)
    short_name = fields.Char('Short Title')
    date_release = fields.Date('Release date')
    author_ids = fields.Many2many('res.partner', string='Authors')
    note = fields.Selection(
        [('draft', 'Not Available'),
         ('available', 'Available'),
         ('lost', 'Lost')],
        'State'
    )
    # cost_price = fields.Float(
    #     'Book Cost', dp.get_precision('Book Price'))
    descreption = fields.Html('Descripttion')
    cover= fields.Binary('Book Cover')
    out_of_print = fields.Boolean('Out of Print?')
    date_update = fields.Date('Release Date')
    date_updated = fields.Datetime('Last Updated')
    pages = fields.Integer('Number of Pages')
    # reader_rating = fields.Float(
    #     'Reader Average Rating'
    #     (14, 4)
    # )
    currency_id = fields.Many2one('res.currency', string='Currency')
    retail_price = fields.Monetary('Retail Price')
    age_days = fields.Float(
        string='Days Since Release',
        compute='_compute_age',
        inverse='_inverse_age',
        search='_search_age',
        store=False,
        compute_sudo=False,
    )
    publisher_id = fields.Many2one(
        'res.partner', string='Publisher')
    publisher_city = fields.Char(
        'Publisher City',
        related='publisher_id.city')

    @api.constrains('date_release')
    def _check_release_date(self):
        for r in self:
            if r.date_release > fields.Date.today():
                raise models.ValidationError(
                    'Release date must be in the past')

    def name_get(self):
        result = []
        for record in self:
            result.append((record.id, u"%s (%s)" % (record.name, record.date_release)))
        return result


