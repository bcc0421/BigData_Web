import web
from index import ShowComment, MyPin, Index
from login import Login
from controlskip import ControlSkip, SkipUserMessage, SkipMainPage, LoginOut, LoginIn, SearchContent, SkipOwnMessage, SkipBigImg,PinFlow,ShowPinDetail,PinFlowMyself ,PinSearchFlow
from register import Register,CheckEmail,CheckName
from images import Thumbnail, SourceImage
from upload import UploadPin, UploadComment, UploadVideo,PortraitUpload
from mainpage import Mainpage
from follow_or_not import Follow, UnFollow, CheckFollow
from delete import DeleteOwnPin
from checkcode import CheckCode
from modify_update import ModifyUserMessage, MovePin, ModifyPassword,EditPin ,ModifyDescription

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
    '/modify/usermessage/(.*)','ModifyUserMessage',
    '/skip/bigimg/(.*)','SkipBigImg',
    '/move/pin/(\d+)','MovePin',
    '/pin_flow/(\d+)','PinFlow',
    '/portrait/upload','PortraitUpload',
    '/showpin/detail/(.*)','ShowPinDetail',
    '/modify/password','ModifyPassword',
    '/edit/pin/(.*)','EditPin',
    '/modify/description','ModifyDescription',
    '/pin_flow/myself','PinFlowMyself',
    '/pin_flow/search','PinSearchFlow',
    '/login_out','LoginOut'
)

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()


