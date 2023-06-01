from tkinter import *
from flask import Flask,redirect, url_for,render_template,request
import os

def d_dtcn():
	root = Tk()
	root.configure(background = "white")

	def function1(): 
		os.system("python drowsiness_detection.py --shape_predictor shape_predictor_68_face_landmarks.dat")
		exit()

	def function2(): 
		os.system("python android_cam.py --shape_predictor shape_predictor_68_face_landmarks.dat")
		exit()

	
		
	root.title("DRIVER DROWSINESS DETECTION SYSTEM")
	Label(root, text="DROWSINESS DETECTION SYSTEM",font=("serif",20),fg="white",bg="black",height=2).grid(row=2,rowspan=2,columnspan=5,sticky=N+E+W+S,padx=5,pady=10)
	Button(root,text="START",font=("serif",20),bg="black",fg='white',command=function1).grid(row=5,columnspan=5,sticky=W+E+N+S,padx=5,pady=5)
	Button(root,text="EXIT",font=("serif",20),bg="black",fg='white',command=root.destroy).grid(row=9,columnspan=5,sticky=W+E+N+S,padx=5,pady=5)

	root.mainloop()