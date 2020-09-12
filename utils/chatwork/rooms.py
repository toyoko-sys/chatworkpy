from utils.chatwork import chatwork
from utils.chatwork import contacts
import os
import requests

class Rooms(chatwork.Chatwork):
    
    def __init__(self, api_token: str, room_id):
        self.room_id = room_id
        super().__init__(api_token)

    # private method
    # make prefix_message_for_to_id_list
    """
    # To: Hogehoge さん
    # To: Fugafuga さん
    """
    def _make_prefix_message_for_to_id_list(self, tos_dict: dict, to_all: bool=False):
        prefix = ''
        if to_all:
            prefix += "[toall]"
        else:
            for to_id, to_name in tos_dict.items():
                prefix += f"[To:{to_id}] {to_name}さん{os.linesep}"
        prefix += os.linesep

        return prefix
    
    def _get_rooms(self):
        return self.exec_request("get", "rooms")

    # To のIdに紐づく名前を取得する
    def _make_tos_dict(self, to_id_list:list):
        tos_dict = []
        response_get_rooms = self._get_rooms()
        for to_id in to_id_list:
            for room in response_get_rooms:
                name = room["name"] if room["type"] == "direct" else None
                if name != None:
                    item = {"to_id" : to_id, "name" : name + " さん"}
                    tos_dict.append(item)

        return tos_dict
        
    def send_message(self, message: str, to_id_list: list, to_all: bool=False):
        aaa = self._make_tos_dict(to_id_list)
        # if response_get_rooms.status_code == 200:
        #     content = response_get_rooms.content
        #     print(content)
        #     aa = content[0]['room_id']

        chatwork_contacts = contacts.Contacts(self.api_token, to_id_list)
        tos_dict = chatwork_contacts.make_tos_dict()
        
        post_url = f'{self.base_url}/rooms/{self.room_id}/messages'

        headers = {'X-ChatWorkToken': self.api_token}
        prefix_message = self._make_prefix_message_for_to_id_list(tos_dict, to_all)
        params = {'body': prefix_message + message}
        return requests.post(post_url, headers=headers, data=params)

