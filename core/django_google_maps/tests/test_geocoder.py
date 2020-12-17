from django import test

from core.django_google_maps.geocoder import GoogleMapsPointAddress, GoogleMapsV3Geocoder

class GeocoderTests(test.TestCase):

    def test_gmaps_reverse_geocoder(self):
        # https://maps.googleapis.com/maps/api/geocode/json?latlng=-12.9510242,-38.4414401&language=pt-BR
        address_obj = GoogleMapsV3Geocoder.parseGeolocation2Address("-12.9510242,-38.4414401")
        self.assertEqual(address_obj.city, "Salvador")
        self.assertEqual(address_obj.country, "Brasil")

    def test_gmaps_reverse_geocoder_english(self):
        # https://maps.googleapis.com/maps/api/geocode/json?latlng=-12.9510242,-38.4414401&language=en-US
        address_obj = GoogleMapsV3Geocoder.parseGeolocation2Address("-12.9510242,-38.4414401", language="en-US")
        self.assertEqual(address_obj.country, "Brazil")
