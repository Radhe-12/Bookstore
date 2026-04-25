from flask import Flask, render_template, request, redirect

app = Flask(__name__)

books = [
    {"name": "Atomic Habits", "category": "Self-help", "price": 499},
    {"name": "The Alchemist", "category": "Fiction", "price": 299},
    {"name": "Clean Code", "category": "Tech", "price": 799},
    {"name": "Rich Dad Poor Dad", "category": "Finance", "price": 399}
]

@app.route("/", methods=["GET"])
def home():
    query = request.args.get("q")
    category = request.args.get("category")

    filtered_books = books

    if query:
        filtered_books = [b for b in filtered_books if query.lower() in b["name"].lower()]

    if category:
        filtered_books = [b for b in filtered_books if b["category"] == category]

    return render_template("index.html", books=filtered_books)


@app.route("/buy/<book_name>")
def buy(book_name):
    return f"You bought {book_name} 🎉"


@app.route("/add", methods=["POST"])
def add_book():
    name = request.form["name"]
    category = request.form["category"]
    price = request.form["price"]

    books.append({"name": name, "category": category, "price": price})

    return redirect("/")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)