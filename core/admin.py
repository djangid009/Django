from django.contrib import admin

from .models import Blog, Rank, Question, Answer, Comment

admin.site.register(Answer)
admin.site.register(Blog)
# admin.site.register(Question_cat)
admin.site.register(Comment)
admin.site.register(Rank)
admin.site.register(Question)
