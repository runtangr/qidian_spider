# qidian_spider
    此项目是基于scrapy,redis,tor，mongodb,graphite，实现的一个分布式网络爬虫。

    使用scrapy-redis实现分布式，tor实现ip池，mongodb存储数据，graphite显示爬虫状态。

# 功能

    一个对https://www.qidian.com 网站的spider，把网站的书名、作者、书籍封面图片地址、书籍简介、网址链接、书籍评价、评论人数下载到本地mongodb。

# 爬虫被禁的策略
    1. 禁用cookie
    2. 实现了一个download middleware，不停的变user-aget
    3. 实现了一个可以每分钟变换ip的tor（国内需要tor前置代理）
    4. selenium获取动态加载数据

# 日志
    log信息默认写到文件中logs/scrapy.log

# 安装
    scrapy
    graphite（可以采用docker）
    redis
    mongodb
    tor
    polipo
    virtualenv

# 使用方法
    1. source venv/bin/activate
    2. pip install -r requirements.txt
    3. 启动tor，polipo
    4. 修改setting.py polipo端口
    5. scrapy crawl qidian

# graphite

# log

