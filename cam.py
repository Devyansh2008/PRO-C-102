import cv2
from numpy import true_divide
def camerycreepy():
    sus=cv2.VideoCapture(0)
    a=True
    while a :
        b,c=sus.read()
        cv2.imwrite("sussybaka.png",c)
        a=False 

camerycreepy()

import dropbox
class PROC102 :
    def __init__(self,accessToken) :
        self.a=accessToken
    
    def Upload(self,source,destination):
        dbx=dropbox.Dropbox(self.a)
        E=open(source,"rb")
        dbx.files_upload(E.read(),destination)


def Sus() :
    AT="sl.BHh2wzEmTZf45DWf8AGflKzcWyebBTF9JBllad8OxhUFkNjzx27CGIBqZfNVb_XLySlBD8p38470J3QmzmvKkxmHDIVexcW2CNmnGw9qk7ktLGEalLWwo1GFDbC1Yr49f51-rhB3RQuH"
    Foil=PROC102(AT)
    s=("C:/Users/Ashish/OneDrive/Documents/Devyansh/Whjr/sussybaka.png")
    d=input("/dripbox.exe")
    Foil.Upload(s,d)
    print("Project compelete")

Sus()