class User:

    def __init__(self, id):
        self.__id = id
    #-------------------------
    ## getter and setter User
    #-------------------------
    def get_a(self):
        return self.__id

    def set_a(self, id):
        self.__id = id