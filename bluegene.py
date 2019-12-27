#bluegene spider
import requests
import re
import os
from bs4 import BeautifulSoup
headers={"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36",
          "Referer": "http://www.lanjiyin.com.cn/index.php/HomeDefault/user/login?app_type=westernmd",
          "Cookie": "acw_tc=2760828815774218161693940e72b395d798f1b9ecf71278599bdf13334563; PHPSESSID=ahdqb5ur5iffvqq7v9jsnu7l77; Hm_lvt_d61eb67134ece75a30b917cd5c862147=1577421615; looyu_id=982d4a66f3b7a6dcd517743369ee8e92_20003140%3A2; looyu_20003140=v%3A63fad4c6f225635266ca694f5ca971c2%2Cref%3A%2Cr%3A%2Cmon%3Ahttp%3A//m9107.looyu.com/monitor%2Cp0%3Ahttp%253A//www.lanjiyin.com.cn/index.php/HomeDefault/index/class_list%253Fcate_id%253D107%2526app_type%253Dwesternmd; Hm_lpvt_d61eb67134ece75a30b917cd5c862147=1577421637"
         }
def get_one_page():

    #url="http://www.lanjiyin.com.cn/index.php/HomeDefault/index/class_list?cate_id=107&app_type=westernmd"
    url="http://www.lanjiyin.com.cn/index.php/HomeDefault/index/video?vid=3180&app_type=westernmd&cate_id=107"
    url="http://www.lanjiyin.com.cn/index.php/HomeDefault/index/video?vid=3180&app_type=westernmd&cate_id=107"
    try:
        catalog=requests.get(url,headers=headers)
        soup=BeautifulSoup(catalog.text,"html.parser")
        
    except:
        print('wrong with get')
    title=soup("div",attrs={"class":"video_title"})[0].string
    
    mp4=soup("video")[0]["src"]
    if os.path.exists("E:/硬盘自带/360Wifi"):
        pass
    else:
        os.mkdir("E:/硬盘自带/360Wifi")
    mp4_url=requests.get(mp4,headers=headers)
    with open("E:/硬盘自带/360Wifi/{}.mp4".format(title),'wb') as f:
        f.write(mp4_url.content)
        f.close
def get_all_url():
    catlog_url="http://www.lanjiyin.com.cn/index.php/HomeDefault/index/class_list?cate_id=107&app_type=westernmd"
    url_head="http://www.lanjiyin.com.cn"
    request=requests.get(catlog_url,headers=headers)
    soup_catlog=BeautifulSoup(request.text,"html.parser")
    
    #<p class="fuMenu_fclass">生理学</p> 对应7本书,建立书籍的文件夹
    
    #<p class="fuMenu_class">对应每一本书的章节，建立章节文件夹
    #div class="div1_class">对应各个视频，<p是名字，<a href 为视频页的地址，建立各文件名字<p
    
if __name__=="__main__":
    get_one_page()
    


             
             
             
