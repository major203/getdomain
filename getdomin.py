#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
import requests,re,time,sys
 

#http请求发送函数
def send_http(url,data,headers):
    while True:     #一直循环，知道访问站点成功
	    try:
	        r=requests.post(url,data,headers)  
	        html=r.text.encode('utf-8')
	        break
	    except requests.exceptions.ConnectionError:
	        print('ConnectionError -- please wait 3 seconds')
	        time.sleep(3)
	    except requests.exceptions.ChunkedEncodingError:
	        print('ChunkedEncodingError -- please wait 3 seconds')
	        time.sleep(3)    
	    except:
	        print('Unfortunitely -- An Unknow Error Happened, Please wait 3 seconds')
	        time.sleep(3)
    return html 


def main(domain,page):
	url = 'https://tool.chinaz.com/subdomain?domain=%s&page=%s' % (domain,page)
	headers = {
	'User-Agent':'hjy_test_post;Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
	}
	data=''
	html = send_http(url,data,headers)
	domain_split=domain.split('.')
	pattern = re.compile(r'[0-9a-zA-Z]+\.'+domain_split[0]+'\.'+domain_split[1])  # 查找数字
	result1 = pattern.findall(html)
	print result1


if __name__ == '__main__':
	main(sys.argv[1],sys.argv[2])
	

