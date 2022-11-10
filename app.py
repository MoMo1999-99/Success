import streamlit as st
import pickle
import numpy as np




    

page_bg_img = ''''
<Style>
[data-testid="stAppViewContainer"]{

background-image: url(https://images.pexels.com/photos/262047/pexels-photo-262047.jpeg?cs=srgb&dl=pexels-pixabay-262047.jpg&fm=jpg&_gl=1*110bvks*_ga*NTUzMjk4NDUyLjE2Njc5MTM2MTQ.*_ga_8JE65Q40S6*MTY2NzkxMzYxNS4xLjEuMTY2NzkxNTI3Ni4wLjAuMA..);    
background-size: cover ;
background-repeat: no-repeat;       
}
</Style>
'''
st.markdown(page_bg_img  , unsafe_allow_html = True)
st.title("it's The Successe Predictor")








pickle_out = open("classifier1.pkl","rb")
model = pickle.load(pickle_out)

def predictor(input_data):
    convert_to_array = np.array(input_data)
    reshape_input = convert_to_array.reshape(1,-1)
    prediction = model.predict(reshape_input) 
    
    if prediction[0] == 1 :
        return 'Congratulaions the restaurant will successe'
    else:
        return 'Unfortunately, the restaurant will fail'





book_table_list = ['Select','Yes','NO']

book_table=st.selectbox('Book Table',book_table_list)

if book_table == 'Yes':
    book_tableEnc = 1
else:
    book_tableEnc = 0
    



online_order_list = ['Select','Yes','NO']

online_order = st.selectbox('Online Order',online_order_list)


if online_order == 'Yes':
    online_orderEnc = 1
else:
    online_orderEnc = 0



location_list = ['Select','Banashankari', 'Basavanagudi', 'Jayanagar', 'JP Nagar',
    'Bannerghatta Road', 'BTM', 'Electronic City', 'HSR',
    'Marathahalli', 'Shanti Nagar', 'Koramangala 5th Block',
    'Koramangala 8th Block', 'Richmond Road', 'Koramangala 7th Block',
    'Koramangala 4th Block', 'Bellandur', 'Sarjapur Road',
    'Whitefield', 'Old Airport Road', 'Indiranagar',
    'Koramangala 1st Block', 'Frazer Town', 'MG Road', 'Brigade Road',
    'Lavelle Road', 'Church Street', 'Ulsoor', 'Residency Road',
    'Shivajinagar', 'St. Marks Road', 'Cunningham Road',
    'Commercial Street', 'Domlur', 'Ejipura', 'Malleshwaram',
    'Kammanahalli', 'Koramangala 6th Block', 'Brookefield',
    'Rajajinagar', 'Banaswadi', 'Kalyan Nagar', 'New BEL Road','others']



location = st.selectbox('Locations',location_list)


locationEnc = 0


if location == 'BTM':
    locationEnc = 0
elif location == 'others':
    locationEnc = 42    
elif location == 'HSR':
    locationEnc = 15
elif location == 'Koramangala 5th Block':
    locationEnc = 23
elif location == 'JP Nagar':
    locationEnc = 17
elif location == 'Whitefield':
    locationEnc = 41
elif location == 'Indiranagar':
    locationEnc = 16
elif location == 'Jayanagar':
    locationEnc = 18    
elif location == 'Marathahalli':
    locationEnc = 30
elif location == 'Bannerghatta Road':
    locationEnc = 3
elif location == 'Bellandur':
    locationEnc = 5
elif location == 'Electronic City':
    locationEnc = 13
elif location == 'Koramangala 1st Block':
    locationEnc = 21
elif location == 'Brigade Road':
    locationEnc = 6
elif location == 'Koramangala 7th Block':
    locationEnc = 25
elif location == 'Koramangala 6th Block':
    locationEnc = 24
elif location == 'Sarjapur Road':
    locationEnc = 36
elif location == 'Ulsoor':
    locationEnc = 40
elif location == 'Koramangala 4th Block':
    locationEnc = 22
elif location == 'Banashankari':
    locationEnc = 1
elif location == 'MG Road':
    locationEnc = 28          
elif location == 'Kalyan Nagar':
    locationEnc = 19
elif location == 'Richmond Road':
    locationEnc = 35
elif location == 'Malleshwaram':
    locationEnc = 29
elif location == 'Frazer Town':
    locationEnc = 14
elif location == 'Basavanagudi':
    locationEnc = 4
elif location == 'Residency Road':
    locationEnc = 34
elif location == 'Brookefield':
    locationEnc = 7
elif location == 'Banaswadi':
    locationEnc = 2
elif location == 'New BEL Road':
    locationEnc = 31    
elif location == 'Kammanahalli':
    locationEnc = 20          
elif location == 'Rajajinagar':
    locationEnc = 33
elif location == 'Church Street':
    locationEnc = 8
elif location == 'Lavelle Road':
    locationEnc = 27
elif location == 'Shanti Nagar':
    locationEnc = 37
elif location == 'Shivajinagar':
    locationEnc = 38
elif location == 'Cunningham Road':
    locationEnc = 10
elif location == 'Domlur':
    locationEnc = 11
elif location == 'Old Airport Road':
    locationEnc = 32
elif location == 'Ejipura':
    locationEnc = 12    
elif location == 'Commercial Street':
    locationEnc = 9
elif location == 'St. Marks Road':
    locationEnc = 39
elif location == 'Koramangala 8th Block':
    locationEnc = 26        
    
    
Number_rest_type = st.number_input("Enter Number Of Rest Type",min_value = 1,max_value=2)   


Quick_Bites = 0
Casual_Dining = 0
Cafe = 0
Delivery = 0
Dessert_Parlor = 0 
Bar = 0
Takeaway = 0
Bakery = 0
Beverage_Shop = 0
Pub = 0
other = 0

rest_type_list = ['Select','Quick Bites','Casual Dining','Cafe','Delivery','Dessert Parlor','Bar','Takeaway','Bakery','Beverage Shop','Pub','other']

if Number_rest_type == 1:
    rest_type = st.selectbox('Rest Type',rest_type_list)
    if rest_type =='Quick Bites':
        Quick_Bites = 1
    elif rest_type =='Casual Dining':
        Casual_Dining = 1
    elif rest_type =='Cafe':
        Cafe = 1
    elif rest_type =='Delivery':
        Delivery = 1
    elif rest_type =='Dessert Parlor':
        Dessert_Parlor = 1
    elif rest_type =='Bar':
        Bar = 1
    elif rest_type =='Takeaway':
        Takeaway = 1
    elif rest_type =='Bakery':
        Bakery = 1
    elif rest_type =='Beverage Shop':
        Beverage_Shop = 1
    elif rest_type =='Pub':
        Pub = 1
    elif rest_type =='other':
        other = 1
elif Number_rest_type == 2:
    rest_type12 = st.selectbox('Rest Type',rest_type_list)    
    if rest_type12 =='Quick Bites': 
        Quick_Bites = 1
    elif rest_type12 =='Casual Dining':
        Casual_Dining = 1
    elif rest_type12 =='Cafe':
        Cafe = 1
    elif rest_type12 =='Delivery':
        Delivery = 1
    elif rest_type12 =='Dessert Parlor':
        Dessert_Parlor = 1
    elif rest_type12 =='Bar':
        Bar = 1
    elif rest_type12 =='Takeaway':
        Takeaway = 1
    elif rest_type12 =='Bakery':
        Bakery = 1
    elif rest_type12 =='Beverage Shop':
        Beverage_Shop = 1
    elif rest_type12 =='Pub':
        Pub = 1
    elif rest_type12 =='other':
        other = 1    
    rest_type2 =  st.selectbox('Seconed Rest Type ',rest_type_list)
    if rest_type2 =='Quick Bites':
        Quick_Bites = 1
    elif rest_type2 =='Casual Dining':
        Casual_Dining = 1
    elif rest_type2 =='Cafe':
        Cafe = 1
    elif rest_type2 =='Delivery':
        Delivery = 1
    elif rest_type2 =='Dessert Parlor':
        Dessert_Parlor = 1
    elif rest_type2 =='Bar':
        Bar = 1
    elif rest_type2 =='Takeaway':
        Takeaway = 1
    elif rest_type2 =='Bakery':
        Bakery = 1
    elif rest_type2 =='Beverage Shop':
        Beverage_Shop = 1
    elif rest_type2 =='Pub':
        Pub = 1
    elif rest_type2 =='other':
        other = 1 











NumberOFcuisines = st.number_input("Enter Number Of Cuisines",min_value = 1,max_value=8)   

cuisines_list=['Select','North Indian','Chinese','South Indian','Fast Food','Biryani','Continental','Desserts','Cafe','Beverages','Italian','Bakery','Street Food','Pizza','Burger','Seafood','Ice Cream','Andhra','Mughlai','Rolls','American','Kerala','Asian','Momos','Finger Food','Juices','Salad','Arabian','Kebab','Mithai','Thai','Other']

North_Indian = 0
Chinese = 0
South_Indian =0
Fast_Food = 0
Biryani = 0
Continental = 0
Desserts =0
Cafe = 0
Beverages = 0
Italian = 0
Bakery = 0
Street_Food = 0
Pizza = 0
Burger = 0
Seafood = 0
Ice_Cream = 0
Andhra = 0
Mughlai = 0
Rolls = 0
American = 0
Kerala = 0
Asian = 0
Momos = 0
Finger_Food = 0
Juices = 0
Salad = 0
Arabian = 0
Kebab = 0
Mithai = 0
Thai = 0
Other2 = 0




