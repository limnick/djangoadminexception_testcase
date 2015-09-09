from .models import BookModel
from django.contrib import admin


@admin.register(BookModel)
class BookAdmin(admin.ModelAdmin):
    readonly_fields = ('error_field_example',)

    list_display = ('author', 'title', 'subject',)
    fields = ('author', 'title', 'subject', 'error_field_example',)

    def error_field_example(self, obj):
        raise IndexError
        return obj.author
