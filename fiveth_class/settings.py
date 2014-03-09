BOT_NAME = 'fiveth_class'

SPIDER_MODULES = ['fiveth_class.spiders']
NEWSPIDER_MODULE = 'fiveth_class.spiders'
ITEM_PIPELINES = ['fiveth_class.pipelines.MyImagesPipline']
# download path
IMAGES_STORE = 'pic_down'
