
/*
Integration for Google Maps in the django admin.

How it works:

You have an address field on the page.
Enter an address and an on change event will update the map
with the address. A marker will be placed at the address.
If the user needs to move the marker, they can and the geolocation
field will be updated.

Only one marker will remain present on the map at a time.

This script expects:

<input type="text" name="address" id="id_address" />
<input type="text" name="geolocation" id="id_geolocation" />

<script type="text/javascript" src="http://maps.google.com/maps/api/js?sensor=false"></script>

*/

function googleMapAdmin() {

    var geocoder = new google.maps.Geocoder();
    var map;
    var marker;

    var self = {
        initialize: function() {
            var lat = 0;
            var lng = 0;
            var zoom = 2;
            // set up initial map to be world view. also, add change
            // event so changing address will update the map
            existinglocation = self.getExistingLocation();
            if (existinglocation) {
                lat = existinglocation[0];
                lng = existinglocation[1];
                zoom = 13;
            }

            var latlng = new google.maps.LatLng(lat,lng);
            var myOptions = {
              zoom: zoom,
              center: latlng,
              mapTypeId: google.maps.MapTypeId.HYBRID
            };
            map = new google.maps.Map(document.getElementById("map_canvas"), myOptions);
            if (existinglocation) {
                self.setMarker(latlng);
            }

            $("#id_address").change(function() {self.codeAddress();});
        },

        getExistingLocation: function() {
            var geolocation = $("#id_geolocation").val();
            if (geolocation) {
                return geolocation.split(',');
            }
        },

        codeAddress: function() {
            var address = $("#id_address").val();
            geocoder.geocode({'address': address}, function(results, status) {
                if (status == google.maps.GeocoderStatus.OK) {
                    var latlng = results[0].geometry.location;
                    map.setCenter(latlng);
                    map.setZoom(13);

                    self.setMarker(latlng);
                    self.updateGeolocation(latlng);
                    self.updateAddress(latlng);
                } else {
                    alert("Geocode was not successful for the following reason: " + status);
                }
            });
        },

        setMarker: function(latlng) {
            if (marker) {
                self.updateMarker(latlng);
            } else {
                self.addMarker({'latlng': latlng, 'draggable': true});
            }
        },

        addMarker: function(Options) {
            marker = new google.maps.Marker({
                map: map,
                position: Options.latlng

            });

            var draggable = Options.draggable || false;
            if (draggable) {
                self.addMarkerDrag(marker);
            }
        },

        addMarkerDrag: function() {
            marker.setDraggable(true);
            google.maps.event.addListener(marker, 'dragend', function(new_location) {
                self.updateGeolocation(new_location.latLng);
                self.updateAddress(new_location.latLng);
            });
        },

        updateMarker: function(latlng) {
            marker.setPosition(latlng);
        },

        updateGeolocation: function(latlng) {
            $("#id_geolocation").val(latlng.lat() + "," + latlng.lng());
        },
        
        updateAddress: function(latlng) {
            geocoder.geocode({'latLng': latlng}, function(results, status) {
                if (status == google.maps.GeocoderStatus.OK) {
                    var addr = results[0].formatted_address;
                    
                    var components=results[0].address_components;

                    for (var component=0;component<(components.length);component++){
                        var type = components[component].types[0];
                        if(type == "locality" || type == "administrative_area_level_2"){
                            var locality = components[component].long_name;
                        }else if(type == "country"){
                            var country = components[component].long_name;
                        }else if(type == "administrative_area_level_1"){
                            var state = components[component].long_name;
                        }else if(type == "neighborhood" || type == "political" || type == "sublocality_level_1" || type == "sublocality"){
                            var bairro = components[component].long_name;
                        }else if(type == "route"){
                            var rua = components[component].long_name;
                        }
                    }
                    
                    $("#id_cidade").val(locality);
                    $("#id_pais").val(country);
                    $("#id_estado").val(state);
                    $("#id_bairro").val(bairro);
                    $("#id_rua").val(rua);              
                    $("#id_address").val(addr);
                } else {
                    alert("Geocode was not successful for the following reason: " + status);
                }
            });
        }
    }

    return self;
}


