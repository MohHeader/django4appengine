from django.conf import settings
from django.http import HttpResponse
import os

def robots(request):
	if request.META['HTTP_HOST'] in settings.STAGING_SERVER_URLS:
		return HttpResponse("""User-agent: *\nDisallow: /""", content_type="text/plain")
	else:
		file_path = os.path.join( os.path.dirname(__file__), "robots.txt")
		file_object = open(file_path, "r")
		return HttpResponse(file_object.read(), content_type="text/plain")