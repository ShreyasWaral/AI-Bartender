# Shrey’s Mixology Hub 🍸🍹🍽️

**Your ultimate party companion — spirited or sober — with the perfect snack on the side.**

---

## ✨ What is it?

**Shrey’s Mixology Hub** is a sleek, AI-powered web app that lets you:
- 🥃 **ShreySpirits**: Get classic and AI-enhanced cocktail ideas based on your pantry.
- 🧃 **ShreyMocktails**: Create refreshing non-alcoholic drinks with only what you have.
- 🍢 **ShreyAppetizers**: Find delicious appetizers that pair perfectly with your drink.

---

## ⚙️ How does it work?

- Uses **TheCocktailDB**  API for real drink data.
- Gemini AI invents realistic, fun recipes if needed.
- Fully custom UI themes for each section.
- Built with **Python Flask**, HTML, CSS & JS.

---

## 📂 Project Structure

```plaintext
ShreysMixologyHub/
├── app.py
├── requirements.txt
├── templates/
├── static/
├── .gitignore
└── .env (ignored)


## 🚀 How to run locally

1. **Clone the repo**
   ```bash
   git clone <your-github-repo-url>
   cd ShreysMixologyHub

2.Create & activate a virtual environment
   python -m venv venv
   # Mac/Linux
   source venv/bin/activate
   # Windows
   venv\Scripts\activate

3.Install dependencies
   pip install -r requirements.txt

4.Add your .env file with your Gemini API key
   GEMINI_API_KEY=YOUR_GEMINI_API_KEY

5.Run it
   app.py

6.Open your browser
   http://127.0.0.1:5000/
