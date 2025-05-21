from google.adk.agents import Agent
from google.adk.tools import google_search
from config import MODEL_ID 
from utils import call_agent

async def translate_text(language: str, text: str) -> str:
    """Agent to translate texts."""
    translator_agent = Agent(
        name="translator_agent",
        model=MODEL_ID,
        instruction="""
        You are a highly accurate translator agent.
        Your task is to translate the given text *exactly* into the specified language, preserving any formatting or special characters.
        Do not add any extra commentary or explanations. Do not add extra new lines (\n). Just return the translated text.
        """,
        description="The agent translates texts with high accuracy.",
        tools=[]
    )
    message_text = f"Translate the following text into {language}: '{text}'"
    response = await call_agent(translator_agent, message_text)
    if not response:
        return f"Sorry, the translation agent could not translate '{text}' to {language}. The model might have returned an empty response."
    return response


async def search_recipes(language: str, ingredients: str, dietary_restrictions: str, culinary: str) -> str:
    """Agent to search for recipes."""
    search_agent = Agent(
        name="search_agent",
        model=MODEL_ID,
        instruction="""
        You are a research assistant. Your role is to use google_search to find recipes based on ingredients,
        dietary restrictions and culinary type.
        Get a max of 5 relevant recipes based on the requirements.
        Please respond in the selected language.
        """,
        description="The agent searches for recipes on Google.",
        tools=[google_search],
    )
    search_agent_entry = f"Selected Language: {language}.\nIngredients: {ingredients}.\nDietary restrictions: {dietary_restrictions}.\nCulinary: {culinary}."
    response = await call_agent(search_agent, search_agent_entry)
    if not response:
        return f"Sorry, the search agent could not find recipes for your input. Please try different ingredients or criteria."
    return response


async def give_recipe(language: str, chosen_recipe: str, recipe_list: str) -> str:
    """Agent to return full recipe steps."""
    recipe_agent = Agent(
        name="recipe_agent",
        model=MODEL_ID,
        instruction="""
        You are a recipe agent. Based on the recipe list, and the chosen recipe.
        You should use google_search to return the step by step recipe for the chosen recipe.
        If you can find, also give the estimated time it takes for cooking this recipe.
        Please respond in the selected language.
        """,
        description="The agent gives the steps to the chosen recipe.",
        tools=[google_search]
    )
    recipe_agent_entry = f"Selected language: {language}.\nChosen recipe:{chosen_recipe}.\nRecipe List: {recipe_list}"
    response = await call_agent(recipe_agent, recipe_agent_entry)
    if not response:
        return f"Sorry, the recipe agent could not retrieve steps for '{chosen_recipe}'. It might not be found or the model returned an empty response."
    return response


async def give_drink_recommendations(language: str, chosen_recipe: str, recipe_list: str) -> str:
    """Agent to give drink recommendations."""
    drink_agent = Agent(
        name="drink_agent",
        model=MODEL_ID,
        instruction="""
        You are a drink specialist. Based on the recipe list, and the chosen recipe.
        You should use google_search to give a recommendation of a drink that would be a perfect match with the chosen recipe.
        Give a max of 3 drink options.
        Please respond in the selected language.
        """,
        description="The agent gives you a recommendation of drinks to match the recipe.",
        tools=[google_search]
    )
    drink_agent_entry = f"Selected language: {language}.\nChosen recipe:{chosen_recipe}.\nRecipe List: {recipe_list}"
    response = await call_agent(drink_agent, drink_agent_entry)
    if not response:
        return f"Sorry, the drink agent could not find recommendations for '{chosen_recipe}'. Please try again."
    return response
