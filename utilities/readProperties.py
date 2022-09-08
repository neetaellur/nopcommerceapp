import configparser
config=configparser.RawConfigParser()
config.read(r".\\configurations\\config.ini")
class ReadConfig:
    @staticmethod
    def getApplicationURL():
        url=config.get('common info','baseurl')
        return url

    @staticmethod
    def getUseremail():
        username=config.get('common info','useremail')
        return username
    @staticmethod
    def getPassword():
        password=config.get('common info','password')
        return password
