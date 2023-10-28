from django.http import *
from django.template import RequestContext, loader
from django.utils.translation import ugettext as _

def index(request):
    context = RequestContext(request, {
        'titlename': _('Task manager Hexlet'),
        'nameapp': _('Task manager'),
        'users': _('Users'),
        'enter': _('Enter'),
        'register': _('Registration'),
        'hello': _('Hello from Hexlet'),
        'subhello': _('Practical programming courses'),
        'learnmore': _('Learn more'),
    })
    template = loader.get_template('index.html')
    return HttpResponse(template.render(context))
 