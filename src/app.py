from model import generate_text
from flask import Flask, request, render_template

def llm(text_in):
  response = generate_text(text_in)

  return next(iter(response[0].values()))

#print (llm("What is AI ? Explain in 3 sentences"))


app = Flask(__name__)

@app.route('/')
def home():
   return render_template('pages/index.html',visibility='hidden')

@app.route('/conversation', methods=['POST'])
def conversation():
  data = request.get_json()
  text_in = data['textInput']
  #text_in = str(request.args.get('textInput'))
  return {'response':llm(text_in)}


if __name__ == '__main__':
    try:
        #app.run(host='0.0.0.0',port=int(8080), debug=True)
        from waitress import serve
        serve(app, host="0.0.0.0", port=8080)
    except:
        print("unexcepted error")