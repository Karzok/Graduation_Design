# _*_ encoding:utf-8 _*_
__author__ = 'Hayter'
__date__ = '2019/4/10 19:56'

from django.conf.urls import url, include

from users.views import UserInfoView, UploadImageView, UpdatePwdView, SendEmailCodeView
from users.views import UpdateEmailView, MyCourseView, MyFavOrgView, MyFavTeacherView, MyFavCourseView, MyMessageView

urlpatterns =[
    # 用户信息
    url(r'^info/$', UserInfoView.as_view(), name="user_info"),

    # 用户头像上传
    url(r'^image/upload/$', UploadImageView.as_view(), name="image_upload"),

    # 用户个人中心修改密码
    url(r'^update/pwd/$', UpdatePwdView.as_view(), name="update_pwd"),

    # 个人中心发送邮箱验证码
    url(r'^sendemail_code/$', SendEmailCodeView.as_view(), name="sendemail_code"),

    # 修改邮箱
    url(r'^update_email/$', UpdateEmailView.as_view(), name="update_email"),

    # 访问我的课程
    url(r'^mycourse/$', MyCourseView.as_view(), name="mycourse"),

    # 用户收藏的机构
    url(r'^myfav/org/$', MyFavOrgView.as_view(), name="myfav_org"),

    # 用户收藏的讲师
    url(r'^myfav/teacher/$', MyFavTeacherView.as_view(), name="myfav_teacher"),

    # 用户收藏的课程
    url(r'^myfav/course/$', MyFavCourseView.as_view(), name="myfav_course"),

    # 用户消息
    url(r'^my_message/$', MyMessageView.as_view(), name="my_message"),
]