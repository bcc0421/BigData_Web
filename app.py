import web
from index import ShowComment, MyPin, Index
from login import Login
from controlskip import ControlSkip, SkipUserMessage, SkipMainPage,LoginOut
from register import Register
from images import Thumbnail, SourceImage
from upload import UploadPin, UploadComment, UploadVideo
from mainpage import Mainpage
from follow_or_not import Follow, UnFollow, GetMyAttention
from delete import DeleteOwnPin

urls = (
    '/', 'Index',
    '/login', 'Login',
    '/register', 'Register',
    '/mainpage','Mainpage',
    '/controlskip/(\d+)','ControlSkip',
    '/thumbnail/(.+)', 'Thumbnail',
    '/source_img/(.+)', 'SourceImage',
    '/skipusermessage','SkipUserMessage',
    '/pin/upload', 'UploadPin',
    '/comment/upload','UploadComment',
    '/comment/show','ShowComment',
    '/ownpin/show','MyPin',
    '/follow/oneuser','Follow',
    '/unfollow/oneuser','UnFollow',
    '/myattention/person','GetMyAttention',
    '/video/upload','UploadVideo',
    '/delete/ownpin','DeleteOwnPin',
    '/skipmainpage','SkipMainPage',
    '/login_out','LoginOut'
)

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()


