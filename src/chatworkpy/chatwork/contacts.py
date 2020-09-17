from chatworkpy.chatwork.chatwork import Chatwork
import requests

class Contacts(Chatwork):
    def __init__(self, api_token, account_id_list: list):
        self.account_id_list = account_id_list
        super().__init__(api_token)

    # To のIdに紐づく名前を取得する
    def make_accounts_list(self):
        accounts_list = []
        res = self._get_contacts()
        for account_id in self.account_id_list:
            for contact in res:
                if account_id == str(contact["account_id"]):
                    item = {"account_id": contact["account_id"], "name": contact["name"]}
                    accounts_list.append(item)
                    break
        return accounts_list
    
    def _get_contacts(self):
        return self.exec_request("get", "contacts")
