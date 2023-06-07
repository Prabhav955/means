from flask import Flask, request, jsonify, render_template

import pickle


app = Flask(__name__)
model = pickle.load(open('/home/ayushiiiii/means/kmeanscluster.pkl','rb'))


@app.route('/')
def home():

    return render_template("untitled.html")

@app.route('/predict',methods=['GET'])
def predict():
  '''
  For rendering results on HTML GUI
  '''
  gender= int(request.args.get('gender'))
  glucose = int(request.args.get('glucose'))
  bp= int(request.args.get('bp'))
  skin_thickness= int(request.args.get('skin_thickness'))
  insulin= int(request.args.get('insulin'))
  bmi= int(request.args.get('bmi'))
  pedigree_function= int(request.args.get('pedigree_function'))
  age = int(request.args.get('age'))


  predict = model.predict([[gender,glucose,bp,skin_thickness,insulin,bmi,pedigree_function,age]])
  if predict==[0]:
    result="patient willhave disease"


  else:
    result="not disease"


  return render_template('untitled.html', prediction_text='Model  has predicted  : {}'.format(result))

if __name__ == '__main__':
 app.run()
