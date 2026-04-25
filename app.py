from flask import Flask, render_template

app = Flask(__name__)

books = [
    {"name": "Atomic Habits", "category": "Self-help", "price": 499},
    {"name": "The Alchemist", "category": "Fiction", "price": 299},
    {"name": "Clean Code", "category": "Tech", "price": 799},
    {"name": "Rich Dad Poor Dad", "category": "Finance", "price": 399},
    {"name": "Think and Grow Rich", "category": "Self-help", "price": 350}
]

@app.route("/")
def home():
    return render_template("index.html", books=books)

if __name__ == "__main__":
    app.run(debug=True)