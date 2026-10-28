from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# In-memory list to store visitor notes
notes = []

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        note = request.form.get('note')
        if note:
            notes.append(note)
        return redirect('/')
    return render_template('index.html', notes=notes)

def about():
    return render_template('about.html')   

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
