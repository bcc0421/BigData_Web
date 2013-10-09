import requests
import web

import conf


class DeleteOwnPin:
    def POST(self):
        i = web.input()
        pin_id = i.pin_id
        r = requests.delete(conf.locate('/pin/%s/delete' % pin_id))
    
        
