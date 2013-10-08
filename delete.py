import conf
import requests
import web
import simplejson
import os
import sys
import locale

class DeleteOwnPin:
    def POST(self):
        i=web.input()
        pinid=i.pin_id
        
        r = requests.delete(conf.locate('/pin/%s/delete' %pinid))
    
        
