# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 15:04:20 2024

@author: o.balde
"""

#from flask import Flask,json,request,jsonify
import streamlit as st
import pickle
#import base64 as b
#app=Flask(__name__)
# def setback(fichier):
#     bin_str=b.get_base64(fichier)
#     page_bg_img='''
#     <style>
#     .stApp{
#         background-image:url("data:image/png;base64,%s");
#         background-size:cover
#         }
#     </style>
#     ''' % bin_str
#     st.markdown(page_bg_img,unsafe_allow_html=True)

model=pickle.load(open('data/randomforest.pkl','rb'))
# fichier='signature.jpg'
# setback(fichier)

def main():
    st.title("Bienvenu de prediction des prix des téléphones portables")
    # les entrees
   # 'Screen Size (inches)','RAM (GB)','Storage (GB)','Battery Capacity (mAh)','Camera Quality (MP)'
    screen=st.text_input("Donner la taille de l'Ecran en (Inches)")
    ram=st.text_input("Donner la capacite de la RAM (GB)")
    storage=st.text_input("Donner la Capacite de stockage (GB)")
    battery=st.text_input('Donner la capacite de la battery (mAh)')
    camera=st.text_input("Donner la qualite du Camera en (MP)")
    # prediction
    if st.button('predict'):
        makeprediction=model.predict([[screen,ram,storage,battery,camera]])
        output=round(makeprediction[0],2)
        # if output==0:
        #     "Le patient n'est pas Malade."
        # else :
        #     "Le patient est Malade."
        st.success('Vous pouvez vendre votre Telephone à {} $'.format(output))
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
