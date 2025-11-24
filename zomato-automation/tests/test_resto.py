from pages.resto_page import Searchresto
from time import sleep


def test_search_restaurant(driver):
    """
    Tests the restaurant search and selection functionality.
    """
    restorent = Searchresto(driver)
    restorent.open_site()
    restorent.select_location("Kengeri Upanagara, Bengaluru, India")
    restorent.search_hotel("Hotel Gowdru Mane")
    sleep(2)
    restorent.select_hotel()


    