if NumberOFcuisines == 1:
    cuisines = st.selectbox('First cuisines',cuisines_list)
    if cuisines == 'North Indian':
        North_Indian = 1
    elif cuisines == "South Indian":
        South_Indian = 1
    elif cuisines == "Fast Food":
        Fast_Food = 1
    elif cuisines == "Biryani":
        Biryani = 1                
    elif cuisines == "Continental":
        Continental = 1
    elif cuisines == "Desserts":
        Desserts = 1
    elif cuisines == "Cafe":
        Cafe = 1
    elif cuisines == "Beverages":
        Beverages = 1
    elif cuisines == "Italian":
        Italian = 1
    elif cuisines == "Bakery":
        Bakery = 1
    elif cuisines == "Street Food":
        Street_Food = 1
    elif cuisines == "Pizza":
        Pizza = 1
    elif cuisines == "Burger":
        Burger = 1
    elif cuisines == "Seafood":
        Seafood = 1
    elif cuisines == "Ice Cream":
        Ice_Cream = 1
    elif cuisines == "Andhra":
        Andhra = 1                
    elif cuisines == "Mughlai":
        Mughlai = 1
    elif cuisines == "Rolls":
        Rolls = 1
    elif cuisines == "American":
        American = 1
    elif cuisines == "Kerala":
        Kerala = 1
    elif cuisines == "Asian":
        Asian = 1
    elif cuisines == "Momos":
        Momos = 1
    elif cuisines == "Finger Food":
        Finger_Food = 1
    elif cuisines == "Juices":
        Juices = 1
    elif cuisines == "Salad":
        Salad = 1
    elif cuisines == "Arabian":
        Arabian = 1        
    elif cuisines == "Kebab":
        Kebab = 1
    elif cuisines == "Mithai":
        Mithai = 1
    elif cuisines == "Thai":
        Thai = 1
    elif cuisines == "Other":
        Other2 = 1       
        


if NumberOFcuisines == 2:
    cuisines12 = st.selectbox('Firt cuisines',cuisines_list)
    if cuisines12 == 'North Indian':
        North_Indian = 1
    elif cuisines12 == "South Indian":
        South_Indian = 1
    elif cuisines12 == "Fast Food":
        Fast_Food = 1
    elif cuisines12 == "Biryani":
        Biryani = 1                
    elif cuisines12 == "Continental":
        Continental = 1
    elif cuisines12 == "Desserts":
        Desserts = 1
    elif cuisines12 == "Cafe":
        Cafe = 1
    elif cuisines12 == "Beverages":
        Beverages = 1
    elif cuisines12 == "Italian":
        Italian = 1
    elif cuisines12 == "Bakery":
        Bakery = 1
    elif cuisines12 == "Street Food":
        Street_Food = 1
    elif cuisines12 == "Pizza":
        Pizza = 1
    elif cuisines12 == "Burger":
        Burger = 1
    elif cuisines12 == "Seafood":
        Seafood = 1
    elif cuisines12 == "Ice Cream":
        Ice_Cream = 1
    elif cuisines12 == "Andhra":
        Andhra = 1                
    elif cuisines12 == "Mughlai":
        Mughlai = 1
    elif cuisines12 == "Rolls":
        Rolls = 1
    elif cuisines12 == "American":
        American = 1
    elif cuisines12 == "Kerala":
        Kerala = 1
    elif cuisines12 == "Asian":
        Asian = 1
    elif cuisines12 == "Momos":
        Momos = 1
    elif cuisines12 == "Finger Food":
        Finger_Food = 1
    elif cuisines12 == "Juices":
        Juices = 1
    elif cuisines12 == "Salad":
        Salad = 1
    elif cuisines12 == "Arabian":
        Arabian = 1        
    elif cuisines12 == "Kebab":
        Kebab = 1
    elif cuisines12 == "Mithai":
        Mithai = 1
    elif cuisines12 == "Thai":
        Thai = 1
    elif cuisines12 == "Other":
        Other2 = 1           
    cuisines2 =  st.selectbox('Seconed cuisines ',cuisines_list)
    if cuisines2 == 'North Indian':
        North_Indian = 1
    elif cuisines2 == "South Indian":
        South_Indian = 1
    elif cuisines2 == "Fast Food":
        Fast_Food = 1
    elif cuisines2 == "Biryani":
        Biryani = 1                
    elif cuisines2 == "Continental":
        Continental = 1
    elif cuisines2 == "Desserts":
        Desserts = 1
    elif cuisines2 == "Cafe":
        Cafe = 1
    elif cuisines2 == "Beverages":
        Beverages = 1
    elif cuisines2 == "Italian":
        Italian = 1
    elif cuisines2 == "Bakery":
        Bakery = 1
    elif cuisines2 == "Street Food":
        Street_Food = 1
    elif cuisines2 == "Pizza":
        Pizza = 1
    elif cuisines2 == "Burger":
        Burger = 1
    elif cuisines2 == "Seafood":
        Seafood = 1
    elif cuisines2 == "Ice Cream":
        Ice_Cream = 1
    elif cuisines2 == "Andhra":
        Andhra = 1                
    elif cuisines2 == "Mughlai":
        Mughlai = 1
    elif cuisines2 == "Rolls":
        Rolls = 1
    elif cuisines2 == "American":
        American = 1
    elif cuisines2 == "Kerala":
        Kerala = 1
    elif cuisines2 == "Asian":
        Asian = 1
    elif cuisines2 == "Momos":
        Momos = 1
    elif cuisines2 == "Finger Food":
        Finger_Food = 1
    elif cuisines2 == "Juices":
        Juices = 1
    elif cuisines2 == "Salad":
        Salad = 1
    elif cuisines2 == "Arabian":
        Arabian = 1        
    elif cuisines2 == "Kebab":
        Kebab = 1
    elif cuisines2 == "Mithai":
        Mithai = 1
    elif cuisines2 == "Thai":
        Thai = 1
    elif cuisines2 == "Other":
        Other2 = 1           
if NumberOFcuisines ==3:
    cuisines13 = st.selectbox('Firt cuisines',cuisines_list)
    if cuisines13 == 'North Indian':
        North_Indian = 1
    elif cuisines13 == "South Indian":
        South_Indian = 1
    elif cuisines13 == "Fast Food":
        Fast_Food = 1
    elif cuisines13 == "Biryani":
        Biryani = 1                
    elif cuisines13 == "Continental":
        Continental = 1
    elif cuisines13 == "Desserts":
        Desserts = 1
    elif cuisines13 == "Cafe":
        Cafe = 1
    elif cuisines13 == "Beverages":
        Beverages = 1
    elif cuisines13 == "Italian":
        Italian = 1
    elif cuisines13 == "Bakery":
        Bakery = 1
    elif cuisines13 == "Street Food":
        Street_Food = 1
    elif cuisines13 == "Pizza":
        Pizza = 1
    elif cuisines13 == "Burger":
        Burger = 1
    elif cuisines13 == "Seafood":
        Seafood = 1
    elif cuisines13 == "Ice Cream":
        Ice_Cream = 1
    elif cuisines13 == "Andhra":
        Andhra = 1                
    elif cuisines13 == "Mughlai":
        Mughlai = 1
    elif cuisines13 == "Rolls":
        Rolls = 1
    elif cuisines13 == "American":
        American = 1
    elif cuisines13 == "Kerala":
        Kerala = 1
    elif cuisines13 == "Asian":
        Asian = 1
    elif cuisines13 == "Momos":
        Momos = 1
    elif cuisines13 == "Finger Food":
        Finger_Food = 1
    elif cuisines13 == "Juices":
        Juices = 1
    elif cuisines13 == "Salad":
        Salad = 1
    elif cuisines13 == "Arabian":
        Arabian = 1        
    elif cuisines13 == "Kebab":
        Kebab = 1
    elif cuisines13 == "Mithai":
        Mithai = 1
    elif cuisines13 == "Thai":
        Thai = 1
    elif cuisines13 == "Other":
        Other2 = 1           
    cuisines23 =  st.selectbox('Seconed cuisines ',cuisines_list)
    if cuisines23 == 'North Indian':
        North_Indian = 1
    elif cuisines23 == "South Indian":
        South_Indian = 1
    elif cuisines23 == "Fast Food":
        Fast_Food = 1
    elif cuisines23 == "Biryani":
        Biryani = 1                
    elif cuisines23 == "Continental":
        Continental = 1
    elif cuisines23 == "Desserts":
        Desserts = 1
    elif cuisines23 == "Cafe":
        Cafe = 1
    elif cuisines23 == "Beverages":
        Beverages = 1
    elif cuisines23 == "Italian":
        Italian = 1
    elif cuisines23 == "Bakery":
        Bakery = 1
    elif cuisines23 == "Street Food":
        Street_Food = 1
    elif cuisines23 == "Pizza":
        Pizza = 1
    elif cuisines23 == "Burger":
        Burger = 1
    elif cuisines23 == "Seafood":
        Seafood = 1
    elif cuisines23 == "Ice Cream":
        Ice_Cream = 1
    elif cuisines23 == "Andhra":
        Andhra = 1                
    elif cuisines23 == "Mughlai":
        Mughlai = 1
    elif cuisines23 == "Rolls":
        Rolls = 1
    elif cuisines23 == "American":
        American = 1
    elif cuisines23 == "Kerala":
        Kerala = 1
    elif cuisines23 == "Asian":
        Asian = 1
    elif cuisines23 == "Momos":
        Momos = 1
    elif cuisines23 == "Finger Food":
        Finger_Food = 1
    elif cuisines23 == "Juices":
        Juices = 1
    elif cuisines23 == "Salad":
        Salad = 1
    elif cuisines23 == "Arabian":
        Arabian = 1        
    elif cuisines23 == "Kebab":
        Kebab = 1
    elif cuisines23 == "Mithai":
        Mithai = 1
    elif cuisines23 == "Thai":
        Thai = 1
    elif cuisines23 == "Other":
        Other2 = 1           
    cuisines3 =  st.selectbox('Thired cuisines ',cuisines_list)
    if cuisines3 == 'North Indian':
        North_Indian = 1
    elif cuisines3 == "South Indian":
        South_Indian = 1
    elif cuisines3 == "Fast Food":
        Fast_Food = 1
    elif cuisines3 == "Biryani":
        Biryani = 1                
    elif cuisines3 == "Continental":
        Continental = 1
    elif cuisines3 == "Desserts":
        Desserts = 1
    elif cuisines3 == "Cafe":
        Cafe = 1
    elif cuisines3 == "Beverages":
        Beverages = 1
    elif cuisines3 == "Italian":
        Italian = 1
    elif cuisines3 == "Bakery":
        Bakery = 1
    elif cuisines3 == "Street Food":
        Street_Food = 1
    elif cuisines3 == "Pizza":
        Pizza = 1
    elif cuisines3 == "Burger":
        Burger = 1
    elif cuisines3 == "Seafood":
        Seafood = 1
    elif cuisines3 == "Ice Cream":
        Ice_Cream = 1
    elif cuisines3 == "Andhra":
        Andhra = 1                
    elif cuisines3 == "Mughlai":
        Mughlai = 1
    elif cuisines3 == "Rolls":
        Rolls = 1
    elif cuisines3 == "American":
        American = 1
    elif cuisines3 == "Kerala":
        Kerala = 1
    elif cuisines3 == "Asian":
        Asian = 1
    elif cuisines3 == "Momos":
        Momos = 1
    elif cuisines3 == "Finger Food":
        Finger_Food = 1
    elif cuisines3 == "Juices":
        Juices = 1
    elif cuisines3 == "Salad":
        Salad = 1
    elif cuisines3 == "Arabian":
        Arabian = 1        
    elif cuisines3 == "Kebab":
        Kebab = 1
    elif cuisines3 == "Mithai":
        Mithai = 1
    elif cuisines3 == "Thai":
        Thai = 1
    elif cuisines3 == "Other":
        Other2 = 1           
