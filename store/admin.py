from django.contrib import admin
from store.models import UserProfileInfo, Category, SubCategory, Product
from datetime import datetime
from django.utils.html import format_html


def change_public_day(modeladmin, request, queryset):
    queryset.update(public_day=datetime.now())


change_public_day.short_description = 'Change public_day to Today'


class ProductAdmin(admin.ModelAdmin):
    # Tắt hiển thị field add/update
    exclude = ('viewed',)

    # Hiển thị các field trong danh sách
    # list_display = ('image_product', 'name', 'price', 'public_day', 'viewed')
    list_display = ('e_image', 'e_name', 'e_price', 'e_public_day', 'e_viewed')

    # Lọc theo field
    list_filter = ('public_day',)

    # Tìm theo field
    search_fields = ('name',)

    actions = [change_public_day]

    @staticmethod
    def image_product(obj):
        return format_html('<img src="%s" style="width: 45px; height: 45px">' % obj.image.url)

    @admin.display(description='Hình sản phẩm')
    def e_image(self, obj):
        return format_html('<img src="%s" style="width: 45px; height: 45px">' % obj.image.url)

    @admin.display(description='Tên sản phẩm')
    def e_name(self, obj):
        return '%s' % obj.name

    @admin.display(description='Giá')
    def e_price(self, obj):
        return '%s' % '{:,}'.format(int(obj.price))

    @admin.display(description='Ngày xuất bản')
    def e_public_day(self, obj):
        return '%s' % obj.public_day

    @admin.display(description='Lượt xem')
    def e_viewed(self, obj):
        return '%s' % obj.viewed


# Register your models here.
admin.site.register(UserProfileInfo)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Product, ProductAdmin)


# Thay đổi tiêu đề Admin
admin.site.site_header = 'EStore Admin'




