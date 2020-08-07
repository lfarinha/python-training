class Data:

    def __init__(self, uid, province_state, country_region, date, confirmed_cases, death):
        self._uid = uid
        self._province_state = province_state
        self._country_region = country_region
        self._date = date
        self._confirmed_cases = confirmed_cases
        self._death = death

    def get_uid(self):
        return self._uid

    def get_province_state(self):
        return self._province_state

    def get_country_region(self):
        return self._country_region

    def get_date(self):
        return self._date

    def get_confirmed_cases(self):
        return self._confirmed_cases

    def get_death(self):
        return self._death
