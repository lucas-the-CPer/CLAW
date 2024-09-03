from crypto import encodeBase64, decodeBase64, encodeBase32, decodeBase32
from scriptRunner import deleteUsers, addUsers
import customtkinter
from CIA import cia
#from CipherID import torchTest
from CodeRed import CDRD

#List of tools to be assinged to buttons
cryptoToolList = ["encodeBase64","decodeBase64", "encodeBase32", "decodeBase32", "Cipher Index Analysis", "Cipher Recognition","Shift Cipher"]
winScriptToolList = ["deleteUsers", "addUsers"]
linScriptToolList = ["linuxScripts"]
ctfToolList = ["codeRed", "osint", "metaDataGrabber", "www"]

#Must match index of titleList and toolList if you want said title to show said tool buttons
titleList = ["Encryption / Decrption", "Window Scripts", "Linux Scripts", "CTF Tools"]
toolList = [cryptoToolList, winScriptToolList, linScriptToolList,ctfToolList]

        

def command(commandName):
    match commandName:
        case "encodeBase64":
            print("this is base64")
            encodeBase64()
        case "decodeBase64":
            decodeBase64()
        case "deleteUsers":
            deleteUsers()
        case "addUsers":
            addUsers()
        case "encodeBase32":
            encodeBase32()
        case "decodeBase32":
            decodeBase32()
        case "Cipher Index Analysis":
            cia()
        case "Cipher Recognition":
            #torchTest()
            pass
        case "CodeRed":
            CDRD()
        
    
def packButtons(buttonList, index, titleList):
    for i in range(len(titleList)):
        if i == index:
            titleList[i].configure(fg_color=  "DarkGoldenrod4")
        else:
            titleList[i].configure(fg_color=  "goldenrod")
    for i in range(len(buttonList)):
        if i == index:
            for j in range(len(buttonList[i])):
                buttonList[i][j].pack(padx = 10, pady = 15, side= customtkinter.TOP)
        else:
            for n in range(len(buttonList[i])):
                buttonList[i][n].pack_forget()


def titleCardCommand(toolList, index, titleList):
    packButtons(toolList, index, titleList)       

