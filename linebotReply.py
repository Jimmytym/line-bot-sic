from flask import Flask
app = Flask(__name__)

from flask import request, abort
from linebot import  LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage,ImageSendMessage,PostbackEvent, LocationSendMessage,TextSendMessage, TemplateSendMessage, ConfirmTemplate, MessageTemplateAction, ButtonsTemplate, PostbackTemplateAction, URITemplateAction, CarouselTemplate, CarouselColumn, ImageCarouselTemplate, ImageCarouselColumn
from urllib.parse import parse_qsl

line_bot_api = LineBotApi('p9lo/8/m92FzXCG+0l90Te27I6YdaEqe7fWgDK4gJtPtiX4HiZ1qj8MGiUa4nTMGLORCEWPAZv4DJaZyRHUFc1soEAjBc7ZhSd5e8NvbkDinPNNx7Ym1YPx16/vjgS/PFFMySlA92Bxl0CditjQElwdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('dae127d3c8e36ea6188b581efd6393e1')
# line_bot_api.push_message('U9c23a5d47eb633a60cc8d14e677b74f4', TextSendMessage(text='歡迎加入台體運資傳BOT，點選下方選單來獲取想了解的資訊喔'))
@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    mtext = event.message.text
    if mtext == '加入社群':
        sendButton(event)

    if mtext == '未來就業':
        sendWork(event)
    
    if mtext == '就業方向':
        sendWork2(event)
   
    if mtext == '學長姐就業分佈比例':
        try:
            message = ImageSendMessage(
                original_content_url = "https://drive.google.com/file/d/1TKi1LjMAlzKxLQqQtBaRz02pLdbgN-jz/view?usp=sharing",
                preview_image_url = "https://drive.google.com/file/d/1TKi1LjMAlzKxLQqQtBaRz02pLdbgN-jz/view?usp=sharing"
            )
            line_bot_api.reply_message(event.reply_token,message)
        except:
            line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))
    
    if mtext == '傳媒業':
        try:
            message = TextSendMessage(  
                text = "在傳媒業方面，可以選擇從事主播、記者、新聞編輯或企劃等等，也可以選擇像是影音剪輯或影視相關工作"
            )
            line_bot_api.reply_message(event.reply_token,message)
        except:
            line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))
    if mtext == '資訊業':
        try:
            message = TextSendMessage(  
                text = "在資訊業方面，可以選擇從事製作網頁、軟體工程師、數據分析師或是職業運動情蒐團隊等資訊相關工作"
            )
            line_bot_api.reply_message(event.reply_token,message)
        except:
            line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))
    if mtext == '洽詢管道':
        try:
            message = [  #串列
                
                TextSendMessage(  #傳送文字
                    text = "如果有其他的問題，歡迎洽詢以下管道喔"
                ),
                
                  TextSendMessage(  #傳送文字
                    text = "運傳系系辦電話：（04）22213108*6131"
                ),
                
                  TextSendMessage(  #傳送文字
                    text = "運傳系官網網址：https://sic.ntus.edu.tw/"
                ),
                  LocationSendMessage(
                title='台灣體育運動大學',
                address='台中市北區雙十路一段16號',
                latitude=24.1490451,  #緯度
                longitude=120.6852107  #經度
            )
                  
            ]
            line_bot_api.reply_message(event.reply_token,message)
        except:
            line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

def sendButton(event):
    try:
        message = TemplateSendMessage(
            alt_text='加入社群',
            template=ButtonsTemplate(
                title='想了解我們的最新消息與活動嗎?歡迎追蹤與加入',  #主標題
                text='以下是我們的官方社群帳號：',  #副標題
                actions=[
                    URITemplateAction(  #開啟網頁
                        label='運傳系系辦臉書社團',
                        uri='https://www.facebook.com/groups/440958489250085'
                    ),
                    URITemplateAction(  #開啟網頁
                        label='運傳系學會粉絲團',
                        uri='https://www.facebook.com/ntus.sic'
                    ),
                    URITemplateAction(  #開啟網頁
                        label='運傳系系學會IG',
                        uri='https://www.instagram.com/ntus.sic/'
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

def sendWork(event):
    try:
        message = TemplateSendMessage(
            alt_text='未來就業',
            template=ConfirmTemplate(
                # title='想了解我們系上什麼樣的就業內容呢？',
                text='想了解我們系上什麼樣的就業內容呢？',
                actions=[
                    MessageTemplateAction(  #按鈕選項
                        label='就業方向',
                        text='就業方向'
                    ),
                    MessageTemplateAction(
                        label='學長姐就業分佈比例',
                        text='學長姐就業分佈比例'
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))
        
def sendWork2(event):
    try:
        message = TemplateSendMessage(
            alt_text='就業方向',
            template=ConfirmTemplate(
                # title='我們系上未來可從事的領域有媒體業、影視業或是資訊業',
                text='想了解哪一項領域可從事的工作嗎？',
                actions=[
                    MessageTemplateAction( 
                        label='傳媒業',
                        text='傳媒業'
                    ),
                    # MessageTemplateAction( 
                    #     label='影視業',
                    #     text='影視業'
                    # ),
                    MessageTemplateAction( 
                        label='資訊業',
                        text='資訊業'
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))
        



# def sendCarousel(event):  #轉盤樣板
#     try:
#         message = TemplateSendMessage(
#             alt_text='轉盤樣板',
#             template=CarouselTemplate(
#                 columns=[
#                     CarouselColumn(
#                         thumbnail_image_url='https://i.imgur.com/4QfKuz1.png',
#                         title='這是樣板一',
#                         text='第一個轉盤樣板',
#                         actions=[
#                             MessageTemplateAction(
#                                 label='文字訊息一',
#                                 text='賣披薩'
#                             ),
#                             URITemplateAction(
#                                 label='連結文淵閣網頁',
#                                 uri='http://www.e-happy.com.tw'
#                             ),
#                             PostbackTemplateAction(
#                                 label='回傳訊息一',
#                                 data='action=sell&item=披薩'
#                             ),
#                         ]
#                     ),
#                     CarouselColumn(
#                         thumbnail_image_url='https://i.imgur.com/qaAdBkR.png',
#                         title='這是樣板二',
#                         text='第二個轉盤樣板',
#                         actions=[
#                             MessageTemplateAction(
#                                 label='文字訊息二',
#                                 text='賣飲料'
#                             ),
#                             URITemplateAction(
#                                 label='連結台大網頁',
#                                 uri='http://www.ntu.edu.tw'
#                             ),
#                             PostbackTemplateAction(
#                                 label='回傳訊息二',
#                                 data='action=sell&item=飲料'
#                             ),
#                         ]
#                     )
#                 ]
#             )
#         )
#         line_bot_api.reply_message(event.reply_token,message)
#     except:
#         line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))



if __name__ == '__main__':
    app.run()
