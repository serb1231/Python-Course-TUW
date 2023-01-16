from multiprocessing.sharedctypes import Value
from typing import Any


class Recipe(object):
    def __init__(self, name = "", dictionary = dict([]), steps = []):
        self.name = name
        self.dictionary = dictionary
        self.steps = steps
    
    def list_ingredients(self):
        stringus = ""
        for key,value in self.dictionary.items():
            stringus =stringus + str(key) + "\t" + str(value) + "\n"
        return stringus
    
    def list_steps(self):
        listus = self.steps
        listus_finalus = []
        numarare = 1
        ana = ""
        for e in listus:
            ana += str(numarare) + ". " + e + '\n'
            listus_finalus.append(ana)
            numarare+=1
        return ana
    def __len__(self):
        return len(self.dictionary)



class ComplexRecipe(Recipe):
    def __init__(self, name = "", dictionary = dict([]), steps = [], recipes = any):
        self.name = name
        self.dictionary = dictionary
        self.steps = steps
        self.recipes = recipes
    
    def list_ingredients(self):
        total_ingred = ""
        for e in self.recipes:
            total_ingred+=e.name + "\n"
            total_ingred+=e.list_ingredients()
        # curent = Recipe(self.name, self.dictionary, self.steps)
        # total_ingred+='\n'
        # total_ingred+= curent.list_ingredients()
        return total_ingred

    def list_steps(self):
        total_steps = ""
        for e in self.recipes:
            total_steps+=e.name + "\n"
            total_steps+=e.list_steps()
        curent = Recipe(self.name, self.dictionary, self.steps)
        total_steps+='\n'
        total_steps+= curent.list_steps()
        return total_steps

    def __len__(self):
        a = len(self.dictionary)
        for e in self.recipes:
            a+=len(e.dictionary)
        return a

class Cookbook(ComplexRecipe):
    def __init__(self, name = "", recipe_name = "", recipes = []):
        self.name = name
        self.recipe_name = recipe_name
        self.recipes = recipes

    def __str__(self):
        etc = ""
        etc +=self.name
        etc+="\n"
        etc +=self.recipe_name
        etc+="\n"
        for e in self.recipes:
            etc +=e.name
            etc+="\n"
            etc +=e.list_ingredients()
            etc+="\n"
            etc +=e.list_steps()
            etc+="\n"
        return etc
    


ingredients = {"flour": 1, "egg": 2}
steps = ["Mix the ingredients well", "Roll the dough thinly"]
pasta = Recipe("pasta", ingredients, steps)
assert 'flour\t1\negg\t2' in pasta.list_ingredients()
assert pasta.list_steps().startswith("1.")
assert len(pasta) == 2

ragout_ingredients = {"meat": 1, "celery": 2, "carot": 3, "tomato paste": 1, "spices": 2}
ragout_steps = ["Cook the vegetables with spices", "Add the meat and let it brown", "Add tomato paste and cook."]
ragout = Recipe("ragout", ragout_ingredients, ragout_steps)
besamel_ingredients = {"flour": 3, "butter": 3, "milk": 5, "nutmeg": 1}
besamel_steps = ["Melt the butter", "Add flour and nutmeg", "Slowly stir in the milk until incorporated"]
besamel = Recipe("besamel", besamel_ingredients, besamel_steps)

lasagne_ingredients = {"parmesan": 3}
lasagne_steps = ["Layer ragout, besamel, and cooked pasta", "Top it off with parmesan", "Cook in the oven"]
lasagne = ComplexRecipe("lasagne", lasagne_ingredients, lasagne_steps, recipes=[pasta, ragout, besamel])

assert "pasta" in lasagne.list_ingredients()
#print(lasagne.list_steps())
assert lasagne.list_steps().count("1") == 4
assert len(lasagne) == 12

cookbook = Cookbook("John Doe", "Big Lasagne Book", [pasta,lasagne])
print(str(cookbook))
print(str(cookbook).count("pasta"))
assert str(cookbook).count("pasta") == 4