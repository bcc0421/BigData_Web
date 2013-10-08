import requests
import simplejson
import web
import conf

render = web.template.render('templates/', base='base2')
pure_render = web.template.render('templates/')

class Pin:
    def __init__(self, data, userprofile,presentuser):
        self.data = data
        self.userprofile = userprofile
        self.presentuser = presentuser

    def render(self):
        return pure_render.pin(self.data,self.userprofile, self.presentuser)
    def rendervedio(self):
        return pure_render.pinvedio(self.data,self.userprofile,self.presentuser)


class PinFlow:
    def GET(self, id):
        res = requests.get(conf.locate('/pin/list?%s' % id))
        json = simplejson.loads(res.text)
        
        pin = []
        for p in json['pins']:
            
            res = requests.get(conf.locate('/user/%s/profile' % p['author_id']))
            profile = simplejson.loads(res.text)
            
            pin_obj = Pin(p,profile)
            pin.append(str(pin_obj.render()))

        return simplejson.dumps({
                    "pins": pin
                })




class ShowComment:

    def GET(self):
        
        i=web.input()
        
        res=requests.get(conf.locate('/comment/%s' % i.img_key_id))
        
        json=simplejson.loads(res.text)
        
        res = requests.get(conf.locate('/user/%s/profile' % web.cookies().get('key')))
        presentuser=simplejson.loads(res.text)
        comments=[]
        
        for c in (json['comments']):
            
            comments.append(str(pure_render.comment(c,presentuser)))


        return simplejson.dumps({
                    "comments": comments
                })    




class MyPin:
    def GET(self):
        res=requests.get(conf.locate('/user/%s/profile' % web.cookies().get('key')))
        presentuser=simplejson.loads(res.text)
       
        res=requests.get(conf.locate('/pin/user/%s' % web.cookies().get('key')))
        
        present_user_pin= simplejson.loads(res.text)
     
        print present_user_pin
      
        pin=[]
        for p in present_user_pin['pins']:
            if(p['type']=='movie'):
    
                res = requests.get(conf.locate('/user/%s/profile' % p['author_id']))
                profile = simplejson.loads(res.text)
                
                pin_obj = Pin(p,profile,presentuser)
                pin.append(str(pin_obj.rendervedio()))
            elif(p['type']=='picture'):
                print p['author_id']
                res = requests.get(conf.locate('/user/%s/profile' % p['author_id']))
                profile = simplejson.loads(res.text)
                
                pin_obj = Pin(p,profile,presentuser)
                pin.append(str(pin_obj.render()))
           
        return simplejson.dumps({
                    "pins": pin
                })

        



