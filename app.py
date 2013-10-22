import web
from index import ShowComment, MyPin
from login import Login
from controlskip import ControlSkip, SkipUserMessage, SkipMainPage,LoginOut, LoginIn,SearchContent,SkipOwnMessage
from register import Register,CheckEmail,CheckName
from images import Thumbnail, SourceImage
from upload import UploadPin, UploadComment, UploadVideo
from mainpage import Mainpage
from follow_or_not import Follow, UnFollow, GetMyAttention,CheckFollow
from delete import DeleteOwnPin
from checkcode import CheckCode
from modify_update import ModifyUpdate

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
    '/loginin','LoginIn',
    '/check/email','CheckEmail',
    '/check/name','CheckName', 
    '/check/code/(.*)','CheckCode',
    '/check/follow','CheckFollow',  
    '/search/content','SearchContent',
    '/skip/ownmessage/(.*)','SkipOwnMessage',
    '/modify/message','ModifyUpdate',
    '/login_out','LoginOut'
    
)

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()


