"""

Link to the exercise: https://platform.stratascratch.com/coding/10354-most-profitable-companies?code_type=2

Find the 3 most profitable companies in the entire world.
Output the result along with the corresponding company name.
Sort the result based on profits in descending order.


DataFrame: forbes_global_2010_2014

'forbes_global_2010_2014'
    company: varchar
    sector: varchar
    industry: varchar
    continent: varchar
    country: varchar
    marketvalue: float
    sales: float
    profits: float
    assets: float
    rank: int
    forbeswebpage: varchar

"""

# Import your libraries
import pandas as pd

# Start writing code
forbes_global_2010_2014.head()

comp = forbes_global_2010_2014.groupby(["company"], as_index=False)["profits"].sum()

comp.sort_values(by=["profits"], ascending=False).head(3)

