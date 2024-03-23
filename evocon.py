import requests
from pandas import DataFrame

class Evocon():
    def __init__(self, username, password, startTime, endTime):
        self.username = username
        self.password = password
        self.startTime, self.endTime = self.format_time(startTime, endTime)

    @staticmethod
    def format_time(startTime, endTime):
        startTime = "{:04}-{:02}-{:02}".format(startTime.year, startTime.month, startTime.day )
        endTime = "{:04}-{:02}-{:02}".format(endTime.year, endTime.month, endTime.day)
        return startTime, endTime
    
    def format_response(self, name):
        val = getattr(self, "response_"+name)
        if str(val.status_code)[0] == "2":
            setattr(self, "res_"+name, DataFrame(val.json()))
        else:
            print("something is wrong!")
            print(self.response.text)


    def oee(self, station_id = 1):
        station_id = "{:.0f}".format(station_id)
        url = f"https://api.evocon.com/api/reports/oee_json?startTime={self.startTime}&endTime={self.endTime}&stationId={station_id}"
        self.response_oee = requests.get(url, auth=(self.username, self.password))
        self.format_response("oee")

    def losses(self, station_id = 1):
        station_id = "{:.0f}".format(station_id)
        url = f"https://api.evocon.com/api/reports/losses_json?startTime={self.startTime}&endTime={self.endTime}&stationId={station_id}"
        self.response_losses = requests.get(url, auth=(self.username, self.password))
        self.format_response("losses")

    def clientmetrics(self, station_id = 1):
        station_id = "{:.0f}".format(station_id)
        url = f"https://api.evocon.com/api/reports/clientmetrics_json?startTime={self.startTime}&endTime={self.endTime}&stationId={station_id}"
        self.response_clientmetrics = requests.get(url, auth=(self.username, self.password))
        self.format_response("clientmetrics")

    def checklists(self, station_id = 1):
        station_id = "{:.0f}".format(station_id)
        url = f"https://api.evocon.com/api/reports/checklists_json?startTime={self.startTime}&endTime={self.endTime}&stationId={station_id}"
        self.response_checklists = requests.get(url, auth=(self.username, self.password))
        self.format_response("checklists")
