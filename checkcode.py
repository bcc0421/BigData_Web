#coding:utf-8
import requests
import simplejson
import web
import conf

render = web.template.render('templates/', base='base2')

class CheckCode:
    def GET(self,code):
        
        r = requests.get(conf.locate("/user/validate/%s" % code))
        re = simplejson.loads(r.text)
        if re['status']=='successfully validated.':
            return render.checkemail_success()  
        else:
            return render.checkemail_fail()
