from flask import Flask, render_template
from monte_carlo import estimate_pi

app = Flask(__name__)

@app.route('/home/<int:num_simulations>')
def home(num_simulations):
    estimated_pi = estimate_pi(num_simulations)
    return render_template('template.html', num_simulations = num_simulations, estimated_pi = estimated_pi * 4)


if __name__ == '__main__':
    app.run()