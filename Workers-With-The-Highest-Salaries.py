
"""
Link to the question: https://platform.stratascratch.com/coding/10353-workers-with-the-highest-salaries?code_type=2

Question ID 10353: You have been asked to find the job titles of the highest-paid employees.
Your output should include the highest-paid title or multiple titles with the same salary.

DataFrames: worker, title       Expected Output Type: pandas.DataFrame

"worker"
    worker_id: int
    first_name: varchar
    last_name: varchar
    salary: int
    joining_date: datetime
    department: varchar

"title"
    worker_ref_id: int
    worker_title: varchar
    affected_from: datetime

"""



import pandas as pd

workers = pd.merge(worker, title, left_on="worker_id", right_on="worker_ref_id")

salary = workers.salary.max()
title = workers.worker_title[workers.salary == salary].tolist()
best_paid = pd.DataFrame(data = title, columns=["best_paid_title"])

best_paid