
from scrapy.conf import settings
import os
import time


class ProxyMiddleware(object):

    def process_request(self, request, spider):
        request.meta['proxy'] = settings.get('HTTP_PROXY')

        # refresh ip
        os.system("""(echo authenticate '"mypassword"'; echo signal newnym; echo \
                   quit) | nc localhost 9051""")
        # time.sleep(2)