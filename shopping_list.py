shopping_list = {
    "piekarnia" : ["chleb", "bułki", "pączki"],
    "warzywniak" : ["marchew", "seler", "rukola"]
}
for shop, things in shopping_list.items():
    print("Idę do: " + shop.capitalize() + ", kupuję tu: " + str(things)) 