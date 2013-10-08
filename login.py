
import requests
import simplejson
import web
import conf

render = web.template.render('templates/', base='base')

class Login:
    def GET(self):
        if(web.cookies().get('email')):
            email=web.cookies().get('email')
            password=web.cookies().get('password')
            return render.login(email,password)
        else:
            email=''
            password=''
            return render.login(email,password)

    def POST(self):
        i = web.input()
        
        if hasattr(i,'remember') :
            if(i.remember=="keep"):
                web.setcookie('email', i.email, expires=3600*24*30)
                web.setcookie('password', i.password, expires=3600*24*30)
            
        # Get the data
        payload = {
            'email': i.email,
            'password': i.password
        }
        headers = {
            'Content-Type': 'application/json'
        }
        res = requests.post(conf.locate("/user/token"),
                            data=simplejson.dumps(payload),
                            headers=headers)

        resp = simplejson.loads(res.text)
        print resp['token']
        print resp['user']['key']
  
        # Process the cookie
        web.setcookie('token', resp['token'], expires=3600*24*30)
        web.setcookie('key',resp['user']['key'],expires=3600*24*30)
      
        return web.seeother('/mainpage')
