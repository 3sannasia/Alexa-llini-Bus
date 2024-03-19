import os
from dotenv import load_dotenv
import requests
import json


class MTD_API:
    def __init__(self):
        load_dotenv()
        self.api = os.getenv("MTD_API_KEY")
        self.data_format = "JSON"
        self.version = "v2.2"
        self.base_url = "https://developer.mtd.org/api/{}/{}/{{}}?key={}".format(self.version, self.data_format, self.api)
        self.changeset_id = None
        self.cache = {}

    def get_routes_by_stop(self, stop_id: str) -> dict: 
        request_method = "getroutesbystop"
        param = {
            "stop_id": stop_id,
            "changeset_id": self.changeset_id
        }
        response = requests.get(self.base_url.format(request_method), params = param)
        response_json = response.json()
        if response.status_code == 202:
            pass
            # data not modified check in cache and return
        elif response.status_code == 200:
            changeset_id = response_json["changeset_id"]
            param["changeset_id"] = changeset_id
            return response_json
        
    def pretty_print(self, data: dict):
        return json.dumps(data, indent=4)
       
if __name__ == "__main__":
    mtd = MTD_API()
    print(mtd.pretty_print(mtd.get_routes_by_stop("IT:1")))


    

