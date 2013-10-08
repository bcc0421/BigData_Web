import requests
import conf

class Thumbnail:
    def GET(self, id):
        res = requests.get(conf.locate('/attachments/thumbnail/%s' % id))
        return res.content

class SourceImage:
    def GET(self, id):
        res = requests.get(conf.locate('/attachments/source/%s' % id))
        return res.content
