class ForegroundColors:
    
    @staticmethod
    def cyan(text):
        return '\033[36m' + text + '\033[0m'
    
    @staticmethod
    def red(text):
        return '\033[31m' + text + '\033[0m'
    
    @staticmethod
    def purple(text):
        return '\033[35m' + text + '\033[0m'

    @staticmethod
    def orange(text):
        return '\033[33m' + text + '\033[0m'
    
    @staticmethod
    def green(text):
        return '\033[32m' + text + '\033[0m'
    
