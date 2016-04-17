from django.contrib import admin

# Register your models here.

from models import Block

class BlockAdmin(admin.ModelAdmin):
	list_display = ("block_name", "block_desc", "block_admin", "create_timestamp", "last_update_timestamp")
	list_filter = ("block_admin", )

admin.site.register(Block, BlockAdmin)
