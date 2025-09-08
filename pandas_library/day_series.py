import pandas as pd

days = {

     1:"Sunday",
     2:"Monday",
     3:"Tuesday",
     4:"Wednesday",
     5:"Thursday",
     6:"Friday",
     7:"Saturday"
}

print(days[4])
my_days = pd.Series(days)

print(my_days)