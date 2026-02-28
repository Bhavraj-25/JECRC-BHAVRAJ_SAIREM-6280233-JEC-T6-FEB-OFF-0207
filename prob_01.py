class Solution:

    def city_revenue(self, orders):
        revenue_dict = {}
        ## Write your code here and don't forget to return value.
        for order in orders:
            city = order["city"]
            amt = order["amount"]

            if city in revenue_dict:
                revenue_dict[city] += amt
            else:
                revenue_dict[city] = amt
        high_rev_city = None
        max_rev = 0

        for city in revenue_dict:
            if revenue_dict[city] > max_rev:
                max_rev = revenue_dict[city]
                high_rev_city = city

        return revenue_dict, high_rev_city