#coding:utf-8
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
        print resp
        if resp.has_key('validation_code'):
            print resp['validation_code']
            r = requests.get(conf.locate("/user/validate/%s" %resp['validation_code']))
            re = simplejson.loads(r.text)
            print re
            return render.checkemail()   
        
           
        
        
        #return render.checkemail(validate_code)
       
        #return web.seeother('/login')
class CheckEmail:
    def GET(self):
        i = web.input() 
        print i.email
        r = requests.get(conf.locate("/user/check_email/%s" % i.email))
        re = simplejson.loads(r.text)
        return simplejson.dumps({
                "status": re['status']
            })

















