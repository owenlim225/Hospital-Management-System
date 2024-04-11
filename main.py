import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import random
import time
import datetime
import mysql.connector

class HospitalManagement:
    def __init__(self, root):
        self.root = root
        self.root.title("Hospital Management")
        self.root.geometry("1366x768+0+0")
        self.root.configure(bg="light blue")  # Set background color

        # Title label
        lbl_title = tk.Label(self.root, bd=20, relief=tk.RIDGE, text="HOSPITAL MANAGEMENT SYSTEM", fg="blue", bg="ghost white", font=("times new roman", 50, "bold"))
        lbl_title.pack(side=tk.TOP, fill=tk.X)

        # ===================================Data frame===================================
        data_frame = tk.Frame(self.root, bd=20, bg="light blue")  # Set background color
        data_frame.place(x=0, y=120, width=1366, height=400)

        # Patient Info LEFT
        data_frame_left = tk.LabelFrame(data_frame, bd=10, relief=tk.RIDGE, padx=10, font=("times new roman", 12, "bold"), text="Patient Information")
        data_frame_left.place(x=0, y=1, width=980, height=350)
        
        # Prescription RIGHT
        data_frame_right = tk.LabelFrame(data_frame, bd=10, relief=tk.RIDGE, padx=10, font=("times new roman", 12, "bold"), text="Prescription")
        data_frame_right.place(x=990, y=1, width=335, height=350)

        #===================================Button frame===================================

        button_frame = tk.Frame(self.root, bd=15, relief=tk.RIDGE, bg="light blue")  # Set background color
        button_frame.place(x=0, y=500, width=1366, height=70)

        #===================================Details frame===================================

        details_frame = tk.Frame(self.root, bd=15, relief=tk.RIDGE, bg="light blue")  # Set background color
        details_frame.place(x=0, y=575, width=1366, height=130)


        #===================================Data Left frame===================================
        lbl_name_tablet = tk.Label(data_frame_left, text="Names of Tablet:", font=("times new roman", 12, "bold"), padx=2, pady=5)
        lbl_name_tablet.grid(row=0, column=0, padx=2, pady=5)


        #===============Left Info===============

        #Name of Tablet
        com_name_tablet = ttk.Combobox(data_frame_left, font=("times new roman", 12, "bold"), width=33)
        com_name_tablet["values"]=("Nice", "Corona Vaccine", "Acetaminophen", "Adderall", "Amlodipine","Ativan") 
        com_name_tablet.grid(row=0, column=1)
        
        #Reference No
        lbl_ref=tk.Label(data_frame_left, font=("times new roman", 12, "bold"), text="Reference No:", padx=2)
        lbl_ref.grid(row=1, column=0, sticky=tk.W)
        txt_ref=tk.Entry(data_frame_left, font=("times new roman", 12, "bold"), width=35)
        txt_ref.grid(row=1, column=1)
        
        #Dose
        lbl_dose=tk.Label(data_frame_left, font=("times new roman", 12, "bold"), text="Dose:", padx=2, pady=4)
        lbl_dose.grid(row=2, column=0, sticky=tk.W)
        txt_dose=tk.Entry(data_frame_left, font=("times new roman", 12, "bold"), width=35)
        txt_dose.grid(row=2, column=1)

        #No of tablets
        lbl_no_of_tablet=tk.Label(data_frame_left, font=("times new roman", 12, "bold"), text="No. of Tablets:", padx=2)
        lbl_no_of_tablet.grid(row=3, column=0, sticky=tk.W)
        txt_no_of_tablet=tk.Entry(data_frame_left, font=("times new roman", 12, "bold"), width=35)
        txt_no_of_tablet.grid(row=3, column=1)
        
        #Lot
        lbl_lot=tk.Label(data_frame_left, font=("times new roman", 12, "bold"), text="Lot:", padx=2, pady=4)
        lbl_lot.grid(row=4, column=0, sticky=tk.W)
        txt_lot=tk.Entry(data_frame_left, font=("times new roman", 12, "bold"), width=35)
        txt_lot.grid(row=4, column=1)

        #Issue date
        lbl_issue_date=tk.Label(data_frame_left, font=("times new roman", 12, "bold"), text="Issue date:", padx=2)
        lbl_issue_date.grid(row=5, column=0, sticky=tk.W)
        txt_issue_date=tk.Entry(data_frame_left, font=("times new roman", 12, "bold"), width=35)
        txt_issue_date.grid(row=5, column=1)
        
        #Expiration date
        lbl_exp_date=tk.Label(data_frame_left, font=("times new roman", 12, "bold"), text="Expiration Date:", padx=2, pady=4)
        lbl_exp_date.grid(row=6, column=0, sticky=tk.W)
        txt_exp_date=tk.Entry(data_frame_left, font=("times new roman", 12, "bold"), width=35)
        txt_exp_date.grid(row=6, column=1)

        #Daily dose
        lbl_daily_dose=tk.Label(data_frame_left, font=("times new roman", 12, "bold"), text="Daily Dose:", padx=2)
        lbl_daily_dose.grid(row=7, column=0, sticky=tk.W)
        txt_daily_dose=tk.Entry(data_frame_left, font=("times new roman", 12, "bold"), width=35)
        txt_daily_dose.grid(row=7, column=1)
        
        #Side effect
        lbl_side_effect=tk.Label(data_frame_left, font=("times new roman", 12, "bold"), text="Side Effect:", padx=2, pady=4)
        lbl_side_effect.grid(row=8, column=0, sticky=tk.W)
        txt_side_effect=tk.Entry(data_frame_left, font=("times new roman", 12, "bold"), width=35)
        txt_side_effect.grid(row=8, column=1)

        #===============Right Info===============

        #Further info
        lbl_further_info=tk.Label(data_frame_left, font=("times new roman", 12, "bold"), text="Further Information:", padx=2)
        lbl_further_info.grid(row=0, column=2, sticky=tk.W)
        txt_further_info=tk.Entry(data_frame_left, font=("times new roman", 12, "bold"), width=35)
        txt_further_info.grid(row=0, column=3)
        
        #Blood pressure
        lbl_blood_pressure=tk.Label(data_frame_left, font=("times new roman", 12, "bold"), text="Blood pressure:", padx=2)
        lbl_blood_pressure.grid(row=1, column=2, sticky=tk.W)
        txt_blood_pressure=tk.Entry(data_frame_left, font=("times new roman", 12, "bold"), width=35)
        txt_blood_pressure.grid(row=1, column=3)
        
        #Storage
        lbl_storage=tk.Label(data_frame_left, font=("times new roman", 12, "bold"), text="Storage:", padx=2, pady=4)
        lbl_storage.grid(row=2, column=2, sticky=tk.W)
        txt_storage=tk.Entry(data_frame_left, font=("times new roman", 12, "bold"), width=35)
        txt_storage.grid(row=2, column=3)

        #Medicine
        lbl_medicine=tk.Label(data_frame_left, font=("times new roman", 12, "bold"), text="Medicine:", padx=2)
        lbl_medicine.grid(row=3, column=2, sticky=tk.W)
        txt_medicine=tk.Entry(data_frame_left, font=("times new roman", 12, "bold"), width=35)
        txt_medicine.grid(row=3, column=3)
        
        #Patient ID
        lbl_patient_ID=tk.Label(data_frame_left, font=("times new roman", 12, "bold"), text="Patient ID:", padx=2, pady=4)
        lbl_patient_ID.grid(row=4, column=2, sticky=tk.W)
        txt_patient_ID=tk.Entry(data_frame_left, font=("times new roman", 12, "bold"), width=35)
        txt_patient_ID.grid(row=4, column=3)

        #Nhs Number
        lbl_nhs_num=tk.Label(data_frame_left, font=("times new roman", 12, "bold"), text="Nhs Number:", padx=2)
        lbl_nhs_num.grid(row=5, column=2, sticky=tk.W)
        txt_nhs_num=tk.Entry(data_frame_left, font=("times new roman", 12, "bold"), width=35)
        txt_nhs_num.grid(row=5, column=3)
        
        #Patient name
        lbl_patient_name=tk.Label(data_frame_left, font=("times new roman", 12, "bold"), text="Patient name:", padx=2, pady=4)
        lbl_patient_name.grid(row=6, column=2, sticky=tk.W)
        txt_patient_name=tk.Entry(data_frame_left, font=("times new roman", 12, "bold"), width=35)
        txt_patient_name.grid(row=6, column=3)

        #Date of birth
        lbl_birth_date=tk.Label(data_frame_left, font=("times new roman", 12, "bold"), text="Birth date:", padx=2)
        lbl_birth_date.grid(row=7, column=2, sticky=tk.W)
        txt_birth_date=tk.Entry(data_frame_left, font=("times new roman", 12, "bold"), width=35)
        txt_birth_date.grid(row=7, column=3)
        
        #Patient Address
        lbl_patient_address=tk.Label(data_frame_left, font=("times new roman", 12, "bold"), text="Patient Address:", padx=2, pady=4)
        lbl_patient_address.grid(row=8, column=2, sticky=tk.W)
        txt_patient_address=tk.Entry(data_frame_left, font=("times new roman", 12, "bold"), width=35)
        txt_patient_address.grid(row=8, column=3)

        #===================================Data Right frame===================================












root = tk.Tk()
obj = HospitalManagement(root)
root.mainloop()