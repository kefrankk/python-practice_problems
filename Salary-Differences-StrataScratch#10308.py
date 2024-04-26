"""
Link to the question: https://platform.stratascratch.com/coding/10308-salaries-differences?code_type=2

Question ID 10308: Write a query that calculates the difference between the highest salaries found in the marketing and engineering departments. 
Output just the absolute difference in salaries.

DataFrames: db_employee, db_deptExpected Output Type: pandas.DataFrame

"db_employee"
  id: int
  first_name: varchar
  last_name: varchar
  salary: int
  department_id: int

"db_dept"
  id: int
  department: varchar

"""

# Import your libraries
import pandas as pd

employees = pd.merge(db_employee, db_dept, left_on="department_id", right_on="id")

marketing_salary = max(employees.salary[employees.department == "marketing"])
engineering_salary = max(employees.salary[employees.department == "engineering"])

difference = marketing_salary - engineering_salary
result = pd.DataFrame(data = [abs(difference)], columns = ["salary_difference"])

result
