################################################################################################################
################################################################################################################
############################################# BigData Journey- PYTHON  #########################################
################################################################################################################
################################################################################################################

#04MAY2019 - pandas dataframe 
#1#Reading csv file as pandas dataframe, Filling null values with required things, droping nulls, interpolate() method for linear guessing the missing values.
import pandas as pd
df = pd.read_csv("File3_nulldata.csv", parse_dates=["Date"])
df.set_index("Date",  inplace=True)
df2=df.fillna(method="bfill", axis="columns")
df3=df.interpolate(method="time")
df4=df.dropna()
df5=df.replace(np.NaN, "XXXXX")
df6= df.replace({ 'Temper':'[A-Za-z]', 'Wind':'[A-Za-z]'},'',regex=True)
#df6 using regular expression to remove non disgits in numeric columns ex: 65KG, 20 mtrs 
df6
df4

#######################################
#2#Group by in pandas dataframe
import numpy as np
import pandas as pd
df=pd.read_csv("File3_rain.csv")
df
o/p:

Date	City	Temper	Wind
0	01-01-2019	Banglore	35	15
1	01-02-2019	Banglore	34	14
2	01-03-2019	Banglore	33	13
3	01-04-2019	Banglore	36	16
4	01-05-2019	HYD	45	8
5	01-06-2019	HYD	47	7
6	01-07-2019	HYD	49	8
7	01-08-2019	Chennai	50	2
8	01-09-2019	Chennai	52	3
9	01-10-2019	Chennai	54	1

df2=df.groupby("City")
df2
for City, City_df in df2:
    print(City)
    print(City_df)
	
Banglore
         Date      City  Temper  Wind
0  01-01-2019  Banglore      35    15
1  01-02-2019  Banglore      34    14
2  01-03-2019  Banglore      33    13
3  01-04-2019  Banglore      36    16
Chennai
         Date     City  Temper  Wind
7  01-08-2019  Chennai      50     2
8  01-09-2019  Chennai      52     3
9  01-10-2019  Chennai      54     1
HYD
         Date City  Temper  Wind
4  01-05-2019  HYD      45     8
5  01-06-2019  HYD      47     7
6  01-07-2019  HYD      49     8

df2.get_group('Banglore')
df2.max()
df2.describe()
%matplotlib inline
df2.plot()
	
	
#############################################
#3#	concatinating dataframes 
India_cool=pd.DataFrame(
{
    "City":["Banglore", "HYD", "Chennai"],
    "Temper": [25,45,65],
    "Humidity":[45,35,25]
}
)
India_cool
US_hot=pd.DataFrame(
{
    "City":["NewYark", "Chicago", "Mexico"],
    "Temper": [25,45,65],
    "Humidity":[45,35,25]
    
}
)

US_hot
df3=pd.concat([India_cool, US_hot])
df3
df4=pd.concat([India_cool, US_hot],ignore_index=True)
df4
df4=pd.concat([India_cool, US_hot],keys=["India_cool", "US_hot"])
df4
	
	
###############
#4#	Joins in Pandas by using merge command on pandas
import pandas as pd
df1=pd.DataFrame(
{
    "City": ["Bang","HYD","Delhi"],
    "Temper": [20,30,40]
}
)
df1

import pandas as pd
df2=pd.DataFrame(
{
    "City": ["HYD","Bang","Chennai","Mumbai"],
    "Rain": [5,6,7,8]
}
)
df2

df3=pd.merge(df1,df2, on="City")
df3
O/P
City	Temper	Rain
0	Bang	20	6
1	HYD	30	5


df4=pd.merge(df1,df2, on="City", how="outer")
df4
O/P

City	Temper	Rain
0	Bang	20.0	6.0
1	HYD	30.0	5.0
2	Delhi	40.0	NaN
3	Chennai	NaN	7.0
4	Mumbai	NaN	8.0

df5=pd.merge(df1,df2, on="City", how="left")
df5
O/P;

City	Temper	Rain
0	Bang	20	6.0
1	HYD	30	5.0
2	Delhi	40	NaN


df6=pd.merge(df1,df2, on="City", how="right", indicator=True)
df6
O/P:
City	Temper	Rain	_merge
0	Bang	20.0	6	both
1	HYD	30.0	5	both
2	Chennai	NaN	7	right_only
3	Mumbai	NaN	8	right_only


