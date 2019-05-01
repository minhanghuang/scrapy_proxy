[TOC]


# 代理池ip爬取



## #0 GitHub

```
https://github.com/Coxhuang/scrapy_proxy
```

## #1 环境

```
Python3.7.3
Scrapy==1.6.0
```

## #2 需求

- 爬取ip代理网站免费的ip
- 把不能用的ip过滤掉
- 目标站点 https://www.xicidaili.com/nt/


## #3 准备

### #3.1 新建一个scrapy项目

```
scrapy startproject proxy_ips
```

```
.
└── proxy_ips
    ├── proxy_ips
    │   ├── __init__.py
    │   ├── items.py
    │   ├── middlewares.py
    │   ├── pipelines.py
    │   ├── settings.py
    │   └── spiders
    │       ├── __init__.py
    └── scrapy.cfg
```

### #3.2 新建爬虫(在spiders目录下)

```
scrapy genspider ips "xicidaili.com"
```

## #4 开始

### #4.1 测试目标站点反爬机制

- 裸跑


```
# -*- coding: utf-8 -*-
import scrapy
class IpsSpider(scrapy.Spider):
    name = 'ips'
    allowed_domains = ['xicidaili.com']
    start_urls = (
        'https://www.xicidaili.com/nt/',
    )
    def parse(self, response):
        print(response.xpath('//*[@id="ip_list"]/tbody/tr[2]/td[2]').extract())
```

```
scrapy crawl ips --nolog
```


> 没有拿到数据

![20190429133316-image.png](https://raw.githubusercontent.com/Coxhuang/yosoro/master/20190429133316-image.png)


- 加User-Agent


settings.py

```
MY_USER_AGENT = [
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
    "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
    "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
    "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
    "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
    "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/2.0 Safari/536.11",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; LBBROWSER)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E; LBBROWSER)",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 LBBROWSER",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; 360SE)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
    "Mozilla/5.0 (iPad; U; CPU OS 4_2_1 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0b13pre) Gecko/20110307 Firefox/4.0b13pre",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:16.0) Gecko/20100101 Firefox/16.0",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",
    "Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
    ]
```


```
DOWNLOADER_MIDDLEWARES = {
   # 'proxy_ips.middlewares.ProxyIpsDownloaderMiddleware': 543,
    'scrapy.downloadermiddleware.useragent.UserAgentMiddleware': None,
    'proxy_ips.middlewares.MyUserAgentMiddleware': 400,
}
```

middlewares.py


```
import random
from scrapy.downloadermiddlewares.useragent import UserAgentMiddleware

class MyUserAgentMiddleware(UserAgentMiddleware):
    '''
    设置User-Agent
    '''

    def __init__(self, user_agent):
        self.user_agent = user_agent

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            user_agent=crawler.settings.get('MY_USER_AGENT')
        )

    def process_request(self, request, spider):
        agent = random.choice(self.user_agent)
        request.headers['User-Agent'] = agent

```

ips.py

```
def parse(self, response):
    print(response.xpath('/html/head/title/text()').extract_first())
    print(response.xpath('//*[@id="ip_list"]/tbody/tr[6]/td[2]/text()').extract_first())
```

![20190430175647-image.png](https://raw.githubusercontent.com/Coxhuang/yosoro/master/20190430175647-image.png)


> 通过xpath能获取网页的数据,但是就是拿不到tbody表格里面的数据 😡



- 在xpath时,把tbody去掉


```
def parse(self, response):
    print(response.xpath('/html/head/title/text()').extract_first())
    print(response.xpath('//*[@id="ip_list"]/tr[6]/td[2]/text()').extract_first())
```
![20190429162502-image.png](https://raw.githubusercontent.com/Coxhuang/yosoro/master/20190429162502-image.png)



### #4.2 获取下一页数据

> 分页url分析


```
https://www.xicidaili.com/nn/1
https://www.xicidaili.com/nn/2
...

```


```
def parse(self, response):
    for page in range(1, 3): # 获取1-2页数据
        url_next = "https://www.xicidaili.com/nn/{}/".format(page)
        yield scrapy.Request(url_next, callback=self.parse_response_next)
```

![20190430192308-image.png](https://raw.githubusercontent.com/Coxhuang/yosoro/master/20190430192308-image.png)



```
def parse_response_next(self,response):

    for tr_line in response.xpath('//*[@id="ip_list"]/tr'):
        ip = tr_line.xpath('td[2]/text()').extract_first()
        port = tr_line.xpath('td[3]/text()').extract_first()
        http = str(ip) + ":" + str(port)
        print(http)
    return None
```

![20190430192659-image.png](https://raw.githubusercontent.com/Coxhuang/yosoro/master/20190430192659-image.png)


> 测试ip是否可用

```
def __check_ip(self,http):
    """
    测试ip可用性
    :param http: ip:port
    :return: None
    """
    proxies = {
        "http": "http://{}".format(http),
        "https": "http://{}".format(http),
    }
    try:
        response = requests.get(
            url,
            headers=headers,
            proxies=proxies,
            timeout=5, # 请求超时时间超过5秒,认为该ip用不了
        )
        if int(response.status_code) == 200:
            print(http)
            return True
    except:
        pass

    return False
```

![20190430195907-image.png](https://raw.githubusercontent.com/Coxhuang/yosoro/master/20190430195907-image.png)

> 把可用的ip写入数据库(这里用MongoDB)

**一定要确保MongoDB可以正常使用**

items.py

```
import scrapy
class ProxyIpsItem(scrapy.Item):
    http = scrapy.Field()
    ip = scrapy.Field()
    port = scrapy.Field()
    is_active = scrapy.Field()
    check_time = scrapy.Field()
```



pipelines.py


```
import pymongo
class ProxyIpsPipeline(object):
    
    def __init__(self):
        host = "127.0.0.1" # MongoDB地址
        port = 27017 # 端口号
        dbName = "proxy" # 数据库名
        client = pymongo.MongoClient(host=host, port=port)
        tdb = client[dbName]
        self.post = tdb["proxytable"] # 表名

    def process_item(self, item, spider):
        bookInfo = dict(item)
        self.post.insert(bookInfo)
        return item
```

ips.py

```
def parse_response_next(self,response):

    for tr_line in response.xpath('//*[@id="ip_list"]/tr'):

        ip = tr_line.xpath('td[2]/text()').extract_first()
        port = tr_line.xpath('td[3]/text()').extract_first()
        http = str(ip) + ":" + str(port)
        ret = self.__check_ip(http=http)
        if ret:
            item = ProxyIpsItem()
            item["http"] = http
            item["ip"] = str(ip)
            item["port"] = str(port)
            item["is_active"] = True
            item["check_time"] = datetime.now()

            yield item
```

settings.py

```
ITEM_PIPELINES = {
   'proxy_ips.pipelines.ProxyIpsPipeline': 300,
}
```


![20190430214641-image.png](https://raw.githubusercontent.com/Coxhuang/yosoro/master/20190430214641-image.png)













