BOT_NAME = 'ubluk'
SPIDER_MODULES = ['ubluk.spiders']
NEWSPIDER_MODULE = 'ubluk.spiders'
ROBOTSTXT_OBEY = True
LOG_LEVEL = 'WARNING'
USER_AGENT = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:66.0) Gecko/20100101 Firefox/66.0',
ITEM_PIPELINES = {
   'ubluk.pipelines.DatabasePipeline': 300,
}
