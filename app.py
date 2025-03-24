from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])  # Change '/register' to '/'
def register():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')

        print(f"Received: Name={name}, Email={email}, Password={password}")

        return render_template('success.html')

    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)