if NumberOFcuisines ==4:
    cuisines14 = st.selectbox('Firt cuisines',cuisines_list)
    if cuisines14 == 'North Indian':
        North_Indian = 1
    elif cuisines14 == "South Indian":
        South_Indian = 1
    elif cuisines14 == "Fast Food":
        Fast_Food = 1
    elif cuisines14 == "Biryani":
        Biryani = 1                
    elif cuisines14 == "Continental":
        Continental = 1
    elif cuisines14 == "Desserts":
        Desserts = 1
    elif cuisines14 == "Cafe":
        Cafe = 1
    elif cuisines14 == "Beverages":
        Beverages = 1
    elif cuisines14 == "Italian":
        Italian = 1
    elif cuisines14 == "Bakery":
        Bakery = 1
    elif cuisines14 == "Street Food":
        Street_Food = 1
    elif cuisines14 == "Pizza":
        Pizza = 1
    elif cuisines14 == "Burger":
        Burger = 1
    elif cuisines14 == "Seafood":
        Seafood = 1
    elif cuisines14 == "Ice Cream":
        Ice_Cream = 1
    elif cuisines14 == "Andhra":
        Andhra = 1                
    elif cuisines14 == "Mughlai":
        Mughlai = 1
    elif cuisines14 == "Rolls":
        Rolls = 1
    elif cuisines14 == "American":
        American = 1
    elif cuisines14 == "Kerala":
        Kerala = 1
    elif cuisines14 == "Asian":
        Asian = 1
    elif cuisines14 == "Momos":
        Momos = 1
    elif cuisines14 == "Finger Food":
        Finger_Food = 1
    elif cuisines14 == "Juices":
        Juices = 1
    elif cuisines14 == "Salad":
        Salad = 1
    elif cuisines14 == "Arabian":
        Arabian = 1        
    elif cuisines14 == "Kebab":
        Kebab = 1
    elif cuisines14 == "Mithai":
        Mithai = 1
    elif cuisines14 == "Thai":
        Thai = 1
    elif cuisines14 == "Other":
        Other2 = 1           
    cuisines24 =  st.selectbox('Seconed cuisines ',cuisines_list)
    if cuisines24 == 'North Indian':
        North_Indian = 1
    elif cuisines24 == "South Indian":
        South_Indian = 1
    elif cuisines24 == "Fast Food":
        Fast_Food = 1
    elif cuisines24 == "Biryani":
        Biryani = 1                
    elif cuisines24 == "Continental":
        Continental = 1
    elif cuisines24 == "Desserts":
        Desserts = 1
    elif cuisines24 == "Cafe":
        Cafe = 1
    elif cuisines24 == "Beverages":
        Beverages = 1
    elif cuisines24 == "Italian":
        Italian = 1
    elif cuisines24 == "Bakery":
        Bakery = 1
    elif cuisines24 == "Street Food":
        Street_Food = 1
    elif cuisines24 == "Pizza":
        Pizza = 1
    elif cuisines24 == "Burger":
        Burger = 1
    elif cuisines24 == "Seafood":
        Seafood = 1
    elif cuisines24 == "Ice Cream":
        Ice_Cream = 1
    elif cuisines24 == "Andhra":
        Andhra = 1                
    elif cuisines24 == "Mughlai":
        Mughlai = 1
    elif cuisines24 == "Rolls":
        Rolls = 1
    elif cuisines24 == "American":
        American = 1
    elif cuisines24 == "Kerala":
        Kerala = 1
    elif cuisines24 == "Asian":
        Asian = 1
    elif cuisines24 == "Momos":
        Momos = 1
    elif cuisines24 == "Finger Food":
        Finger_Food = 1
    elif cuisines24 == "Juices":
        Juices = 1
    elif cuisines24 == "Salad":
        Salad = 1
    elif cuisines24 == "Arabian":
        Arabian = 1        
    elif cuisines24 == "Kebab":
        Kebab = 1
    elif cuisines24 == "Mithai":
        Mithai = 1
    elif cuisines24 == "Thai":
        Thai = 1
    elif cuisines24 == "Other":
        Other2 = 1           
    cuisines34 =  st.selectbox('Thired cuisines ',cuisines_list)
    if cuisines34 == 'North Indian':
        North_Indian = 1
    elif cuisines34 == "South Indian":
        South_Indian = 1
    elif cuisines34 == "Fast Food":
        Fast_Food = 1
    elif cuisines34 == "Biryani":
        Biryani = 1                
    elif cuisines34 == "Continental":
        Continental = 1
    elif cuisines34 == "Desserts":
        Desserts = 1
    elif cuisines34 == "Cafe":
        Cafe = 1
    elif cuisines34 == "Beverages":
        Beverages = 1
    elif cuisines34 == "Italian":
        Italian = 1
    elif cuisines34 == "Bakery":
        Bakery = 1
    elif cuisines34 == "Street Food":
        Street_Food = 1
    elif cuisines34 == "Pizza":
        Pizza = 1
    elif cuisines34 == "Burger":
        Burger = 1
    elif cuisines34 == "Seafood":
        Seafood = 1
    elif cuisines34 == "Ice Cream":
        Ice_Cream = 1
    elif cuisines34 == "Andhra":
        Andhra = 1                
    elif cuisines34 == "Mughlai":
        Mughlai = 1
    elif cuisines34 == "Rolls":
        Rolls = 1
    elif cuisines34 == "American":
        American = 1
    elif cuisines34 == "Kerala":
        Kerala = 1
    elif cuisines34 == "Asian":
        Asian = 1
    elif cuisines34 == "Momos":
        Momos = 1
    elif cuisines34 == "Finger Food":
        Finger_Food = 1
    elif cuisines34 == "Juices":
        Juices = 1
    elif cuisines34 == "Salad":
        Salad = 1
    elif cuisines34 == "Arabian":
        Arabian = 1        
    elif cuisines34 == "Kebab":
        Kebab = 1
    elif cuisines34 == "Mithai":
        Mithai = 1
    elif cuisines34 == "Thai":
        Thai = 1
    elif cuisines34 == "Other":
        Other2 = 1           
    cuisines4 =  st.selectbox('Fourth cuisines ',cuisines_list)
    if cuisines4 == 'North Indian':
        North_Indian = 1
    elif cuisines4 == "South Indian":
        South_Indian = 1
    elif cuisines4 == "Fast Food":
        Fast_Food = 1
    elif cuisines4 == "Biryani":
        Biryani = 1                
    elif cuisines4 == "Continental":
        Continental = 1
    elif cuisines4 == "Desserts":
        Desserts = 1
    elif cuisines4 == "Cafe":
        Cafe = 1
    elif cuisines4 == "Beverages":
        Beverages = 1
    elif cuisines4 == "Italian":
        Italian = 1
    elif cuisines4 == "Bakery":
        Bakery = 1
    elif cuisines4 == "Street Food":
        Street_Food = 1
    elif cuisines4 == "Pizza":
        Pizza = 1
    elif cuisines4 == "Burger":
        Burger = 1
    elif cuisines4 == "Seafood":
        Seafood = 1
    elif cuisines4 == "Ice Cream":
        Ice_Cream = 1
    elif cuisines4 == "Andhra":
        Andhra = 1                
    elif cuisines4 == "Mughlai":
        Mughlai = 1
    elif cuisines4 == "Rolls":
        Rolls = 1
    elif cuisines4 == "American":
        American = 1
    elif cuisines4 == "Kerala":
        Kerala = 1
    elif cuisines4 == "Asian":
        Asian = 1
    elif cuisines4 == "Momos":
        Momos = 1
    elif cuisines4 == "Finger Food":
        Finger_Food = 1
    elif cuisines4 == "Juices":
        Juices = 1
    elif cuisines4 == "Salad":
        Salad = 1
    elif cuisines4 == "Arabian":
        Arabian = 1        
    elif cuisines4 == "Kebab":
        Kebab = 1
    elif cuisines4 == "Mithai":
        Mithai = 1
    elif cuisines4 == "Thai":
        Thai = 1
    elif cuisines4 == "Other":
        Other2 = 1           
