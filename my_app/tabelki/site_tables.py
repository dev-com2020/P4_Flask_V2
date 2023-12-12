from flask import *
import pandas as pd

app4 = Flask(__name__)


@app4.route('/')
def show_tables():
    data = pd.read_excel('imiona.xlsx', sheet_name="Wynik2")
    data.set_index(['Name'], inplace=True)
    data.index.name = None
    females = data.loc[data.Gender == 'K']
    males = data.loc[data.Gender == 'M']
    return render_template('view2.html', tables=[females.to_html(classes='female'),
                                                males.to_html(classes='male')],
                           titles=['na', 'Female students', 'Male students'])

if __name__ == '__main__':
    app4.run(debug=True)