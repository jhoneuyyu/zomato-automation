from pages.spot_page import Bookspot
from time import sleep


def test_book_spot(driver):
    bookspot = Bookspot(driver)
    bookspot.open_site()
    bookspot.click_on_spot()
    bookspot.enter_location("Brigade Road, Bangalore")
    bookspot.enter_spot_name("RCB Bar & Cafe")
    bookspot.click_button()
    bookspot.book_table()
    bookspot.click_date_dropdown()
    bookspot.click_gust_dropdown()
    bookspot.click_dinner_dropdown()
    bookspot.select_slot()
    bookspot.choose_offer()
    bookspot.click_cart()
    sleep(9)
    