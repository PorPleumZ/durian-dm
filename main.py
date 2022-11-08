# import the necessary packages
#from keras.models import load_model
#import sklearn
#import numpy as np
import flask
import pandas as pd
import pickle

# initialize our Flask application and the Keras model
app = flask.Flask(__name__)
filename = 'finalized_model.sav'
model = pickle.load(open(filename, 'rb'))

def predict_from_file(file):
    df  = pd.read_excel(file)

    X_test = df.iloc[:, 1:]

    pred = model.predict(X_test)

    return pred

@app.route("/predict", methods=["POST"])
def predict():
    # initialize the data dictionary that will be returned from the view
    data = {"success": False}
    model = 0
    # ensure an data was properly uploaded to our endpoint
    if flask.request.method == "POST":

        file = flask.request.files.get('file')
        file.save('input.xlsx')
        result = predict_from_file(file)


        print(result)

        data['DM'] = result.tolist()

        # indicate that the request was a success
        data["success"] = True
    # return the data dictionary as a JSON response
    return flask.jsonify(data)

# if this is the main thread of execution first load the model and
# then start the server
if __name__ == "__main__":
    print(("* Loading Keras model and Flask starting server..."
        "please wait until server has fully started"))

    #app.run(debug=True)
    app.run(host='0.0.0.0', port = 5001)
