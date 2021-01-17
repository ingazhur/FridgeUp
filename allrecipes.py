from Hackdavis.ab_recipes import Recipes

class Allrecipes(Recipes):

    def find_name(self):
        try:
            name = self.soup.find(class_='headline heading-content').text
            return name
        except:
            return "Not available"

    def find_ingredients(self):
        try:
            ing = self.soup.find_all(class_='ingredients-item-name')
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

    def find_image(self):
        try:
            img = self.soup.find_all('div', {'class': 'inner-container js-inner-container  image-overlay'})
            print(img)
        except:
            return "Not available"

    def find_preptime(self):
        pass


if __name__ == "__main__":
    a = Allrecipes('https://www.allrecipes.com/recipe/34413/paella/?internalSource=hub%20recipe&referringContentType=Search&clickId=cardslot%202')
    print(a.find_image())





