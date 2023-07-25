

isDebug =False

class Log():
    # ANSI颜色转义码
    COLORS = {
        'reset': '\033[0m',
        'red': '\033[31m',
        'green': '\033[32m',
        'yellow': '\033[33m',
        'blue': '\033[34m',
        'purple': '\033[35m',
        'cyan': '\033[36m',
        'white': '\033[37m'
    }
    @staticmethod
    def setDebug(value):
        global isDebug
        isDebug =value

    @staticmethod
    def d(message):
        if isDebug:
            print(f"{Log.COLORS['green']}[DEBUG] {message}{Log.COLORS['reset']}")

    @staticmethod
    def i(message):
        if isDebug:
            print(f"{Log.COLORS['blue']}[INFO] {message}{Log.COLORS['reset']}")

    @staticmethod
    def w(message):
        if isDebug:
            print(f"{Log.COLORS['yellow']}[WARNING] {message}{Log.COLORS['reset']}")

    @staticmethod
    def e(message):
        if isDebug:
            print(f"{Log.COLORS['red']}[ERROR] {message}{Log.COLORS['reset']}")