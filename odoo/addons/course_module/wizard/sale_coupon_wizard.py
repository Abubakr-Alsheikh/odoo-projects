from odoo import models, fields, api

class SaleCouponWizard(models.TransientModel):
    _name = 'sale.coupon.wizard'
    _description = "Sale Coupon Wizard"

    partner_id = fields.Many2one('res.partner', string="Customer", required=True)
    from_date = fields.Date(string="From Date", required=True)
    to_date = fields.Date(string="To Date", required=True)
    sale_order_ids = fields.Many2many('sale.order', string="Sale Orders")
    default_product_id = fields.Many2one('product.product',  string='Default Product', required=True)

    def action_fetch_sale_orders(self):
        self.sale_order_ids = self.env['sale.order'].search([
            ('partner_id', '=', self.partner_id.id),
            ('date_order', '>=', self.from_date),
            ('date_order', '<=', self.to_date)
        ])
        return {
            'type': 'ir.actions.act_window',
            'res_model': self._name,
            'view_mode': 'form',
            'res_id': self.id,
            'target': 'new',
        }


    def action_generate_coupon(self):
        if len(self.sale_order_ids) > 5:
            self.env['sale.coupon'].create({
                'product_id': self.default_product_id.id,
                'customer_id': self.partner_id.id,
                'percentage': 50.0,
            })