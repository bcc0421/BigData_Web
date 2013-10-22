#coding:utf-8
import requests
import simplejson
import web
import conf

class ModifyUpdate:
    def POST(self):
        i=web.input()
        print i.email
        print i.password
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
        print "^^^^^^^^^^^^^^^"
        print res
        print res.text
