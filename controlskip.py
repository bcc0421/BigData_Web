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
    def render_myself(self):
        return pure_render.myselfpin(self.data, self.user_profile, self.present_user)
    def render_video(self):
        return pure_render.pinvedio(self.data, self.user_profile, self.present_user)
    def render_myself_video(self):
        return pure_render.myselfvediopin(self.data, self.user_profile, self.present_user)
    def render_other_user(self):
        return pure_render.otheruserpin(self.data, self.user_profile, self.present_user)
    def render_other_user_video(self):
        return pure_render.otheruservideo(self.data, self.user_profile, self.present_user)

class ControlSkip:
    def GET(self, id):
        board_list = ['校外教育', '远程办公', '智慧之门', '美容美体', '情感天地',
                      '健康管理', '娱乐人生', '家政辅导', '购物天堂', '职业生涯',
                      '社区服务', '公共信息']
        board_id = int(id) - 1

        board_name = board_list[board_id]
        res = requests.get(conf.locate('/user/%s/profile' % web.cookies().get('key')))
        present_user = simplejson.loads(res.text)
        res = requests.get(conf.locate('/pin/list/%s' % id))
        json = simplejson.loads(res.text)
        pins_length=len(json['pins'])
        last_pin_key=json['pins'][pins_length-1]['key']
        pins = [[], [], [], []]
        for i, p in enumerate(json['pins']):
            if p['type'] == 'movie':
                res = requests.get(conf.locate('/user/%s/profile' % p['author_id']))
                profile = simplejson.loads(res.text)
                p['thumbnail'] = p['movie_id'].split('.')[0] + '.jpg'
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
        return render.showboard(pins, present_user, board_name, id, last_pin_key, pins_length)


class SkipUserMessage:
    def GET(self):
        res = requests.get(conf.locate('/user/%s/profile' % web.cookies().get('key')))
        present_user = simplejson.loads(res.text)
        res = requests.get(conf.locate('/pin/user/%s' % web.cookies().get('key')))
        present_user_pin = simplejson.loads(res.text)
        pins_length=len(present_user_pin['pins'])
        last_pin_key=present_user_pin['pins'][pins_length-1]['key']
        pins = [[], [], [], []]
        for i, p in enumerate(present_user_pin['pins']):
            if p['type'] == 'movie':
                res = requests.get(conf.locate('/user/%s/profile' % p['author_id']))
                profile = simplejson.loads(res.text)
                p['thumbnail'] = p['movie_id'].split('.')[0] + '.jpg'
                i %= 4
                pin_obj = Pin(p, profile, present_user)
                pins[i].append(pin_obj.render_myself_video())
            elif p['type'] == 'picture':
                board_list = [u'校外教育', u'远程办公', u'智慧之门', u'美容美体', u'情感天地',
                              u'健康管理', u'娱乐人生', u'家政辅导', u'购物天堂', u'职业生涯',
                              u'社区服务', u'公共信息']
                board_id = str(p['board_id'])
                board_id = int(board_id) - 1
                board_name = board_list[board_id]
                p['bord_name'] = board_name
                res = requests.get(conf.locate('/user/%s/profile' % p['author_id']))
                profile = simplejson.loads(res.text)
                i %= 4
                pin_obj = Pin(p, profile, present_user)
                pins[i].append(pin_obj.render_myself())

        headers = {
            'X-Token': web.cookies().get('token')
        }
        res = requests.get(conf.locate('/following/%s' % web.cookies().get('key')), headers=headers)
        result = simplejson.loads(res.text)
        attentions = []
        for attention in result:
            attentions.append(str(pure_render.attention_list(attention)))
        attentions_len = len(attentions)
        res = requests.get(conf.locate('/follower/%s' % web.cookies().get('key')), headers=headers)
        result = simplejson.loads(res.text)
        followds = []
        for followd in result:
            followds.append(str(pure_render.followed_list(followd)))
        followds_len = len(followds)
        return render.usermessage(pins, present_user, attentions, attentions_len, followds, followds_len,pins_length,last_pin_key,web.cookies().get('key'))


