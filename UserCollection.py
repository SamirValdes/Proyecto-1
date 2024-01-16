import DoubleList as dl
class UserCollection:
    def __init__(self):
        self.__user=dl.DoubleList()
        
    @property
    def user(self):
        return self.__user

    def add(self,u):
        self.__user.addLast(u)
            
    def find(self,u):   
        temp=self.__user.first()
        while temp !=None and temp.data.Username!=u:
            temp=temp.next
            
        if temp==None:
                return None
        else:
                return temp 
            
    def remove(self,username):
        temp=self.find(username)
        if temp !=None:
            self.__user.remove(temp)
            return temp.data
        else:
            return None
          
            
    def print(self):
        temp=self.__user.first()
        while temp !=None:
            print(temp.data.Username)
            temp=temp.next       
            
    def addUserSong(self,username,name,Song):
        temp=self.find(username)
        temp2=Song.find(name)
        if temp !=None:
            if temp2 !=None:
                    temp.data.addSong(temp2.data)
                    temp2.data.addSong(temp.data)
            else:
                 print("Error: La cancion no existe")
                    
                    
        else:
            print("Eror: el usuario no existe")
            
                        
                
# else no encuentra la cancion o el usuario                

    def playUserList(self,username):
        temp=self.find(username)
        if temp !=None:
            print(temp.data)
            temp=temp.next
        
        

            
            
            
                        
           