class Song ():
    def __init__(self,c,n,a,al,y):
        self.__code=c
        self.__artist=a
        self.__name=n
        self.__album=al
        self.__year=y

    @property
    def code(self):
        return self.__code
    
    @property
    def artist(self):
        return self.__artist
            
    @property
    def name(self):
        return self.__name    
    
    @property
    def album(self):
        return self.__album
    
    @property
    def year(self):
        return self.__year
    
    @code.setter
    def code(self,n):
         self.__code=n
         
    @artist.setter
    def artist(self,n):
        self.__artist=n         
         
    @name.setter
    def name(self,n):
        self.__name=n
           
    @album.setter
    def album(self,n):
        self.__album=n
    
    @year.setter
    def year(self,n):
        self.__year=n

    def __str__(self):
        return self.code+" "+self.name+" "+self.artist+" "+self.album+" "+str(self.year)           
         
    
    