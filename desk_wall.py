import requests,random
import os
#wp_num=raw_input("Enter the wallpaper's number> ")   #In case of user-input!
#if int(wp_num)>999999 and int(wp_num)<1:             #To be used in case of user input! 
#    print "The URL does not exists!"
#    exit(0)
#print str(res_jpg.status_code)

while True:
    wp_num=str(random.randint(1,999999)) #NSFW        
    res_jpg=requests.get("https://wallpapers.wallhaven.cc/wallpapers/full/wallhaven-"+wp_num+".jpg")
    if res_jpg.status_code==requests.codes.ok:
        fp=open("img_wall_desktop.jpg",'wb')
        for data in res_jpg.iter_content(100000):
            fp.write(data)
        fp.close()
        wall_path=os.path.abspath("img_wall_desktop.jpg")
        break
    else:
        res_png=requests.get("https://wallpapers.wallhaven.cc/wallpapers/full/wallhaven-"+wp_num+".png")
        if res_png.status_code==requests.codes.ok:
            fp=open("img_wall_desktop.png",'wb')
            for data in res_png.iter_content(100000):
                fp.write(data)
            fp.close()
            wall_path=os.path.abspath("img_wall_desktop.png")
            break 
os.system("gsettings set org.gnome.desktop.background picture-uri file://"+wall_path) 
print "Your wallpaper has been set!"
