from flask import Flask, render_template, request
import requests
import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

app = Flask(__name__)

# Gemini config
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel('gemini-1.5-flash')

COCKTAILDB_BASE_URL = "https://www.thecocktaildb.com/api/json/v1/1/"
MEALDB_BASE_URL = "https://www.themealdb.com/api/json/v1/1/"


# ================================
# Main Landing Page
# ================================
@app.route("/", methods=["GET"])
def home():
    return render_template("home.html")

# ================================
# ShreySpirits ROUTE (Cocktails)
# ================================

@app.route("/cocktails", methods=["GET", "POST"])
def cocktails():
    cocktail_info = None
    ai_response = None

    if request.method == "POST":
        ingredients_input = request.form.get("ingredients")
        ingredients = [i.strip() for i in ingredients_input.split(",") if i.strip()]
        
        possible_cocktails = {}

        for ingredient in ingredients:
            url = f"{COCKTAILDB_BASE_URL}filter.php?i={ingredient}"
            res = requests.get(url)
            data = res.json()

            if data["drinks"]:
                for drink in data["drinks"]:
                    drink_id = drink["idDrink"]
                    if drink_id not in possible_cocktails:
                        possible_cocktails[drink_id] = {
                            "count": 1,
                            "name": drink["strDrink"],
                            "image": drink["strDrinkThumb"]
                        }
                    else:
                        possible_cocktails[drink_id]["count"] += 1

        if possible_cocktails:
            # Pick the drink with the most matching ingredients
            best_match = max(possible_cocktails.values(), key=lambda x: x["count"])

            # Get detailed instructions
            lookup_url = f"{COCKTAILDB_BASE_URL}search.php?s={best_match['name']}"
            drink_details = requests.get(lookup_url).json()["drinks"][0]

            instructions = drink_details["strInstructions"]

            cocktail_info = {
                "name": best_match["name"],
                "image": best_match["image"],
                "instructions": instructions
            }

            # Gemini: make it fun
            prompt = (
                f"You are an expert AI Bartender. The user has these ingredients: {', '.join(ingredients)}. "
                f"The best cocktail match is '{best_match['name']}'. "
                f"ONLY use these ingredients in your explanation. Do NOT invent or add any new ingredients, fruits, or flavors. "
                f"There are no official cocktails found for this combination. "
                f"Invent a realistic and delicious cocktail recipe that uses ONLY these ingredients — "
                f"Return your entire answer as clean, valid HTML only. Use proper headings (h2, h3), lists (ul, ol), and paragraphs to structure it well. "
                f"Do NOT wrap it in backticks, triple backticks, markdown code fences, or markdown formatting. "
                f"Output ONLY the raw HTML for direct rendering. "
                f"Include a short fun description of the cocktail, its instructions (based on the official recipe if you want), variations that stay within the given ingredients only, "
                f"and a fun serving tip. "
                f"Do NOT add any disclaimers, comments, or explanations. "
                f"IMPORTANT: Before sending your reply, RECHECK that your answer is ONLY valid HTML with NO backticks, NO code fences, NO markdown. "
                f"If you see any backticks — remove them. Output ONLY the clean HTML."
                f"Remove ```html and ``` when you give output."
            )

            response = model.generate_content(prompt)
            ai_response = response.text

        

        else:
            ai_response = "Sorry, I couldn't find any matching cocktails with those ingredients."

    return render_template("cocktails.html", cocktail=cocktail_info, ai_response=ai_response)


# ====================================
# ShreyMocktails ROUTE (Mocktails)
# ====================================
@app.route("/mocktails", methods=["GET", "POST"])
def mocktails():
    mocktail_info = None
    ai_response = None

    if request.method == "POST":
        ingredients_input = request.form.get("ingredients")
        ingredients = [i.strip() for i in ingredients_input.split(",") if i.strip()]

        # Use Gemini to INVENT a mocktail — no alcohol
        prompt = (
            f"You are an expert AI Mocktail Mixologist. The user has these ingredients: {', '.join(ingredients)}. "
            f"ONLY use these ingredients in your explanation. Do NOT invent or add any new ingredients, fruits, or flavors. "
            f"Invent a realistic and delicious NON-ALCOHOLIC mocktail recipe that uses ONLY these ingredients. "
            f"Return your entire answer as clean, valid HTML only. "
            f"Use proper headings (h2, h3), lists (ul, ol), and paragraphs to structure it well. "
            f"Do NOT wrap it in backticks, triple backticks, markdown code fences, or markdown formatting. "
            f"Output ONLY the raw HTML for direct rendering. "
            f"Include a short fun description of the mocktail, its step-by-step instructions, variations that stay within the given ingredients only, "
            f"and a fun serving tip. "
            f"Do NOT add any disclaimers, comments, or explanations. "
            f"IMPORTANT: Before sending your reply, RECHECK that your answer is ONLY valid HTML with NO backticks, NO code fences, NO markdown. "
            f"If you see any backticks — remove them. Output ONLY the clean HTML."
            f"Remove ```html and ``` when you give output."
        )

        response = model.generate_content(prompt)
        ai_response = response.text

    return render_template("mocktails.html", mocktail=mocktail_info, ai_response=ai_response)


# ====================================
# ShreyAppetizers ROUTE (Appetizers)
# ====================================
@app.route("/appetizers", methods=["GET", "POST"])
def appetizers():
    ai_response = None

    if request.method == "POST":
        drink_name = request.form.get("drink_name")
        extra_ingredients = request.form.get("extra_ingredients")

        prompt = (
            f"You are an expert gourmet chef. The user is drinking: '{drink_name}'. "
            f"ONLY use this drink and any optional ingredients choices: '{extra_ingredients}'. "
            f"Do NOT invent or add any new core ingredients that were not mentioned. "
            f"Your task: suggest ONE realistic, delicious appetizer or snack recipe that pairs perfectly with this drink. "
            f"Keep it simple, classy, and plausible. "
            f"Return your entire answer as clean, valid HTML only. "
            f"Use proper headings (h2, h3), lists (ul, ol), and paragraphs to structure it well. "
            f"Do NOT wrap it in backticks, triple backticks, markdown code fences, or markdown formatting. "
            f"Output ONLY the raw HTML for direct rendering — no disclaimers, no explanations, no markdown. "
            f"Include a short fun description, a clear ingredient list (if needed), step-by-step instructions, "
            f"and a short serving tip. "
            f"IMPORTANT: Before sending your reply, RECHECK that your answer is ONLY valid HTML with NO backticks, "
            f"NO code fences, NO markdown. If you see any backticks — remove them."
            f"Remove ```html and ``` when you give output."
        )

        response = model.generate_content(prompt)
        ai_response = response.text

    return render_template("appetizers.html", ai_response=ai_response)



if __name__ == "__main__":
    app.run(debug=True)
