import time, urllib.request, json, vkapi, random

owner_id = "33908741"
item_id = "379316901"
type = "photo"

#ТИПЫ ОБЪЕКТОВ:
#post — запись на стене пользователя или группы;
#comment — комментарий к записи на стене;
#photo — фотография;
#audio — аудиозапись;
#video — видеозапись;
#note — заметка;
#photo_comment — комментарий к фотографии;
#video_comment — комментарий к видеозаписи;
#topic_comment — комментарий в обсуждении;
#sitepage — страница сайта, на котором установлен

random.seed(version=2) 

while (True):
    vkapi.executeApiRequest("likes.add", {"owner_id": owner_id, "item_id": item_id, "type": type})
    time.sleep(random.random() * 5)
    vkapi.executeApiRequest("likes.delete", {"owner_id": owner_id, "item_id": item_id, "type": type})
    time.sleep(random.random() * 5)
    print('success')