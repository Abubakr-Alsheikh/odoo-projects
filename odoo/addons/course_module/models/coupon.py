from odoo import models, fields

class SaleCoupon(models.Model):
    _name = 'sale.coupon'
    _description = "Sale Coupon"

    product_id = fields.Many2one('product.product', string="Product", required=True)
    customer_id = fields.Many2one('res.partner', string="Customer", required=True)
    percentage = fields.Float(string="Percentage", required=True)