import conf
import requests
import web
import simplejson
import os
import sys
import locale

render=web.template.render('templates/' ,base='base2')

class UploadPin:
    
    def POST(self):
        i = web.input()
        print "1111111."
        print i.board_id
        boardlist=['education','remotworking','intelligence','beauty','emotion','health_management','entertainment','Domestic_counseling','shopping','career','community_services','public_information']

        board_id=boardlist.index(i.board_id)+1

  
        
        # buffer
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
        uuid=simplejson.loads(upload_res.text);
        uuid=uuid['id']
    
        payload = {
            'introduction': i.introduction
            
            
        }
        
        headers = {
            'X-Token': web.cookies().get('token'),
            'Content-Type': 'application/json'
        }
       
        res = requests.post(conf.locate('/pin/create/%s/%s' %(board_id,uuid)),
                            data=simplejson.dumps(payload),
                            headers=headers)
        
       
        
        return web.seeother('/controlskip/%s' % board_id)
       
class UploadComment:
    def POST(self):
        
        i=web.input()
       
        
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
        
            #f = None

            #if 'upload_vedio' in x:
              # f = x['upload_vedio'].value
  
            #files = {'file': f}
            #res = requests.post(conf.locate1('/file_upload/'),files=files)

            #indexid=res['file_name'].index('.')
            upload_res =None
            media = x.get('upload_video', None)        
            if media is not None:           
                if media.type == 'video/mp4' or media.type == 'video/x-flv':           
                    files = {'file': media.value}               
                    data = {'type': media.type}                
                    upload_res = requests.post(conf.locate1('/file_upload/'), files=files, data=data) 
                    upload_res=simplejson.loads(upload_res.text)

            print upload_res
            key=upload_res['file_name']
            boardlist = ['education', 'remotworking', 'intelligence', 'beauty', 'emotion', 'health_management',
                     'entertainment', 'Domestic_counseling', 'shopping', 'career', 'community_services',
                     'public_information']
                  
            board_id=boardlist.index(i.board_id)+1
           
            payload = {

            'introduction': i.introduction,
           
            'movie_id':key
    
                     }
        
            headers = {
                'X-Token': web.cookies().get('token'),
                'Content-Type': 'application/json'
             }
            
            res = requests.post(conf.locate('/pin/create/%s' % board_id),
                                data=simplejson.dumps(payload),
                                headers=headers)         


            return web.seeother('/controlskip/%s' % board_id)
        
        
           
          
            
            

                    

    






