function googleMapAdminDoisPontos() {

    var geocoder = new google.maps.Geocoder();
    var map;
    var markerUm;
    var markerDois;

    var self = {
        initialize: function() {
            var lat = 0;
            var lng = 0;
            var zoom = 2;
            // set up initial map to be world view. also, add change
            // event so changing address will update the map
            existinglocation = self.getExistingLocation();
            if (existinglocation != '') {
                lat = existinglocation[0];
                lng = existinglocation[1];
                zoom = 13;
            }
            var latlng = new google.maps.LatLng(lat,lng);
            var latlngDois = null;
            
            existinglocation_dois = self.getExistingLocationDois();
            if (existinglocation_dois != '') {
                lat_dois = existinglocation_dois[0];
                lng_dois = existinglocation_dois[1];
                latlngDois = new google.maps.LatLng(lat_dois,lng_dois);
            }else{
                latlngDois = new google.maps.LatLng( toString(parseFloat(lat)+0.095), toString(parseFloat(lng)+0.095) );
            }

            var myOptions = {
              zoom: zoom,
              center: latlng,
              mapTypeId: google.maps.MapTypeId.HYBRID
            };
            map = new google.maps.Map(document.getElementById("map_canvas"), myOptions);
            if (existinglocation) {
                self.setMarker(latlng);
                self.setMarkerDois(latlngDois);
            }

            $("#id_origem_address").change(function() {self.codeAddress();});
            $("#id_destino_address").change(function() {self.codeAddressDois();});
        },

        getExistingLocation: function() {
            var geolocation = $("#id_origem_geolocation").val();
            if (geolocation) {
                return geolocation.split(',');
            }
            return '';
        },

        getExistingLocationDois: function() {
            var geolocation = $("#id_destino_geolocation").val();
            if (geolocation) {
                return geolocation.split(',');
            }
            return '';
        },

        codeAddress: function() {
            var address = $("#id_origem_address").val();
            geocoder.geocode({'address': address}, function(results, status) {
                if (status == google.maps.GeocoderStatus.OK) {
                    var latlng = results[0].geometry.location;
                    map.setCenter(latlng);
                    map.setZoom(13);

                    self.setMarker(latlng);
                    self.updateGeolocation(latlng);
                    self.updateAddress(latlng);
                } else {
                    alert("Geocode was not successful for the following reason: " + status);
                }
            });
        },
        codeAddressDois: function() {
            var address = $("#id_destino_address").val();
            geocoder.geocode({'address': address}, function(results, status) {
                if (status == google.maps.GeocoderStatus.OK) {
                    var latlng = results[0].geometry.location;
                    map.setCenter(latlng);
                    map.setZoom(13);

                    self.setMarkerDois(latlng);
                    self.updateGeolocationDois(latlng);
                    self.updateAddressDois(latlng);
                } else {
                    alert("Geocode was not successful for the following reason: " + status);
                }
            });
        },

        setMarker: function(latlng) {
            if (markerUm) {
                self.updateMarker(latlng);
            }
            else {
                self.addMarker({'latlng': latlng, 'draggable': true});
            }
        },
        setMarkerDois: function(latlng) {
            if (markerDois != null) {
                self.updateMarkerDois(latlng);
            }
            else {
                self.addMarker({'latlng': latlng, 'draggable': true});
            }
        },

        addMarker: function(Options) {
            markerUm = new google.maps.Marker({
                map: map,
                position: Options.latlng
            });
            markerUm.setIcon('http://maps.google.com/mapfiles/ms/icons/red-dot.png')
            markerDois = new google.maps.Marker({
                map: map,
                position: Options.latlng
            });
            markerDois.setIcon('http://maps.google.com/mapfiles/ms/icons/green-dot.png')

            var draggable = Options.draggable || false;
            if (draggable) {
                self.addMarkerDrag(markerUm);
                self.addMarkerDrag(markerDois);
            }
        },

        addMarkerDrag: function() {
            markerUm.setDraggable(true);
            google.maps.event.addListener(markerUm, 'dragend', function(new_location) {
                self.updateGeolocation(new_location.latLng);
                self.updateAddress(new_location.latLng);
            });
            markerDois.setDraggable(true);
            google.maps.event.addListener(markerDois, 'dragend', function(new_location) {
                self.updateGeolocationDois(new_location.latLng);
                self.updateAddressDois(new_location.latLng);
            });
        },

        updateMarker: function(latlng) {
            markerUm.setPosition(latlng);
        },
        updateMarkerDois: function(latlng) {
            markerDois.setPosition(latlng);
        },

        updateGeolocation: function(latlng) {
            $("#id_origem_geolocation").val(latlng.lat() + "," + latlng.lng());
        },
        updateGeolocationDois: function(latlng) {
            $("#id_destino_geolocation").val(latlng.lat() + "," + latlng.lng());
        },
        
        updateAddress: function(latlng) {
            geocoder.geocode({'latLng': latlng}, function(results, status) {
                if (status == google.maps.GeocoderStatus.OK) {
                    var addr = results[0].formatted_address;
                    
                    var components=results[0].address_components;

                    for (var component=0;component<(components.length);component++){
                        var type = components[component].types[0];
                        if(type == "locality" || type == "administrative_area_level_2"){
                            var locality = components[component].long_name;
                        }else if(type == "country"){
                            var country = components[component].long_name;
                        }else if(type == "administrative_area_level_1"){
                            var state = components[component].long_name;
                        }else if(type == "neighborhood" || type == "sublocality_level_1" || type == "sublocality"){
                            var bairro = components[component].long_name;
                        }else if(type == "route"){
                            var rua = components[component].long_name;
                        }
                    }
                    
                    $("#id_origem_cidade").val(locality);
                    $("#id_origem_pais").val(country);
                    $("#id_origem_estado").val(state);
                    $("#id_origem_bairro").val(bairro);
                    $("#id_origem_rua").val(rua);              
                    $("#id_origem_address").val(addr);
                } else {
                    alert("Geocode was not successful for the following reason: " + status);
                }
            });
        },
        updateAddressDois: function(latlng) {
            geocoder.geocode({'latLng': latlng}, function(results, status) {
                if (status == google.maps.GeocoderStatus.OK) {
                    var addr = results[0].formatted_address;
                    
                    var components=results[0].address_components;

                    for (var component=0;component<(components.length);component++){
                        var type = components[component].types[0];
                        if(type == "locality" || type == "administrative_area_level_2"){
                            var locality = components[component].long_name;
                        }else if(type == "country"){
                            var country = components[component].long_name;
                        }else if(type == "administrative_area_level_1"){
                            var state = components[component].long_name;
                        }else if(type == "neighborhood" || type == "sublocality_level_1" || type == "sublocality"){
                            var bairro = components[component].long_name;
                        }else if(type == "route"){
                            var rua = components[component].long_name;
                        }
                    }
                    
                    $("#id_destino_cidade").val(locality);
                    $("#id_destino_pais").val(country);
                    $("#id_destino_estado").val(state);
                    $("#id_destino_bairro").val(bairro);
                    $("#id_destino_rua").val(rua);              
                    $("#id_destino_address").val(addr);
                } else {
                    alert("Geocode was not successful for the following reason: " + status);
                }
            });
        }
    }

    return self;
}

$(document).ready(function() {
    if($( "#id_origem_address" ).length){
        $("#map_canvas").remove();
        var googlemap_doispontos = googleMapAdminDoisPontos();
        googlemap_doispontos.initialize();
        $("#id_origem_address").addClass("form-control");
        $("#id_destino_address").addClass("form-control");
    }else{
        var googlemap = googleMapAdmin();
        googlemap.initialize();
    }


});