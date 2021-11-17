import scrapy, json, re

1111
class AutoriaSpider(scrapy.Spider):
    name = "Autoria"
    start_urls = ['https://auto.ria.com/uk/legkovie/tesla/?page=' + str(p) for p in range(1, 99)]

    def parse(self, response, **kwargs):

        if response.status == 200:
            for carData in response.css("div.content"):
                data = {
                    "car_model": carData.css("span.blue.bold::text").get(),
                    "car_year": (carData.css("a.address").get())[-9:-5],
                    "car_mileage": (carData.css("li.item-char::text").get()).strip(),
                    "car_url": carData.css("a.address::attr(href)").get(),
                    "car_price_usd": carData.css("span.bold.green.size22::text").get() + "USD",
                    "car_price_uah": (" ".join(re.findall(r'\d+', (carData.css("span.i-block").get()))) + "UAH")
                }
                with open("savedCarsData1.json", 'a', encoding="utf-8") as f1:
                    json.dump(data, f1, ensure_ascii=False, indent=4)
