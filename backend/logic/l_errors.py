class UniqueDataError(Exception):
    info : str
    
    def __init__(self, info : str):
        self.info = info

    def show(self):
        return  self.__class__.__name__ + " : " + self.info + " already taken"