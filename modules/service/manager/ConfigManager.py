import json


class ConfigKey():
    THEMES_PATH = "ThemesPath"
    INIT_NEED_PATH = "InitNeedPath"
    CACHE_PATH = "CachePath"
    COMPLETE_PATH = "CompletePath"
    SYS_FFMPEG_PATH = "SysFFmpegPath"


appName = "HLB站缓存合并1.1"


class ConfigManager:
    def __init__(self, configPath):
        self.configPath = configPath
        self.config = self.loadConfig()

    def loadConfig(self):
        try:
            with open(self.configPath, "r", encoding='utf-8') as file:
                config_str = file.read()
            return json.loads(config_str)
        except json.JSONDecodeError as e:
            print("配置文件不是一个有效的JSON文件:", e)
            return {}
        except Exception as e:
            print("加载配置文件时出现错误:", e)
            return {}

    def save(self):
        config_str = json.dumps(self.config)
        with open(self.configPath, "w", encoding='utf-8') as file:
            file.write(config_str)

    def get(self, key):
        if self.isExist(key):
            return self.config.get(key)
        else:
            return None

    def add(self, key, value):
        self.config[key] = value

    def addJson(self, jsonObj):
        # 将json对象转换为字典
        dictObj = json.loads(jsonObj)
        # 合并两个字典
        self.config.update(dictObj)

    def addByDict(self, dictObj):
        self.updateByDict(dictObj)

    def updateByDict(self, dictObj):
        # 合并两个字典
        self.config.update(dictObj)

    def remove(self, key):
        if key in self.config:
            del self.config[key]

    def update(self, key, value):
        if key in self.config:
            self.config[key] = value

    def isExist(self, key):
        if key in self.config:
            return True
        else:
            return False
