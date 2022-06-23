import pandas as p
data = p.DataFrame([["4'3" , "19"], ["5'8", "18" ], ["5'11", "18"]], index = ["yami","bilal","ian"], columns=["hight","age"])
deta = p.read_csv(r"cereal.csv") #<- IMPORTS CSV FILE WITH DATA
#atribute is method without ()

df.columns # shows columnsl

df['name'] #to show rows
df['name'].to_list() #makes names into list
.value_counts

import pandas as w
>>> import matplotlib as plt
>>> df = w.read_csv("grades.csv")
>>> dfone = df.loc[df.section ==1, "grade"]
>>> dfone.plot(kind = 'hist', density=True, bins = 5)

numpy = numerical python   works well with tenserflow pyttorch

arrays and dimension - - - zero dimensional arrray is one number
table - 2 dimention
1 index per demintion

----------------HW 5----------------------------------------
set(deta['age_desc'].to_list()) # used to check uniqui elements of ages [ shows
set(deta['ethnicity'].to_list())
#{nan, 'Turkish', 'Latino', 'Hispanic', 'Asian', 'Black', 'White-European', 'Pasifika', 'Middle Eastern', 'South Asian', 'Others'}
deta['ethnicity'].value_counts # shows numer next to eth

eth = (deta['ethnicity'].to_list()) # contains all the content under ethnicity (703)
uniq_eth = set(eth) # unique ethnicities
for item in uniq_eth: #prints group with freq
    counts = eth.count(item)
    print(item, counts)
nan 95
Turkish 6
Latino 20
Hispanic 13
Asian 123
Black 43
White-European 233
Pasifika 12
Middle Eastern 92
South Asian 36
Others 31        #prints all this showing demografics   and segmentation  and divesification )too many white(

    
