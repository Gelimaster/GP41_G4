import os
import subprocess
def open():
    #x = subprocess.check_output(os.system("start cmd /k python3 scanfinger.py ")) 
    x = subprocess.check_output(os.system("start cmd /k dir ")) 
    # os.system("taskkill /f /im cmd.exe")
    print(x)  


def test():
    # returned_text = subprocess.getoutput(os.system("start cmd /k dir   /k exit"))
    x =os.system("start cmd /k python3 scanfinger.py")
    print(os.system("dir"))
    # cmd = ['start','cmd','/k','dir','']
    # subprocess.Popen(cmd)
    # y=subprocess.Popen(x).pid
    return str(x)




if __name__ == '__main__':
    print(test())

     