from typing import List

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        N = len(recipes)
        recipesOk = [None]*N
        recipesIndexs = dict(zip(recipes,range(N)))
        suppliesSet = set(supplies)
        def helper(recipe_i, inprocessing = []):
            nonlocal recipesOk, recipesIndexs, suppliesSet
            if(recipe_i in inprocessing):
                return False
            if recipesOk[recipe_i] is not None:
                return recipesOk[recipe_i]
            required_ingredients = ingredients[recipe_i]
            canCreat = True 
            for ingredient in required_ingredients:
                if ingredient in suppliesSet:
                    continue
                else:
                    if ingredient in recipesIndexs:
                        if (helper (recipesIndexs[ingredient], [*inprocessing, recipe_i])):
                            continue
                        else:
                            canCreat = False
                            break

                    else:
                        canCreat = False
                        break
            recipesOk[recipe_i] = canCreat
            return canCreat
        ret = []
        for i in range(N):
            if helper(i):
                ret.append(recipes[i])
        return ret


s = Solution()
# print(s.findAllRecipes(recipes = ["bread"], ingredients = [["yeast","flour"]], supplies = ["yeast","flour","corn"]))
# print(s.findAllRecipes(recipes = ["bread","sandwich"], ingredients = [["yeast","flour"],["bread","meat"]], supplies = ["yeast","flour","meat"]))

print(s.findAllRecipes(recipes = ["ju","fzjnm","x","e","zpmcz","h","q"], 
ingredients = [["d"],["hveml","f","cpivl"],["cpivl","zpmcz","h","e","fzjnm","ju"],["cpivl","hveml","zpmcz","ju","h"],["h","fzjnm","e","q","x"],["d","hveml","cpivl","q","zpmcz","ju","e","x"],["f","hveml","cpivl"]], 
supplies = ["f","hveml","cpivl","d"]))