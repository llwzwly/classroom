#-*- utf-8 -*-
import requests
import re
import urllib.request
import time
import threading

def cbk(a, b, c):
    '''回调函数
    @a:已经下载的数据块
    @b:数据块的大小
    @c:远程文件的大小
    '''
    per = 100.0*a*b/c 
    
    if per == 0:
        print('开始下载')

    elif per > 100:
        per = 100
        print(images_name, r'%.2f%%' % per, '下载完成')
    
def get_image(page):
        
    work_path = r'C:\Users\温志伟\Desktop\Untitled-1.txt'
    headers = {
        'User-Agent':'Chrome'
    }

    #下载网页源代码并读取为字符串
    try:
        result = requests.get(r'https://www.qiushibaike.com/imgrank/page/%s/' % page, headers = headers)
        with open(work_path, 'w', encoding = 'utf8') as f:
            f.write(result.text)
        with open(r'C:\Users\温志伟\Desktop\Untitled-1.txt', encoding = 'utf8') as f:
            content = f.read()   
            
        #利用正则表达式提取图片地址
        image_address = re.findall(r'<img src="(//pic.qiushibaike.com\S+\.[jpeg]+)".+>', content)
        
        for i in image_address:
            global images_name
            i = 'http:' + i
            images_name = ''.join(re.findall(r'app\S+\.[jpeg]+', i)) 
            image_path = r'C:\Users\温志伟\Desktop\image\%s' % images_name
            urllib.request.urlretrieve(i, image_path, cbk)
    
    except:
        print('页面%d图片下载失败' % page)


if __name__ == '__main__':
    start_time = time.time()
    try:
        start_number = input('请输入你想得到的起始页面：')
        end_number = input('请输入你想得到的终止页面：')
        for page in range(int(start_number), int(end_number)+1):
            t = threading.Thread(target=get_image, args=(page,))
            t.start()
        print('下载所需等待时间:', time.time() - start_time)

    except:
        print('Error:线程未启动')

    else:
        print('success')
    