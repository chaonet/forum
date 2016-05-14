from django.contrib import admin

from models import Comment

class CommentAdmin(admin.ModelAdmin):
	list_display = ("block", "article", "owner", 
					"content", "status", "to_comment_id", 
					"create_timestamp", "last_update_timestamp"
				   )
	list_filter = ("block",)
	search_fields = ["content",]

admin.site.register(Comment, CommentAdmin)
