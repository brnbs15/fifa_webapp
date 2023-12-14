import streamlit as st
import pandas as pd
import joblib

#python -m streamlit run file.py
pickled_model = joblib.load('./models/fifa_classifier_model_dtree.pkl')
st.set_page_config(layout="wide")
st.title('FIFA cards classification')
id=246621
col1, col2, col3 , col4,col5, col6,col7,col8 = st.columns([0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1],gap="small")
with col1:
    st.header(":green[Player details]",)
    name =hash(st.text_input("Name"))
    age = st.slider('Age',min_value=1, max_value=100,value=25)
    value = st.text_input('Value(euro)')
    wage = st.text_input('Wage(euro)')
    st.write("Extra attributes:")
    special = st.slider('Special',min_value=1, max_value=100,value=50)
    international = st.slider('International Reputation',min_value=1, max_value=100,value=50)
    weekfoot = st.slider('Week foot',min_value=1, max_value=100,value=50)
    skill = st.slider('Skill moves',min_value=1, max_value=100,value=50)
with col2:
    st.header(":green[Shooting]")
    attposition = st.slider('Att. Position',min_value=1, max_value=100,value=50)
    finish = st.slider('Finising',min_value=1, max_value=100,value=50)
    shotp = st.slider('Shoot power',min_value=1, max_value=100,value=50)
    longshot = st.slider('Long shot',min_value=1, max_value=100,value=50)
    volley = st.slider('Volleys',min_value=1, max_value=100,value=50,)
    penalty = st.slider('Penalty',min_value=1, max_value=100,value=50)
with col3:
    st.header(":green[Passing]",)
    vision = st.slider('Vision',min_value=1, max_value=100,value=50,)
    cross = st.slider('Crossing',min_value=1, max_value=100,value=50)
    fkacc = st.slider('Freekick accuracy',min_value=1, max_value=100,value=50)
    shortpass = st.slider('ShortPassing',min_value=1, max_value=100,value=50)
    longpass = st.slider('Longpass',min_value=1, max_value=100,value=50)
    curve = st.slider('Curve',min_value=1, max_value=100,value=50)
with col4:
    st.header(":green[Dribling:]")
    agility = st.slider('Agility',min_value=1, max_value=100,value=50)
    balance = st.slider('Balance',min_value=1, max_value=100,value=50)
    react = st.slider('Reaction',min_value=1, max_value=100,value=50)
    ballcont = st.slider('Ball control',min_value=1, max_value=100,value=50)
    dribling = st.slider('Dribling',min_value=1, max_value=100,value=50)
    composure = st.slider('Composure',min_value=1, max_value=100,value=50)
with col5:
    st.header(":green[Defending:]")
    intercept = st.slider('Interception',min_value=1, max_value=100,value=50)
    headacc = st.slider('Head accuracy',min_value=1, max_value=100,value=50)
    standtack = st.slider('Standing Tackle',min_value=1, max_value=100,value=50)
    slidtack = st.slider('Sliding Tackle',min_value=1, max_value=100,value=50)
    marking = st.slider('Marking',min_value=1, max_value=100,value=50)

with col6:
    st.header(":green[Physical:]")
    jump = st.slider('Jump',min_value=1, max_value=100,value=50)
    stamina = st.slider('Stamina',min_value=1, max_value=100,value=50)
    strength = st.slider('Strength',min_value=1, max_value=100,value=50)
    aggr = st.slider('Aggressive',min_value=1, max_value=100,value=50)
    st.header(":green[Pace:]")
    sprint = st.slider('Sprint speed',min_value=1, max_value=100,value=50)
    accel = st.slider('Acceleration',min_value=1, max_value=100,value=50)
