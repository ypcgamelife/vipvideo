#
# '''
#  http://jx.598110.com/?url=
#  http://jx.598110.com/v/6.php?url=
#  http://jx.598110.com/v/2.php?url=
#  http://jx.598110.com/v/3.php?url=
#  http://jx.598110.com/v/1.php?url=
#  http://jx.598110.com/v/5.php?url=
#  http://jx.598110.com/v/4.php?url=
#  https://jx.618g.com/?url=   https://jqaaa.com/jx.php?url=   https://jiexi.071811.cc/jx2.php?url=
#  https://ejiafarm.com/dy/jiexi.php?url=  https://beaacc.com/api.php?url=   https://api.fastflv.cc/jiexi/?url=
#  http://yun.baiyug.cn/vip/index.php?url=
#
#  var url_adress = (GetQueryString("url"));
#
#   var height_g = ($(window).height());
#
#   if (url_adress.indexOf("qq.com") > 0) {
#
#      play('v/6.php?url=');
#
#  }else if(url_adress.indexOf("iqiyi.com")>=0) {
#
#    play('v/2.php?url=');
#     }else if(url_adress.indexOf("tudou.com")>=0) {
#
#    play('v/3.php?url=');
#
#     }else if(url_adress.indexOf("pptv.com")>=0) {
#
#    play('v/3.php?url=');
#
#    }else if(url_adress.indexOf("youku.com") > 0){
#
#       play('v/1.php?url=');
#    }else if(url_adress.indexOf("mgtv.com") > 0){
#
#       play('v/2.php?url=');
#
#    }else if(url_adress.indexOf("le.com") > 0){
#
#       play('v/2.php?url=');
#
# 	 }else if(url_adress.indexOf("fun.tv") > 0){
#
#       play('v/5.php?url=');
#
#    }else if(url_adress.indexOf("sohu.com") > 0){
#
#       play('v/3.php?url=');
#
#     }
# else
# {
#         play('v/4.php?url=');
#
#   }
#
#
# '''
#encoding=utf-8
import tkinter
import tkinter.messagebox
import webbrowser

def Button():
    vip=['http://jx.598110.com/v/1.php?url=',
         'http://jx.598110.com/v/2.php?url=',
         'http://jx.598110.com/v/3.php?url=',
         'http://jx.598110.com/v/4.php?url=',
         'http://jx.598110.com/v/5.php?url=',
         'http://jx.598110.com/v/6.php?url=',
         'http://jx.598110.com/?url=',
         'https://jx.618g.com/?url=',
         'https://jqaaa.com/jx.php?url=',
         'https://jiexi.071811.cc/jx2.php?url=',
         'https://beaacc.com/api.php?url=',
         'https://api.fastflv.cc/jiexi/?url='
         ]
    td= varRadio.get()
    if td not in range(0,12):
        td=0
    #print(td)
    #a = 'http://www.a305.org/flv.php?url=' if varRadio.get() else 'http://www.82190555.com/video.php?url='
    a=vip[td]
    #print(a)
    b = entry_movie_link.get()
    webbrowser.open(a+b)
def qk():
    entry_movie_link.delete(0,'end')


def about():
    abc='''
    经过测试爱奇艺、优酷、腾讯、土豆、PPTV、芒果、乐视、搜狐等VIP视频可以播放
    链接格式为
    https://www.iqiyi.com/v_19rrdgdwpg.html
    如果不行，请换一个通道看看。如果都不行，就表示解析不行了。
    '''
    tkinter.messagebox.showinfo(title='帮助文件', message=abc)
def zzxx():
    msg='''
    Python学习
    '''
    tkinter.messagebox.showinfo(title='联系方式', message=msg)
