
from django.contrib import admin
from django.utils.html import format_html

from .models import ContactMessage


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):

    # Table columns
    list_display = (
        "name",
        "email",
        "subject",
        "message_preview",
        "created_at",
    )

    # Search functionality
    search_fields = (
        "name",
        "email",
        "subject",
        "message",
    )

    # Filters
    list_filter = (
        "created_at",
    )

    # Date navigation
    date_hierarchy = "created_at"

    # Default sorting
    ordering = ("-created_at",)

    # Pagination
    list_per_page = 15

    # Clickable fields
    list_display_links = (
        "name",
        "subject",
    )

    # Read-only timestamp
    readonly_fields = (
        "created_at",
    )

    # Form layout
    fieldsets = (
        ("Client Information", {
            "fields": (
                "name",
                "email",
                "subject",
            )
        }),

        ("Project Message", {
            "fields": (
                "message",
            )
        }),

        ("Submission Details", {
            "fields": (
                "created_at",
            )
        }),
    )

    save_on_top = True

    empty_value_display = "Not provided"

    def message_preview(self, obj):
        message = obj.message or ""

        if len(message) > 65:
            message = message[:65] + "..."

        return format_html(
            '<span title="{}">{}</span>',
            obj.message,
            message,
        )

    message_preview.short_description = "Message Preview"
