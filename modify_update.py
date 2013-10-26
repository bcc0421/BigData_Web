#coding:utf-8
import requests
import simplejson
import web
import conf


class ModifyUpdate:
    def POST(self):
        i = web.input()
        payload = {
            'password': i.password,
            'username': i.name
        }
        headers = {
            'X-Token': web.cookies().get('token'),
            'Content-Type': 'application/json'
        }
        res = requests.put(conf.locate("/user/%s/update" % web.cookies().get('key')),
                           data=simplejson.dumps(payload),
                           headers=headers)
class MovePin:
        def GET(self,boardid):
            i=web.input();
            print i.img_key_id
            print boardid
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