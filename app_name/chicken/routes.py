from app_name.api import rest_api, docs
from .resources.chickens import Chickens
from .resources.css_colors import CSSColors

# chickens
rest_api.add_resource(Chickens, "/chickens")
docs.register(Chickens)

# css-colors
rest_api.add_resource(CSSColors, "/css-colors")
docs.register(CSSColors)