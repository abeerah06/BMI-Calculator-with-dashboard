import streamlit as slt 
import numpy as np 
slt.title("BMI Calculator")
weight = slt.number_input(label='Enter your weight in kgs: ', placeholder=60, value=60)
height = slt.number_input(label='Enter your height: ', placeholder=170, value=1.0, step=0.01)
unit = slt.selectbox('Select Units: ', ['cm','m','inches'])
if unit == 'cm':
    bmi = (weight/(height**2))
elif unit == 'm':
    bmi= (weight/(height**2))
elif unit == 'inches':
    bmi = ((weight*2.20462)/(height**2))*703
slt.write('Your BMI is', round(bmi, 2))
if (bmi<18.5):
    slt.write('You are extremly underweight')
elif((bmi>=18.5) & (bmi<25)):
    slt.write('You are healthy')
else:
    slt.write('You are overweight')


