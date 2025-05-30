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


async def search_recipes(language: str, ingredients: str, dietary_restrictions: str, culinary: str, tools: str) -> str:
    """Agent to search for recipes."""
    search_agent = Agent(
        name="search_agent",
        model=MODEL_ID,
        instruction="""
        You are a research assistant. Your job is to use google_search to find recipes based on the following user-provided inputs:
        Ingredients
        Dietary restrictions
        Culinary type (e.g., Italian, Indian)
        Specific tools or methods (e.g., air fryer, Instant Pot)
        Return exactly 5 relevant recipes if possible. If fewer than 5 high-quality matches are found, return only those that are relevant—never return more than 5.
        Format your response as a numbered list using emoji bullets:
        1️⃣, 2️⃣, 3️⃣, 4️⃣, 5️⃣
        Each recipe should include:
        The name of the recipe (bold or standout if formatting allows)
        A short, engaging description
        Respond in the selected language.
        """,
        description="The agent searches for recipes on Google.",
        tools=[google_search],
    )
    search_agent_entry = f"Selected Language: {language}.\nIngredients: {ingredients}.\nDietary restrictions: {dietary_restrictions}.\nCulinary: {culinary}.\nSpecific tools or methods: {tools}"
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
        You are a recipe agent. Based on a provided list of recipe options and a selected recipe, use google_search to find a detailed step-by-step version of the selected recipe.
        If multiple high-quality results are available, you may return up to two options. Each result should follow this exact structure:
        Start with the estimated cooking time, preceded by a clock emoji: ⏰
        Then list the ingredients and quantities
        Follow with the step-by-step instructions, using:
        Number emoji bullets (1️⃣, 2️⃣, 3️⃣...) for each step
        <br/> tags to separate each step
        Format clearly and consistently.
        Respond in the selected language.
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
        You are a drink specialist. Based on the provided recipe list and the selected recipe, use google_search to recommend up to 3 drinks that would pair well with the selected dish.
        For each drink, include:
        The name of the drink
        A short description explaining why it pairs well
        If applicable, specify whether it is alcoholic or non-alcoholic (e.g., wine, mocktail, juice)
        Do not start your response with conversational phrases like "Sure," "Okay," or "I can help with that."
        Simply begin the response directly with the list of drink pairings.
        Use the following format for each item:
        1️⃣ Drink Name (Type): Short description...
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
