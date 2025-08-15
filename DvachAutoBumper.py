import requests
import base64
import os
import random
import json
import time

def generateComment(i):
    return 'bump{0}'.format(i)

#https://2ch.hk/makaba/posting.fcgi
#Параметры для передачи:
#json = 1
#task = post
#board - код доски
#thread - номер треда - для создания нового треда необходимо проставить 0
#email - значение поля e-mail
#name - имя
#subject - тема сообщения
#comment - комментарий, максимальное количество символов - 15000
#image - изображение для отправки

#settings
thread = '120611792'
images_folder = r'D:\folderwtf\ABU'
default_image_url = 'https://pp.vk.me/c628323/v628323196/35bbc/vSget3STAFs.jpg'
comments_list_file = r'C:\Users\bastr\Desktop\comments.txt'
COMMENT_DELIMETER_LINE = '###'

try:
    images_list = [image_name for image_name in os.listdir(images_folder) if image_name.endswith('.jpg')]
    comments_list = open(comments_list_file, 'r').read().split('\n' + COMMENT_DELIMETER_LINE + '\n')
    default_image = requests.get(default_image_url).content

    data = {
        'json':'1',
        'task':'post',
        'board':'b',
        'thread': thread,
        'email':'cho@epta.kek',
        'name':'MDA',
        'subject':'LALKA_OLOLO'
        }
    images = {}

    print('Starting...')
    i = 0
    random.seed(version=2)
    while (True):
        #image selecting for post
        if (i < len(images_list)):
            images['image'] = open(images_folder + '\\' + images_list[i] , "rb")              
        elif (len(images_list) != 0):
            rand = random.randint(0, len(images_list) - 1)
            images['image'] = open(images_folder + '\\' + images_list[rand] , "rb") 
        else:
            images['image'] = default_image

        #comment selecting for post
        if (i < len(comments_list)):
            data['comment'] = comments_list[i]
        else:
            data['comment'] = generateComment(i)

        #post execution
        response = requests.post('https://2ch.hk/makaba/posting.fcgi', data = data, files = images)

        #result processing
        if (json.loads(response.content.decode("utf-8"))['Error'] != None):
            raise BaseException(json.loads(response.content.decode("utf-8"))['Reason'])
        
        print('Bump {0} executed'.format(i))
        i += 1
        time.sleep(random.randint(30, 50))

except BaseException as e:
    print('ПИЗДА НАХУЙ:')
    print(e)

