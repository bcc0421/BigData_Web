#coding:utf-8
import requests
import web
import simplejson

import conf


render = web.template.render('templates/', base='base2')


class UploadPin:
    def POST(self):
        i = web.input()
        
        board_list = [u'校外教育', u'远程办公', u'智慧之门', u'美容美体', u'情感天地',
                      u'健康管理', u'娱乐人生', u'家政辅导', u'购物天堂', u'职业生涯',
                      u'社区服务',u'公共信息']
        print "****************************88"
        print i.board_id
        board_id = board_list.index(i.board_id) + 1
        x = web.input(upload_pic={})
        f = None
        if 'upload_pic' in x:
            f = x['upload_pic'].value
            # upload a file
        headers2 = {
            'X-Token': web.cookies().get('token')
        }
        upload_res = requests.post(conf.locate('/attachments/upload'),
                                   data=f,
                                   headers=headers2)
        uuid = simplejson.loads(upload_res.text)
        uuid = uuid['id']
        payload = {
            'introduction': i.introduction
        }
        headers = {
            'X-Token': web.cookies().get('token'),
            'Content-Type': 'application/json'
        }
        res = requests.post(conf.locate('/pin/create/%s/%s' % (board_id, uuid)),
                            data=simplejson.dumps(payload),
                            headers=headers)

        return web.seeother('/controlskip/%s' % board_id)


class UploadComment:
    def POST(self):
        i = web.input()
        payload = {
            'content': i.content,
        }
        headers = {
            'X-Token': web.cookies().get('token'),
            'Content-Type': 'application/json'
        }
        res = requests.post(conf.locate('/comment/%s/create' % i.img_key_id),
                            data=simplejson.dumps(payload),
                            headers=headers)


class UploadVideo:
    def POST(self):
        i = web.input()
        x = web.input(upload_video={})
        upload_res = None
        media = x.get('upload_video', None)
        if media is not None:
            if media.type == 'video/mp4' or media.type == 'video/x-flv':
                files = {'file': media.value}
                data = {'type': media.type}
                upload_res = requests.post(conf.media_server('/file_upload/'), files=files, data=data)
                upload_res = simplejson.loads(upload_res.text)

        key = upload_res['file_name']
        board_list = [u'校外教育', u'远程办公', u'智慧之门', u'美容美体', u'情感天地',
                      u'健康管理', u'娱乐人生', u'家政辅导', u'购物天堂', u'职业生涯',
                      u'社区服务',u'公共信息']
        board_id = board_list.index(i.board_id) + 1
        payload = {
            'introduction': i.introduction,
            'movie_id': key
        }
        headers = {
            'X-Token': web.cookies().get('token'),
            'Content-Type': 'application/json'
        }
        res = requests.post(conf.locate('/pin/create/%s' % board_id),
                            data=simplejson.dumps(payload),
                            headers=headers)

        return web.seeother('/controlskip/%s' % board_id)
        
        
           
          
            
            

                    

    






























