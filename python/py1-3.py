class stri:
    
    def __inti__(self,st,va):
        self.st=st
        self.va=va

    def getString(self):
        self.st=input()
    def putString(self):
        self.va=self.st.upper()
        print(self.va)
s=stri()
s.getString()
s.putString()


