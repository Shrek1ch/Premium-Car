from flask import Flask, render_template
from database import get_car
app = Flask(__name__)

@app.route('/')
def index():
    # title - переменная, которая будет доступна в шаблоне
    car = get_car()
    return render_template(
        'index.html', 
        title="Каталог",
        car=car,
    )




app.run(debug=True)