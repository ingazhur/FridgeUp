from Hackdavis.ab_recipes import Recipes

# name, type, ingredients, url
class Simplyrecipes(Recipes):

    def find_name(self):
        try:
            name = self.soup.find(class_='entry-title').text
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
    s = Simplyrecipes('https://www.simplyrecipes.com/recipes/mexican_red_chili_sauce/')
    print(s.find_ingredients())