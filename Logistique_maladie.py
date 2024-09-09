# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 15:04:20 2024

@author: o.balde
"""

#from flask import Flask,json,request,jsonify
import streamlit as st
import pickle
#app=Flask(__name__)
model=pickle.load(open('data/logistique.pkl','rb'))

def main():
    st.title("Bienvenu de prediction de l'etat de sante Cardiaque des Patients")
    # les entrees
   # age	sex	cp	trestbps	chol	fbs	restecg	thalach	exang	oldpeak	slope	ca	thal
    age=st.text_input("Donner l'age")
    sex=st.text_input("Donner le sexe")
    cp=st.text_input('Donner le type de douleurs toraxiques')
    trestbps=st.text_input("Donner la pression artérielle au repos (en mm Hg à l'admission à l'hôpital)")
    chol=st.text_input("Donner le taux de cholestérol sérique en mg/dl")
    fbs=st.text_input("Le (glycémie à jeun > 120 mg/dl): (1 = vrai ; 0 = faux) ")
    restecg=st.text_input('résultats électrocardiographiques au repos')
    thalach=st.text_input("fréquence cardiaque maximale atteinte")
    exang=st.text_input("angine de poitrine induite par l'exercice (1 = oui ; 0 = non)")
    oldpeak=st.text_input("dépression ST induite par l'exercice par rapport au repos")
    slope=st.text_input("la pente du segment ST de pointe à l'effort")
    ca=st.text_input("nombre de vaisseaux principaux (0-3) colorés par flourosopie")
    thal=st.text_input("Thal : 3 = normal ; 6 = défaut fixe ; 7 = défaut réversible")
    # prediction
    if st.button('predict'):
        makeprediction=model.predict([[age,sex,cp,trestbps,	chol,fbs,restecg,thalach,exang,	oldpeak,slope,ca,thal]])
        output=round(makeprediction[0])
        if output==0:
            "Le patient n'est pas Malade."
        else :
            "Le patient est Malade."
        #st.success('You can by your ... for {}'.format(output))
if __name__=='__main__':
    main()
    
# @app.route('/')
# def home():
#     return 'Bienvenue sur le site de prediction des prix'
# @app.route("/predict", methods=["GET"])
# def predict():
#     v1=request.args.get('valeur1')
#     v2=request.args.get('valeur1')
#     v3=request.args.get('valeur1')
#     makeprediction=model.predict()
