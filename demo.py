
'''�༶�ļ�'''

'''����߼�:1.����ҳ����������.
2.��������ļ�.��ȡҳ������,���з���.�������������ҳ��,ֱ�ӽ�����������
3.'''
#function���ö�ģ��
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

# ָ��ChromeDriver��·��
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
        print(b_url, "��ҳ�治����")



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
        #image_urls ʵ������һ���б��������ַ�����ʹ�� + "image_urls" ʵ�����ǽ��ַ��� "image_urls" ���ӵ��б� image_urls ��ĩβ�����Ǵ���ġ�
        for url in image_urls:
            image_urls2 = "https://www.fantasyfactory.xyz" +'/' + url
            print(image_urls2)
            download_image(image_urls2, folder)

        #print(image_urls)




driver.quit()

def main():
    with ThreadPoolExecutor(max_workers=100) as executor:
        executor.submit(thread_page)

'''ҳ��ֱ�ӷ�������'''

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
        folder = 'test'  # �ļ������ƣ����Ը�����Ҫ�޸�
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




'''ҳ���޷�ֱ�ӷ���,��Ҫchromdriverģ��'''



chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

# ָ��ChromeDriver��·��
chromedriver_path =  r'C:\\Users\\21016.LAPTOP-KGP1GRG0\AppData\Local\Programs\Python\Python39\chromedriver.exe'

# ��������ͼƬ���ļ���
if not os.path.exists('tets'):
    os.mkdir('tets')

# ����ChromeDriver��Service����
service = Service(chromedriver_path)

# ����Chrome��ͷ���������
driver = webdriver.Chrome(service=service, options=chrome_options)

# Ŀ����ַ
url = "https://www.wnacg.com/photos-slide-aid-140784.html"

# �������󲢻�ȡ��ҳ����
driver.get(url)
html = driver.page_source

# ʹ��BeautifulSoup������ҳ
soup = BeautifulSoup(html, 'html.parser')

# ��������img��ǩ
img_tags = soup.find_all('img')
for img_tag in img_tags:
    # ��ȡͼƬ����
    img_url = 'https:'+ img_tag['src']
    print(img_url)

    # �ж������Ƿ���ָ��������
    if 'https://img3.qy0.ru/' in img_url:

        # ����ͼƬ
        img_data = requests.get(img_url).content


        # ��ȡͼƬ����
        img_name = img_url.split('/')[-1]

        # ����ͼƬ������
        with open(f"tets/{img_name}", 'wb') as f:
            f.write(img_data)
            print(f"����ͼƬ��{img_name}")

# �ر������
driver.quit()


