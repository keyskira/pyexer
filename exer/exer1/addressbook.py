import os
import cPickle


def addtocontacts():
    name = raw_input("Please input name: ")
    telnumber = raw_input("Please input telephone number: ")
    if len(contacts) != 0:
        for j in contacts.keys():
            if name == j:
                print "Already there! contacts will not be updated!"
                break
        else:
            contacts[name] = telnumber
    else:
        contacts[name] = telnumber
    print contacts


def removepeople():
    name = raw_input("Please input name: ")
    del contacts[name]


def savetofile():
    f = open("contact.data", "w")
    cPickle.dump(contacts, f)
    f.close()


def readfile():
    if len(contacts) == 0:
        print "There is nothing."
    else:
        return contacts


def findpeople():
    name = raw_input("Who do you want to find?")
    return contacts[name]



if os.path.isfile("contact.data"):
    f = open("contact.data")
    contacts = cPickle.load(f)
    f.close()
    print contacts
else:
    contacts = {}
    f = open("contact.data", "w")
    cPickle.dump(contacts, f)
    f.close()

welcomeword = """Welcome to my address book.
Input the number to do something!
1. add a people into contact
2. find a people from contact
3. list the contact
4. remove the people"""
print welcomeword
donumber = raw_input("what can i do for you? --> ")
if donumber == "1":
    addtocontacts()
    savetofile()
elif donumber == "2":
    findpeople = findpeople()
    print findpeople
elif donumber == "3":
    lists = readfile()
    try:
        print ("Name".ljust(5) + "Tel Number".rjust(20))
        for i in lists:
            print (str(i).ljust(5)+str(contacts[i]).rjust(20))
    except TypeError:
        pass
elif donumber == "4":
    removepeople()
    savetofile()
else:
    print "Oops,you cant let me do somgthing I cant do."
