from django.contrib import admin
from .models import QuestionType, QuestionBank

# Register your models here.
admin.site.register(QuestionType)
admin.site.register(QuestionBank)
# admin.site.register(Options)

