
from django.conf import settings
from django.forms import widgets
from django.utils.encoding import force_text
from django.utils.safestring import mark_safe
from django.forms.utils import flatatt

class GoogleMapsAddressWidget(widgets.TextInput):
    "a widget that will place a google map right after the #id_address field"
    
    class Media:
        css = {'all': (settings.STATIC_URL + 'django_google_maps/css/google-maps-admin.css',),}
        js = (
            'https://ajax.googleapis.com/ajax/libs/jquery/1.11.2/jquery.min.js',
            'https://maps.google.com/maps/api/js?sensor=false',
            'https://maps.googleapis.com/maps/api/js?key=AIzaSyCjgKnfGt9jwJ-gagFNBTi6DnXiPdRFmvA&callback=initMap',
            settings.STATIC_URL + 'django_google_maps/js/google-maps-admin.js',
        )

    def render(self, name, value, attrs=None, renderer=None):
        if value is None:
            value = ''
        # final_attrs = self.build_attrs(attrs, type=self.input_type, name=name)
        final_attrs = self.build_attrs(attrs, extra_attrs={'type':self.input_type, 'name':name})
        if value != '':
            # Only add the 'value' attribute if a value is non-empty.
            final_attrs['value'] = force_text(self.format_value(value))
        return mark_safe(u'<input%s /><div class="map_canvas_wrapper"><div id="map_canvas"></div></div>' % flatatt(final_attrs))
