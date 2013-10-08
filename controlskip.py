
import requests
import simplejson
import web
import conf

render = web.template.render('templates/', base='base2')
pure_render = web.template.render('templates/')

class Pin:
    def __init__(self, data,userprofile, presentuser):
        self.data = data
        self.userprofile = userprofile
        self.presentuser = presentuser
        
        

    def render(self):
        return pure_render.pin(self.data,self.userprofile,self.presentuser)

    def rendervedio(self):
        return pure_render.pinvedio(self.data,self.userprofile,self.presentuser)


class ControlSkip:
    def GET(self,id):
        
        boardlist=['education','remotworking','intelligence','beauty','emotion','health_management','entertainment','Domestic_counseling','shopping','career','community_services','public_information']

        boardid=int(id)-1
        board_name=boardlist[boardid]

        res=requests.get(conf.locate('/user/%s/profile' % web.cookies().get('key')))
        presentuser=simplejson.loads(res.text)
        
        #username=json['user']['username']
 
        res = requests.get(conf.locate('/pin/list/%s' %id))
        json = simplejson.loads(res.text)
         
        pins = [[], [], [], []]

        for i, p in enumerate(json['pins']):

            if(p['type']=='movie'):

                res = requests.get(conf.locate('/user/%s/profile' % p['author_id']))
                profile = simplejson.loads(res.text)
                
                i = i % 4
                pin_obj = Pin(p,profile,presentuser)
               
                pins[i].append(pin_obj.rendervedio())
               
            elif(p['type']=='picture'):
                print p['author_id']
                res = requests.get(conf.locate('/user/%s/profile' % p['author_id']))
                profile = simplejson.loads(res.text)
                
                print profile
                i = i % 4
                pin_obj = Pin(p,profile,presentuser)
               
                pins[i].append(pin_obj.render())

        #return render.index(pins)
        return render.showboard(pins,presentuser,board_name)
class SkipUserMessage:
     def GET(self):
        res=requests.get(conf.locate('/user/%s/profile' % web.cookies().get('key')))
        presentuser=simplejson.loads(res.text)
       
        res=requests.get(conf.locate('/pin/user/%s' % web.cookies().get('key')))
        
        present_user_pin= simplejson.loads(res.text)
        pins = [[], [], [], []]

        for i, p in enumerate(present_user_pin['pins']):

            if(p['type']=='movie'):

                res = requests.get(conf.locate('/user/%s/profile' % p['author_id']))
                profile = simplejson.loads(res.text)
                
                i = i % 4
                pin_obj = Pin(p,profile,presentuser)
               
                pins[i].append(pin_obj.rendervedio())
               
            elif(p['type']=='picture'):
                print p['author_id']
                res = requests.get(conf.locate('/user/%s/profile' % p['author_id']))
                profile = simplejson.loads(res.text)
                
                print profile
                i = i % 4
                pin_obj = Pin(p,profile,presentuser)
               
                pins[i].append(pin_obj.render())
         
        headers={

            'X-Token':web.cookies().get('token')        
        }
     
        res=requests.get(conf.locate('/following/%s' % web.cookies().get('key')),headers=headers)

        re=simplejson.loads(res.text)

        attentions=[]

        for atten in re:
            
            attentions.append(str(pure_render.attention_list(atten)))

         
         #return simplejson.dumps({

            #    "attentions":attentions

             #   })
        #return render.index(pins)
        return render.usermessage(pins,presentuser,attentions)
    
class SkipMainPage:
    
        def GET(self):
             return web.seeother('/mainpage')















































