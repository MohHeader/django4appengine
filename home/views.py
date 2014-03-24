from django.shortcuts  import render_to_response
from django.template import RequestContext

from libs.password_required.decorators import password_required

@password_required
def index(request):
    template_context = {'request':request}
    return render_to_response('home.html', template_context,
        RequestContext(request))