if NumberOFcuisines ==5:
    cuisines15 = st.selectbox('Firt cuisines',cuisines_list)
    if cuisines15 == 'North Indian':
        North_Indian = 1
    elif cuisines15 == "South Indian":
        South_Indian = 1
    elif cuisines15 == "Fast Food":
        Fast_Food = 1
    elif cuisines15 == "Biryani":
        Biryani = 1                
    elif cuisines15 == "Continental":
        Continental = 1
    elif cuisines15 == "Desserts":
        Desserts = 1
    elif cuisines15 == "Cafe":
        Cafe = 1
    elif cuisines15 == "Beverages":
        Beverages = 1
    elif cuisines15 == "Italian":
        Italian = 1
    elif cuisines15 == "Bakery":
        Bakery = 1
    elif cuisines15 == "Street Food":
        Street_Food = 1
    elif cuisines15 == "Pizza":
        Pizza = 1
    elif cuisines15 == "Burger":
        Burger = 1
    elif cuisines15 == "Seafood":
        Seafood = 1
    elif cuisines15 == "Ice Cream":
        Ice_Cream = 1
    elif cuisines15 == "Andhra":
        Andhra = 1                
    elif cuisines15 == "Mughlai":
        Mughlai = 1
    elif cuisines15 == "Rolls":
        Rolls = 1
    elif cuisines15 == "American":
        American = 1
    elif cuisines15 == "Kerala":
        Kerala = 1
    elif cuisines15 == "Asian":
        Asian = 1
    elif cuisines15 == "Momos":
        Momos = 1
    elif cuisines15 == "Finger Food":
        Finger_Food = 1
    elif cuisines15 == "Juices":
        Juices = 1
    elif cuisines15 == "Salad":
        Salad = 1
    elif cuisines15 == "Arabian":
        Arabian = 1        
    elif cuisines15 == "Kebab":
        Kebab = 1
    elif cuisines15 == "Mithai":
        Mithai = 1
    elif cuisines15 == "Thai":
        Thai = 1
    elif cuisines15 == "Other":
        Other2 = 1           
    cuisines25 =  st.selectbox('Seconed cuisines ',cuisines_list)
    if cuisines25 == 'North Indian':
        North_Indian = 1
    elif cuisines25 == "South Indian":
        South_Indian = 1
    elif cuisines25 == "Fast Food":
        Fast_Food = 1
    elif cuisines25 == "Biryani":
        Biryani = 1                
    elif cuisines25 == "Continental":
        Continental = 1
    elif cuisines25 == "Desserts":
        Desserts = 1
    elif cuisines25 == "Cafe":
        Cafe = 1
    elif cuisines25 == "Beverages":
        Beverages = 1
    elif cuisines25 == "Italian":
        Italian = 1
    elif cuisines25 == "Bakery":
        Bakery = 1
    elif cuisines25 == "Street Food":
        Street_Food = 1
    elif cuisines25 == "Pizza":
        Pizza = 1
    elif cuisines25 == "Burger":
        Burger = 1
    elif cuisines25 == "Seafood":
        Seafood = 1
    elif cuisines25 == "Ice Cream":
        Ice_Cream = 1
    elif cuisines25 == "Andhra":
        Andhra = 1                
    elif cuisines25 == "Mughlai":
        Mughlai = 1
    elif cuisines25 == "Rolls":
        Rolls = 1
    elif cuisines25 == "American":
        American = 1
    elif cuisines25 == "Kerala":
        Kerala = 1
    elif cuisines25 == "Asian":
        Asian = 1
    elif cuisines25 == "Momos":
        Momos = 1
    elif cuisines25 == "Finger Food":
        Finger_Food = 1
    elif cuisines25 == "Juices":
        Juices = 1
    elif cuisines25 == "Salad":
        Salad = 1
    elif cuisines25 == "Arabian":
        Arabian = 1        
    elif cuisines25 == "Kebab":
        Kebab = 1
    elif cuisines25 == "Mithai":
        Mithai = 1
    elif cuisines25 == "Thai":
        Thai = 1
    elif cuisines25 == "Other":
        Other2 = 1           
    cuisines35 =  st.selectbox('Thired cuisines ',cuisines_list)
    if cuisines35 == 'North Indian':
        North_Indian = 1
    elif cuisines35 == "South Indian":
        South_Indian = 1
    elif cuisines35 == "Fast Food":
        Fast_Food = 1
    elif cuisines35 == "Biryani":
        Biryani = 1                
    elif cuisines35 == "Continental":
        Continental = 1
    elif cuisines35 == "Desserts":
        Desserts = 1
    elif cuisines35 == "Cafe":
        Cafe = 1
    elif cuisines35 == "Beverages":
        Beverages = 1
    elif cuisines35 == "Italian":
        Italian = 1
    elif cuisines35 == "Bakery":
        Bakery = 1
    elif cuisines35 == "Street Food":
        Street_Food = 1
    elif cuisines35 == "Pizza":
        Pizza = 1
    elif cuisines35 == "Burger":
        Burger = 1
    elif cuisines35 == "Seafood":
        Seafood = 1
    elif cuisines35 == "Ice Cream":
        Ice_Cream = 1
    elif cuisines35 == "Andhra":
        Andhra = 1                
    elif cuisines35 == "Mughlai":
        Mughlai = 1
    elif cuisines35 == "Rolls":
        Rolls = 1
    elif cuisines35 == "American":
        American = 1
    elif cuisines35 == "Kerala":
        Kerala = 1
    elif cuisines35 == "Asian":
        Asian = 1
    elif cuisines35 == "Momos":
        Momos = 1
    elif cuisines35 == "Finger Food":
        Finger_Food = 1
    elif cuisines35 == "Juices":
        Juices = 1
    elif cuisines35 == "Salad":
        Salad = 1
    elif cuisines35 == "Arabian":
        Arabian = 1        
    elif cuisines35 == "Kebab":
        Kebab = 1
    elif cuisines35 == "Mithai":
        Mithai = 1
    elif cuisines35 == "Thai":
        Thai = 1
    elif cuisines35 == "Other":
        Other2 = 1           
    cuisines45 =  st.selectbox('Fourth cuisines ',cuisines_list)
    if cuisines45 == 'North Indian':
        North_Indian = 1
    elif cuisines45 == "South Indian":
        South_Indian = 1
    elif cuisines45 == "Fast Food":
        Fast_Food = 1
    elif cuisines45 == "Biryani":
        Biryani = 1                
    elif cuisines45 == "Continental":
        Continental = 1
    elif cuisines45 == "Desserts":
        Desserts = 1
    elif cuisines45 == "Cafe":
        Cafe = 1
    elif cuisines45 == "Beverages":
        Beverages = 1
    elif cuisines45 == "Italian":
        Italian = 1
    elif cuisines45 == "Bakery":
        Bakery = 1
    elif cuisines45 == "Street Food":
        Street_Food = 1
    elif cuisines45 == "Pizza":
        Pizza = 1
    elif cuisines45 == "Burger":
        Burger = 1
    elif cuisines45 == "Seafood":
        Seafood = 1
    elif cuisines45 == "Ice Cream":
        Ice_Cream = 1
    elif cuisines45 == "Andhra":
        Andhra = 1                
    elif cuisines45 == "Mughlai":
        Mughlai = 1
    elif cuisines45 == "Rolls":
        Rolls = 1
    elif cuisines45 == "American":
        American = 1
    elif cuisines45 == "Kerala":
        Kerala = 1
    elif cuisines45 == "Asian":
        Asian = 1
    elif cuisines45 == "Momos":
        Momos = 1
    elif cuisines45 == "Finger Food":
        Finger_Food = 1
    elif cuisines45 == "Juices":
        Juices = 1
    elif cuisines45 == "Salad":
        Salad = 1
    elif cuisines45 == "Arabian":
        Arabian = 1        
    elif cuisines45 == "Kebab":
        Kebab = 1
    elif cuisines45 == "Mithai":
        Mithai = 1
    elif cuisines45 == "Thai":
        Thai = 1
    elif cuisines45 == "Other":
        Other2 = 1           
    cuisines5 =  st.selectbox('Fifth cuisines ',cuisines_list)
    if cuisines5 == 'North Indian':
        North_Indian = 1
    elif cuisines5 == "South Indian":
        South_Indian = 1
    elif cuisines5 == "Fast Food":
        Fast_Food = 1
    elif cuisines5 == "Biryani":
        Biryani = 1                
    elif cuisines5 == "Continental":
        Continental = 1
    elif cuisines5 == "Desserts":
        Desserts = 1
    elif cuisines5 == "Cafe":
        Cafe = 1
    elif cuisines5 == "Beverages":
        Beverages = 1
    elif cuisines5 == "Italian":
        Italian = 1
    elif cuisines5 == "Bakery":
        Bakery = 1
    elif cuisines5 == "Street Food":
        Street_Food = 1
    elif cuisines5 == "Pizza":
        Pizza = 1
    elif cuisines5 == "Burger":
        Burger = 1
    elif cuisines5 == "Seafood":
        Seafood = 1
    elif cuisines5 == "Ice Cream":
        Ice_Cream = 1
    elif cuisines5 == "Andhra":
        Andhra = 1                
    elif cuisines5 == "Mughlai":
        Mughlai = 1
    elif cuisines5 == "Rolls":
        Rolls = 1
    elif cuisines5 == "American":
        American = 1
    elif cuisines5 == "Kerala":
        Kerala = 1
    elif cuisines5 == "Asian":
        Asian = 1
    elif cuisines5 == "Momos":
        Momos = 1
    elif cuisines5 == "Finger Food":
        Finger_Food = 1
    elif cuisines5 == "Juices":
        Juices = 1
    elif cuisines5 == "Salad":
        Salad = 1
    elif cuisines5 == "Arabian":
        Arabian = 1        
    elif cuisines5 == "Kebab":
        Kebab = 1
    elif cuisines5 == "Mithai":
        Mithai = 1
    elif cuisines5 == "Thai":
        Thai = 1
    elif cuisines5 == "Other":
        Other2 = 1           

