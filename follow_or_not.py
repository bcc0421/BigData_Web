#coding:utf-8
import requests
import simplejson
import web
import conf

pure_render = web.template.render("templates/")


class Follow:
    def GET(self):
        i = web.input()
        headers = {
            'X-Token': web.cookies().get('token')
        }
        res = requests.get(conf.locate('/fo/%s' % i.user_id), headers=headers)
        res = simplejson.loads(res.text)


class UnFollow:
    def GET(self):
        i = web.input()
        headers = {
            'X-Token': web.cookies().get('token')
        }
        r = requests.get(conf.locate('/unfo/%s' % i.user_id), headers=headers)




class CheckFollow:
    def GET(self):
        i = web.input()
        headers = {
            'X-Token': web.cookies().get('token')
        }
        res = requests.get(conf.locate('/following/%s' % web.cookies().get('key')), headers=headers)
        result = simplejson.loads(res.text)
        if len(result):
            for attention in result:

                if attention['key'] == i.user_id:
                    return simplejson.dumps({
                        "attentions": 'followd'
                    })

            return simplejson.dumps({
                "attentions": 'unfollowd'
            })
        else:
            return simplejson.dumps({
                "attentions": 'unfollowd'
            })



