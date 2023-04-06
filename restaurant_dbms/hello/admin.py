from django.contrib import admin
from hello.models import Customer,Staff,Menu,Payment,Offers,Orders,Serves

# Register your models here.
admin.site.register(Customer)
admin.site.register(Staff)
admin.site.register(Menu)
admin.site.register(Payment)
admin.site.register(Offers)
admin.site.register(Orders)
admin.site.register(Serves)
admin.site.site_header = "Restaurant Admin"
admin.site.index_title = "BRUNCH Database"