from openerp import models, fields

# Extend product.template model with beers informations

class Brewery_product_template(models.Model):
    _name = 'product.template'
    _inherit = 'product.template'
    
    brewery_ibu_level   = fields.Float(string='Amertume (IBU)')
    brewery_abv_level   = fields.Float(string='Teneur en alcool (ABV)')    
    brewery_has_gluten  = fields.Boolean(string='Contient du gluten' )
    brewery_is_bio      = fields.Boolean(string='Bio' )
    brewery_is_beer     = fields.Boolean(string='Bière')
    brewery_category    = fields.Many2one('product.brewery_beers_style', 'Style')
    brewery_untappd_url = fields.Char("Url Untappd")
    
class Brewery_beers_style(models.Model):
    _name = 'product.brewery_beers_style'
    _description = 'Style de bières'
    
    name = fields.Char('Nom')