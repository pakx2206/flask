from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    title = 'Pan Tadeusz'
    author = 'Adam Mickiewicz'
    books = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
    return render_template('index.html', title=title, author=author, books=books)

@app.route('/<book_number>.html')
def book(book_number):
    return render_template(f'k{book_number}.html')

if __name__ == '__main__':
    app.run()