if __name__ == '__main__':
    root=tkinter.Tk()
    root.title('VIP视频解析软件')
    root['width']=550
    root['height']=350

    menubar = tkinter.Menu(root)
    helpmenu = tkinter.Menu(menubar, tearoff=0)
    helpmenu.add_command(label='帮助', command=about)
    helpmenu.add_command(label='信息', command=zzxx)
    menubar.add_cascade(label='帮助(H)', menu=helpmenu)
    root.config(menu=menubar)

    varentry1= tkinter.StringVar(value='')
    lab_movie_gallery=tkinter.Label(root, text='选择视频播放通道')
    lab_movie_gallery.place(x=20,y=20,width=100,height=20)
    varRadio=tkinter.IntVar(value=5)

    Radiobutton1_movie_gallery = tkinter.Radiobutton(root, variable=varRadio, value=0, text='视频通道01')
    Radiobutton2_movie_gallery = tkinter.Radiobutton(root, variable=varRadio, value=1, text='视频通道02')
    Radiobutton3_movie_gallery = tkinter.Radiobutton(root, variable=varRadio, value=2, text='视频通道03')
    Radiobutton4_movie_gallery = tkinter.Radiobutton(root, variable=varRadio, value=3, text='视频通道04')
    Radiobutton5_movie_gallery = tkinter.Radiobutton(root, variable=varRadio, value=4, text='视频通道05')
    Radiobutton6_movie_gallery = tkinter.Radiobutton(root, variable=varRadio, value=5, text='视频通道06')
    Radiobutton7_movie_gallery = tkinter.Radiobutton(root, variable=varRadio, value=6, text='视频通道07')
    Radiobutton8_movie_gallery = tkinter.Radiobutton(root, variable=varRadio, value=7, text='视频通道08')
    Radiobutton9_movie_gallery = tkinter.Radiobutton(root, variable=varRadio, value=8, text='视频通道09')
    Radiobutton10_movie_gallery = tkinter.Radiobutton(root, variable=varRadio, value=9, text='视频通道10')
    Radiobutton11_movie_gallery = tkinter.Radiobutton(root, variable=varRadio, value=10, text='视频通道11')
    Radiobutton12_movie_gallery = tkinter.Radiobutton(root, variable=varRadio, value=11, text='视频通道12')
    # Radiobutton13_movie_gallery = tkinter.Radiobutton(root, variable=varRadio, value=12, text='视频通道13')
    # Radiobutton14_movie_gallery = tkinter.Radiobutton(root, variable=varRadio, value=13, text='视频通道14')

    Radiobutton1_movie_gallery.place(x=130,y=20,width=100,height=20)
    Radiobutton2_movie_gallery.place(x=250, y=20, width=100, height=20)
    Radiobutton3_movie_gallery.place(x=370, y=20, width=100, height=20)
    Radiobutton4_movie_gallery.place(x=130,y=50,width=100,height=20)
    Radiobutton5_movie_gallery.place(x=250, y=50, width=100, height=20)
    Radiobutton6_movie_gallery.place(x=370, y=50, width=100, height=20)
    Radiobutton7_movie_gallery.place(x=130,y=80,width=100,height=20)
    Radiobutton8_movie_gallery.place(x=250, y=80, width=100, height=20)
    Radiobutton9_movie_gallery.place(x=370, y=80, width=100, height=20)
    Radiobutton10_movie_gallery.place(x=130,y=110,width=100,height=20)
    Radiobutton11_movie_gallery.place(x=250, y=110, width=100, height=20)
    Radiobutton12_movie_gallery.place(x=370, y=110, width=100, height=20)
    # Radiobutton13_movie_gallery.place(x=130,y=140,width=100,height=20)
    # Radiobutton14_movie_gallery.place(x=250, y=140, width=100, height=20)

    varentry2=tkinter.StringVar(value='https://www.iqiyi.com/v_19rrdgdwpg.html')
    lab_movie_link = tkinter.Label(root, text='视频播放链接')
    lab_movie_link.place(x=20, y=180, width=100, height=20)
    entry_movie_link = tkinter.Entry(root, textvariable=varentry2)
    entry_movie_link.place(x=130, y=180, width=300, height=20)
    button_movie_link=tkinter.Button(root,text='清空',command=qk)
    button_movie_link.place(x=440,y=180,width=30,height=20)
    lab_remind = tkinter.Label(root, text='将视频链接复制到框内，点击播放VIP视频，将打开默认浏览器打开视频')
    lab_remind.place(x=50, y=210, width=400, height=20)
    varbutton=tkinter.StringVar
    button_movie= tkinter.Button(root, text='播放VIP视频', command=Button)
    button_movie.place(x=140, y=240, width=200, height=60)

    root.mainloop()
