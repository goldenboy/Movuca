#!/usr/bin/python
# -*- coding: utf-8 -*-

from handlers.person import Person


def usertimeline():
    person = Person('usertimeline')
    return person.render("app/person/usertimeline")


def publictimeline():
    person = Person('publictimeline')
    return person.render("app/person/publictimeline")


def privatetimeline():
    person = Person('privatetimeline')
    return person.render("app/person/privatetimeline")


def followers():
    person = Person()
    person.followers(request.args(0))
    return person.render()


def following():
    person = Person()
    person.following(request.args(0))
    return person.render()


def contacts():
    person = Person()
    person.contacts(request.args(0))
    person.context.left_sidebar_enabled = True
    return person.render('app/person/contacts')


def search():
    person = Person()
    person.context.left_sidebar_enabled = True
    person.search(request.vars.get('q'))
    return person.render('app/person/search')


def follow():
    person = Person()
    return person.follow()


def unfollow():
    person = Person()
    return person.unfollow()


def show():
    person = Person()
    person.show(request.args(0) or session.auth.user.id)
    return person.render('app/person/show')


def board():
    person = Person()
    person.board(request.args(0) or session.auth.user.id)
    return person.render('app/person/board')


def account():
    person = Person("account")
    return person.render('app/person/account')


def facebook():
    person = Person("facebook")
    return person.render()


def user():
    redirect(CURL('person', 'facebook', args=request.args, vars=request.vars))


def loginbare():
    person = Person("loginbare")
    return person.render('app/person/loginbare')


def messages():
    return 'This page is under construction, feel free to contribute <-- go back and click on GitHub link'


def check_availability():
    person = Person()
    items = dict(field=request.args(0),
                  value=request.args(1))
    error = person.check_availability(items)
    if error:
        items['error'] = error[items['field']]
        items['img'] = str(IMG(_title=items['error'], _class="%(field)s_availability_img" % items, _src=URL('static', person.context.theme_name, args=['images', 'icons', 'notright.24.png'])))
        return "jQuery('.%(field)s_availability_img').hide();jQuery('#auth_user_%(field)s').css({'border': '1px solid red'});jQuery('#auth_user_%(field)s').parent().append('%(img)s');" % items
    else:
        items['img'] = str(IMG(_title=T("Available"), _class="%(field)s_availability_img" % items, _src=URL('static', person.context.theme_name, args=['images', 'icons', 'right.24.png'])))
        return "jQuery('.%(field)s_availability_img').hide();jQuery('#auth_user_%(field)s').css({'border': '1px solid green'});jQuery('#auth_user_%(field)s').parent().append('%(img)s');" % items
