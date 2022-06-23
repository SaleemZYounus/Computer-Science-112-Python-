for x in range(1,4):
    for y in range(1, 4):
        for z in range(1, 4): #runss through these inner ones first
            print(f'({x}, {y}, {z})')


----------------HW 5----------------------------------------
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
deta = pd.read_csv(r"Autism-Adult-Data.csv")



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
ethni  = deta.ethnicity.value_counts() #<<< this better

gen = deta['gender'].to_list()
uniq_gen = set(gen)

for item in uniq_gen:
    counts = gen.count(item)
    print(item, counts)

f 337
m 367 #results

female_eth = deta.loc[deta.gender =='f', "ethnicity"].value_counts() <<<<<
female_eth = deta.loc[deta.gender =='f', "ethnicity"].to_list()
uniq_fem = set(female_eth)
for item in uniq_fem:
    counts = female_eth.count(item)
    print(item, counts) #prints out the total number or females from each country

female_eth = deta.loc[deta.gender =='f', "ethnicity"].value_counts()
male_eth = deta.loc[deta.gender =='m', "ethnicity"].value_counts()^<<<<<
male_eth.plot(kind = 'bar', title = 'Ethnicity of Males') #bar chart with male eth
female_eth.plot(kind = 'bar', title = 'Ethnicity of Females')
uniq_male = set(male_eth)
for item in uniq_male:
    counts = male_eth.count(item)
    print(item, counts)   


y = np.array([asd.count("YES"), asd.count("NO")]) #pie chart
mylabels = ["YES", "NO"]
myexplode = [0.2, 0]

plt.pie(y, labels = mylabels, explode = myexplode, shadow = [2])
plt.legend(title = "Does individual have ASD:")
plt.show()p

#plt.pyplot.legend(labels=cont.index, ncol=10 )

cont = deta['contry_of_res'].value_counts()  #bar chart for countries - horiz
plt.tick_params(axis='x', labelsize=10)
plt.tick_params(axis='y', labelsize=5.5)
plt.ylabel('Country of Residence', fontsize = 11)
plt.xlabel('Number of Subjects Residing in Each Country', fontsize = 12)
plt.barh(y = cont.index, width = cont)
plt.show()


eth = deta.ethnicity.value_counts()
 #eth pie
ethni = np.array(eth)
mylabels = ['White-European', 'Asian', 'Middle Eastern', 'Black', 'South Asian', 'Others', 'Latino', 'Hispanic', 'Pasifika', 'Turkish',]
plt.title("Ethnicity", fontsize =20)
plt.pie(ethni, labels = mylabels)

plt.show()

deta['age'].hist() #age
plt.title('Age of Subjects')
plt.xlabel('Age')
plt.ylabel('Number of ppl')
plt.show()

deta.age.mean()
29.19400855920114
deta.age.median()
27.0
deta.age.mode()
21.0
dtype: float64
deta.age.std()
9.71152590893556
