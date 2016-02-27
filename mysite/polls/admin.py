from django.contrib import admin

from .models import Question

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'field': ['question_text']})
        ('Date information', {'field': ['pub_date']})
        ]
    
admin.site.register(Question, QuestionAdmin)
