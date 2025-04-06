class UniqueDataError(Exception):
    info : str
    code = 111
    
    def __init__(self, info : str):
        self.info = info

    def show(self):
        return  self.__class__.__name__ + " : " + self.info + " already taken"

    def __repr__(self):
        return self.show()
    
class AuthenticationError(Exception):
    info : str
    code = 222
    
    def __init__(self, info : str):
        self.info = info

    def show(self):
        return  self.__class__.__name__ + " : " + self.info + " incorrect password"
    
    def __repr__(self):
        return self.show()
    
class NoSuchFileError(Exception):
    info : str
    code = 333
    
    def __init__(self, info : str):
        self.info = info

    def show(self):
        return  self.__class__.__name__ + " : " + self.info + " no such file"
    
    def __repr__(self):
        return self.show()