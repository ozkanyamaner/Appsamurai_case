import requests

url_1 = "https://prod-storyly-media.s3.eu-west-1.amazonaws.com/test-scenarios/sample_1.json"
url_2 = "https://prod-storyly-media.s3.eu-west-1.amazonaws.com/test-scenarios/sample_2.json"
url_3 = "https://prod-storyly-media.s3.eu-west-1.amazonaws.com/test-scenarios/sample_3.json"

r_1 = requests.get(url_1)
r_2 = requests.get(url_2)
r_3 = requests.get(url_3)

#Creating Python dictionaries from json files
data_1 = r_1.json()
data_2 = r_2.json()
data_3 = r_3.json()

# A function to calculate the total price using the dictionary:
def calculateCost(item):
    #Checks whether the item is a terminal item or the item has a list of sub-items
    if 'price' in item.keys(): # Terminal item case (base case of recursion)
        return item['count'] * item['price']
    else: # Non-terminal item case
        sum = 0
        for sub_item in item['items']:
            sum += (calculateCost(sub_item))
        return sum * item['count']

print("Total costs for the given json files:")
print(calculateCost(data_1))
print(calculateCost(data_2))
print(calculateCost(data_3))



