"""
Django Feedme

Mixins.py

Author: Derek Stegelman
"""
from __future__ import unicode_literals
import json

from django.http import HttpResponse


class AjaxableResponseMixin(object):
    """
    Mixin to add AJAX support to a form.
    Must be used with an object-based FormView (e.g. CreateView)
    """

    def render_to_json_response(self, context, **response_kwargs):
        """
        Render the output as JSON
        :param context:
        :param response_kwargs:
        :return:
        """
        data = json.dumps(context)
        response_kwargs['content_type'] = 'application/json'
        return HttpResponse(data, **response_kwargs)

    def form_invalid(self, form):
        """
        If the request is made via AJAX return as such.
        :param form:
        :return:
        """
        response = super(AjaxableResponseMixin, self).form_invalid(form)
        if self.request.is_ajax():
            return self.render_to_json_response(form.errors, status=400)
        else:
            return response

    def form_valid(self, form):
        """
        We make sure to call the parent's form_valid() method because
        it might do some processing (in the case of CreateView, it will
        call form.save() for example).
        """
        response = super(AjaxableResponseMixin, self).form_valid(form)
        if self.request.is_ajax():
            data = {
                'pk': self.object.pk,
            }
            return self.render_to_json_response(data)
        else:
            return response
