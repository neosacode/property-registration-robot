from unicodedata import normalize


class EasySelenium:
    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(10)

    def get_element(self, css_selector):
        return self.driver.find_element_by_css_selector(css_selector)

    def get_elements(self, css_selector):
        return self.driver.find_elements_by_css_selector(css_selector)

    def unaccent(self, text, lower=True):
        text = normalize('NFKD', text).encode('ASCII', 'ignore').decode('utf8')
        return text.lower() if lower else text

    def select_option_by_text(self, css_selector, text):
        text_unaccent = self.unaccent(text)
        options = self.get_elements(css_selector)

        for option in options:
            if text_unaccent == self.unaccent(option.text):
                option.click()
                return option