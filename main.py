# -*- coding:utf-8 -*-

import requests
import datetime

# https://pypi.org/project/chatpywork/
# pip install chatpywork

# https://developer.chatwork.com/ja/endpoints.html
from src.chatworkpy.config import Config
from src.chatworkpy.chatwork import chatwork, rooms

def main():
    config_file = './config.yml'
    config = Config(config_file).content
    api_token = config["CHATWORK_API_TOKEN"]
    room_id = '52230684'
    chatwork_rooms = rooms.Rooms(api_token, room_id)
    #room = chatpywork.Room(room_id, api_token)
    try:

        account_id1 = 970114  ## HT
        #account_id2 = '2761593'  ## th
        to_id_list = []
        to_id_list.append(account_id1)
        #chatwork_rooms.send_message("hello", to_id_list)
        dt_now = datetime.datetime.now()
        td_3d = datetime.timedelta(days=3)
        limit_datetime = dt_now + td_3d
        chatwork_rooms.send_task("hello", to_id_list, limit_datetime)
        #raise ValueError("exception: value error!")
    except ValueError as e:
        print(e)
        #room.send_message(e, to={account_id1: ""})
    except Exception as ex:
        print(ex)

main()