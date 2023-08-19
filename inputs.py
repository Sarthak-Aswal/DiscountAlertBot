

#gets url of amazon product from user
def getURL():
    userInput=input("Enter the product url:")
    return userInput


#gets email from user
def getMail():
    userMail = input("Enter you email:")
    return userMail


#gets user agent from a file called userAgent.txt
def getUserAgent():
    with open("userAgent.txt",'r') as ua:
        useragent = ua.read().strip()
    return useragent
