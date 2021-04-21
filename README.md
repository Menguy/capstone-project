# capstone-project
Materials associated to the Capstone project - Eric Menguy


This project contains main materials of Capstone project:

1. The notebook "part1 and part 2" describes the Business objective, EDA , Data visualization and Modeling parts of the project

Note: the variable "price" has been considered as the revenue of a purchase (a purchase act being identified by the attribute Invoice_ID. I am not sure if it is correct and if price had to be viewed as a unit price (and to multiply by the number of streams viewed...).
Note: the baseline model is the one differentiating arima model ((p,d,q) = (0,1,0)). rmse is the indicator used to compare the performane of the model to the baseline model.

2. The notebook "part 3 " describes the deployment part of the project

Note: to simplify the construction of the deployment phase, I have focused on the forecast of revenue (6 stepas ahead) for all the countries (and not by country).

Note: The unittest has been applied on the test of a date value as input parameter

3. The other materials are:
- app.py 
- DockerFile
- Requirements (for Docker)
- "capstone - unittest.py" (python program for unittest)
- "capstone - logging.py" (python program for logging)
- Aggregated monthly data "all countries" : file invoices.csv
- Aggregated monthly data "all countries" for the period august to december 2019: file invoices_production.csv
