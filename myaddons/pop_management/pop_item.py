# -*- coding: utf-8 -*-

from odoo import fields, models, api

class Pop(models.Model):
    _name = 'pop.item'

    name = fields.Char('Pop\'s name',required=True)
    current_price = fields.Float()
    category = fields.Selection([('disney', 'Disney'),('marvel','Marvel'),('dc_comics','DC Comics')])
    number = fields.Integer()

    order_ids = fields.One2many('pop.order', 'pop_id')
    price_evolutions_ids = fields.One2many('price.evol', 'pop_id')


class PriceEvolution(models.Model):
    _name= 'price.evol'

    name = fields.Char('Evolution of the Pop\'s price')
    price = fields.Float()
    date = fields.Datetime()
    
    pop_id = fields.Many2one('pop.item',string="Pop")