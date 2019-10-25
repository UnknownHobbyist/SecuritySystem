import json

class JSONSERVICE:
    @staticmethod
    def getJson() -> dict:
        file = open('source/json.json')
        json_file = json.load(file)
        file.close()
        return json_file

    @staticmethod
    def setJson(j:dict):
        file = open('source/json.json',"w")
        file.write(json.dumps(j))
        file.close()
