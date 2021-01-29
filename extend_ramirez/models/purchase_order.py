
from odoo import _, api, fields, models

class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    qty_product = fields.Integer(
        string='Cantidad',
        compute="_compute_qty_product"
    )

    @api.depends('order_line.product_uom_qty')
    def _compute_qty_product(self):
        for rec in self:
            if rec.order_line:
                for l in rec.order_line:
                    if l.product_qty:
                        rec.qty_product += l.product_qty
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
        data['data'][tmpl_id]["price_total"] += line.price_total
        if data['data'][tmpl_id].get("display_name"): return
        data['data'][tmpl_id]["image_128"] = line.product_id.image_128
        data['data'][tmpl_id]["price_unit"] = line.price_unit
        data['data'][tmpl_id][
            "display_name"] = line.product_id.product_tmpl_id.display_name
        data['data'][tmpl_id]["taxes"] = ', '.join(
            map(lambda x: (x.description or x.name), line.taxes_id))