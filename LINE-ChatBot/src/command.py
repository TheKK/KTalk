# -*- coding: utf-8 -*-

from random import randint
from src.news import *
from settings import *

class Command:
    def __init__(self, data):
	self.data = data
        self.__boss_name = Settings().HERE_IAM_YOUR_BOSS

        self.jawab = \
        [
            "wah ada si bos %s, sungkem bos!", 
            "tuan muda sekaligus bos yang aku hormati %s",
            "hormat grak! bos %s datang ...",
            "mengabdi pada boss %s!",
            "*ngumpet, pak bos %s dateng",
            "wahai pak bos %s ku yang mulia",
            "bos ku %s yang tampan akhirnya berbicara", 
            "hormat sama pak boss %s yang ganteng",
            "boss %s datang , boss %s datang *sungkem",
            "pak bos %s ku yang kucinta",
            "aku setia, mengabdi pada bos %s"
        ]

	self.replyGroup = {
		'玉山': [
			'我知道我知道，喵',
			'是臺灣最高的山，喵',
		],
		'news': [
			self.get_news
		],
		'atm_location': [
			'這個功能還在施工中，請耐心等待噢，喵'
		],
		'temmi': [
			self.send_tommi_pic
		],
		'random': [
			# '喵喵喵喵',
			# '偷偷告訴你，我的名字叫做...',
			# '最近迷上一隻要上大學的貓咪呢！',
			self.play_a_game
		]
	}

	self.cmd = [
			{'keywords': ['玉山'], 'group': '玉山'},
			{'keywords': ['消息', '訊息', '新聞'], 'group': 'news'},
			{'keywords': ['atm', '提款機'], 'group': 'atm_location'},
			{'keywords': ['hoi', 'temmi'], 'group': 'temmi'}
	]

        self.commands = \
        [
            "!botreply",
            "!botkatamutiara",
            "!botbioskop",
            "!bottranslate",
            "!botmeme",
            "!botyoutubemp3",
            "!botyoutubedl",
	    "!hoi",
	    "!news",
	    "!temmi",
            "!bothelp",
            "!botkick" # this only works for the instruction of the boss.
        ]

        self.help_info = " \
            \n[+] Bot Help & About [+] \n \
            \n[~] List Of Commands: \n \
            \n[1]. !botreply <pesan> \
            \n[2]. !botkatamutiara \
            \n[3]. !botbioskop\
            \n[4]. !bottranslate <pesan> ( ID - EN / EN - ID) \
            \n[5]. !botmeme \
            \n[6]. !botyoutubemp3 <url youtube> \
            \n[7]. !botyoutubedl <url youtube> \
            \n[8]. !hoi \n \
            \n[9]. !news \n \
            \n[10]. !bothelp \n \
            \n[x] Coded by snoww0lf with Love & Peace <3. [x]"

    def play_a_game(self):
        reply = """
                先別提那個了，你有聽過 flappy cat 嗎？
                http://kindersung.github.io/flappy/'
        """
	self.data.sendMessage(reply)

    def send_tommi_pic(self):
	self.data.sendMessage('HOI!')
	self.data.sendImage('./temmi.gif')

    def get_news(self):
        news = get_all_news()
        news_msg = '喵，這裏是今天玉山銀行的相關訊息：'
        i = 0
        for new in news['news']:
            news_msg += ('[%d]' + new['title'] + '\n') % i
            i += 1
        return news_msg

    def do_bot_reply(self, lineMsg):
	msg = lineMsg.text.lower()
	group = 'random'
    	replys = self.replyGroup['random']
    
    	for cmd in self.cmd:
    		for keyword in cmd['keywords']:
    			if keyword in msg:
				group = cmd['group']
				replys = self.replyGroup[group]
				break
    
    	reply = replys[randint(0, len(replys) - 1)]

	print('[MESSAGE] %s' % msg)
	print('[GROUP]: %s' % group)
	print('[REPLY] %s' % reply)

	if hasattr(reply, '__call__'):
		reply()
	else:
		self.data.sendMessage(reply)
    
    def bot_cmd(self, selected):
        return self.commands[selected]

    def bos_reply(self):
        return self.jawab[randint(0, len(self.jawab)-1)] % (self.__boss_name)

    def bos_name(self):
        return self.__boss_name
        
    def help(self):
        return self.help_info
