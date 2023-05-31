from django.contrib import admin
#CustomUserをインポート
from .models import CustomUser

class CustomUserAdmin(admin.ModelAdmin):

    #レコード一覧に
    list_display = ('id', 'username')
    #表示するカラムにリンクを設定
    list_display_links = ('id', 'username')

#Django管理サイトに
admin.site.register(CustomUser, CustomUserAdmin)