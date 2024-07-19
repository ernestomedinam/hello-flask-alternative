from app_name.api import rest_api, docs
from .resources.hello import Hello

# hello resource
rest_api.add_resource(Hello, "/hello")
docs.register(Hello)
