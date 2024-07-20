from app_name.api import rest_api, docs
from .resources.chickens import Chickens

# chickens
rest_api.add_resource(Chickens, "/chickens")
docs.register(Chickens)
