# -*- coding:utf-8 -*-

import requests
import datetime

# https://pypi.org/project/chatpywork/
# pip install chatpywork

# https://developer.chatwork.com/ja/endpoints.html
from utils.chatwork import chatwork
from utils.chatwork import rooms

def main():
    api_token = ''
    chatwork_rooms = rooms.Rooms(api_token)
    room_id = '52230684'
    #room = chatpywork.Room(room_id, api_token)
    try:

        account_id1 = '970114'  ## HT
        #account_id2 = '2761593'  ## th
        to_id_list = []
        to_id_list.append(account_id1)
        chatwork_rooms.send_message("", to_id_list)
        raise ValueError("exception: value error!")
    except ValueError as e:
        print(e)
        #room.send_message(e, to={account_id1: ""})

main()