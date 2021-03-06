from django.contrib import admin

from .models import (
    Distribution,
    Individual,
    Training,
    Household,
)

admin.site.register(Training)


@admin.register(Individual)
class IndividualAdmin(admin.ModelAdmin):
    list_display = ('site', 'first_name',)
    display = 'Individual'


@admin.register(Distribution)
class DistributionAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'program',
        'create_date',
        'modified_date',
    )
    display = 'Program Dashboard'


@admin.register(Household)
class HouseholdAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', )
    search_fields = ('name',)
    list_filter = ('name', )
    display = 'Household'
