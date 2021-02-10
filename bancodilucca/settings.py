BOT_NAME = 'bancodilucca'

SPIDER_MODULES = ['bancodilucca.spiders']
NEWSPIDER_MODULE = 'bancodilucca.spiders'
FEED_EXPORT_ENCODING = 'utf-8'
LOG_LEVEL = 'ERROR'
DOWNLOAD_DELAY = 0

ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {
	'bancodilucca.pipelines.BancodiluccaPipeline': 100,

}