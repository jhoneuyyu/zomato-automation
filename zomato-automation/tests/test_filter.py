from pages.filter_page import FilterPage


def test_apply_filter(driver):
    filter=FilterPage(driver)
    filter._open_site()
    filter.click_on_filter()
    filter.click_on_sort()
    filter.high_to_low()
    filter.click_on_apply()
    filter.click_on_dining()
    filter.click_on_filter()
    filter.click_on_cuisis()
    filter.input_cuisines("Indian")
    filter.click_on_north_indian()
    filter.cuisines_filter_click()
    filter.click_on_rating()


    