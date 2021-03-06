#coding: utf-8

from django.conf import settings
import re

class MobileMiddleware(object):

	def is_mobile_useragent(self,request):

		if request.META.has_key('HTTP_USER_AGENT'):
			user_agent = request.META['HTTP_USER_AGENT']

			pattern = "(up.browser|up.link|mmp|symbian|smartphone|midp|wap|phone|windows ce|pda|mobile|mini|palm|netfront)"

			if hasattr(settings, 'MOBILE_PATTERN'):
				pattern = settings.MOBILE_PATTERN

			prog = re.compile(pattern, re.IGNORECASE)
			match = prog.search(user_agent)
			return match

		return False

	def process_request(self, request):

		domain = request.META.get('HTTP_HOST', '').split('.')

		if 'm' in domain or 'mobile' in domain:
			request.is_mobile = True

		elif self.is_mobile_useragent(request):
			request.is_mobile = True
		else:
			request.is_mobile = False

		if request.is_mobile:
			pass
			#settings.TEMPLATE_DIRS = settings.MOBILE_TEMPLATE_DIRS
		else:
			pass
			#settings.TEMPLATE_DIRS = settings.DESKTOP_TEMPLATE_DIRS
			
		return None