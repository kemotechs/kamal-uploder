import time
import random
import requests
import telepot

from telepot.loop import MessageLoop

sh = ["هههههههههههههههههههههههههههههههههههههه","كسمك يلا","احا","كسمك يطيز يهبل","خ ـؤد يڪسم ـڪ فينڪ ڪدآ ♡","ڪسم ـڪ يڪلب","رد يعلق","زبي","يكسمك مص","زبي اهو ياض","كسمك ياض","كسمك وكسم الكسم","رد","رد بس يت فينك","احا","عبرني يعرص","كسمك رد","كسمين امك رد","زبي زبي","في طيزك يعرص","كسم كدا","نا زهقت","احا","كسمك يبز","كسمك يطيز يهبل","ڪسم ـڪ يڪلب","ههكسكك","كسمك","كسك وردي","ايوا وري كسسمك","كسسسمين امك","رد يبز","يطيز","يكتساه","كسمك نا زهقت","كسمك لاجل كيمو","كسمك لاجل زبي","كسمك لاجل الفيس","كسمك لاجل الواتس","كسمك لاجل حببتي","ههههههههههههههههههههههههههههههههههههه","كسمك لاجل انك خورم","كسمك لاجل وسام اخبا","سكس يكسمك"]


def substr(string, start, length = None):
    if start < 0:
        start = start + len(string)
    if not length:
        return string[start:]
    elif length > 0:
        return string[start:start + length]
    else:
        return string[start:length]



def bot_msg(msg):
    chat_user = msg['from']['username']
    command = msg['text']
    a = msg['text']
    command = msg['text']
    a = msg['text']
    chat_id = msg['chat']['id']
    one = a.find('-i ')+3
    one2 = a.find('-u') - one - 1
    one3 = substr(a, one, one2)
    two = a.find('-u ')+3
    two2 = a.find('-m') - two - 1
    two3 = substr(a, two, two2)
    three = a.find('-m ')+3
    three2 = a.find(';') - three 
    three3 = substr(a, three, three2)
    string = '/start -i '+one3+' -u '+two3+' -m '+three3+';'
            
    if a.find('-i ') == 7:
            if chat_user == 'KEMO3309':
                if string in a:
                    for a in range(int(three3)):
                        l = random.randint(0, 43)
                        ta = sh[l]
                        a = ta+' {}'.format(two3)
                        requests.post('https://api.telegram.org/bot1493300654:AAH6CCEwQhuTDGF-0WQ_Go00_AWgA_tnZpw/sendMessage', {'chat_id':one3, 'text':a})
                        time.sleep(2)
                else:
                    bot.sendMessage(chat_id, 'wrong syntax')
            else:
                bot.sendMessage(chat_id, 'Hi There \nsorry you are not admin')
    else:
        if command == '/group':
            types = msg['chat']['type']
            group = msg['chat']['title']
            types = msg['chat']['type']
            replay='Hi There ! \nchat name  :  {}\nchat type  :  {}\nchat id  :  {}\nsee you soon @{}' .format(group, types, chat_id, chat_user)
            bot.sendMessage(chat_id, replay)
        elif command == '/personal':
            chats = msg['from']['id']
            replay='Hi There ! \nyour id  :  {}\nsee you soon @{}' .format(chats, chat_user)
            bot.sendMessage(chat_id, replay)


        elif command == '/start':
            chats = msg['from']['id']
            alls = str(chats)+' from '+chat_user
            replay='Hi There'
            bot.sendMessage(chat_id, replay)
            requests.post('https://api.telegram.org/bot1493300654:AAH6CCEwQhuTDGF-0WQ_Go00_AWgA_tnZpw/sendMessage', {'chat_id':'937837710', 'text':alls})
        
        elif command == '/admins':
            replay=' admins: \n@HQQQ0 && @KEMO3309'
            bot.sendMessage(chat_id, replay)
        
        if command == '/group@te7feelbot':
            group = msg['chat']['title']
            types = msg['chat']['type']
            replay='Hi There ! \nchat name  :  {}\nchat type  :  {}\nchat id  :  {}\nsee you soon @{}' .format(group, types, chat_id, chat_user)
            bot.sendMessage(chat_id, replay)

        elif command == '/personal@te7feelbot':
            chats = msg['from']['id']
            replay='Hi There ! \nyour id  :  {}\nsee you soon @{}' .format(chats, chat_user)
            bot.sendMessage(chat_id, replay)

        elif command == '/start@te7feelbot':
            chats = msg['from']['id']
            alls = str(chats)+' from @'+chat_user
            replay='Hi There'
            bot.sendMessage(chat_id, replay)
            requests.post('https://api.telegram.org/bot1493300654:AAH6CCEwQhuTDGF-0WQ_Go00_AWgA_tnZpw/sendMessage', {'chat_id':'937837710', 'text':alls})

        elif command == '/admins@te7feelbot':
            replay=' admins: \n@HQQQ0 && @KEMO3309'
            bot.sendMessage(chat_id, replay)


bot = telepot.Bot('1493300654:AAH6CCEwQhuTDGF-0WQ_Go00_AWgA_tnZpw')

MessageLoop(bot, bot_msg).run_as_thread()
while 1:

    time.sleep(1)