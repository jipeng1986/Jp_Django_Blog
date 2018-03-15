from django.conf.urls import url
from . import views
from django.conf import settings
from django.contrib.auth import views as auth_views

urlpatterns = [
    # -- 系统内置模板 --
    # 登录
    url(r'^new-login/$', auth_views.login, {"template_name": "account/login.html"}, name='user_login'),
    # 退出
    url(r'^logout/$', auth_views.logout, {"template_name": "account/logout.html"}, name='user_logout'),
    # 忘记密码
    url(r'^password-change/$', auth_views.password_change,
        {"post_change_redirect": "/account/password-change-done"}, name='password_change'),
    url(r'^password-change-done/$', auth_views.password_change_done, name='password_change_done'),
    # 重置密码
    url(r'^password-reset/$', auth_views.password_reset,
        {"template_name": "account/password_reset_form.html",
         "email_template_name": "account/password_reset_email.html",
         "subject_template_name": "account/password_reset_subject.txt",
         "post_reset_redirect": "/account/password-reset-done"}, name='password_reset'),
    url(r'^password-reset-done/$', auth_views.password_reset_done,
        {"template_name": "account/password_reset_done.html"}, name='password_reset_done'),
    url(r'^password-reset-confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/$', auth_views.password_reset_confirm,
        {"template_name": "account/password_reset_confirm.html",
         "post_reset_redirect": "/account/password-reset-complete"}, name='password_reset_confirm'),
    url(r'^password-reset-complete/$', auth_views.password_reset_complete,
        {"template_name": "account/password_reset_complete.html"}, name='password_reset_complete'),

    # -- 自定义模板 --
    # 注册
    # url(r'^login/$', views.user_login, name='user_login'),
    url(r'^register/$', views.register, name="user_register"),
]
