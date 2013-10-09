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
        if res.has_key('id'):
            return simplejson.dumps({
                "relationship_id": res['id']
            })
        elif res.has_key('status'):
            return simplejson.dumps({
                "relationship_id": res['status']
            })


class UnFollow:
    def GET(self):
        i = web.input()
        headers = {
            'X-Token': web.cookies().get('token')
        }
        requests.get(conf.locate('/unfo/%s' % i.user_id), headers=headers)


class GetMyAttention:
    def GET(self):
        headers = {
            'X-Token': web.cookies().get('token')
        }
        res = requests.get(conf.locate('/following/%s' % web.cookies().get('key')), headers=headers)
        re = simplejson.loads(res.text)
        attentions = []
        for attention in re:
            attentions.append(str(pure_render.attention_list(attention)))
        return simplejson.dumps({
            "attentions": attentions
        })
            
        




