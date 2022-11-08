# import the necessary packages
import requests
import time
from time import localtime, strftime
import traceback



# initialize the Keras REST API endpoint URL
KERAS_REST_API_URL = "http://127.0.0.1:5001/predict"
#KERAS_REST_API_URL = "http://app02-stg.inwini.com/rvp/predict"
#KERAS_REST_API_URL = "https://amr-anomaly-ce6ez7jgkq-uc.a.run.app/predict"


# load the input dict and construct the payload for the request


try:
    myfiles = {'file': open('Durain_RawData_Lot_1_2_Multi_Measure_700_1100_No_Outlier.xlsx', 'rb')}
    start = time.time()
    r = requests.post(KERAS_REST_API_URL, files=myfiles).json()
    # ensure the request was successful
    if r["success"]:
        # loop over the predictions and display them
        end = time.time()
        print("[INFO] calculation at {} for sample number {} took {:.6f} seconds".format(strftime("%Y%m%d%H%M%S", localtime()),0,end - start))
        print('DM =', r["DM"])
        print('==========================')
    # otherwise, the request failed
    else:
        print("Request failed")
    #time.sleep(5)

except Exception as e:
    print("[INFO] request fail at {} for sample number {}".format(strftime("%Y%m%d%H%M%S", localtime()), 0))
    print('==========================')
    print(traceback.print_exc())
    time.sleep(1)
#i += 1

