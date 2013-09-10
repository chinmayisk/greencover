from django.shortcuts import render, render_to_response
from models import Tree
import simplejson
from django.http import HttpResponse
from django.template import Context


def index(request):
	HEAD = '''
	<!DOCTYPE html>
<html>
  <head>
    <meta name="viewport" content="initial-scale=1.0, user-scalable=no">
    <meta charset="utf-8">
    <title>GreenCover - Bangalore</title>
    <link href="/static/css/default.css" rel="stylesheet">
    <script src="https://maps.googleapis.com/maps/api/js?v=3.exp&sensor=false"></script>
    <script>
      function initialize() {
        var mapOptions = {
          zoom: 11,
          center: new google.maps.LatLng(12.9838, 77.5407),
          mapTypeId: google.maps.MapTypeId.ROADMAP
        };
        var map = new google.maps.Map(document.getElementById('map-canvas'), mapOptions);
        setMarkers(map, trees);
      }

      var trees = ['''
	BODY = '''
	];

      function setMarkers(map, locations) {
        var image = {
          url: '/static/images/tree2.png',
          size: new google.maps.Size(31, 33),
          origin: new google.maps.Point(0,0),
          anchor: new google.maps.Point(0, 33),
        };
      
        for (var i = 0; i < locations.length; i++) {
          var beach = locations[i];
          var myLatLng = new google.maps.LatLng(beach[1], beach[2]);
          var marker = new google.maps.Marker({
            position: myLatLng,
            map: map,
            icon: image,
            title: beach[0],
            animation: google.maps.Animation.DROP,
            zIndex: beach[3],
          }); 
        }
      }
      google.maps.event.addDomListener(window, 'load', initialize);

    </script>
  </head>
  <body>
    <div id="map-canvas"></div>
    <div id="footer">Created by Ankitha Heroorkar, Chinmayi SK, Hiemanshu Sharma.</div>
  </body>
</html>
	'''
	objects = Tree.objects
	count = objects.count()
	markers = ''
	for i in objects.all():
		markers += '[\'%s\', %f, %f, %d], ' %(i.name, i.x, i.y, count)
		count -= 1
	html = HEAD + markers + BODY
	return HttpResponse(html)

def treeinfo(request, tree_id):
	tree = Tree.objects.get(pk=tree_id)
	treeinfo = ('{"tree" : {"name" : "%s", "color" : "%s", "coord" : "%s,%s", "state" : "%s"},}' %(tree.name, tree.color, tree.x, tree.y, "Blooming"))
	print treeinfo
	return render(request, 'treeinfo.html', Context(treeinfo))