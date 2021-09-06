from django.contrib import admin
from .models import Test, Contact, Tag

# Register your models here.
# admin.site.register(Test)
# admin.site.register([Test, Contact, Tag])


class TagInline(admin.TabularInline):
    """
    内联(Inline)显示
    上面的 Contact 是 Tag 的外部键，所以有外部参考的关系。
    而在默认的页面显示中，将两者分离开来，无法体现出两者的从属关系。
    我们可以使用内联显示，让 Tag 附加在 Contact 的编辑页面上显示。
    """
    model = Tag


class ContactAdmin(admin.ModelAdmin):

    """
    # fields = ('name', 'email')

    # List
    我们也可以自定义该页面的显示，比如在列表中显示更多的栏目，
    只需要在 ContactAdmin 中增加 list_display 属性

    # search
    搜索功能在管理大量记录时非常有，我们可以使用 search_fields 为该列表页增加搜索栏

    # Inline
    内联(Inline)显示
    """
    list_display = ('name','age','email')  # List
    search_fields = ('name',)  # search
    inlines = [TagInline]  # Inline
    fieldsets = (
        ['Main', {
            'fields': ('name', 'email'),
        }],
        ['Advance', {
            'classes': ('collapse',),  # CSS样式，隐藏字段
            'fields': ('age',),
        }],
    )


admin.site.register(Contact, ContactAdmin)
admin.site.register([Test])