if NumberOFcuisines ==6:  
    cuisines16 = st.selectbox('Firt cuisines',cuisines_list)
    if cuisines16 == 'North Indian':
        North_Indian = 1
    elif cuisines16 == "South Indian":
        South_Indian = 1
    elif cuisines16 == "Fast Food":
        Fast_Food = 1
    elif cuisines16 == "Biryani":
        Biryani = 1                
    elif cuisines16 == "Continental":
        Continental = 1
    elif cuisines16 == "Desserts":
        Desserts = 1
    elif cuisines16 == "Cafe":
        Cafe = 1
    elif cuisines16 == "Beverages":
        Beverages = 1
    elif cuisines16 == "Italian":
        Italian = 1
    elif cuisines16 == "Bakery":
        Bakery = 1
    elif cuisines16 == "Street Food":
        Street_Food = 1
    elif cuisines16 == "Pizza":
        Pizza = 1
    elif cuisines16 == "Burger":
        Burger = 1
    elif cuisines16 == "Seafood":
        Seafood = 1
    elif cuisines16 == "Ice Cream":
        Ice_Cream = 1
    elif cuisines16 == "Andhra":
        Andhra = 1                
    elif cuisines16 == "Mughlai":
        Mughlai = 1
    elif cuisines16 == "Rolls":
        Rolls = 1
    elif cuisines16 == "American":
        American = 1
    elif cuisines16 == "Kerala":
        Kerala = 1
    elif cuisines16 == "Asian":
        Asian = 1
    elif cuisines16 == "Momos":
        Momos = 1
    elif cuisines16 == "Finger Food":
        Finger_Food = 1
    elif cuisines16 == "Juices":
        Juices = 1
    elif cuisines16 == "Salad":
        Salad = 1
    elif cuisines16 == "Arabian":
        Arabian = 1        
    elif cuisines16 == "Kebab":
        Kebab = 1
    elif cuisines16 == "Mithai":
        Mithai = 1
    elif cuisines16 == "Thai":
        Thai = 1
    elif cuisines16 == "Other":
        Other2 = 1            
    cuisines26 =  st.selectbox('Seconed cuisines ',cuisines_list)
    if cuisines26 == 'North Indian':
        North_Indian = 1
    elif cuisines26 == "South Indian":
        South_Indian = 1
    elif cuisines26 == "Fast Food":
        Fast_Food = 1
    elif cuisines26 == "Biryani":
        Biryani = 1                
    elif cuisines26 == "Continental":
        Continental = 1
    elif cuisines26 == "Desserts":
        Desserts = 1
    elif cuisines26 == "Cafe":
        Cafe = 1
    elif cuisines26 == "Beverages":
        Beverages = 1
    elif cuisines26 == "Italian":
        Italian = 1
    elif cuisines26 == "Bakery":
        Bakery = 1
    elif cuisines26 == "Street Food":
        Street_Food = 1
    elif cuisines26 == "Pizza":
        Pizza = 1
    elif cuisines26 == "Burger":
        Burger = 1
    elif cuisines26 == "Seafood":
        Seafood = 1
    elif cuisines26 == "Ice Cream":
        Ice_Cream = 1
    elif cuisines26 == "Andhra":
        Andhra = 1                
    elif cuisines26 == "Mughlai":
        Mughlai = 1
    elif cuisines26 == "Rolls":
        Rolls = 1
    elif cuisines26 == "American":
        American = 1
    elif cuisines26 == "Kerala":
        Kerala = 1
    elif cuisines26 == "Asian":
        Asian = 1
    elif cuisines26 == "Momos":
        Momos = 1
    elif cuisines26 == "Finger Food":
        Finger_Food = 1
    elif cuisines26 == "Juices":
        Juices = 1
    elif cuisines26 == "Salad":
        Salad = 1
    elif cuisines26 == "Arabian":
        Arabian = 1        
    elif cuisines26 == "Kebab":
        Kebab = 1
    elif cuisines26 == "Mithai":
        Mithai = 1
    elif cuisines26 == "Thai":
        Thai = 1
    elif cuisines26 == "Other":
        Other2 = 1           
    cuisines36 =  st.selectbox('Thired cuisines ',cuisines_list)
    if cuisines36 == 'North Indian':
        North_Indian = 1
    elif cuisines36 == "South Indian":
        South_Indian = 1
    elif cuisines36 == "Fast Food":
        Fast_Food = 1
    elif cuisines36 == "Biryani":
        Biryani = 1                
    elif cuisines36 == "Continental":
        Continental = 1
    elif cuisines36 == "Desserts":
        Desserts = 1
    elif cuisines36 == "Cafe":
        Cafe = 1
    elif cuisines36 == "Beverages":
        Beverages = 1
    elif cuisines36 == "Italian":
        Italian = 1
    elif cuisines36 == "Bakery":
        Bakery = 1
    elif cuisines36 == "Street Food":
        Street_Food = 1
    elif cuisines36 == "Pizza":
        Pizza = 1
    elif cuisines36 == "Burger":
        Burger = 1
    elif cuisines36 == "Seafood":
        Seafood = 1
    elif cuisines36 == "Ice Cream":
        Ice_Cream = 1
    elif cuisines36 == "Andhra":
        Andhra = 1                
    elif cuisines36 == "Mughlai":
        Mughlai = 1
    elif cuisines36 == "Rolls":
        Rolls = 1
    elif cuisines36 == "American":
        American = 1
    elif cuisines36 == "Kerala":
        Kerala = 1
    elif cuisines36 == "Asian":
        Asian = 1
    elif cuisines36 == "Momos":
        Momos = 1
    elif cuisines36 == "Finger Food":
        Finger_Food = 1
    elif cuisines36 == "Juices":
        Juices = 1
    elif cuisines36 == "Salad":
        Salad = 1
    elif cuisines36 == "Arabian":
        Arabian = 1        
    elif cuisines36 == "Kebab":
        Kebab = 1
    elif cuisines36 == "Mithai":
        Mithai = 1
    elif cuisines36 == "Thai":
        Thai = 1
    elif cuisines36 == "Other":
        Other2 = 1           
    cuisines46 =  st.selectbox('Fourth cuisines ',cuisines_list)
    if cuisines46 == 'North Indian':
        North_Indian = 1
    elif cuisines46 == "South Indian":
        South_Indian = 1
    elif cuisines46 == "Fast Food":
        Fast_Food = 1
    elif cuisines46 == "Biryani":
        Biryani = 1                
    elif cuisines46 == "Continental":
        Continental = 1
    elif cuisines46 == "Desserts":
        Desserts = 1
    elif cuisines46 == "Cafe":
        Cafe = 1
    elif cuisines46 == "Beverages":
        Beverages = 1
    elif cuisines46 == "Italian":
        Italian = 1
    elif cuisines46 == "Bakery":
        Bakery = 1
    elif cuisines46 == "Street Food":
        Street_Food = 1
    elif cuisines46 == "Pizza":
        Pizza = 1
    elif cuisines46 == "Burger":
        Burger = 1
    elif cuisines46 == "Seafood":
        Seafood = 1
    elif cuisines46 == "Ice Cream":
        Ice_Cream = 1
    elif cuisines46 == "Andhra":
        Andhra = 1                
    elif cuisines46 == "Mughlai":
        Mughlai = 1
    elif cuisines46 == "Rolls":
        Rolls = 1
    elif cuisines46 == "American":
        American = 1
    elif cuisines46 == "Kerala":
        Kerala = 1
    elif cuisines46 == "Asian":
        Asian = 1
    elif cuisines46 == "Momos":
        Momos = 1
    elif cuisines46 == "Finger Food":
        Finger_Food = 1
    elif cuisines46 == "Juices":
        Juices = 1
    elif cuisines46 == "Salad":
        Salad = 1
    elif cuisines46 == "Arabian":
        Arabian = 1        
    elif cuisines46 == "Kebab":
        Kebab = 1
    elif cuisines46 == "Mithai":
        Mithai = 1
    elif cuisines46 == "Thai":
        Thai = 1
    elif cuisines46 == "Other":
        Other2 = 1           
    cuisines56 =  st.selectbox('Fifth cuisines ',cuisines_list)
    if cuisines56 == 'North Indian':
        North_Indian = 1
    elif cuisines56 == "South Indian":
        South_Indian = 1
    elif cuisines56 == "Fast Food":
        Fast_Food = 1
    elif cuisines56 == "Biryani":
        Biryani = 1                
    elif cuisines56 == "Continental":
        Continental = 1
    elif cuisines56 == "Desserts":
        Desserts = 1
    elif cuisines56 == "Cafe":
        Cafe = 1
    elif cuisines56 == "Beverages":
        Beverages = 1
    elif cuisines56 == "Italian":
        Italian = 1
    elif cuisines56 == "Bakery":
        Bakery = 1
    elif cuisines56 == "Street Food":
        Street_Food = 1
    elif cuisines56 == "Pizza":
        Pizza = 1
    elif cuisines56 == "Burger":
        Burger = 1
    elif cuisines56 == "Seafood":
        Seafood = 1
    elif cuisines56 == "Ice Cream":
        Ice_Cream = 1
    elif cuisines56 == "Andhra":
        Andhra = 1                
    elif cuisines56 == "Mughlai":
        Mughlai = 1
    elif cuisines56 == "Rolls":
        Rolls = 1
    elif cuisines56 == "American":
        American = 1
    elif cuisines56 == "Kerala":
        Kerala = 1
    elif cuisines56 == "Asian":
        Asian = 1
    elif cuisines56 == "Momos":
        Momos = 1
    elif cuisines56 == "Finger Food":
        Finger_Food = 1
    elif cuisines56 == "Juices":
        Juices = 1
    elif cuisines56 == "Salad":
        Salad = 1
    elif cuisines56 == "Arabian":
        Arabian = 1        
    elif cuisines56 == "Kebab":
        Kebab = 1
    elif cuisines56 == "Mithai":
        Mithai = 1
    elif cuisines56 == "Thai":
        Thai = 1
    elif cuisines56 == "Other":
        Other2 = 1           
    cuisines6 =  st.selectbox('Sixth cuisines ',cuisines_list)
    if cuisines6 == 'North Indian':
        North_Indian = 1
    elif cuisines6 == "South Indian":
        South_Indian = 1
    elif cuisines6 == "Fast Food":
        Fast_Food = 1
    elif cuisines6 == "Biryani":
        Biryani = 1                
    elif cuisines6 == "Continental":
        Continental = 1
    elif cuisines6 == "Desserts":
        Desserts = 1
    elif cuisines6 == "Cafe":
        Cafe = 1
    elif cuisines6 == "Beverages":
        Beverages = 1
    elif cuisines6 == "Italian":
        Italian = 1
    elif cuisines6 == "Bakery":
        Bakery = 1
    elif cuisines6 == "Street Food":
        Street_Food = 1
    elif cuisines6 == "Pizza":
        Pizza = 1
    elif cuisines6 == "Burger":
        Burger = 1
    elif cuisines6 == "Seafood":
        Seafood = 1
    elif cuisines6 == "Ice Cream":
        Ice_Cream = 1
    elif cuisines6 == "Andhra":
        Andhra = 1                
    elif cuisines6 == "Mughlai":
        Mughlai = 1
    elif cuisines6 == "Rolls":
        Rolls = 1
    elif cuisines6 == "American":
        American = 1
    elif cuisines6 == "Kerala":
        Kerala = 1
    elif cuisines6 == "Asian":
        Asian = 1
    elif cuisines6 == "Momos":
        Momos = 1
    elif cuisines6 == "Finger Food":
        Finger_Food = 1
    elif cuisines6 == "Juices":
        Juices = 1
    elif cuisines6 == "Salad":
        Salad = 1
    elif cuisines6 == "Arabian":
        Arabian = 1        
    elif cuisines6 == "Kebab":
        Kebab = 1
    elif cuisines6 == "Mithai":
        Mithai = 1
    elif cuisines6 == "Thai":
        Thai = 1
    elif cuisines6 == "Other":
        Other2 = 1           

