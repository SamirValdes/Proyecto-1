import DoubleList as dl
class User():
    def __init__(self ,n):
        self.__Username=n
        self.__userSongList=dl.DoubleList()
 
    @property
    def Username(self):
        return self.__Username

    @Username.setter
    def Username(self,n):
        self.__Username=n        
    
    def addSong(self,n):
        self.__userSongList.addFirst(n)

    def findSong(self,nombre):
        temp=self.__UserSong.first()
        while temp !=None and temp.data.name!=nombre:
            temp=temp.next
            
            if temp==None:
                return None
            else:
                return temp 
            
    def removeSongs(self,name):
        temp=self.findSong(name)
        if temp !=None:
            self.__userSongList.remove(temp ) 
            
    def playList(self):
        temp=self.__userSongList.first()
        while temp !=None:
            print(temp.data.Username)
            temp=temp.next
                         
    def __str__(self):
        return self.__Username            
           