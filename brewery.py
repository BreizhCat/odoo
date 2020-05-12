from openerp import models, fields

# Extend product.template model with calories

class Brewery_product_template(models.Model):
    _name = 'product.template'
    _inherit = 'product.template'
    
    ibu     =  fields.Float(string='Amertume (IBU)')
    abv     =  fields.Float(string='Teneur en alcool (ABV)')
    gluten  =  fields.Boolean(string='Contient du gluten' )
    abcde =  fields.Boolean(string='test')
