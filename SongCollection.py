import DoubleList as dl
class SongCollection():
    def __init__(self):
        self.__songs=dl.DoubleList()
        
    def add(self,u):
        self.__songs.addLast(u)
               
    def find(self,nombre):   
        temp=self.__songs.first()
        while temp !=None and temp.data.name!=nombre:
            temp=temp.next
                
        if temp==None:
            return None
        else:
                return temp  
                
    def remove(self,name,User):
        temp=self.find(name)
        if temp !=None:
            self.__songs.remove(temp)
            temp2=User.user.first()
            while temp2 !=None:
                temp2.data.removeSongs(name)
                temp2=temp2.next
                print(temp,temp2.data.name)

     

        
    def play(self):
        temp=self.__songs.first()
        while temp !=None:
            print("Reproduciendo: "+temp.data.artist+" "+temp.data.name)
            temp=temp.next
        

        
                                        