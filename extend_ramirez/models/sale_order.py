
from odoo import _, api, fields, models

class SaleOrder(models.Model):
    _inherit = "sale.order"

    qty_product = fields.Integer(
        string='Cantidad',
        compute="_compute_qty_product"
    )

    @api.depends('order_line.product_uom_qty')
    def _compute_qty_product(self):
        for rec in self:
            if rec.order_line:
                for l in rec.order_line:
                    if l.product_uom_qty:
                        rec.qty_product += l.product_uom_qty
                    else:
                        rec.qty_product += 0

            else:
                rec.qty_product = 0

    @staticmethod
    def update_values(postion, idx, data, line):
        tmpl_id = line.product_id.product_tmpl_id.id
        if line.product_id.id not in postion:
            idx[line.product_id.product_tmpl_id.id] += 1
            postion.update({
                line.product_id.id: idx[line.product_id.product_tmpl_id.id]
            })
            talla = ""
            for t in line.product_id.product_template_attribute_value_ids:
                if t.attribute_id.name == "Talla":
                    talla = t.name
            data['cols'][tmpl_id][
                idx[line.product_id.product_tmpl_id.id]
            ] = talla
        data['data'][tmpl_id][
            postion[line.product_id.id]
        ] += line.product_uom_qty
        data['data'][tmpl_id]["price_unit_cal"] = line.price_unit_cal
        data['data'][tmpl_id]["price_total"] += line.price_total
        if data['data'][tmpl_id].get("display_name"): return
        data['data'][tmpl_id]["image_128"] = line.product_id.image_128
        data['data'][tmpl_id]["price_unit"] = line.price_unit
        data['data'][tmpl_id]["display_name"] = line.product_id.product_tmpl_id.display_name
        data['data'][tmpl_id]["discount"] += line.discount      
        data['data'][tmpl_id]["taxes"] = ', '.join(map(lambda x: (x.description or x.name), line.tax_id))



class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    price_unit_cal = fields.Float(
        string='Precio Unitario',
        compute="_compute_price_unit_cal"
    )



    @api.depends('product_uom_qty','price_unit','discount','price_subtotal')
    def _compute_price_unit_cal(self):
        for rec in self:
            if rec.product_uom_qty and rec.price_subtotal:
                rec.price_unit_cal = rec.price_subtotal / rec.product_uom_qty
            else:
                rec.price_unit_cal = 0.00


