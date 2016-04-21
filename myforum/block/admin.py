from django.contrib import admin

# Register your models here.

from models import Block

class BlockAdmin(admin.ModelAdmin):
	list_display = ("name", "desc", "admin", "create_timestamp", "last_update_timestamp")
	list_filter = ("admin", )

admin.site.register(Block, BlockAdmin)
