from django.contrib import admin

from django_admin_listfilter_dropdown.filters import DropdownFilter, RelatedDropdownFilter

from .models import fee, concession_type, fees_type, class_fees, fees_source

admin.site.register(concession_type)
admin.site.register(fees_type)
admin.site.register(class_fees)

@admin.register(fee)
class feeAdmin(admin.ModelAdmin):
    list_display = ('Gr_num','fee_code', 'fee_dues' , 'paid_source' , 'class_name', 'paid' , 'gardian_code', 'due_date' , 'paid_date')
    #list_filter = ('gender', 'classes')
    list_filter = (
        # for ordinary fields
        # ('class_name', DropdownFilter),
        ('class_name', RelatedDropdownFilter),
        ('paid', DropdownFilter),
        # for related fields
        )
    search_fields = ('Gr_num', 'paid')



admin.site.register(fees_source)