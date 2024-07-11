from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import TemplateView

from landing.forms import TemplateForm


class LandingView(TemplateView):
    template_name = 'landing/index.html'

    def post(self, request, *args, **kwargs):
        received_data: dict = request.POST.copy()  # Приняли данные в словарь

        # Заголовок HTTP_X_FORWARDED_FOR используется для идентификации исходного IP-адреса клиента,
        # который подключается к веб-серверу через HTTP-прокси или балансировщик нагрузки.
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]  # Получение IP
        else:
            ip = request.META.get('REMOTE_ADDR')  # Получение IP

        user_agent = request.META.get('HTTP_USER_AGENT')

        received_data["ip"] = ip
        received_data["user_agent"] = user_agent

        print(received_data)

        form = TemplateForm(received_data)
        if form.is_valid():
            return JsonResponse(data=form.cleaned_data,
                                json_dumps_params={"indent": 4,
                                                   "ensure_ascii": False})
        context = self.get_context_data(**kwargs)
        context["form"] = form
        return self.render_to_response(context)
