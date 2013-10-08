
import web
import conf
import simplejson
import requests


render=web.template.render('templates/',base='base')
class Mainpage:
    def GET(self):

        
        res=requests.get(conf.locate('/user/%s/profile' % web.cookies().get('key')))
        json=simplejson.loads(res.text)
        username=json['user']['username']
        

        return render.mainpage(username)





