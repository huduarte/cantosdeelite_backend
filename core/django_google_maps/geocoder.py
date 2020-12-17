from geopy.geocoders import GoogleV3

class GoogleMapsPointAddress(object):

    def __init__(self, formatted_address=None, address=None, geolocation=None, 
        city=None, country=None, state=None, neighborhood=None, street=None):
        self.formatted_address = formatted_address
        self.geolocation = geolocation
        self.city = city
        self.country = country
        self.state = state
        self.neighborhood = neighborhood
        self.street = street

class GoogleMapsV3Geocoder(object):

    @staticmethod
    def parseGeolocation2Address(str_geolocation, language="pt-BR"):
        geopoint_address = GoogleMapsPointAddress()  # retorno do metodo
        
        geolocator = GoogleV3()
        location = geolocator.reverse(str_geolocation, exactly_one=True, language=language)
        raw_location = location.raw

        geopoint_address.formatted_address = raw_location.get("formatted_address")

        address_components = raw_location.get("address_components")
        for component in address_components:

            if GoogleMapsV3Geocoder.hasComponent(["locality", "administrative_area_level_2"], component["types"]):
                geopoint_address.city = component["long_name"]

            elif GoogleMapsV3Geocoder.hasComponent(["country"], component["types"]):
                geopoint_address.country = component["long_name"]

            elif GoogleMapsV3Geocoder.hasComponent(["administrative_area_level_1"], component["types"]):
                geopoint_address.state = component["long_name"]

            elif GoogleMapsV3Geocoder.hasComponent(["neighborhood", "sublocality_level_1", "sublocality"], component["types"]):
                geopoint_address.neighborhood = component["long_name"]

            elif GoogleMapsV3Geocoder.hasComponent(["route"], component["types"]):
                geopoint_address.street = component["long_name"]

        return geopoint_address

    @staticmethod
    def hasComponent(listA, listB):
        return not set(listA).isdisjoint(listB)
