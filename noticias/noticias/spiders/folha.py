import scrapy
from ..items import NoticiasItem


class CNNSpider(scrapy.Spider):
    name = 'folha'
    allowed_domains = ['www1.folha.uol.com.br']
    start_urls = ['https://www1.folha.uol.com.br/ultimas-noticias/']

    def parse(self, response):  

        items = NoticiasItem() 

        all_div_noticias = response.css(".c-headline--newslist")     

        for noticias in all_div_noticias:
            title = noticias.css('.c-headline__title::text').extract(),
            subtitulo = noticias.css('.c-headline__standfirst::text').extract(),
            url = noticias.css('.c-image-aspect-ratio__link::attr(href)').extract(),
            data = noticias.css('.c-headline__dateline::text').extract(),
            image_url = noticias.css('.c-image-aspect-ratio__image::attr(src)').extract(),       
            
           
            items['title'] = title
            items['subtitulo'] = subtitulo
            items['url'] = url
            items['data'] = data
            items['image_url'] = image_url
            
   
            
            yield items