#coding: utf-8

from django.shortcuts import render_to_response
from django.template import RequestContext

try:
    from functools import wraps
except ImportError: 
    def wraps(wrapped, assigned=('__module__', '__name__', '__doc__'),
              updated=('__dict__',)):
        def inner(wrapper):
            for attr in assigned:
                setattr(wrapper, attr, getattr(wrapped, attr))
            for attr in updated:
                getattr(wrapper, attr).update(getattr(wrapped, attr, {}))
            return wrapper
        return inner


def render_to(template=None, mobile_template=None, mimetype="text/html"):
	"""
	This is a modified version of the decorator with the same name that can be found on django-annoying 

	When is_mobile is True the template used to rendered is:
	M_TEMPLATE in returned dictionary, mobile_template decorator_parameter 
	or TEMPLATE if there arent any mobile templates

	"""
	def renderer(function):
		@wraps(function)
		def wrapper(request, *args, **kwargs):
			output = function(request, *args, **kwargs)
			if not isinstance(output, dict):
				return output

			tmpl = output.pop('TEMPLATE', template)
			m_tmpl = output.pop('M_TEMPLATE', mobile_template)

			if request.is_mobile and m_tmpl:
				tmpl = m_tmpl			

			return render_to_response(tmpl, output, \
                        context_instance=RequestContext(request), mimetype=mimetype)
		return wrapper
	return renderer