if NumberOFcuisines ==7:
    cuisines17 = st.selectbox('Firt cuisines',cuisines_list)
    if cuisines17 == 'North Indian':
        North_Indian = 1
    elif cuisines17 == "South Indian":
        South_Indian = 1
    elif cuisines17 == "Fast Food":
        Fast_Food = 1
    elif cuisines17 == "Biryani":
        Biryani = 1                
    elif cuisines17 == "Continental":
        Continental = 1
    elif cuisines17 == "Desserts":
        Desserts = 1
    elif cuisines17 == "Cafe":
        Cafe = 1
    elif cuisines17 == "Beverages":
        Beverages = 1
    elif cuisines17 == "Italian":
        Italian = 1
    elif cuisines17 == "Bakery":
        Bakery = 1
    elif cuisines17 == "Street Food":
        Street_Food = 1
    elif cuisines17 == "Pizza":
        Pizza = 1
    elif cuisines17 == "Burger":
        Burger = 1
    elif cuisines17 == "Seafood":
        Seafood = 1
    elif cuisines17 == "Ice Cream":
        Ice_Cream = 1
    elif cuisines17 == "Andhra":
        Andhra = 1                
    elif cuisines17 == "Mughlai":
        Mughlai = 1
    elif cuisines17 == "Rolls":
        Rolls = 1
    elif cuisines17 == "American":
        American = 1
    elif cuisines17 == "Kerala":
        Kerala = 1
    elif cuisines17 == "Asian":
        Asian = 1
    elif cuisines17 == "Momos":
        Momos = 1
    elif cuisines17 == "Finger Food":
        Finger_Food = 1
    elif cuisines17 == "Juices":
        Juices = 1
    elif cuisines17 == "Salad":
        Salad = 1
    elif cuisines17 == "Arabian":
        Arabian = 1        
    elif cuisines17 == "Kebab":
        Kebab = 1
    elif cuisines17 == "Mithai":
        Mithai = 1
    elif cuisines17 == "Thai":
        Thai = 1
    elif cuisines17 == "Other":
        Other2 = 1           
    cuisines27 =  st.selectbox('Seconed cuisines ',cuisines_list)
    if cuisines27 == 'North Indian':
        North_Indian = 1
    elif cuisines27 == "South Indian":
        South_Indian = 1
    elif cuisines27 == "Fast Food":
        Fast_Food = 1
    elif cuisines27 == "Biryani":
        Biryani = 1                
    elif cuisines27 == "Continental":
        Continental = 1
    elif cuisines27 == "Desserts":
        Desserts = 1
    elif cuisines27 == "Cafe":
        Cafe = 1
    elif cuisines27 == "Beverages":
        Beverages = 1
    elif cuisines27 == "Italian":
        Italian = 1
    elif cuisines27 == "Bakery":
        Bakery = 1
    elif cuisines27 == "Street Food":
        Street_Food = 1
    elif cuisines27 == "Pizza":
        Pizza = 1
    elif cuisines27 == "Burger":
        Burger = 1
    elif cuisines27 == "Seafood":
        Seafood = 1
    elif cuisines27 == "Ice Cream":
        Ice_Cream = 1
    elif cuisines27 == "Andhra":
        Andhra = 1                
    elif cuisines27 == "Mughlai":
        Mughlai = 1
    elif cuisines27 == "Rolls":
        Rolls = 1
    elif cuisines27 == "American":
        American = 1
    elif cuisines27 == "Kerala":
        Kerala = 1
    elif cuisines27 == "Asian":
        Asian = 1
    elif cuisines27 == "Momos":
        Momos = 1
    elif cuisines27 == "Finger Food":
        Finger_Food = 1
    elif cuisines27 == "Juices":
        Juices = 1
    elif cuisines27 == "Salad":
        Salad = 1
    elif cuisines27 == "Arabian":
        Arabian = 1        
    elif cuisines27 == "Kebab":
        Kebab = 1
    elif cuisines27 == "Mithai":
        Mithai = 1
    elif cuisines27 == "Thai":
        Thai = 1
    elif cuisines27 == "Other":
        Other2 = 1           
    cuisines37 =  st.selectbox('Thired cuisines ',cuisines_list)
    if cuisines37 == 'North Indian':
        North_Indian = 1
    elif cuisines37 == "South Indian":
        South_Indian = 1
    elif cuisines37 == "Fast Food":
        Fast_Food = 1
    elif cuisines37 == "Biryani":
        Biryani = 1                
    elif cuisines37 == "Continental":
        Continental = 1
    elif cuisines37 == "Desserts":
        Desserts = 1
    elif cuisines37 == "Cafe":
        Cafe = 1
    elif cuisines37 == "Beverages":
        Beverages = 1
    elif cuisines37 == "Italian":
        Italian = 1
    elif cuisines37 == "Bakery":
        Bakery = 1
    elif cuisines37 == "Street Food":
        Street_Food = 1
    elif cuisines37 == "Pizza":
        Pizza = 1
    elif cuisines37 == "Burger":
        Burger = 1
    elif cuisines37 == "Seafood":
        Seafood = 1
    elif cuisines37 == "Ice Cream":
        Ice_Cream = 1
    elif cuisines37 == "Andhra":
        Andhra = 1                
    elif cuisines37 == "Mughlai":
        Mughlai = 1
    elif cuisines37 == "Rolls":
        Rolls = 1
    elif cuisines37 == "American":
        American = 1
    elif cuisines37 == "Kerala":
        Kerala = 1
    elif cuisines37 == "Asian":
        Asian = 1
    elif cuisines37 == "Momos":
        Momos = 1
    elif cuisines37 == "Finger Food":
        Finger_Food = 1
    elif cuisines37 == "Juices":
        Juices = 1
    elif cuisines37 == "Salad":
        Salad = 1
    elif cuisines37 == "Arabian":
        Arabian = 1        
    elif cuisines37 == "Kebab":
        Kebab = 1
    elif cuisines37 == "Mithai":
        Mithai = 1
    elif cuisines37 == "Thai":
        Thai = 1
    elif cuisines37 == "Other":
        Other2 = 1           
    cuisines47 =  st.selectbox('Fourth cuisines ',cuisines_list)
    if cuisines47 == 'North Indian':
        North_Indian = 1
    elif cuisines47 == "South Indian":
        South_Indian = 1
    elif cuisines47 == "Fast Food":
        Fast_Food = 1
    elif cuisines47 == "Biryani":
        Biryani = 1                
    elif cuisines47 == "Continental":
        Continental = 1
    elif cuisines47 == "Desserts":
        Desserts = 1
    elif cuisines47 == "Cafe":
        Cafe = 1
    elif cuisines47 == "Beverages":
        Beverages = 1
    elif cuisines47 == "Italian":
        Italian = 1
    elif cuisines47 == "Bakery":
        Bakery = 1
    elif cuisines47 == "Street Food":
        Street_Food = 1
    elif cuisines47 == "Pizza":
        Pizza = 1
    elif cuisines47 == "Burger":
        Burger = 1
    elif cuisines47 == "Seafood":
        Seafood = 1
    elif cuisines47 == "Ice Cream":
        Ice_Cream = 1
    elif cuisines47 == "Andhra":
        Andhra = 1                
    elif cuisines47 == "Mughlai":
        Mughlai = 1
    elif cuisines47 == "Rolls":
        Rolls = 1
    elif cuisines47 == "American":
        American = 1
    elif cuisines47 == "Kerala":
        Kerala = 1
    elif cuisines47 == "Asian":
        Asian = 1
    elif cuisines47 == "Momos":
        Momos = 1
    elif cuisines47 == "Finger Food":
        Finger_Food = 1
    elif cuisines47 == "Juices":
        Juices = 1
    elif cuisines47 == "Salad":
        Salad = 1
    elif cuisines47 == "Arabian":
        Arabian = 1        
    elif cuisines47 == "Kebab":
        Kebab = 1
    elif cuisines47 == "Mithai":
        Mithai = 1
    elif cuisines47 == "Thai":
        Thai = 1
    elif cuisines47 == "Other":
        Other2 = 1           
    cuisines57 =  st.selectbox('Fifth cuisines ',cuisines_list)
    if cuisines57 == 'North Indian':
        North_Indian = 1
    elif cuisines57 == "South Indian":
        South_Indian = 1
    elif cuisines57 == "Fast Food":
        Fast_Food = 1
    elif cuisines57 == "Biryani":
        Biryani = 1                
    elif cuisines57 == "Continental":
        Continental = 1
    elif cuisines57 == "Desserts":
        Desserts = 1
    elif cuisines57 == "Cafe":
        Cafe = 1
    elif cuisines57 == "Beverages":
        Beverages = 1
    elif cuisines57 == "Italian":
        Italian = 1
    elif cuisines57 == "Bakery":
        Bakery = 1
    elif cuisines57 == "Street Food":
        Street_Food = 1
    elif cuisines57 == "Pizza":
        Pizza = 1
    elif cuisines57 == "Burger":
        Burger = 1
    elif cuisines57 == "Seafood":
        Seafood = 1
    elif cuisines57 == "Ice Cream":
        Ice_Cream = 1
    elif cuisines57 == "Andhra":
        Andhra = 1                
    elif cuisines57 == "Mughlai":
        Mughlai = 1
    elif cuisines57 == "Rolls":
        Rolls = 1
    elif cuisines57 == "American":
        American = 1
    elif cuisines57 == "Kerala":
        Kerala = 1
    elif cuisines57 == "Asian":
        Asian = 1
    elif cuisines57 == "Momos":
        Momos = 1
    elif cuisines57 == "Finger Food":
        Finger_Food = 1
    elif cuisines57 == "Juices":
        Juices = 1
    elif cuisines57 == "Salad":
        Salad = 1
    elif cuisines57 == "Arabian":
        Arabian = 1        
    elif cuisines57 == "Kebab":
        Kebab = 1
    elif cuisines57 == "Mithai":
        Mithai = 1
    elif cuisines57 == "Thai":
        Thai = 1
    elif cuisines57 == "Other":
        Other2 = 1           
    cuisines67 =  st.selectbox('Sixth cuisines ',cuisines_list)
    if cuisines67 == 'North Indian':
        North_Indian = 1
    elif cuisines67 == "South Indian":
        South_Indian = 1
    elif cuisines67 == "Fast Food":
        Fast_Food = 1
    elif cuisines67 == "Biryani":
        Biryani = 1                
    elif cuisines67 == "Continental":
        Continental = 1
    elif cuisines67 == "Desserts":
        Desserts = 1
    elif cuisines67 == "Cafe":
        Cafe = 1
    elif cuisines67 == "Beverages":
        Beverages = 1
    elif cuisines67 == "Italian":
        Italian = 1
    elif cuisines67 == "Bakery":
        Bakery = 1
    elif cuisines67 == "Street Food":
        Street_Food = 1
    elif cuisines67 == "Pizza":
        Pizza = 1
    elif cuisines67 == "Burger":
        Burger = 1
    elif cuisines67 == "Seafood":
        Seafood = 1
    elif cuisines67 == "Ice Cream":
        Ice_Cream = 1
    elif cuisines67 == "Andhra":
        Andhra = 1                
    elif cuisines67 == "Mughlai":
        Mughlai = 1
    elif cuisines67 == "Rolls":
        Rolls = 1
    elif cuisines67 == "American":
        American = 1
    elif cuisines67 == "Kerala":
        Kerala = 1
    elif cuisines67 == "Asian":
        Asian = 1
    elif cuisines67 == "Momos":
        Momos = 1
    elif cuisines67 == "Finger Food":
        Finger_Food = 1
    elif cuisines67 == "Juices":
        Juices = 1
    elif cuisines67 == "Salad":
        Salad = 1
    elif cuisines67 == "Arabian":
        Arabian = 1        
    elif cuisines67 == "Kebab":
        Kebab = 1
    elif cuisines67 == "Mithai":
        Mithai = 1
    elif cuisines67 == "Thai":
        Thai = 1
    elif cuisines67 == "Other":
        Other2 = 1           
    cuisines7 =  st.selectbox('Seventh cuisines ',cuisines_list)
    if cuisines7 == 'North Indian':
        North_Indian = 1
    elif cuisines7 == "South Indian":
        South_Indian = 1
    elif cuisines7 == "Fast Food":
        Fast_Food = 1
    elif cuisines7 == "Biryani":
        Biryani = 1                
    elif cuisines7 == "Continental":
        Continental = 1
    elif cuisines7 == "Desserts":
        Desserts = 1
    elif cuisines7 == "Cafe":
        Cafe = 1
    elif cuisines7 == "Beverages":
        Beverages = 1
    elif cuisines7 == "Italian":
        Italian = 1
    elif cuisines7 == "Bakery":
        Bakery = 1
    elif cuisines7 == "Street Food":
        Street_Food = 1
    elif cuisines7 == "Pizza":
        Pizza = 1
    elif cuisines7 == "Burger":
        Burger = 1
    elif cuisines7 == "Seafood":
        Seafood = 1
    elif cuisines7 == "Ice Cream":
        Ice_Cream = 1
    elif cuisines7 == "Andhra":
        Andhra = 1                
    elif cuisines7 == "Mughlai":
        Mughlai = 1
    elif cuisines7 == "Rolls":
        Rolls = 1
    elif cuisines7 == "American":
        American = 1
    elif cuisines7 == "Kerala":
        Kerala = 1
    elif cuisines7 == "Asian":
        Asian = 1
    elif cuisines7 == "Momos":
        Momos = 1
    elif cuisines7 == "Finger Food":
        Finger_Food = 1
    elif cuisines7 == "Juices":
        Juices = 1
    elif cuisines7 == "Salad":
        Salad = 1
    elif cuisines7 == "Arabian":
        Arabian = 1        
    elif cuisines7 == "Kebab":
        Kebab = 1
    elif cuisines7 == "Mithai":
        Mithai = 1
    elif cuisines7 == "Thai":
        Thai = 1
    elif cuisines7 == "Other":
        Other2 = 1           

