import requests

class Employee:
    """
    Description:
        Sample Employee Class for unitTesting
    """

    raise_amount = 15.7

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    @property
    def email(self):
        return "{}.{}@gmail.com".format(self.first, self.last)

    @property
    def full_name(self):
        return "{} {}".format(self.first, self.last)

    def hike(self):
        self.pay = int(self.pay * self.raise_amount)

    def monthly_schedule(self, month):
        response = requests.get(f"http://company.com/{self.last}/{month}")
        if response.ok:
            return response.text
        else:
            return "Bad Request!"
