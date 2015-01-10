from django.contrib import admin

# Register your models here.
from .models import Person

import reversion


class PersonAdmin(reversion.VersionAdmin):

    class Meta:
        model = Person


admin.site.register(Person, PersonAdmin)
