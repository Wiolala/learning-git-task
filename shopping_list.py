shopping_list = {
    "piekarnia" : ["chleb", "bułki", "pączki"],
    "warzywniak" : ["marchew", "seler", "rukola"]
}
for shop, things in shopping_list.items():
    print("Idę do: " + shop.capitalize() + ", kupuję tu: " + str(things)) 

number_of_products = (len(shopping_list["piekarnia"]) + len(shopping_list["warzywniak"]))
print("W sumie kupuję " +str(number_of_products) + " produktów.")