class SkipOwnMessage:
    def GET(self, ownkey):
        res = requests.get(conf.locate('/user/%s/profile' % ownkey))
        present_user = simplejson.loads(res.text)
        res = requests.get(conf.locate('/pin/user/%s' % ownkey))
        present_user_pin = simplejson.loads(res.text)
        pins_length=len(present_user_pin['pins'])
        last_pin_key=present_user_pin['pins'][pins_length-1]['key']
        pins = [[], [], [], []]
        for i, p in enumerate(present_user_pin['pins']):
            if p['type'] == 'movie':
                res = requests.get(conf.locate('/user/%s/profile' % p['author_id']))
                profile = simplejson.loads(res.text)
                p['thumbnail'] = p['movie_id'].split('.')[0] + '.jpg'
                i %= 4
                pin_obj = Pin(p, profile, present_user)
                pins[i].append(pin_obj.render_other_user_video())
            elif p['type'] == 'picture':
                board_list = [u'校外教育', u'远程办公', u'智慧之门', u'美容美体', u'情感天地',
                              u'健康管理', u'娱乐人生', u'家政辅导', u'购物天堂', u'职业生涯',
                              u'社区服务', u'公共信息']
                board_id = str(p['board_id'])
                board_id = int(board_id) - 1
                board_name = board_list[board_id]
                p['bord_name'] = board_name
                res = requests.get(conf.locate('/user/%s/profile' % p['author_id']))
                profile = simplejson.loads(res.text)
                i %= 4
                pin_obj = Pin(p, profile, present_user)
                pins[i].append(pin_obj.render_other_user())

        headers = {
            'X-Token': web.cookies().get('token')
        }
        res = requests.get(conf.locate('/following/%s' % ownkey), headers=headers)
        result = simplejson.loads(res.text)
        attentions = []
        for attention in result:
            attentions.append(str(pure_render.attention_list(attention)))
        attentions_len = len(attentions)
        res = requests.get(conf.locate('/follower/%s' % ownkey), headers=headers)
        result = simplejson.loads(res.text)
        followds = []
        for followd in result:
            followds.append(str(pure_render.followed_list(followd)))
        followds_len = len(followds)
        return render.usermessage(pins, present_user, attentions, attentions_len, followds, followds_len,pins_length,last_pin_key,web.cookies().get('key'))

class SkipMainPage:
    def GET(self):
        return web.seeother('/mainpage')


class LoginOut:
    def GET(self):
        web.setcookie('token', '', expires=-1)
        return web.seeother('/login')


class LoginIn:
    def GET(self):
        return web.seeother('/login')


class SearchContent:
    def POST(self):
        res = requests.get(conf.locate('/user/%s/profile' % web.cookies().get('key')))
        present_user = simplejson.loads(res.text)
        i = web.input()
        payload = {
            'keyword': i.content_search
        }
        headers = {
            'X-Token': web.cookies().get('token'),
            'Content-Type': 'application/json'
        }
        res = requests.post(conf.locate('/pin/search/'),
                            data=simplejson.dumps(payload),
                            headers=headers)
        r = simplejson.loads(res.text)
        pins_length=len(r['pins'])
        last_pin_key=r['pins'][pins_length-1]['key']
        if len(r['pins']):
            pins = [[], [], [], []]
            for i, p in enumerate(r['pins']):
                if p['type'] == 'movie':
                    res = requests.get(conf.locate('/user/%s/profile' % p['author_id']))
                    profile = simplejson.loads(res.text)
                    p['thumbnail'] = p['movie_id'].split('.')[0] + '.jpg'
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
            return render.searchshowboard(pins, present_user,pins_length,last_pin_key)
        else:
            return render.searchnothing()

