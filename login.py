#coding:utf-8
import requests
import simplejson
import web
import conf
render = web.template.render('templates/', base='base')
class Login:
    def GET(self):
        if (web.cookies().get('email')):
            email = web.cookies().get('email')
            password = web.cookies().get('password')
            return render.login(email, password)
        else:
            email = ''
            password = ''
            return render.login(email, password)

    def POST(self):
        i = web.input()
        if hasattr(i, 'remember'):
            if (i.remember == "keep"):
                web.setcookie('email', i.email, expires=3600 * 24 * 30)
                web.setcookie('password', i.password, expires=3600 * 24 * 30)
            # Get the data
        payload = {
            'email': i.email,
            'password': i.password
        }
        headers = {
            'Content-Type': 'application/json'
        }
        res = requests.post(
            conf.locate("/user/token"),
            data=simplejson.dumps(payload),
            headers=headers
        )
        response = simplejson.loads(res.text)
        # Process the cookie
        if response.has_key('error'):
            return simplejson.dumps({
                "status": 'error'
            })
        else:
            web.setcookie('token', response['token'], expires=3600 * 24 * 30)
            web.setcookie('key', response['user']['key'], expires=3600 * 24 * 30)
            return simplejson.dumps({
                "status": 'ok'
            })