#coding:utf-8
import requests
import simplejson
import web
import conf

render = web.template.render('templates/', base='base2')
pure_render = web.template.render('templates/')


class Pin:
    def __init__(self, data, user_profile, present_user):
        self.data = data
        self.user_profile = user_profile
        self.present_user = present_user

    def render(self):
        return pure_render.pin(self.data, self.user_profile, self.present_user)

    def render_video(self):
        return pure_render.pinvedio(self.data, self.user_profile, self.present_user)


class ShowComment:
    def GET(self):
        i = web.input()
        res = requests.get(conf.locate('/comment/%s' % i.img_key_id))
        json = simplejson.loads(res.text)
        res = requests.get(conf.locate('/user/%s/profile' % web.cookies().get('key')))
        present_user = simplejson.loads(res.text)
        comments = []
        for c in (json['comments']):
            comments.append(str(pure_render.comment(c, present_user)))

        return simplejson.dumps({
            "comments": comments
        })


class MyPin:
    def GET(self):
        res = requests.get(conf.locate('/user/%s/profile' % web.cookies().get('key')))
        present_user = simplejson.loads(res.text)
        res = requests.get(conf.locate('/pin/user/%s' % web.cookies().get('key')))
        present_user_pin = simplejson.loads(res.text)
        pin = []
        for p in present_user_pin['pins']:
            if p['type'] == 'movie':
                res = requests.get(conf.locate('/user/%s/profile' % p['author_id']))
                profile = simplejson.loads(res.text)
                pin_obj = Pin(p, profile, present_user)
                pin.append(str(pin_obj.render_video()))
            elif p['type'] == 'picture':
                res = requests.get(conf.locate('/user/%s/profile' % p['author_id']))
                profile = simplejson.loads(res.text)
                pin_obj = Pin(p, profile, present_user)
                pin.append(str(pin_obj.render()))

        return simplejson.dumps({
            "pins": pin
        })

        



