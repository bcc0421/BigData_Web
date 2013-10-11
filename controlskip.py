#coding:utf-8
import threading
import time
import requests
import simplejson
import web

import conf

UPDATE_INTERVAL = 0.01
pins = [[], [], [], []]

render = web.template.render('templates/', base='base2')
pure_render = web.template.render('templates/')


def alive_count(lst):
    alive = map(lambda x: 1 if x.isAlive() else 0, lst)
    return reduce(lambda a, b: a + b, alive)


class PinRender(threading.Thread):
    def __init__(self, profile, i, p, present_user):
        super(PinRender, self).__init__()
        self.profile = profile
        self.i = i
        self.p = p
        self.present_user = present_user
        self.pin_obj = None

    def run(self):
        self.pin_obj = Pin(self.p, self.profile, self.present_user)
        if self.p['type'] == 'movie':
            self.i %= 4
            pins[self.i].append(self.pin_obj.render_video())
        elif self.p['type'] == 'picture':
            self.i %= 4
            pins[self.i].append(self.pin_obj.render())


class Pin:
    def __init__(self, data, user_profile, present_user):
        self.data = data
        self.user_profile = user_profile
        self.present_user = present_user

    def render(self):
        return pure_render.pin(self.data, self.user_profile, self.present_user)

    def render_video(self):
        return pure_render.pinvedio(self.data, self.user_profile, self.present_user)


class ControlSkip:
    def GET(self, id):
        board_list = ['education', 'remotworking', 'intelligence', 'beauty', 'emotion', 'health_management',
                      'entertainment', 'Domestic_counseling', 'shopping', 'career', 'community_services',
                      'public_information']
        board_id = int(id) - 1
        board_name = board_list[board_id]
        res = requests.get(conf.locate('/user/%s/profile' % web.cookies().get('key')))
        present_user = simplejson.loads(res.text)
        res = requests.get(conf.locate('/pin/list/%s' % id))
        json = simplejson.loads(res.text)
        global pins
        pins = [[], [], [], []]
        profile = {}
        pin_threads = []
        for i, p in enumerate(json['pins']):
            profile['user'] = p['author']
            pin_thread = PinRender(profile, i, p, present_user)
            pin_threads.append(pin_thread)

        for thread in pin_threads:
            thread.start()

        while alive_count(pin_threads) > 0:
            time.sleep(UPDATE_INTERVAL)

        return render.showboard(pins, present_user, board_name)


class SkipUserMessage:
    def GET(self):
        res = requests.get(conf.locate('/user/%s/profile' % web.cookies().get('key')))
        present_user = simplejson.loads(res.text)
        res = requests.get(conf.locate('/pin/user/%s' % web.cookies().get('key')))
        present_user_pin = simplejson.loads(res.text)
        pins = [[], [], [], []]
        for i, p in enumerate(present_user_pin['pins']):
            if p['type'] == 'movie':
                res = requests.get(conf.locate('/user/%s/profile' % p['author_id']))
                profile = simplejson.loads(res.text)
                i %= 4
                pin_obj = Pin(p, profile, present_user)
                pins[i].append(pin_obj.render_video())
            elif p['type'] == 'picture':
                res = requests.get(conf.locate('/user/%s/profile' % p['author_id']))
                profile = simplejson.loads(res.text)
                print profile
                i %= 4
                pin_obj = Pin(p, profile, present_user)
                pins[i].append(pin_obj.render())

        headers = {
            'X-Token': web.cookies().get('token')
        }

        res = requests.get(conf.locate('/following/%s' % web.cookies().get('key')), headers=headers)
        result = simplejson.loads(res.text)
        attentions = []
        for attention in result:
            attentions.append(str(pure_render.attention_list(attention)))
        return render.usermessage(pins, present_user, attentions)


class SkipMainPage:
    def GET(self):
        return web.seeother('/mainpage')















































