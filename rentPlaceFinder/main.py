from properties import Property
from responses import Response
p = Property()
p.fetch_listings()
property_listings = p.get_properties()


r = Response()
r.enter_responses(property_listings)