from django.contrib import admin
from .models import Department, News_volume_issue, Posts, Category, Sub_category,Submission
from django.contrib.auth.admin import UserAdmin

# Register your models here.

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['deptName','deptCode']
    search_fields = ['deptCode','deptName']

@admin.register(News_volume_issue)
class AdminRegister(admin.ModelAdmin):
    list_display = ['volume','issue','month_year','deptId']
    list_filter = ['month_year']

@admin.register(Posts)
class VolumePosts(admin.ModelAdmin):
    list_display = [x.name for x in Posts._meta.fields]
    list_filter = ['categoryID']
    fields = ['categoryID','subcategoryID','postTitle','slug','postDetails','postingDate','postURL','postImage','lastUpdatedBy','volumeID','isActive']
    prepopulated_fields={'slug':('postTitle',), }

    def get_queryset(self, request):
        abc = super(VolumePosts, self).get_queryset(request)
        operator = request.user.id
        return abc.filter(postedBy=operator)

    def save_model(self, request, obj, form, change):
        if not obj.postedBy:
            obj.postedBy = request.user
        obj.save()

@admin.register(Category)
class PostCategory(admin.ModelAdmin):
    list_display =[ 'id','categoryName']

@admin.register(Sub_category)
class SubCategory(admin.ModelAdmin):
    list_display = ['subCategory']

admin.site.register(Submission)