# -*- coding: utf-8 -*-

from odoo import fields, models, api

class Customer(models.Model):
    _name = 'pop.customer'

    name = fields.Char('Customer\'s name',required=True)
    email = fields.Char('e-mail adress')
    
    order_ids = fields.One2many('pop.order', 'customer_id')

    
class Order(models.Model):
    _name = 'pop.order'

    name = fields.Char('Evolution of the Pop\'s price')
    order_number = fields.Integer(required=True)

    pop_id = fields.Many2one('pop.item', string="Pop")
    customer_id = fields.Many2one('pop.customer', string="Customer")