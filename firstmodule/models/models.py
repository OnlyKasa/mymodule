# -*- coding: utf-8 -*-

# from odoo import models, fields
#
# class firstmodule(models.Model) :
#     _name = 'firstmodule.firstmodule'
#     name = fields.Char()
# value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#     self.value2 = float(self.value) / 100
# import random
from datetime import datetime
from odoo import models, fields, api
DEFAULT_SERVER_DATE_FORMAT = '%Y-%m-%d'


class Testmodels(models.Model):
    _name = 'testmodels'
    name = fields.Char(string='Tên công việc', requied=True)
    description = fields.Text(string='Miêu tả công việc')
    work = fields.Many2many('refermodels', 'name', string="Người làm")


class Refermodel(models.Model):
    _name = 'refermodels'
    name = fields.Char(string='Tên của người dùng', requied=True)
    user_id = fields.Char(string='id')
    sex = fields.Boolean(default=True, string='Giới tính')
    bird_day = fields.Date(string='Ngay sinh')
    age = fields.Integer(string='Tuoi', compute='_show_age')
    work_refer = fields.Many2many('testmodels', string="Công việc đang làm")

    # @api.multi
    # def have_name(self):
    #     for re in self:
    #         re.user_id = str(random.randint(1, 1e5))

    @api.multi
    @api.onchange('bird_day')
    @api.depends('bird_day')
    def _show_age(self):
        if self.bird_day:
            bird_day = datetime.strptime(str(self.bird_day), DEFAULT_SERVER_DATE_FORMAT)
            print bird_day
            self.age = datetime.today().year - bird_day.year
            if self.age <= 0:
                self.bird_day = False
                return {
                    'warning': {
                        'title': "BIRD DAY",
                        'message': "Value not true",
                    }
                }
