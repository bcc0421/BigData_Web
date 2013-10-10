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


class ControlSkip:
    def GET(self, id):
        board_list = ['校外教育', '远程办公', '智慧之门', '美容美体', '情感天地',
                      '健康管理', '娱乐人生', '家政辅导', '购物天堂', '职业生涯',
                      '社区服务','公共信息']
        board_id = int(id) - 1
        board_name = board_list[board_id]
        res = requests.get(conf.locate('/user/%s/profile' % web.cookies().get('key')))
        present_user = simplejson.loads(res.text)
        res = requests.get(conf.locate('/pin/list/%s' % id))
        json = simplejson.loads(res.text)
        pins = [[], [], [], []]
        for i, p in enumerate(json['pins']):
            if p['type'] == 'movie':
                res = requests.get(conf.locate('/user/%s/profile' % p['author_id']))
                profile = simplejson.loads(res.text)
                i %= 4
                pin_obj = Pin(p, profile, present_user)
                pins[i].append(pin_obj.render_video())
            elif p['type'] == 'picture':
                res = requests.get(conf.locate('/user/%s/profile' % p['author_id']))
                if res.status_code == 200:
                    profile = simplejson.loads(str(res.text))
                    i %= 4
                    pin_obj = Pin(p, profile, present_user)
                    pins[i].append(pin_obj.render())
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
        attentions_len=len(attentions)
        
        return render.usermessage(pins, present_user, attentions,attentions_len)


class SkipMainPage:
    def GET(self):
        return web.seeother('/mainpage')















































