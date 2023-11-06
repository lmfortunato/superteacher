from django.shortcuts import render

def index(request):
    http_response = render(
        request = request,
        template_name = "index.html",
    )

    return http_response

# def sign_up(request):
#     http_response = render(
#         request = request,
#         template_name = "sign-up.html"
#     )