from openerp import models, fields

# Extend product.template model with calories

class Brewery_product_template(models.Model):
    _name = 'product.template'
    _inherit = 'product.template'
    
    ibu_level = fields.Float(string='Amertume (IBU)')
    abv_level = fields.Float(string='Teneur en alcool (ABV)')    
    has_gluten = fields.Boolean(string='Contient du gluten' )