#######################################
#5# Pivot tables for making table structures as like as we want 
df1=pd.read_csv("File3_rain.csv")
df1
O/P;
Date	City	Temper	Wind
0	01-01-2019	Banglore	35	15
1	01-02-2019	Banglore	34	14
2	01-03-2019	Banglore	33	13
3	01-04-2019	Banglore	36	16
4	01-05-2019	HYD	45	8
5	01-06-2019	HYD	47	7
6	01-07-2019	HYD	49	8
7	01-08-2019	Chennai	50	2
8	01-09-2019	Chennai	52	3
9	01-10-2019	Chennai	54	1

df2=df1.pivot_table(index="Date", columns="City")
df2
O/P;
				Temper	 			Wind
City	Banglore	Chennai	HYD	Banglore	Chennai	HYD
Date						
01-01-2019	35.0	NaN	NaN	15.0	NaN	NaN
01-02-2019	34.0	NaN	NaN	14.0	NaN	NaN
01-03-2019	33.0	NaN	NaN	13.0	NaN	NaN
01-04-2019	36.0	NaN	NaN	16.0	NaN	NaN
01-05-2019	NaN	NaN	45.0	NaN	NaN	8.0
01-06-2019	NaN	NaN	47.0	NaN	NaN	7.0
01-07-2019	NaN	NaN	49.0	NaN	NaN	8.0
01-08-2019	NaN	50.0	NaN	NaN	2.0	NaN
01-09-2019	NaN	52.0	NaN	NaN	3.0	NaN
01-10-2019	NaN	54.0	NaN	NaN	1.0	NaN


#margin is used to get values in both columns side, rowside values
import pandas as pd
df=pd.read_csv("File3_rain.csv")
df
df.pivot_table(columns="City", index="Date", margins=True)

Temper	Wind
City	Banglore	Chennai	HYD	All	Banglore	Chennai	HYD	All
Date								
01-01-2019	35.0	NaN	NaN	35	15.0	NaN	NaN	15
01-02-2019	34.0	NaN	NaN	34	14.0	NaN	NaN	14
01-03-2019	33.0	NaN	NaN	33	13.0	NaN	NaN	13
01-04-2019	36.0	NaN	NaN	36	16.0	NaN	NaN	16
01-05-2019	NaN	NaN	45.0	45	NaN	NaN	8.000000	8
01-06-2019	NaN	NaN	47.0	47	NaN	NaN	7.000000	7
01-07-2019	NaN	NaN	49.0	49	NaN	NaN	8.000000	8
01-08-2019	NaN	50.0	NaN	50	NaN	2.0	NaN	2
01-09-2019	NaN	52.0	NaN	52	NaN	3.0	NaN	3
01-10-2019	NaN	54.0	NaN	54	NaN	1.0	NaN	1
All	34.5	52.0	47.0	43	14.5	2.0	7.666667	8

#Converting string column into datetime format in pandas
df["Date"] = pd.to_datetime(df["Date"])

#by using grouper,frequency, key we can make results basedon grouper
df.pivot_table(index=pd.Grouper(freq="M", key="Date"), columns="City")

Temper	Wind
City	Banglore	Chennai	HYD	Banglore	Chennai	HYD
Date						
2019-01-31	34.5	52.0	47.0	14.5	2.0	7.666667


#reading Apple stock market files
df=pd.read_csv("File5_AppleStock.csv", parse_dates=["date"])
df.head(5)

O/P:
date	close	volume	open	high	low
0	2019-10-05	197.18	41208710	199.95	198.850	192.770
1	2019-09-05	200.72	34908610	202.90	201.680	196.660
2	2019-08-05	202.90	26339500	202.86	205.340	201.750
3	2019-07-05	202.86	38763700	208.48	207.418	200.825
4	2019-06-05	208.48	32443110	211.75	208.840	203.500

type(df.date[0])
o/P:
pandas._libs.tslibs.timestamps.Timestamp































################################################################################################################
################################################################################################################
############################################# Python Ruff - Practice ############################################
################################################################################################################
################################################################################################################

#04MAY2019
def tinnavara():
    print("Hello tinnavaraaa...!!")
    x=10
    def inside_tinnava():
        print("Inside")
        y=20
        print("X=", x)
    inside_tinnava()
    print("y=", y)


s = 1+1+1+\
    1+1+\
    1