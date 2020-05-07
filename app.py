from flask import Flask
from flask import render_template
from flask import redirect
from flask import url_for
from flask import request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sentimentanalysis')
def sentimentanalysis():
    return render_template('sent.html')


@app.route('/sent3')
def sent3():
    x = ["happy","important","animated","quiet","accepting","festive","spirited","certain","kind","ecstatic","thrilled","relaxed","satisfied","wonderful","serene","glad","free","easy","cheerful","bright","sunny","blessed","merry","reassured","elated","jubilant"]
    try:
        txt=request.args.get('nm')
        b=[txt]
        for i in b:
            for j in x:
                if j in i:
                    d='y'
                    break
                else:
                    d='n'
    except Exception as e:
        pass
    return render_template('sent3.html',x=x,b=b,d=d)


if __name__== '__main__':
    app.run()





