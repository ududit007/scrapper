from django.contrib import admin

from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'email', 'is_active'
    )
    list_display_links = ('name',)
    exclude = ('groups', 'user_permissions', 'last_login')

    def save_model(self, request, obj, form, change):
        """Override save method of django admin.

        :param request: request object
        :param obj: model instance
        :param form: model form object
        :param change: boolean, is True if the object is being changed,
                        and False if it's being added.
        :return:
        """
        password = form.cleaned_data.get('password', 'mindfire')
        obj.set_password(password)
        obj.save()
