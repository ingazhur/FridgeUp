from Hackdavis.ab_recipes import Recipes

# name, type, ingredients, url
class Epicurious(Recipes):

    def find_name(self):
        try:
            name = self.soup.find('h1', {'itemprop': 'name'}).text
            return name
        except:
            return "Not available"

    def find_ingredients(self):
        try:
            ing = self.soup.find_all(class_='ingredient')
            ingredients = []
            str = ""
            if ing[0] == "":
                str = "Not available"
            for i in ing:
                ingredients.append(i.text)
            for i in ingredients:
                str += i + '\n'
            return str
        except:
            return "Not available"

if __name__ == "__main__":
    e = Epicurious('https://www.epicurious.com/recipes/food/views/mint-cookies-and-cream-cookie-pie-tosi')
    print(e.find_name())