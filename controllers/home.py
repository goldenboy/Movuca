#!/usr/bin/python
# -*- coding: utf-8 -*-

# from gluon.tools import Auth
# auth = Auth(DAL(None))

if session.auth and session.auth.user:
    time_expire = 0
else:
    time_expire = 300


#@auth.requires_login()
#@cache(request.env.path_info, time_expire=time_expire, cache_model=cache.ram)
def index():
    from handlers.home import Home
    home = Home(['featured', 'ads'])
    home.context.left_sidebar_enabled = True
    home.context.right_sidebar_enabled = True
    home.context.header_enabled = True
    return home.render("app/home")


def base():
    from handlers.base import Base
    base = Base()
    base.context.teste = "TESTEEEE"
    return base.render("app/base")


def search():
    q = request.vars.q
    kind = request.vars.kind
    if kind == "user":
        redirect(CURL("person", "search", vars={"q": q}))
    elif kind == "article":
        redirect(CURL("article", "search", vars={"q": q}))
    return "search"
