from Hackdavis.ab_recipes import Recipes

class Tasty(Recipes):
    def find_name(self):
        try:
            name = self.soup.find(class_='recipe-name extra-bold xs-mb05 md-mb1').text
            return name
        except:
            return "Not available"

    def find_ingredients(self):
        try:
            ing = self.soup.find_all(class_='ingredient xs-mb1 xs-mt0')
            ingredients = []
            str = ""
            if ing[0] == "":
                str = "Not available"
            for i in ing:
                ingredients.append(i.text.strip())
            for i in ingredients:
                str += i + '\n'
            return str
        except:
            return "Not available"

if __name__ == "__main__":
    t = Tasty("https://tasty.co/recipe/easy-sausage-pasta")
    print(t.find_ingredients())