with col7:
    st.header(":green[Goalkeeper attributes:]")
    goaliecheckbox=st.checkbox(label="Are you a goalkeeper?")
    
    if goaliecheckbox==False:
        gkdiv = st.slider('Goalkeeper Diving',min_value=1, max_value=100,value=0)
        gkhand = st.slider('Goalkeeper Handling',min_value=1, max_value=100,value=0)
        gkkick = st.slider('Goalkeeper Kicking',min_value=1, max_value=100,value=0)
        gkpos = st.slider('Goalkeeper Positioning',min_value=1, max_value=100,value=0)
        gkref = st.slider('Goalkeepe Reflex',min_value=1, max_value=100,value=0)
    else:
        gkdiv = st.slider('Goalkeeper Diving',min_value=1, max_value=100,value=50)
        gkhand = st.slider('Goalkeeper Handling',min_value=1, max_value=100,value=50)
        gkkick = st.slider('Goalkeeper Kicking',min_value=1, max_value=100,value=50)
        gkpos = st.slider('Goalkeeper Positioning',min_value=1, max_value=100,value=50)
        gkref = st.slider('Goalkeepe Reflex',min_value=1, max_value=100,value=50)
input_data = [[id,name,age,value,wage,special,international,weekfoot,skill,
                cross,finish,headacc,shortpass,volley,dribling,curve,fkacc,longpass,ballcont,accel,
                sprint,agility,react,balance,shotp,jump,stamina,strength,
                longshot,aggr,intercept,attposition,vision,penalty,
                composure,marking,standtack,slidtack,gkdiv,gkhand,gkkick,gkpos,gkref]]
def idgenerator(id):
    id=id+1
    input_data[0][0]=id
def pace_calc(sprint,accel):
    return round((sprint+accel)/2)
def sho_calc(attposition,finish,shotp,longshot,volley,penalty):
    return round((attposition+finish+shotp+longshot+volley+penalty)/6)
def pas_calc(vision,cross,fkacc,shortpass,longpass,curve):
    return round((vision+cross+fkacc+shortpass+longpass+curve)/6)
def dri_calc(agility,balance,react,ballcont,dribling,composure):
    return round((agility+balance+react+ballcont+dribling+composure)/6)
def phy_calc(jump,stamina,strength,aggr):
    return round((jump+ stamina+strength+aggr)/4)
def def_calc(intercept,headacc,standtack,slidtack,marking):
    return round((intercept+headacc+standtack+slidtack+marking)/5)
def ovr_calc():
    return round((def_calc(intercept,headacc,standtack,slidtack,marking)+
phy_calc(jump,stamina,strength,aggr)+dri_calc(agility,balance,react,ballcont,dribling,composure)+pas_calc(vision,cross,fkacc,shortpass,longpass,curve)+
sho_calc(attposition,finish,shotp,longshot,volley,penalty)+pace_calc(sprint,accel))/6)
with col8:
    if st.button('Create Fifa card',type="primary"):
        card_prediction = pickled_model.predict(input_data)
        
        if card_prediction[0]==1:
            st.image('./card_pics/bronze_card_fifa.jpg', caption='bronze')
        elif card_prediction[0] ==2:
            st.image('./card_pics/silver_card_fifa.jpg', caption='silver')
        else:
            st.image('./card_pics/gold_card_fifa.jpg', caption='gold')
        
        st.success(card_prediction)
    st.subheader(str(ovr_calc())+" :red[ovr]")
    alcol1,alcol2=st.columns(2,gap="small")
    with alcol1:
        if goaliecheckbox==False:
            st.subheader(str(pace_calc(sprint,accel)) + " :red[PAC]")
            st.subheader(str(sho_calc(attposition,finish,shotp,longshot,volley,penalty)) + " :red[SHO]")
            st.subheader(str(pas_calc(vision,cross,fkacc,shortpass,longpass,curve)) + " :red[PAS]")
        else:
            st.subheader(str(gkdiv) + " :red[DIV]")
            st.subheader(str(gkhand) + " :red[HAN]")
            st.subheader(str(gkkick) + " :red[KIC]")
    with alcol2:
        if goaliecheckbox==False:
            st.subheader(str(dri_calc(agility,balance,react,ballcont,dribling,composure)) + " :red[DRI]")
            st.subheader(str(def_calc(intercept,headacc,standtack,slidtack,marking)) + " :red[DEF]")
            st.subheader(str(phy_calc(jump,stamina,strength,aggr)) + " :red[PHY]")
        else:
            st.subheader(str(gkref) + " :red[REF]")
            st.subheader(str(pace_calc(sprint,accel)) + " :red[SPE]")
            st.subheader(str(gkpos) + " :red[POS]")