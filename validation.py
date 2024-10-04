
def empty(datalist):
    for d in datalist:
        if  d =='':
            return True
        

def checkdigit(data) : 
    if(data.isdigit()):
        return False
    else:
        return True      

def checkalpha(data):
    if(data.isalpha()) :
        return False  
    else:
        return True 