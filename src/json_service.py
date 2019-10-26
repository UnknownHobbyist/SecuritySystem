import json

class JsonService:
    #method for getting json.json file
    @staticmethod
    def getJson() -> dict:
        file = open('../rsc/login_data.json')
        json_file = json.load(file)
        file.close()
        return json_file

    #method for changing json.json values
    @staticmethod
    def setJson(j:dict):
        file = open('../rsc/login_data.json',"w")
        file.write(json.dumps(j))
        file.close()
