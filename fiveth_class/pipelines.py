from scrapy.contrib.pipeline.images import ImagesPipeline

# change the file name to real name
class MyImagesPipline(ImagesPipeline):
    def file_path(self, request, response=None, info=None):
        image_guid = request.url.split('/')[-1]
        return 'full/%s' % (image_guid)
