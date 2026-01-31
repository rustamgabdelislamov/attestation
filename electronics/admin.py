from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse
from electronics.models import Organization, Contact, Product


class OrganizationAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "contact",
        "hierarchy_level",
        "debt_to_supplier",
        "supplier_link",
        "id",
    )  # Поле иерархического уровня вычисляем динамически
    list_filter = ("contact__city",)  # фильтр по городу
    actions = ["clear_debts"]  # Admin action для очистки долгов

    def clear_debts(self, request, queryset):
        for obj in queryset:
            obj.debt_to_supplier = 0
            obj.save()

    clear_debts.short_description = "Очистить задолженность"

    def hierarchy_level(self, obj):
        level = 0
        current_obj = obj
        while current_obj.supplier is not None:
            current_obj = current_obj.supplier
            level += 1
        return level

    hierarchy_level.short_description = "Уровень иерархии"

    def supplier_link(self, obj):
        if obj.supplier:
            return format_html(
                '<a href="{}">{}</a>',
                reverse(
                    "admin:electronics_organization_change", args=[obj.supplier.id]
                ),
                obj.supplier.name,
            )
        return "-"

    supplier_link.short_description = "Поставщик"
    supplier_link.allow_tags = True


class ContactAdmin(admin.ModelAdmin):
    list_display = ("email", "id")


admin.site.register(Organization, OrganizationAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Product)
