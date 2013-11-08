#coding:utf-8
import requests
import simplejson
import web
import conf

render = web.template.render('templates/', base='base2')
pure_render = web.template.render('templates/')

class ModifyPassword:
        def POST(self):
            i=web.input()
            payload = {
                'email':i.email,
                'password':i.oldpwd,
                'new_password':i.newpwd
            }
            headers = {
                'X-Token': web.cookies().get('token'),
                'Content-Type': 'application/json'
            }
            res = requests.post(conf.locate("/user/password"),
                               data=simplejson.dumps(payload),
                               headers=headers)


class ModifyUserMessage:
        def GET(self,ownkey):
            res = requests.get(conf.locate('/user/%s/profile' % ownkey))
            present_user = simplejson.loads(res.text)
            return render.setaccount(present_user)
class MovePin:
        def GET(self,boardid):
            i=web.input()
            payload = {
                'board_id':boardid
            }
            headers = {
                'X-Token': web.cookies().get('token'),
                'Content-Type': 'application/json'
            }
            res = requests.put(conf.locate("/pin/%s/update" % i.img_key_id),
                               data=simplejson.dumps(payload),
                               headers=headers)
class EditPin:
    def GET(self,pinkey):
        pinkey=pinkey
        return render.editpin(pinkey)

class ModifyDescription:
    def POST(self):
        i=web.input()
        payload = {
            'introduction':i.description,
        }
        headers = {
            'X-Token': web.cookies().get('token'),
            'Content-Type': 'application/json'
        }
        res = requests.put(conf.locate("/pin/%s/update" % i.img_key_id),
                           data=simplejson.dumps(payload),
                           headers=headers)
