## About the code files

Here lists the files and their main function in our project.

 - [preprocess.py](https://bitbucket.org/INF_560_Practicum/team-blue-bird/src/master/preprocess.py) 
    - by Shuting Ye
    - After initial preprocessing(filter out mac id whose records is less than 3 and convert each json file into csv format), this preprocessing code is mainly to drop the duplicate records and concat each 5 files into one.
 - [clean.py](https://bitbucket.org/INF_560_Practicum/team-blue-bird/src/master/clean.py) 
    - by Zilu Li
    - Preprocess data. Filter out mac id whose records is less than 3. Rename columns. Convert file into csv.
 - [crawler.py](https://bitbucket.org/INF_560_Practicum/team-blue-bird/src/master/crawler.py) 
    - by Zilu Li
    - Crawl flight information from airportia.
 - [continous.py](https://bitbucket.org/INF_560_Practicum/team-blue-bird/src/master/continous.py)
    - by Xinyang Zhang
    - Calculate the continous days that one macid have, if one macid appears in the airport more than 4 days continous. 
    - We will assert him/she has high possibility that belongs to the employer list.
    - The first method to distinguish the employer and passenger.
    
 - [calculate_frequency.py](https://bitbucket.org/INF_560_Practicum/team-blue-bird/src/master/calculate_frequency.py)
    - by Xinyang Zhang
    - Calculate the total frequency of per macid within 5 months as the second method to distinguish the employer and passenger.
    
 - [dis_depart_arrival.py](https://bitbucket.org/INF_560_Practicum/team-blue-bird/src/master/dis_depart_arrival.py)
    - by Xinyang Zhang
    - Distinguish the departure and arrival passenger
 
 - [renumber.py](https://bitbucket.org/INF_560_Practicum/team-blue-bird/src/master/renumber.py)
    - by Xinyang Zhang
    - After we filter all of the employer and arrival passengers, we need to renumber all of the macid.
    - We need to treat even if the same macid as the different person in differernt days.
    - Since he/she may take the differernt flight and may go to the different destination.
    
 - [filterdeparture.py](https://bitbucket.org/INF_560_Practicum/team-blue-bird/src/master/filterdeparture.py)
    - by Shuting Ye
    - Filter out some departure passengers who don't have enough records to calculate their total shopping time. So only keep those passengers who have at least one record in any of the five shopping zones in the South Pier building and at least two other records out of the shopping zone.
    - The output file only contains records relating to the passengers who meet the above criterion.
 - [tst.py](https://bitbucket.org/INF_560_Practicum/team-blue-bird/src/master/tst.py)
    - by Shuting Ye
    - Calculate the total shopping time of each passenger and the total shopping time is the combination of all shopping time they spent in each shopping zone. 
    - Basicly, the shopping time in one shopping zone is calculated by adding up the time they spent inside the shopping zone, the propotional time they spent entering into and geting out of the shopping zone. The propotionality is referred by comparing the distance between two location points(one inside the shopping zone and another out of the shopping zone) and the distance between the point inside the shopping zone and the point on the boudary of the zone.
    - The output file contains the total shopping time in seconds (macid, total shopping time).
 - [flight_mapping.R](https://bitbucket.org/INF_560_Practicum/team-blue-bird/src/master/flight_mapping.R) 
    - by Gavin Michaels
    - After preprocessing occurs, this file finds the last record for each departing mac_id per flight trip. 
    - Then, calculates weighted distance between physical location of last_record and flights and time of last records and flights. Using this, assigns probability of passenger being on a flight, and returns a list of probability per flight.
 - [Blue_bird_model_8_more_models.ipynb](https://bitbucket.org/INF_560_Practicum/team-blue-bird/src/master/Blue_bird_model_8_more_models.ipynb)
    - by Shuting Ye and Xinyang Zhang
    - Apply 8 commonly used regression models on the train data and predict the total shopping time for each flight based on the flight information.
    - The 8 models are Linear Regression, Elastic Net, Bayesian Ridge, KNN, Gradient Boosting, Lasso, Decision Tree, Ada Boosting.
    - Use GridSearchCV to tune the hyper parameters for each models and evaluate their performance using 10-flod cross validation with RMSE.
    - The overall RMSE results are shown in a table and the XGBoost performs best with RMSE of 33.98.
 - [flask_react](https://bitbucket.org/INF_560_Practicum/team-blue-bird/src/master/flask_react)
    - by Ding Wang
    - All the website source code, frontend and backend
    - Use React and antd for frontend building and flask for the backend building.
    - Take a date in future and flight information of that day to give an optimized gate assigment that can Maximize passengers' shopping time
    - Provide both gate assignment recommandation and top 5 gate for each flight.
    - Visualizing gates that assigned flight on map and information of flights.
 - [Bluebirdmodel.ipynb](https://bitbucket.org/INF_560_Practicum/team-blue-bird/src/master/Bluebirdmodel.ipynb) 
    - by Zilu Li
    - Preprocessed data, performed the feature transformation, missing data imputation and outlier detection. 
    - Built a ML pipline with cross validation and feature importance selection for XGBoost and LightGBM.
    - Used GridSearchCV to find the best hyper parameters for both models and evaluated them in RMSE. 
 - [app.py](https://bitbucket.org/INF_560_Practicum/team-blue-bird/src/master/app.py) 
    - by Zilu Li
    - The backend service for website including, wrapping XGBoost model, calculating top5 gate for each flight, schedule the gate for multiple flights and map information.

    
