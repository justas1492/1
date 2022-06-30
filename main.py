from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods = ['POST', 'GET'])
def Skaiciuoti():
    l = ''
    sum = ''
    if request.method =='POST' and 'kaina' in request.form and 'sanaudos' in request.form and 'atstumas' in request.form:
        k = float(request.form.get('kaina'))
        s = float(request.form.get('sanaudos'))
        a = float(request.form.get('atstumas'))
        l = round((s * a)/100,2)
        sum = round(l*k,2)
    return render_template('index.html',l=l,sum=sum)

if __name__ == "__main__":
    app.run(debug=True)