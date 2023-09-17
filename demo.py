
'''多级文件'''

'''设计逻辑:1.请求页面所有日期.
2.进入二级文件.爬取页面连接,进行访问.如果不存在三级页面,直接进行链接下载
3.'''
#function调用多模块
from bs4 import BeautifulSoup
import requests
import re
from concurrent.futures import ThreadPoolExecutor
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

b_url = ""
bb_url = ""
image_urls2 = ""

def download_image(image_urls2, folder):
    response = requests.get(image_urls2)
    print(response)
    if response.status_code == 200:
        filename = image_urls2.split('/')[-1]
        filepath = os.path.join(folder, filename)
        with open(filepath, 'wb') as f:
            f.write(response.content)
        print(f"Downloaded: {filename}")
    else:
        print(f"Failed to download: {image_urls2}")

def data():
    global b_url
    global a
    global b
    for a in range(12, 13):
        for b in range(2022, 2023):
            data_time = "{}.{:02d}".format(b, a)
            print(data_time)
            b_url = "https://www.fantasyfactory.xyz/{}/".format(data_time)
            print(b_url)
            requests1 = requests.get(b_url)

data()

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

# 指定ChromeDriver的路径
chromedriver_path = r'C:\\Users\\21016.LAPTOP-KGP1GRG0\AppData\Local\Programs\Python\Python39\chromedriver.exe'
service = Service(chromedriver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

def xiaoding():
    global bb_url
    requests1 = requests.get(b_url)
    if requests1.status_code == 200:
        response = requests1.text
        soup = BeautifulSoup(response, "html.parser")
        all_links = soup.find_all('a')

        for link in all_links:
            href = link.get('href')
            content = link.string
            if href and '{}'.format(b) in href:
                pattern = r'({}.{}\S+)'.format(b,a)
                match = re.search(pattern, href)
                if match:
                    bb_url = "https://www.fantasyfactory.xyz/{}".format(match.group(1))
                    print(bb_url)
                else:
                    print("error")
    else:
        print(b_url, "该页面不存在")



def thread_page():
    response3 = requests.get("https://www.fantasyfactory.xyz/2022.12/fairy%20maid/")
    if response3.status_code == 200:
        response4 = response3.text
        #image_urls = re.findall(r'<img src="(_h5ai/public/cache/thumbs/.*?)"', response4)\
        #image_urls = re.findall(r'2022.12/.*?',response4)
        '''if his link only perfect link can use findall .if not must use patern'''
        pattern2 = r'(2022\.12/[^"]+)'
        image_urls = re.findall(pattern2,response4)
        folder = 'test'
        if not os.path.exists(folder):
            os.makedirs(folder)
        #image_urls = "https://www.fantasyfactory.xyz" + "image_urls"
        #image_urls 实际上是一个列表，而不是字符串。使用 + "image_urls" 实际上是将字符串 "image_urls" 连接到列表 image_urls 的末尾，这是错误的。
        for url in image_urls:
            image_urls2 = "https://www.fantasyfactory.xyz" +'/' + url
            print(image_urls2)
            download_image(image_urls2, folder)

        #print(image_urls)




driver.quit()

def main():
    with ThreadPoolExecutor(max_workers=100) as executor:
        executor.submit(thread_page)

'''页面直接访问链接'''

def download_image(url, folder):
    response = requests.get(url)
    if response.status_code == 200:
        filename = url.split('/')[-1]
        filepath = os.path.join(folder, filename)
        with open(filepath, 'wb') as f:
            f.write(response.content)
        print(f"Downloaded: {filename}")
    else:
        print(f"Failed to download: {url}")

def scrape_images(url):
    response = requests.get(url)
    if response.status_code == 200:
        html = response.text
        image_urls = re.findall(r'<img src="(https://images2\.imgbox\.com/.*?)"', html)
        folder = 'test'  # 文件夹名称，可以根据需要修改
        if not os.path.exists(folder):
            os.makedirs(folder)
        for image_url in image_urls:
            download_image(image_url, folder)
    else:
        print(f"Failed to scrape images from: {url}")

base_url = "https://534798.xyz/e/action/ShowInfo.php?classid=1&id=27876&page="

for page in range(1, 85):
    url = base_url + str(page)
    scrape_images(url)




'''页面无法直接访问,需要chromdriver模拟'''



chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

# 指定ChromeDriver的路径
chromedriver_path =  r'C:\\Users\\21016.LAPTOP-KGP1GRG0\AppData\Local\Programs\Python\Python39\chromedriver.exe'

# 创建保存图片的文件夹
if not os.path.exists('tets'):
    os.mkdir('tets')

# 创建ChromeDriver的Service对象
service = Service(chromedriver_path)

# 创建Chrome无头浏览器对象
driver = webdriver.Chrome(service=service, options=chrome_options)

# 目标网址
url = "https://www.wnacg.com/photos-slide-aid-140784.html"

# 发送请求并获取网页内容
driver.get(url)
html = driver.page_source

# 使用BeautifulSoup解析网页
soup = BeautifulSoup(html, 'html.parser')

# 查找所有img标签
img_tags = soup.find_all('img')
for img_tag in img_tags:
    # 获取图片链接
    img_url = 'https:'+ img_tag['src']
    print(img_url)

    # 判断链接是否在指定域名下
    if 'https://img3.qy0.ru/' in img_url:

        # 下载图片
        img_data = requests.get(img_url).content


        # 提取图片名称
        img_name = img_url.split('/')[-1]

        # 保存图片到本地
        with open(f"tets/{img_name}", 'wb') as f:
            f.write(img_data)
            print(f"保存图片：{img_name}")

# 关闭浏览器
driver.quit()


