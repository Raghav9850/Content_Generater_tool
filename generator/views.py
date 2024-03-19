# from django.shortcuts import render

# # Create your views here.
# # generator/views.py

# from django.shortcuts import render, redirect
# from django.http import HttpResponse
# from .forms import InputForm
# from .models import GeneratedContent
# import google.generativeai as genai
# from .utils import *
# # Function to generate content using Google Generative AI

# def generate_content(user_input):
#     genai.configure(api_key="AIzaSyCOHUOnBiq5EQZCj1Xwamy42BfAgGcfHss")
#     model = genai.GenerativeModel('gemini-pro')
#     response = model.generate_content(user_input)

#     if hasattr(response, 'candidates') and response.candidates:
#         # Extracting text from the response
#         generated_text = response.candidates[0].content.parts[0].text
#         return generated_text
#     else:
#         return "Failed to generate content"

# def input_form_view(request):
#     if request.method == 'POST':
#         form = InputForm(request.POST)
#         if form.is_valid():
#             user_input = form.cleaned_data['user_input']
#             generated_content = generate_content(f"provide contant on{user_input}")
#             GeneratedContent.objects.create(user_input=user_input, generated_content=generated_content)
#             return redirect('content_display')
#     else:
#         form = InputForm()
#     return render(request, 'input_form.html', {'form': form})

# def content_display_view(request):
#     latest_generated_content = GeneratedContent.objects.latest('id')
#     return render(request, 'content_display.html', {'content': latest_generated_content})

# def download_pdf_view(request):
#     latest_generated_content = GeneratedContent.objects.latest('id')
#     pdf_content = generate_content_pdf(latest_generated_content.generated_content)
#     response = HttpResponse(pdf_content, content_type='application/pdf')
#     response['Content-Disposition'] = 'attachment; filename="generated_content.pdf"'
#     return response

# def download_txt_view(request):
#     latest_generated_content = GeneratedContent.objects.latest('id')
#     txt_content = generate_content_txt(latest_generated_content.generated_content)
#     response = HttpResponse(txt_content, content_type='text/plain')
#     response['Content-Disposition'] = 'attachment; filename="generated_content.txt"'
#     return response

from django.shortcuts import render

# Create your views here.
# generator/views.py

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import InputForm
import google.generativeai as genai
from .utils import *
# Function to generate content using Google Generative AI
global_generated_content = None
def generate_content(user_input):
    genai.configure(api_key="AIzaSyCOHUOnBiq5EQZCj1Xwamy42BfAgGcfHss")
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(user_input)

    if hasattr(response, 'candidates') and response.candidates:
        # Extracting text from the response
        generated_text = response.candidates[0].content.parts[0].text
        return generated_text
    else:
        return "Failed to generate content"

def input_form_view(request):
    global global_generated_content
    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            user_input = form.cleaned_data['user_input']
            generated_content = generate_content(user_input)
            global_generated_content = generated_content 
            return redirect('content_display')
    else:
        form = InputForm()
    return render(request, 'input_form.html', {'form': form})

def content_display_view(request):
    global global_generated_content
    return render(request, 'content_display.html', {'content': global_generated_content})

def download_pdf_view(request):
    global global_generated_content
    pdf_content = generate_content_pdf(global_generated_content)
    response = HttpResponse(pdf_content, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="generated_content.pdf"'
    return response

def download_txt_view(request):
    global global_generated_content
    txt_content = generate_content_txt(global_generated_content)
    response = HttpResponse(txt_content, content_type='text/plain')
    response['Content-Disposition'] = 'attachment; filename="generated_content.txt"'
    return response
