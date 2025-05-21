from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from agents import (
    translate_text,
    search_recipes,
    give_recipe,
    give_drink_recommendations
)

app = FastAPI()

# --- Request Models ---

class TranslateRequest(BaseModel):
    language: str
    text: str

class RecipeSearchRequest(BaseModel):
    language: str
    ingredients: str
    dietary_restrictions: str
    culinary: str

class RecipeDetailsRequest(BaseModel):
    language: str
    chosen_recipe: str
    recipe_list: str

# --- API Endpoints ---

@app.post("/translate")
async def translate_route(req: TranslateRequest):
    """
    Translates text using the Translator Agent.
    """
    try:
        result = await translate_text(req.language, req.text)
        return {"result": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Translation failed: {e}")


@app.post("/search-recipes")
async def search_recipes_route(req: RecipeSearchRequest):
    """
    Searches for recipes using the Search Agent.
    """
    try:
        result = await search_recipes(req.language, req.ingredients, req.dietary_restrictions, req.culinary)
        return {"result": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Recipe search failed: {e}")


@app.post("/give-recipe")
async def give_recipe_route(req: RecipeDetailsRequest):
    """
    Provides full recipe steps for a chosen recipe using the Recipe Agent.
    """
    try:
        result = await give_recipe(req.language, req.chosen_recipe, req.recipe_list)
        return {"result": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Fetching recipe details failed: {e}")


@app.post("/drink-recommendations")
async def drink_recommendations_route(req: RecipeDetailsRequest):
    """
    Provides drink recommendations for a chosen recipe using the Drink Agent.
    """
    try:
        result = await give_drink_recommendations(req.language, req.chosen_recipe, req.recipe_list)
        return {"result": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Drink recommendation failed: {e}")

