# _*_ encoding:utf-8 _*_
__author__ = 'Hayter'
__date__ = '2019/3/19 8:57'

import xadmin
from xadmin import views
import requests

from users.models import EmailVerifyRecord, Banner


class BaseSetting(object):
    enable_themes = False
    use_bootswatch = False


class GlobalSettings(object):
    site_footer = "Hayter"
    menu_style = "accordion"


class EmailVerifyRecordAdmin(object):
    list_display = ['code', 'email', 'send_type', 'send_time']
    search_fields = ['code', 'email', 'send_type']
    list_filter = ['code', 'email', 'send_type', 'send_time']


class BannerAdmin(object):
    list_display = ['title', 'image', 'url', 'index', 'add_time']
    search_fields = ['title', 'image', 'url', 'index']
    list_filter = ['title', 'image', 'url', 'index', 'add_time']


xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
xadmin.site.register(Banner, BannerAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)
