import scrapy

class RedditSpider(scrapy.Spider):
	name='reddit'
	start_urls=['https://www.reddit.com']

	def parse(self,response):
		links=response.xpath('//img/@src')
		html=''

		for link in links:
		#Extracting the url text from the elements
			url = link.get()
		#check if the url contains an image extension
			if any(extension in url for extension in ['.jpg','.gif','.png']):
				html+='''
				<a href="{url}" target="_blank"> 
					<img src="{url}" height="33%" width="33%" />
				</a>
				'''.format(url=url)

				#open an Html file, save the results
				with open('frontpage.html','a') as page:
					page.write(html)
				#close the file
		page.close()

		