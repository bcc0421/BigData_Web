
import requests
import simplejson
import web
import conf

render = web.template.render('templates/', base='base2')

class Register:
    def POST(self):
        i = web.input()
        
        # Get the data
        payload = {
            'email': i.email,
            'password': i.register_pwd,
            'birthday': '',
            'username': i.register_username,
            'gender': '',
            'introduction': ''
        }
        headers = {
            'Content-Type': 'application/json'
        }
        
        res = requests.post(conf.locate("/user/create"),
                            data=simplejson.dumps(payload),
                            headers=headers)
        
        resp = simplejson.loads(res.text)
        
        
      
      
        return web.seeother('/login')
