from django.contrib import admin

# Register your models here.

from myquora.models import (Answer, AnswerAdmin, Author, AuthorAdmin, Comment,
                            CommentAdmin, Question, QuestionAdmin, FeedbackAdmin ,Feedback)



admin.site.register(Author, AuthorAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Feedback, FeedbackAdmin)