from openerp import models, fields

# Extend product.template model with calories

class Brewery_product_template(models.Model):
    _name = 'product.template'
    _inherit = 'product.template'
    
    brewery_ibu_level   = fields.Float(string='Amertume (IBU)')
    brewery_abv_level   = fields.Float(string='Teneur en alcool (ABV)')    
    brewery_has_gluten  = fields.Boolean(string='Contient du gluten' )
    brewery_is_bio      = fields.Boolean(string='Bio' )
    brewery_is_beer     = fields.Boolean(string='Bière')
    brewery_untappd_url = fields.Char("Url Untappd")
    
