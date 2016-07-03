from django.contrib import admin

from models import UserMessage

class UserMessageAdmin(admin.ModelAdmin):
	list_display = ("owner", "content", "link", "status", 
					"create_timestamp", "last_update_timestamp"
				   )
	list_filter = ("status",)
	search_fields = ["content",]

admin.site.register(UserMessage, UserMessageAdmin)
