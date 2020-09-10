from utils.chatwork import chatwork
from utils.chatwork import contacts
import os
import requests

class Rooms(chatwork.Chatwork):
    
    def __init__(self, room_id):
        self.room_id = room_id

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

    def send_message(self, message: str, to_id_list: list, to_all: bool=False):
        chatwork_contacts = contacts.Contacts(to_id_list)
        tos_dict = chatwork_contacts.make_tos_dict()
        
        post_url = f'{self.base_url}/rooms/{self.room_id}/messages'

        headers = {'X-ChatWorkToken': self.api_token}
        prefix_message = self._make_prefix_message_for_to_id_list(tos_dict, to_all)
        params = {'body': prefix_message + message}
        return requests.post(post_url, headers=headers, data=params)

