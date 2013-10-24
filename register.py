#coding:utf-8
import requests
import simplejson
import web
import conf

render = web.template.render('templates/', base='base2')


class Register:
    def POST(self):
        input = web.input()
        # Get the data
        payload = {
            'email': input.email,
            'password': input.register_pwd,
            'birthday': '',
            'username': input.register_username,
            'gender': '',
            'introduction': ''
        }
        headers = {
            'Content-Type': 'application/json'
        }
        results = requests.post(conf.locate("/user/create"),
                            data=simplejson.dumps(payload),
                            headers=headers)
        result = simplejson.loads(results.text)
        if result.has_key('validation_code'):
            return web.seeother('/check/code/%s' % result['validation_code'])


class CheckEmail:
    def GET(self):
        input = web.input()
        results = requests.get(conf.locate("/user/check_email/%s" % input.email))
        result = simplejson.loads(results.text)
        return simplejson.dumps({
            "status": result['status']
        })


class CheckName:
    def GET(self):
        input = web.input()
        results = requests.get(conf.locate("/user/check_username/%s" % input.name))
        result = simplejson.loads(results.text)
        return simplejson.dumps({
            "status": result['status']
        })















