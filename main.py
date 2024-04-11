import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkcalendar import DateEntry
import random
import time
import datetime
import mysql.connector

class HospitalManagement(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Hospital Management")
        self.geometry("1366x768+0+0")
        self.configure(bg="linen")  # Set background color

        self.strvars = {}  # Make it an instance variable

        #Int Var of each datangina
        variables = [
            "name_tablet", "ref", "dose", "no_of_tablet", "lot", "issue_date", "exp_date",
            "daily_dose", "side_effect", "further_info", "blood_pressure", "storage",
            "medicine", "patient_ID", "Nhs_num", "patient_name", "birth_date", "patient_address"
        ]

        # Dictionary to na StringVar para di na paisa isa tangina
        for var_name in variables:
            self.strvars[var_name] = tk.StringVar()

        self.mainFrame()
        self.mainButton()
        self.mainDetails()

    def mainFrame(self):
        # Title label
        lbl_title = tk.Label(self, bd=20, relief=tk.RIDGE, text="HOSPITAL MANAGEMENT SYSTEM", fg="blue", bg="linen",
                             font=("times new roman", 45, "bold"))
        lbl_title.pack(side=tk.TOP, fill=tk.X)

        # ===================================Data frame===================================
        data_frame = tk.Frame(self, bd=20, relief=tk.RIDGE, bg="linen")  # Set background color
        data_frame.place(x=0, y=110, width=1366, height=322)

        # Patient Info LEFT
        data_frame_left = tk.LabelFrame(data_frame, bd=10, relief=tk.RIDGE, padx=10, font=("times new roman", 11, "bold"),
                                        text="Patient Information")
        data_frame_left.place(x=0, y=1, width=980, height=280)

        # Prescription RIGHT
        data_frame_right = tk.LabelFrame(data_frame, bd=10, relief=tk.RIDGE, padx=10, font=("times new roman", 11, "bold"),
                                         text="Prescription")
        data_frame_right.place(x=980, y=1, width=345, height=280)

        # ===============Patient Info (Left)===============

        # Name of Tablet
        lbl_name_tablet = tk.Label(data_frame_left, text="Names of Tablet:", font=("times new roman", 11, "bold"),
                                   padx=2, pady=5)
        lbl_name_tablet.grid(row=0, column=0, padx=2, pady=5)
        com_name_tablet = ttk.Combobox(data_frame_left, font=("times new roman", 11, "bold"), width=33)
        com_name_tablet["values"] = ("Nice", "Corona Vaccine", "Acetaminophen", "Adderall", "Amlodipine", "Ativan")
        com_name_tablet.grid(row=0, column=1)

        # Reference No
        lbl_ref = tk.Label(data_frame_left, font=("times new roman", 11, "bold"), text="Reference No:", padx=2)
        lbl_ref.grid(row=1, column=0, sticky=tk.W)
        txt_ref = tk.Entry(data_frame_left, textvariable=self.strvars['ref'], font=("times new roman", 11, "bold"),
                           width=35)
        txt_ref.grid(row=1, column=1)

        # Dose
        lbl_dose = tk.Label(data_frame_left, font=("times new roman", 11, "bold"), text="Dose:", padx=2, pady=4)
        lbl_dose.grid(row=2, column=0, sticky=tk.W)
        txt_dose = tk.Entry(data_frame_left, textvariable=self.strvars['dose'], font=("times new roman", 11, "bold"),
                            width=35)
        txt_dose.grid(row=2, column=1)

        # No of tablets
        lbl_no_of_tablet = tk.Label(data_frame_left, font=("times new roman", 11, "bold"), text="No. of Tablets:",
                                     padx=2)
        lbl_no_of_tablet.grid(row=3, column=0, sticky=tk.W)
        txt_no_of_tablet = tk.Entry(data_frame_left, textvariable=self.strvars['no_of_tablet'],
                                    font=("times new roman", 11, "bold"), width=35)
        txt_no_of_tablet.grid(row=3, column=1)

        # Lot
        lbl_lot = tk.Label(data_frame_left, font=("times new roman", 11, "bold"), text="Lot:", padx=2, pady=4)
        lbl_lot.grid(row=4, column=0, sticky=tk.W)
        txt_lot = tk.Entry(data_frame_left, textvariable=self.strvars['lot'], font=("times new roman", 11, "bold"),
                           width=35)
        txt_lot.grid(row=4, column=1)

        # Issue date
        lbl_issue_date = tk.Label(data_frame_left, font=("times new roman", 11, "bold"), text="Issue date:", padx=2)
        lbl_issue_date.grid(row=5, column=0, sticky=tk.W)
        txt_issue_date = tk.Entry(data_frame_left, textvariable=self.strvars['issue_date'],
                                  font=("times new roman", 11, "bold"), width=35)
        txt_issue_date.grid(row=5, column=1)

        # Expiration date
        lbl_exp_date = tk.Label(data_frame_left, font=("times new roman", 11, "bold"), text="Expiration Date:",
                                padx=2, pady=4)
        lbl_exp_date.grid(row=6, column=0, sticky=tk.W)
        txt_exp_date = tk.Entry(data_frame_left, textvariable=self.strvars['exp_date'],
                                font=("times new roman", 11, "bold"), width=35)
        txt_exp_date.grid(row=6, column=1)

        # Daily dose
        lbl_daily_dose = tk.Label(data_frame_left, font=("times new roman", 11, "bold"), text="Daily Dose:", padx=2)
        lbl_daily_dose.grid(row=7, column=0, sticky=tk.W)
        txt_daily_dose = tk.Entry(data_frame_left, textvariable=self.strvars['daily_dose'],
                                   font=("times new roman", 11, "bold"), width=35)
        txt_daily_dose.grid(row=7, column=1)

        # Side effect
        lbl_side_effect = tk.Label(data_frame_left, font=("times new roman", 11, "bold"), text="Side Effect:",
                                    padx=2, pady=4)
        lbl_side_effect.grid(row=8, column=0, sticky=tk.W)
        txt_side_effect = tk.Entry(data_frame_left, textvariable=self.strvars['side_effect'],
                                    font=("times new roman", 11, "bold"), width=35)
        txt_side_effect.grid(row=8, column=1)

        # ===============Patient Info (Right)===============

        # Further info
        lbl_further_info = tk.Label(data_frame_left, font=("times new roman", 11, "bold"),
                                     text="Further Information:", padx=45)
        lbl_further_info.grid(row=0, column=2, sticky=tk.W)
        txt_further_info = tk.Entry(data_frame_left, textvariable=self.strvars['further_info'],
                                    font=("times new roman", 11, "bold"), width=35)
        txt_further_info.grid(row=0, column=3)

        # Blood pressure
        lbl_blood_pressure = tk.Label(data_frame_left, font=("times new roman", 11, "bold"), text="Blood pressure:",
                                       padx=45)
        lbl_blood_pressure.grid(row=1, column=2, sticky=tk.W)
        txt_blood_pressure = tk.Entry(data_frame_left, textvariable=self.strvars['blood_pressure'],
                                       font=("times new roman", 11, "bold"), width=35)
        txt_blood_pressure.grid(row=1, column=3)

        # Storage
        lbl_storage = tk.Label(data_frame_left, font=("times new roman", 11, "bold"), text="Storage:", padx=45)
        lbl_storage.grid(row=2, column=2, sticky=tk.W)
        txt_storage = tk.Entry(data_frame_left, textvariable=self.strvars['storage'],
                                font=("times new roman", 11, "bold"), width=35)
        txt_storage.grid(row=2, column=3)

        # Medicine
        lbl_medicine = tk.Label(data_frame_left, font=("times new roman", 11, "bold"), text="Medicine:", padx=45)
        lbl_medicine.grid(row=3, column=2, sticky=tk.W)
        txt_medicine = tk.Entry(data_frame_left, textvariable=self.strvars['medicine'],
                                 font=("times new roman", 11, "bold"), width=35)
        txt_medicine.grid(row=3, column=3)

        # Patient ID
        lbl_patient_ID = tk.Label(data_frame_left, font=("times new roman", 11, "bold"), text="Patient ID:", padx=45)
        lbl_patient_ID.grid(row=4, column=2, sticky=tk.W)
        txt_patient_ID = tk.Entry(data_frame_left, textvariable=self.strvars['patient_ID'],
                                   font=("times new roman", 11, "bold"), width=35)
        txt_patient_ID.grid(row=4, column=3)

        # Nhs Number
        lbl_Nhs_num = tk.Label(data_frame_left, font=("times new roman", 11, "bold"), text="Nhs Number:", padx=45)
        lbl_Nhs_num.grid(row=5, column=2, sticky=tk.W)
        txt_Nhs_num = tk.Entry(data_frame_left, textvariable=self.strvars['Nhs_num'],
                                font=("times new roman", 11, "bold"), width=35)
        txt_Nhs_num.grid(row=5, column=3)

        # Patient name
        lbl_patient_name = tk.Label(data_frame_left, font=("times new roman", 11, "bold"), text="Patient name:",
                                      padx=45)
        lbl_patient_name.grid(row=6, column=2, sticky=tk.W)
        txt_patient_name = tk.Entry(data_frame_left, textvariable=self.strvars['patient_name'],
                                       font=("times new roman", 11, "bold"), width=35)
        txt_patient_name.grid(row=6, column=3)

        # Date of birth
        lbl_birth_date = tk.Label(data_frame_left, font=("times new roman", 11, "bold"), text="Birth date:",
                                     padx=45)
        lbl_birth_date.grid(row=7, column=2, sticky=tk.W)
        txt_birth_date = DateEntry(data_frame_left, textvariable=self.strvars['birth_date'],
                                     font=("times new roman", 12, "bold"), width=33, background='darkblue',
                                     foreground='white', borderwidth=2)
        txt_birth_date.grid(row=7, column=3)

        # Patient Address
        lbl_patient_address = tk.Label(data_frame_left, font=("times new roman", 11, "bold"),
                                         text="Patient Address:", padx=45)
        lbl_patient_address.grid(row=8, column=2, sticky=tk.W)
        txt_patient_address = tk.Entry(data_frame_left, textvariable=self.strvars['patient_address'],
                                          font=("times new roman", 11, "bold"), width=35)
        txt_patient_address.grid(row=8, column=3)

        #===============Prescription Info (Right)===============
        self.txt_prescription=tk.Text(data_frame_right, font=("times new roman", 11, "bold"), width=38, height=13, padx=2, pady=6)
        self.txt_prescription.grid(row=0, column=0)



        #===================================Button frame===================================
    def mainButton(self):
        button_frame = tk.Frame(self, bd=15, relief=tk.RIDGE, bg="linen")  # Set background color
        button_frame.place(x=0, y=430, width=1366, height=70)


        #===============Buttons===============        
        # Buttons
        button_texts = ["Prescription", "Prescription Data", "Update", "Delete", "Reset", "Exit"]
        button_colours = ["green", "green", "green", "green", "green", "green"]
        button_commands = [None, None, None, None, None, None]  # Fill this list with the respective command functions if needed




        




        for i, (text, color, command) in enumerate(zip(button_texts, button_colours, button_commands)):
            btn_prescription = tk.Button(
                button_frame,
                text=text,
                bg=color,
                fg="white",
                font=("times new roman", 11, "bold"),
                width=23,
                height=1,
                padx=4,
                pady=6,
                command=command
            )
            btn_prescription.grid(row=0, column=i)

        

        #===================================Details frame (bottom)===================================
        #Main frame
    def mainDetails(self):
        details_frame = tk.Frame(self, bd=20, relief=tk.RIDGE, bg="linen")
        details_frame.place(x=0, y=500, width=1366, height=205)

        # Scrollbars
        scroll_x = ttk.Scrollbar(details_frame, orient=tk.HORIZONTAL)
        scroll_y = ttk.Scrollbar(details_frame, orient=tk.VERTICAL)

        # Hospital Table
        self.hospital_table = ttk.Treeview(details_frame, columns=("nameoftable", "ref", "dose", "nooftablets", "lot",
                                                                    "issuedate", "expdate", "dailydose", "storage",
                                                                    "Nhsnumber", "patientname", "birthdate",
                                                                    "patientaddress"),
                                            xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.config(command=self.hospital_table.xview)
        scroll_y.config(command=self.hospital_table.yview)

        scroll_x.pack(side=tk.BOTTOM, fill=tk.X)
        scroll_y.pack(side=tk.RIGHT, fill=tk.Y)

        # Headings
        headings = ["Name of Tablet", "Reference No:", "Dose:", "No. of Tablets:", "Lot:", "Issue date:",
                    "Expiration Date:", "Daily Dose:", "Storage:", "Nhs Number:", "Patient name:", "Birth date:",
                    "Address:"]
        columns = ["nameoftable", "ref", "dose", "nooftablets", "lot", "issuedate", "expdate", "dailydose",
                   "storage", "Nhsnumber", "patientname", "birthdate", "patientaddress"]

        for heading, col in zip(headings, columns):
            self.hospital_table.heading(col, text=heading, anchor=tk.CENTER)
            self.hospital_table.column(col, width=100, anchor=tk.CENTER)

        self.hospital_table["show"] = "headings"
        self.hospital_table.pack(fill=tk.BOTH, expand=1)
        
        

        
        
        
        
        
        
        
        
        

app = HospitalManagement()
app.mainloop()
