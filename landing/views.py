from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import TemplateView

from landing.forms import TemplateForm, ContactForm


class LandingView(TemplateView):
    template_name = 'landing/index.html'

    def post(self, request, *args, **kwargs):
        received_data = request.POST.copy()

        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]  # Получение IP
        else:
            ip = request.META.get('REMOTE_ADDR')  # Получение IP
        user_agent = request.META.get('HTTP_USER_AGENT')
        received_data["ip"] = ip
        received_data["user_agent"] = user_agent

        if "main_button" in request.POST:
            form = TemplateForm(received_data)
            if form.is_valid():
                return JsonResponse(data=form.cleaned_data,
                                    json_dumps_params={"indent": 4,
                                                       "ensure_ascii": False})
            context = self.get_context_data(**kwargs)
            context["form"] = form
            return self.render_to_response(context)

        elif "contact_button" in request.POST:
            form = ContactForm(received_data)
            if form.is_valid():
                return JsonResponse(data=form.cleaned_data,
                                    json_dumps_params={"indent": 4,
                                                       "ensure_ascii": False})
            context = self.get_context_data(**kwargs)
            context["contact_form"] = form
            return self.render_to_response(context)
        else:
            raise ValueError("Ошибка определения имени кнопки при вызове представления LandingView")
