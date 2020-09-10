from utils.chatwork import chatwork
import requests

class Contacts(chatwork.Chatwork):
    def __init__(self, to_id_list: list):
        self.to_id_list = to_id_list

    # To のIdに紐づく名前を取得する
    def make_tos_dict(self):
        tos_dict = {}
        aaa = self._get_contact_name()
        for to_id in self.to_id_list:
            item = (to_id, "name" + to_id)
            tos_dict.update([item])
        return tos_dict
    
    def _get_contact_name(self):
        get_url = f'{self.base_url}/contacts'

        headers = {'X-ChatWorkToken': self.api_token}
        return requests.get(get_url, headers=headers)
