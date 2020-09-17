# -*- coding:utf-8 -*-

import requests
import datetime
import logging

# https://pypi.org/project/chatpywork/
# pip install chatpywork

# https://developer.chatwork.com/ja/endpoints.html
from chatworkpy.config import Config
from chatworkpy.chatwork.rooms import Rooms
from chatworkpy.chatwork.contacts import Contacts

def main():
    config_file_path = './src/config.yml'
    try:
        # account_id1 = 970114  ## HT
        # #account_id2 = '2761593'  ## th
        # account_id_list = []
        # account_id_list.append(account_id1)
        # accounts_dict = {}
        
        # #NOTE: やめたほうがいい
        # accounts_dict = chatwork_rooms._make_accounts_dict(account_id_list)
        # #NOTE: 手動で作るパターン
        # accounts_dict = accounts_dict.append({"account_id" : account_id, "name" : "infbot"})
        # chatwork_rooms.send_message("hello", accounts_dict)
        # dt_now = datetime.datetime.now()
        # td_3d = datetime.timedelta(days=3)
        # limit_datetime = dt_now + td_3d
        # chatwork_rooms.send_task("hello", account_id_list, limit_datetime)
        # #raise ValueError("exception: value error!")
        chatwork_config = Config(config_file_path).content["ALERT"]
        logging.error(f"ALERT IS {chatwork_config['IS_ENABLE']}")
        import traceback
        error_message = traceback.format_exc()  ##NOTE: get exception message
        if not chatwork_config["IS_ENABLE"]:
            logging.error(error_message)
            return

        api_token = chatwork_config["CHATWORK_API_TOKEN"]


        #NOTE: test contacts
        to_account_list = chatwork_config["CHATWORK_TO_ACCOUNT_LIST"]
        account_id_list = []
        for account in to_account_list:
            account_id_list.append(account["ID"])
        chatwork_contacts = Contacts(api_token, account_id_list)
        res = chatwork_contacts._get_contacts()
        print(res)
        accounts_list = chatwork_contacts.make_accounts_list()


        room_id = chatwork_config["CHATWORK_ROOM_ID"]
        to_account_list = chatwork_config["CHATWORK_TO_ACCOUNT_LIST"]
        accounts_dict = []
        for account in to_account_list:
            accounts_dict.append({"account_id" : account["ID"], "name" : account["NAME"]})
        chatwork_rooms = Rooms(api_token, room_id)
        #chatwork_rooms.send_message(error_message, accounts_dict)
    except ValueError as e:
        print(e)
        #room.send_message(e, to={account_id1: ""})
    except Exception as ex:
        print(ex)

main()