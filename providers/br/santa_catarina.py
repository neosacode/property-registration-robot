import time
from settings import BR_SC_USERNAME, BR_SC_PASSWORD


class Provider:
    _login_url = 'https://central.centralrisc.com.br'
    _registration_url = 'https://central.centralrisc.com.br/meu/pedidoadd'
    _username = BR_SC_USERNAME
    _password = BR_SC_PASSWORD

    def __init__(self, es):
        self.es = es

    def login(self):
        self.es.driver.get(self._login_url)

        username = self.es.get_element('input[name=username]')
        password = self.es.get_element('input[name=password]')

        username.send_keys(self._username)
        password.send_keys(self._password)

        submit = self.es.get_element('button[type="submit"]')
        submit.click()

    def select_registration_city(self, city_name):
        self.es.driver.get(self._registration_url)
        self.es.select_option_by_text('#cidade > option', city_name)

    def request_registration(self, city_name, address):
        self.select_registration_city(city_name)
        registry_offices = self.es.get_elements('#serventia > option:not([value=""])')


        for i in range(0, len(registry_offices)):
            office = self.es.get_elements('#serventia > option:not([value=""])')[i]
            office.click()
            # Select the property registration option
            self.es.select_option_by_text('#tipocertidao > option:not([value=""])', 'Certidão de Inteiro Teor (matrícula atualizada)')
            time.sleep(2)
            # Select the develiry form as e-mail
            self.es.select_option_by_text('#envio > option:not([value=""])', 'E-mail')
            # Select the document type
            self.es.select_option_by_text('#tiponumero > option:not([value=""])', 'Matrícula')
            # Set document number to 00 for a search by address
            self.es.get_element('#numero').send_keys('00')
            # Set the address of the property
            self.es.get_element('#enderecoCompleto').send_keys(address)
            # Save the registration request
            self.es.get_element('#btn_salvar').click()


            # Stops the request when it does no have more registry offices
            if id(registry_offices[-1]) == id(office):
                break

            # Repeat the select city process again
            self.select_registration_city(city_name)