class SkipMainPage:
    def GET(self):
        return web.seeother('/mainpage')


class SkipBigImg:
    def GET(self, imgkey):
        return render.showbigimg(imgkey)
class PinFlowMyself:
    def GET(self):
        i = web.input()
        res = requests.get(conf.locate('/pin/user/%s?%s' % (i.pin_author_key,i.last_pin_key)))
        present_user_pin = simplejson.loads(res.text)
        for p in present_user_pin['pins']:
            if p['type'] == 'movie':
                p['thumbnail'] = p['movie_id'].split('.')[0] + '.jpg'
        return simplejson.dumps({
            'pins': present_user_pin['pins']
        })

class PinFlow:
    def GET(self, id):
        i = web.input()
        board_list = ['校外教育', '远程办公', '智慧之门', '美容美体', '情感天地',
                      '健康管理', '娱乐人生', '家政辅导', '购物天堂', '职业生涯',
                      '社区服务', '公共信息']
        board_id = int(id) - 1
        res = requests.get(conf.locate('/pin/list/%s?%s' % (id, i.last_pin_key)))
        json = simplejson.loads(res.text)
        for p in json['pins']:
            if p['type'] == 'movie':
                p['thumbnail'] = p['movie_id'].split('.')[0] + '.jpg'
        return simplejson.dumps({
            'pins': json['pins']
        })
class PinSearchFlow:
    def GET(self):
        i=web.input()
        res = requests.get(conf.locate('/pin/search?%s' % (i.last_pin_key)))
        json = simplejson.loads(res.text)
        for p in json['pins']:
            if p['type'] == 'movie':
                p['thumbnail'] = p['movie_id'].split('.')[0] + '.jpg'
        return simplejson.dumps({
            'pins': json['pins']
        })
class ShowPinDetail:
    def GET(self, pinkey):
        res = requests.get(conf.locate('/pin/%s' % pinkey))
        pin_profile = simplejson.loads(res.text)
        res = requests.get(conf.locate('/user/%s/profile' % pin_profile['pin']['author_id']))
        author_profile = simplejson.loads(res.text)
        res = requests.get(conf.locate('/user/%s/profile' % web.cookies().get('key')))
        present_user = simplejson.loads(res.text)
        headers = {
            'X-Token': web.cookies().get('token')
        }
        res = requests.get(conf.locate('/comment/%s' % pin_profile['pin']['key']))
        json = simplejson.loads(res.text)
        comments = []
        for c in (json['comments']):
            comments.append(str(pure_render.comment(c, present_user)))
        res = requests.get(conf.locate('/following/%s' % web.cookies().get('key')), headers=headers)
        result = simplejson.loads(res.text)
        if len(result):
            for attention in result:
                if attention['key'] == pin_profile['pin']['author_id']:
                    pin_profile['status'] = "followd"
                    if pin_profile['pin']['type'] == 'picture':
                        return render.pindetail(pin_profile, author_profile, present_user, comments)
                    else:
                        pin_profile['pin']['thumbnail'] = pin_profile['pin']['movie_id'].split('.')[0] + '.jpg'
                        return render.vediodetail(pin_profile, author_profile, present_user, comments)
            pin_profile['status'] = "unfollowd"
            if pin_profile['pin']['type'] == 'picture':
                return render.pindetail(pin_profile, author_profile, present_user, comments)
            else:
                pin_profile['pin']['thumbnail'] = pin_profile['pin']['movie_id'].split('.')[0] + '.jpg'
                return render.vediodetail(pin_profile, author_profile, present_user, comments)
        else:
            pin_profile['status'] = "unfollowd"
            if pin_profile['pin']['type'] == 'picture':
                return render.pindetail(pin_profile, author_profile, present_user, comments)
            else:
                pin_profile['pin']['thumbnail'] = pin_profile['pin']['movie_id'].split('.')[0] + '.jpg'
                return render.vediodetail(pin_profile, author_profile, present_user, comments)