if NumberOFcuisines ==8:    
    cuisines18 = st.selectbox('Firt cuisines',cuisines_list)
    if cuisines18 == 'North Indian':
        North_Indian = 1
    elif cuisines18 == "South Indian":
        South_Indian = 1
    elif cuisines18 == "Fast Food":
        Fast_Food = 1
    elif cuisines18 == "Biryani":
        Biryani = 1                
    elif cuisines18 == "Continental":
        Continental = 1
    elif cuisines18 == "Desserts":
        Desserts = 1
    elif cuisines18 == "Cafe":
        Cafe = 1
    elif cuisines18 == "Beverages":
        Beverages = 1
    elif cuisines18 == "Italian":
        Italian = 1
    elif cuisines18 == "Bakery":
        Bakery = 1
    elif cuisines18 == "Street Food":
        Street_Food = 1
    elif cuisines18 == "Pizza":
        Pizza = 1
    elif cuisines18 == "Burger":
        Burger = 1
    elif cuisines18 == "Seafood":
        Seafood = 1
    elif cuisines18 == "Ice Cream":
        Ice_Cream = 1
    elif cuisines18 == "Andhra":
        Andhra = 1                
    elif cuisines18 == "Mughlai":
        Mughlai = 1
    elif cuisines18 == "Rolls":
        Rolls = 1
    elif cuisines18 == "American":
        American = 1
    elif cuisines18 == "Kerala":
        Kerala = 1
    elif cuisines18 == "Asian":
        Asian = 1
    elif cuisines18 == "Momos":
        Momos = 1
    elif cuisines18 == "Finger Food":
        Finger_Food = 1
    elif cuisines18 == "Juices":
        Juices = 1
    elif cuisines18 == "Salad":
        Salad = 1
    elif cuisines18 == "Arabian":
        Arabian = 1        
    elif cuisines18 == "Kebab":
        Kebab = 1
    elif cuisines18 == "Mithai":
        Mithai = 1
    elif cuisines18 == "Thai":
        Thai = 1
    elif cuisines18 == "Other":
        Other2 = 1           
    cuisines28 =  st.selectbox('Seconed cuisines ',cuisines_list)
    if cuisines28 == 'North Indian':
        North_Indian = 1
    elif cuisines28 == "South Indian":
        South_Indian = 1
    elif cuisines28 == "Fast Food":
        Fast_Food = 1
    elif cuisines28 == "Biryani":
        Biryani = 1                
    elif cuisines28 == "Continental":
        Continental = 1
    elif cuisines28 == "Desserts":
        Desserts = 1
    elif cuisines28 == "Cafe":
        Cafe = 1
    elif cuisines28 == "Beverages":
        Beverages = 1
    elif cuisines28 == "Italian":
        Italian = 1
    elif cuisines28 == "Bakery":
        Bakery = 1
    elif cuisines28 == "Street Food":
        Street_Food = 1
    elif cuisines28 == "Pizza":
        Pizza = 1
    elif cuisines28 == "Burger":
        Burger = 1
    elif cuisines28 == "Seafood":
        Seafood = 1
    elif cuisines28 == "Ice Cream":
        Ice_Cream = 1
    elif cuisines28 == "Andhra":
        Andhra = 1                
    elif cuisines28 == "Mughlai":
        Mughlai = 1
    elif cuisines28 == "Rolls":
        Rolls = 1
    elif cuisines28 == "American":
        American = 1
    elif cuisines28 == "Kerala":
        Kerala = 1
    elif cuisines28 == "Asian":
        Asian = 1
    elif cuisines28 == "Momos":
        Momos = 1
    elif cuisines28 == "Finger Food":
        Finger_Food = 1
    elif cuisines28 == "Juices":
        Juices = 1
    elif cuisines28 == "Salad":
        Salad = 1
    elif cuisines28 == "Arabian":
        Arabian = 1        
    elif cuisines28 == "Kebab":
        Kebab = 1
    elif cuisines28 == "Mithai":
        Mithai = 1
    elif cuisines28 == "Thai":
        Thai = 1
    elif cuisines28 == "Other":
        Other2 = 1           
    cuisines38 =  st.selectbox('Thired cuisines ',cuisines_list)
    if cuisines38 == 'North Indian':
        North_Indian = 1
    elif cuisines38 == "South Indian":
        South_Indian = 1
    elif cuisines38 == "Fast Food":
        Fast_Food = 1
    elif cuisines38 == "Biryani":
        Biryani = 1                
    elif cuisines38 == "Continental":
        Continental = 1
    elif cuisines38 == "Desserts":
        Desserts = 1
    elif cuisines38 == "Cafe":
        Cafe = 1
    elif cuisines38 == "Beverages":
        Beverages = 1
    elif cuisines38 == "Italian":
        Italian = 1
    elif cuisines38 == "Bakery":
        Bakery = 1
    elif cuisines38 == "Street Food":
        Street_Food = 1
    elif cuisines38 == "Pizza":
        Pizza = 1
    elif cuisines38 == "Burger":
        Burger = 1
    elif cuisines38 == "Seafood":
        Seafood = 1
    elif cuisines38 == "Ice Cream":
        Ice_Cream = 1
    elif cuisines38 == "Andhra":
        Andhra = 1                
    elif cuisines38 == "Mughlai":
        Mughlai = 1
    elif cuisines38 == "Rolls":
        Rolls = 1
    elif cuisines38 == "American":
        American = 1
    elif cuisines38 == "Kerala":
        Kerala = 1
    elif cuisines38 == "Asian":
        Asian = 1
    elif cuisines38 == "Momos":
        Momos = 1
    elif cuisines38 == "Finger Food":
        Finger_Food = 1
    elif cuisines38 == "Juices":
        Juices = 1
    elif cuisines38 == "Salad":
        Salad = 1
    elif cuisines38 == "Arabian":
        Arabian = 1        
    elif cuisines38 == "Kebab":
        Kebab = 1
    elif cuisines38 == "Mithai":
        Mithai = 1
    elif cuisines38 == "Thai":
        Thai = 1
    elif cuisines38 == "Other":
        Other2 = 1           
    cuisines48 =  st.selectbox('Fourth cuisines ',cuisines_list)
    if cuisines48 == 'North Indian':
        North_Indian = 1
    elif cuisines48 == "South Indian":
        South_Indian = 1
    elif cuisines48 == "Fast Food":
        Fast_Food = 1
    elif cuisines48 == "Biryani":
        Biryani = 1                
    elif cuisines48 == "Continental":
        Continental = 1
    elif cuisines48 == "Desserts":
        Desserts = 1
    elif cuisines48 == "Cafe":
        Cafe = 1
    elif cuisines48 == "Beverages":
        Beverages = 1
    elif cuisines48 == "Italian":
        Italian = 1
    elif cuisines48 == "Bakery":
        Bakery = 1
    elif cuisines48 == "Street Food":
        Street_Food = 1
    elif cuisines48 == "Pizza":
        Pizza = 1
    elif cuisines48 == "Burger":
        Burger = 1
    elif cuisines48 == "Seafood":
        Seafood = 1
    elif cuisines48 == "Ice Cream":
        Ice_Cream = 1
    elif cuisines48 == "Andhra":
        Andhra = 1                
    elif cuisines48 == "Mughlai":
        Mughlai = 1
    elif cuisines48 == "Rolls":
        Rolls = 1
    elif cuisines48 == "American":
        American = 1
    elif cuisines48 == "Kerala":
        Kerala = 1
    elif cuisines48 == "Asian":
        Asian = 1
    elif cuisines48 == "Momos":
        Momos = 1
    elif cuisines48 == "Finger Food":
        Finger_Food = 1
    elif cuisines48 == "Juices":
        Juices = 1
    elif cuisines48 == "Salad":
        Salad = 1
    elif cuisines48 == "Arabian":
        Arabian = 1        
    elif cuisines48 == "Kebab":
        Kebab = 1
    elif cuisines48 == "Mithai":
        Mithai = 1
    elif cuisines48 == "Thai":
        Thai = 1
    elif cuisines48 == "Other":
        Other2 = 1           
    cuisines58 =  st.selectbox('Fifth cuisines ',cuisines_list)
    if cuisines58 == 'North Indian':
        North_Indian = 1
    elif cuisines58 == "South Indian":
        South_Indian = 1
    elif cuisines58 == "Fast Food":
        Fast_Food = 1
    elif cuisines58 == "Biryani":
        Biryani = 1                
    elif cuisines58 == "Continental":
        Continental = 1
    elif cuisines58 == "Desserts":
        Desserts = 1
    elif cuisines58 == "Cafe":
        Cafe = 1
    elif cuisines58 == "Beverages":
        Beverages = 1
    elif cuisines58 == "Italian":
        Italian = 1
    elif cuisines58 == "Bakery":
        Bakery = 1
    elif cuisines58 == "Street Food":
        Street_Food = 1
    elif cuisines58 == "Pizza":
        Pizza = 1
    elif cuisines58 == "Burger":
        Burger = 1
    elif cuisines58 == "Seafood":
        Seafood = 1
    elif cuisines58 == "Ice Cream":
        Ice_Cream = 1
    elif cuisines58 == "Andhra":
        Andhra = 1                
    elif cuisines58 == "Mughlai":
        Mughlai = 1
    elif cuisines58 == "Rolls":
        Rolls = 1
    elif cuisines58 == "American":
        American = 1
    elif cuisines58 == "Kerala":
        Kerala = 1
    elif cuisines58 == "Asian":
        Asian = 1
    elif cuisines58 == "Momos":
        Momos = 1
    elif cuisines58 == "Finger Food":
        Finger_Food = 1
    elif cuisines58 == "Juices":
        Juices = 1
    elif cuisines58 == "Salad":
        Salad = 1
    elif cuisines58 == "Arabian":
        Arabian = 1        
    elif cuisines58 == "Kebab":
        Kebab = 1
    elif cuisines58 == "Mithai":
        Mithai = 1
    elif cuisines58 == "Thai":
        Thai = 1
    elif cuisines58 == "Other":
        Other2 = 1           
    cuisines68 =  st.selectbox('Sixth cuisines ',cuisines_list)
    if cuisines68 == 'North Indian':
        North_Indian = 1
    elif cuisines68 == "South Indian":
        South_Indian = 1
    elif cuisines68 == "Fast Food":
        Fast_Food = 1
    elif cuisines68 == "Biryani":
        Biryani = 1                
    elif cuisines68 == "Continental":
        Continental = 1
    elif cuisines68 == "Desserts":
        Desserts = 1
    elif cuisines68 == "Cafe":
        Cafe = 1
    elif cuisines68 == "Beverages":
        Beverages = 1
    elif cuisines68 == "Italian":
        Italian = 1
    elif cuisines68 == "Bakery":
        Bakery = 1
    elif cuisines68 == "Street Food":
        Street_Food = 1
    elif cuisines68 == "Pizza":
        Pizza = 1
    elif cuisines68 == "Burger":
        Burger = 1
    elif cuisines68 == "Seafood":
        Seafood = 1
    elif cuisines68 == "Ice Cream":
        Ice_Cream = 1
    elif cuisines68 == "Andhra":
        Andhra = 1                
    elif cuisines68 == "Mughlai":
        Mughlai = 1
    elif cuisines68 == "Rolls":
        Rolls = 1
    elif cuisines68 == "American":
        American = 1
    elif cuisines68 == "Kerala":
        Kerala = 1
    elif cuisines68 == "Asian":
        Asian = 1
    elif cuisines68 == "Momos":
        Momos = 1
    elif cuisines68 == "Finger Food":
        Finger_Food = 1
    elif cuisines68 == "Juices":
        Juices = 1
    elif cuisines68 == "Salad":
        Salad = 1
    elif cuisines68 == "Arabian":
        Arabian = 1        
    elif cuisines68 == "Kebab":
        Kebab = 1
    elif cuisines68 == "Mithai":
        Mithai = 1
    elif cuisines68 == "Thai":
        Thai = 1
    elif cuisines68 == "Other":
        Other2 = 1           
    cuisines78 =  st.selectbox('Seventh cuisines ',cuisines_list)
    if cuisines78 == 'North Indian':
        North_Indian = 1
    elif cuisines78 == "South Indian":
        South_Indian = 1
    elif cuisines78 == "Fast Food":
        Fast_Food = 1
    elif cuisines78 == "Biryani":
        Biryani = 1                
    elif cuisines78 == "Continental":
        Continental = 1
    elif cuisines78 == "Desserts":
        Desserts = 1
    elif cuisines78 == "Cafe":
        Cafe = 1
    elif cuisines78 == "Beverages":
        Beverages = 1
    elif cuisines78 == "Italian":
        Italian = 1
    elif cuisines78 == "Bakery":
        Bakery = 1
    elif cuisines78 == "Street Food":
        Street_Food = 1
    elif cuisines78 == "Pizza":
        Pizza = 1
    elif cuisines78 == "Burger":
        Burger = 1
    elif cuisines78 == "Seafood":
        Seafood = 1
    elif cuisines78 == "Ice Cream":
        Ice_Cream = 1
    elif cuisines78 == "Andhra":
        Andhra = 1                
    elif cuisines78 == "Mughlai":
        Mughlai = 1
    elif cuisines78 == "Rolls":
        Rolls = 1
    elif cuisines78 == "American":
        American = 1
    elif cuisines78 == "Kerala":
        Kerala = 1
    elif cuisines78 == "Asian":
        Asian = 1
    elif cuisines78 == "Momos":
        Momos = 1
    elif cuisines78 == "Finger Food":
        Finger_Food = 1
    elif cuisines78 == "Juices":
        Juices = 1
    elif cuisines78 == "Salad":
        Salad = 1
    elif cuisines78 == "Arabian":
        Arabian = 1        
    elif cuisines78 == "Kebab":
        Kebab = 1
    elif cuisines78 == "Mithai":
        Mithai = 1
    elif cuisines78 == "Thai":
        Thai = 1
    elif cuisines78 == "Other":
        Other2 = 1           
    cuisines8 =  st.selectbox('Eighth cuisines ',cuisines_list)
    if cuisines8 == 'North Indian':
        North_Indian = 1
    elif cuisines8 == "South Indian":
        South_Indian = 1
    elif cuisines8 == "Fast Food":
        Fast_Food = 1
    elif cuisines8 == "Biryani":
        Biryani = 1                
    elif cuisines8 == "Continental":
        Continental = 1
    elif cuisines8 == "Desserts":
        Desserts = 1
    elif cuisines8 == "Cafe":
        Cafe = 1
    elif cuisines8 == "Beverages":
        Beverages = 1
    elif cuisines8 == "Italian":
        Italian = 1
    elif cuisines8 == "Bakery":
        Bakery = 1
    elif cuisines8 == "Street Food":
        Street_Food = 1
    elif cuisines8 == "Pizza":
        Pizza = 1
    elif cuisines8 == "Burger":
        Burger = 1
    elif cuisines8 == "Seafood":
        Seafood = 1
    elif cuisines8 == "Ice Cream":
        Ice_Cream = 1
    elif cuisines8 == "Andhra":
        Andhra = 1                
    elif cuisines8 == "Mughlai":
        Mughlai = 1
    elif cuisines8 == "Rolls":
        Rolls = 1
    elif cuisines8 == "American":
        American = 1
    elif cuisines8 == "Kerala":
        Kerala = 1
    elif cuisines8 == "Asian":
        Asian = 1
    elif cuisines8 == "Momos":
        Momos = 1
    elif cuisines8 == "Finger Food":
        Finger_Food = 1
    elif cuisines8 == "Juices":
        Juices = 1
    elif cuisines8 == "Salad":
        Salad = 1
    elif cuisines8 == "Arabian":
        Arabian = 1        
    elif cuisines8 == "Kebab":
        Kebab = 1
    elif cuisines8 == "Mithai":
        Mithai = 1
    elif cuisines8 == "Thai":
        Thai = 1
    elif cuisines8 == "Other":
        Other2 = 1       
    
    
DishLikedCount = st.number_input("Enter Number Of Dish Liked",min_value = 0,max_value=7)   

    
cost = st.number_input("Enter Average Cost For Two Pearson")   




test = [book_tableEnc,online_orderEnc
        ,cost,locationEnc,DishLikedCount
        ,Number_rest_type
        ,Quick_Bites,Casual_Dining
        ,Cafe,Delivery,Dessert_Parlor
        ,Bar,Takeaway,Bakery,Beverage_Shop
        ,Pub,other,NumberOFcuisines
        ,North_Indian,Chinese,South_Indian
        ,Fast_Food,Biryani,Continental
        ,Desserts,Cafe,Beverages
        ,Italian,Bakery,Street_Food
        ,Pizza,Burger,Seafood
        ,Ice_Cream,Andhra,Mughlai
        ,Rolls,American,Kerala
        ,Asian,Momos,Finger_Food
        ,Juices,Salad,Arabian
        ,Kebab,Mithai,Thai
        ,Other2]    


result = ""
if st.button("Predict"):
    result = predictor(test)
    
st.success(result)


