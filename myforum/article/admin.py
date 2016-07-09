# coding: utf-8

from django.contrib import admin

from models import Article
from comment.models import Comment

class CommentInline(admin.TabularInline):
    model = Comment
    can_delete = False
    raw_id_fields = ("owner",)
    readonly_fields = ("block", "to_comment_id", "owner", "content", "status")

    # 作用同 can_delete = False
    # def has_delete_permission(self, request, obj=None):
    #     return False

    def has_add_permission(self, request):
        return False

class ArticleAdmin(admin.ModelAdmin):
    list_display = ("block", "owner", "title", "content", "status","create_timestamp","last_update_timestamp")
    search_fields = ["title","content"]
    list_filter = ("block", )
    actions = ['make_published']
    inlines = [
        CommentInline,
    ]

    def make_published(self, request, queryset):
        rows_updated = queryset.update(status=1)
        if rows_updated == 1:
            message_bit = u"1 条"
        else:
            message_bit = u"%s 条" % rows_updated
        self.message_user(request, u"%s 成功设置为精华" % message_bit)
    make_published.short_description = u"设置精华"

admin.site.register(Article, ArticleAdmin)