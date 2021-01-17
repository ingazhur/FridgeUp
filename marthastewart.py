from Hackdavis.ab_recipes import Recipes

# name, type, ingredients, url
class Marthastewart(Recipes):

    def find_name(self):
        try:
            name = self.soup.find(class_='headline heading-content').text
            return name
        except:
            return "Not available"

    def find_ingredients(self):
        try:
            ing = self.soup.find_all(class_='ingredients-item-name')
            str = ""
            if ing[0] == "":
                str = "Not available"
            ingredients = []
            for i in ing:
                ingredients.append(i.text.strip())
            str = ""
            for i in ingredients:
                str += i + '\n'
            return str
        except:
            return "Not available"

if __name__ == "__main__":
    m = Marthastewart('https://www.marthastewart.com/7871641/mark-consuelos-kelly-ripa-secret-to-marriage')
    print(m.find_ingredients())