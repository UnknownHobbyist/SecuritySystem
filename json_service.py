import json


class JsonService:
    # method for getting json.json file
    @staticmethod
    def getJson() -> dict:
        file = open("source/json.json")
        json_file = json.load(file)
        file.close()
        return json_file

    # method for changing json.json values
    @staticmethod
    def setJson(j: dict):
        file = open("source/json.json", "w")
        file.write(json.dumps(j))
        file.close()
