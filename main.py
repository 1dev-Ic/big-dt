from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField
from kivy.uix.progressbar import ProgressBar
from kivymd.uix.pickers import MDDatePicker
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.dialog import MDDialog
from kivymd.uix.menu import MDDropdownMenu
from kivy.lang import Builder
from kivy.clock import Clock
from datetime import datetime, date, timedelta
from kivy.metrics import dp
import sqlite3
import json
import os.path
from kivy.uix.image import Image
from kivy.properties import ObjectProperty
from helpers import *
from kivy.core.window import Window

# Window.size = (350 , 600)

class WelcomeScreen(Screen):
    progress_bar = ObjectProperty()
    progress_value = 0
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Set background color to grey
        self.md_bg_color = (0.5, 0.5, 0.5, 1)
        # Add label above the logo
        top_label = MDLabel(text='ASCHMA SSHIA E-DATA TOOL', halign='center', pos_hint={'center_x': 0.5, 'center_y': 0.9}, font_style='H4')
        self.add_widget(top_label)
        # Load the image and add it to the screen
        self.add_widget(Image(source='img/ADSCHMA-logo.png', size_hint=(None, None), size=(200, 200), pos_hint={'center_x': 0.5, 'center_y': 0.6}))
        # Add enter button below the image
        enter_button = MDRectangleFlatButton(text='Get Me In', pos_hint={'center_x': 0.5, 'center_y': 0.3}, on_release=self.on_getstarted_button_click)
        self.add_widget(enter_button)
        # Add progress bar below the button
        self.progress_bar = ProgressBar(max=100, pos_hint={'center_x': 0.5, 'center_y': 0.2}, size_hint=(0.8, None), height=10)
        self.add_widget(self.progress_bar)  
        # Add label below the progress bar
        bottom_label = MDLabel(text='© 2023 Powered by Ishaya, Chahyaandida [08143171712].', halign='center', pos_hint={'center_x': 0.5, 'center_y': 0.1}, font_style='Body1')
        self.add_widget(bottom_label)
    def on_enter(self):
        Clock.schedule_interval(self.update_progress, 0)  
    def on_getstarted_button_click(self, instance):
        # Get the running instance of the app
        app = MDApp.get_running_app()
        # Change the root widget of the app to the main page
        app.root.current = 'main_screen'
    def update_progress(self, dt):
        # Update the progress value
        self.progress_value += 1
        self.progress_bar.value = self.progress_value
        # Stop the progress bar animation when it reaches 100
        if self.progress_value >= 100:
            self.progress_value = 0
            Clock.unschedule(self.update_progress)

class BaseScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Create the toolbar
        self.add_widget(Builder.load_string(basescreen_help))

class MainScreen(BaseScreen):
    pass

class SSHIAScreen(BaseScreen):
    pass

class InputDataScreen(BaseScreen):
    pass

class ViewScreen(BaseScreen):
    pass

class ExportScreen(BaseScreen):
    pass

class PHCDataViewScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # create a data table widget for the student details
        table = MDDataTable(
            size_hint=(0.9, 0.85),
            pos_hint={'center_x': 0.5, 'center_y': 0.45},
            column_data=[("QUESTION", dp(100)), ("FINDINGS", dp(30))],
            row_data= self.populate_data(),
            use_pagination=True,
            rows_num = 1
        )
        # add data table to the screen
        self.add_widget(table)
    # method to populate table data
    def populate_data(self):
        # get the data from the database or some other source
        conn = sqlite3.connect('ASCHMA/db/sshiadb.db')
        c = conn.cursor()
        try:
            c.execute("SELECT * FROM phc_data")
        except sqlite3.OperationalError:  # catch error if table doesn't exist
            return []  # return empty list if table doesn't exist
        rows = c.fetchall()
        if not rows:  # if no rows in the table, return empty list
            return []
        data_list = []  # create empty list to store data for each record
        for row in rows:
            total_deaths = int(row[27]) + int(row[28]) + int(row[29]) + int(row[30])
            total_services = int(row[10]) + int(row[11]) + int(row[12]) + int(row[13]) + int(row[14]) + int(row[15]) + int(row[16]) + int(row[17]) + int(row[18]) + int(row[19]) + int(row[20]) + int(row[21]) + int(row[22]) + int(row[23]) + int(row[24]) + int(row[25])
            data = [
                "Name of Health facility", row[0],
                "Reporting Month", row[1],
                "Did you receive list of enrollees for this facility? ", row[2],
                "What is the total number of enrollees in your facility? ", row[3],
                "Have you received payment for capitation?", row[4],
                "What date have you received payment?", row[5],
                "Were you notified through pay advice or any documentary means?", row[6],
                "Amount received for capitation", row[7],
                "Number of enrollees that access service in this facility?", row[8],
                "Number of services utilised by enrollees in this facility", total_services,
                "Number of referred enrollees from this facility", row[10],
                "Number of enrollees that attend ANC", row[11],
                "Number of enrollees that had normal delivery", row[12],
                "Number of enrollees that accessed in immunization", row[13],
                "Number of enrolles that were treated for malaria (Under 5 years old)", row[14],
                "Number of enrollees that were treated for malaria (Above 5 years old)", row[15],
                "Number of enrollees that were screened for hypertension", row[16],
                "Number of enrollees that were screened for diabetes mellitus", row[17],
                "Number of enrollees that were treated for typhoid fever", row[18],
                "Number of enrollees that were treated for respiratory tract infection (Under 5 years old)", row[19],
                "Number of enrollees that were treated for respiratory tract infection (Above 5 years old)", row[20],
                "Number of enrollees that were treated for diarrhoea (Under 5 years old)", row[21],
                "Number of enrollees that were treated for diarrhoea (Above 5 years old)", row[22],
                "Number of enrollees that were treated for urinary tract infection", row[23],
                "Number of enrollees that were treated for gastroenteritis", row[24],
                "Others", row[25],
                "Total deaths", total_deaths,
                "Maternal deaths", row[27],
                "Neonatal deaths", row[28],
                "Infant deaths", row[29],
                "Children deaths", row[30]   
            ]
            data_list.append(data)  # append data for this record to list
        conn.close()
        return data_list
    
class SHCDataViewScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # create a data table widget for the student details
        table = MDDataTable(
            size_hint=(0.9, 0.85),
            pos_hint={'center_x': 0.5, 'center_y': 0.45},
            column_data=[("QUESTION", dp(100)), ("FINDINGS", dp(30))],
            row_data= self.populate_data(),
            use_pagination=True,
            rows_num = 1
        )
        # add data table to the screen
        self.add_widget(table)
    # method to populate table data
    def populate_data(self):
        # get the data from the database or some other source
        conn = sqlite3.connect('ASCHMA/db/sshiadb.db')
        c = conn.cursor()
        try:
            c.execute("SELECT * FROM shc_data")
        except sqlite3.OperationalError:  # catch error if table doesn't exist
            return []  # return empty list if table doesn't exist
        rows = c.fetchall()
        if not rows:  # if no rows in the table, return empty list
            return []
        data_list = []  # create empty list to store data for each record
        for row in rows:
            total_deaths = int(row[18]) + int(row[19]) + int(row[20]) + int(row[21])
            data = [
                "Name of Health facility", row[0],
                "When was the last claim submitted to SSHIA?", row[1],
                "Which month did you cover?", row[2],
                "Amount requested in the last submitted claims stated above", row[3],
                "When was the last claim reimbursement received?", row[4],
                "Indicate the month for which the reimbursement covers", row[5],
                "Reimbursement received", row[6],
                "Number of enrollees that were referred to your facility in the reporting month", row[7],
                "Number of enrollees that were referred for cesarean section", row[8],
                "Number of enrollees that were treated for hypertension", row[9],
                "Number of enrollees were treated for diabetes mellitus", row[10],
                "Number of enrollees that were treated for severe malaria (Under 5 years old)", row[11],
                "Number of enrollees that were treated for severe malaria (above 5 years old)", row[12],
                "Number of enrollees that were treated for complicated RTI (Under 5 years old)", row[13],
                "Number of enrollees that were treated for complicated RTI (Above 5 years old)", row[14],
                "Number of enrollees that were treated for complicated typhoid fever", row[15],
                "Others", row[16],
                "Total deaths", total_deaths,
                "Maternal deaths", row[18],
                "Neonatal deaths", row[19],
                "Infant deaths", row[20],
                "Children deaths", row[21]   
            ]
            data_list.append(data)  # append data for this record to list
        conn.close()
        return data_list
    
class SSHIADataViewScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # create a data table widget for the student details
        table = MDDataTable(
            size_hint=(0.9, 0.85),
            pos_hint={'center_x': 0.5, 'center_y': 0.45},
            column_data=[("QUESTION", dp(120)), ("FINDINGS", dp(20))],
            row_data= self.populate_data(),
            use_pagination=True,
            rows_num = 1
        )
        # add data table to the screen
        self.add_widget(table)
        
    # method to populate table data
    def populate_data(self):
        # get the data from the database or some other source
        conn = sqlite3.connect('ASCHMA/db/sshiadb.db')
        c = conn.cursor()
        try:
            c.execute("SELECT * FROM phc_data")
        except sqlite3.OperationalError:  # catch error if table doesn't exist
            return []  # return empty list if table doesn't exist
        rows = c.fetchall()
        if not rows:  # if no rows in the table, return empty list
            return []
        #fetching from shc db
        try:
            c.execute("SELECT * FROM shc_data")
        except sqlite3.OperationalError:  # catch error if table doesn't exist
            pass  # return empty list if table doesn't exist
        items = c.fetchall()
        if not items and not rows:  # if no rows in the table, return empty list
            return []
        
        data_list = []  # create empty list to store data for each record
       
        ######## calculate the total for each column in shc db#######
        claims_reimbursed_not_lt30_days = claims_reimbursed_rm = submited_claims_w30days = submited_claims_for_rm = s_date_last_claim = s_month_covered = s_amount_requested = s_date_claim_reimbursed = s_imburment_month = s_reimbursement_amount = s_referred_enrollees = s_caesarean = s_treated_hypertension = s_treated_diabetes_mellitus = s_treated_malaria_under_5 = s_treated_malaria_above_5 = s_treated_rti_under_5 = s_treated_rti_above_5 = s_treated_typhoid = s_others = s_total_deaths = s_maternal_death = s_neonatal = s_infant = s_children = 0
        for item in items: 
            # s_health_facility_name += int(item[0])
            s_date_last_claim = datetime.strptime(item[1], '%d/%m/%Y')
            s_month_covered = datetime.strptime(item[2], '%B').month
            s_amount_requested += int(item[3])
            s_date_claim_reimbursed = datetime.strptime(item[4], '%d/%m/%Y')
            s_imburment_month = datetime.strptime(item[5], '%B').month
            s_reimbursement_amount += int(item[6])
            s_referred_enrollees += int(item[7])
            s_caesarean += int(item[8])
            s_treated_hypertension += int(item[9])
            s_treated_diabetes_mellitus += int(item[10])
            s_treated_malaria_under_5 += int(item[11])
            s_treated_malaria_above_5 += int(item[12])
            s_treated_rti_under_5 += int(item[13])
            s_treated_rti_above_5 += int(item[14])
            s_treated_typhoid += int(item[15])
            s_others += int(item[16])
            # s_total_deaths += int(item[17])
            s_maternal_death += int(item[18])
            s_neonatal += int(item[19])
            s_infant += int(item[20])
            s_children += int(item[21])
            s_total_deaths += s_maternal_death + s_neonatal + s_infant + s_children
            
            # Get the current month and year
            current_month = date.today().month
            current_year = date.today().year

            # Calculate the previous month and year
            if current_month == 1:
                previous_month = 12
                previous_year = current_year - 1
            else:
                previous_month = current_month - 1
                previous_year = current_year

            # Check if s_month_covered is equal to the previous month
            if s_month_covered == previous_month:
                submited_claims_for_rm += 1

            # Calculate the end of the previous month
            end_of_reporting_month = datetime(previous_year, current_month, 1) - timedelta(days=1)

            # Calculate the number of days between the end of the previous month
            # and s_date_last_claim
            days_since_reporting_month_end = (s_date_last_claim - end_of_reporting_month).days

            # Check if s_date_last_claim is within 30 days from the end of the previous month
            if days_since_reporting_month_end <= 30:
                submited_claims_w30days += 1
            
            # Number of SHCs in this LGA whose vetted claims were reimbursed for the reporting month    
            if s_imburment_month == previous_month:
                claims_reimbursed_rm += 1
            
            #calulate the number of days within when last claim submited and when reimbursent received    
            days_not_later_than_30_days = (s_date_claim_reimbursed - s_date_last_claim).days
            
            #check Number of SHCs in this LGA whose vetted claims were reimbursed not later than 30 days from claim submission for the reporting month
            if days_not_later_than_30_days <= 30:
                claims_reimbursed_not_lt30_days += 1
            
        ####### calculate the total for each column in phc db########
        report_month = received_list = total_enrollees = received_payment = payment_date = notified_payment = capitation_received = service_enrollees = utilised_services = referred_enrollees = anc_enrollees = normal_delivery = immunization_services = treated_malaria_under_5 = treated_malaria_above_5 = treated_hypertension = treated_diabetes_mellistus = treated_typhoid = treated_rti_under_5 = treated_rti_above_5 = treated_diarrhea_under_5 = treated_diarrhea_above_5 = treated_uti = treated_gastroenteritis = others = total_deaths = maternal_death = neonatal = infant = children = payment_in_five_days = 0
        for row in rows:
            report_month = datetime.strptime(row[1], '%B').month
            received_list += row[2] == "Yes"
            total_enrollees += int(row[3])
            received_payment += row[4] == "Yes"
            # notified_payment += int(row[6]) == "Yes"
            capitation_received += int(row[7])
            service_enrollees += int(row[8])
            # utilised_services += int(row[9])
            referred_enrollees += int(row[10])
            anc_enrollees += int(row[11])
            normal_delivery += int(row[12])
            immunization_services += int(row[13])
            treated_malaria_under_5 += int(row[14])
            treated_malaria_above_5 += int(row[15])
            treated_hypertension += int(row[16])
            treated_diabetes_mellistus += int(row[17])
            treated_typhoid += int(row[18])
            treated_rti_under_5 += int(row[19])
            treated_rti_above_5 += int(row[20])
            treated_diarrhea_under_5 += int(row[21])
            treated_diarrhea_above_5 += int(row[22])
            treated_uti += int(row[23])
            treated_gastroenteritis += int(row[24])
            others += int(row[25])
            # total_deaths += int(row[26])
            maternal_death += int(row[27])
            neonatal += int(row[28])
            infant += int(row[29])
            children += int(row[30])
            total_deaths = maternal_death + neonatal + infant + children
            total_services = referred_enrollees + anc_enrollees + normal_delivery + immunization_services + treated_malaria_under_5 + treated_malaria_above_5 + treated_hypertension + treated_diabetes_mellistus + treated_typhoid + treated_rti_under_5 + treated_rti_above_5 + treated_diarrhea_under_5 + treated_diarrhea_above_5 + treated_uti + treated_gastroenteritis + others
            # exception to pass empty datefield for capitation payment
            if row[5] != '' or len(row[5]) != 0:
                payment_date = datetime.strptime(row[5], '%d/%m/%Y').day
                #condition to check whether payment was made in 5 days
                if payment_date <= 5 and payment_date <= report_month:
                    payment_in_five_days += 1
                
        data = [
            ############## ENROLLMENT####################
            "***ENROLLMENT***" , "***",
            "Number of PHCs in this LGA that received the list of BHCPF enrollees for for the reporting month? ", received_list,
            "Total number of BHCPF enrollees in this LGA",total_enrollees,
            " ", " ",
            
            ################## FINANCIAL ############# MANAGEMENT ##########
            "***FINANCIAL MANAGEMENT***" , "***",
            "Number of PHCs in this LGA that received payment for capitation in the reporting month", received_payment,
            "Number of PHCs that received payment for capitation within the first five days of the reporting month", payment_in_five_days,
            "Amount in total received by PHCs in this LGA for capitation in the reporting month", capitation_received,
            "The number of SHCs in this LGA that submitted claims to SSHIA for the reporting month", submited_claims_for_rm,
            "The number of SHCs in this LGA that submitted claims to SSHIA within 30 days from the end of the reporting month", submited_claims_w30days,
            "Total amount requested in the claims submitted for the reporting month", s_amount_requested,
            "Number of SHCs in this LGA whose vetted claims were reimbursed for the reporting month", claims_reimbursed_rm,
            "Number of SHCs in this LGA whose vetted claims were reimbursed not later than 30 days from claim submission for the reporting month", claims_reimbursed_not_lt30_days,
            "Total amount reimbursed", s_reimbursement_amount,
            " ", " ",
            
            ########## PHC ###### SERVICE UTILIZATION ########### 
            "***PHC SERVICE UTILIZATION***" , "***",
            "Number of enrollees that access service in this PHCs in the reporting month?", service_enrollees,
            "Number of services utilised by enrollees in this LGA for the reporting month", total_services,
            "Number of enrollees in total that were referred from PHCs in the reporting month", referred_enrollees,
            "Number of BHCPF enrollees that attend ANC in PHCs in this LGA", anc_enrollees,
            "Number of BHCPF enrollees that had normal delivery in PHCs in this LGA in the reporting month", normal_delivery,
            "Number of BHCPF enrollees that accessed in immunization in PHCs in this LGA in the reporting month", immunization_services,
            "Number of BHCPF enrolles that were treated for malaria in PHCs in this LGA in the reporting month (Under 5 years old)", treated_malaria_under_5,
            "Number of BHCPF enrollees that were treated for malaria in PHCs in this LGA in the reporting month (Above 5 years old)", treated_malaria_above_5,
            "Number of BHCPF enrollees that were screened for hypertension in PHCs in this LGA in the reporting month", treated_hypertension,
            "Number of BHCPF enrollees that were screened for diabetes mellitus in PHCs in this LGA in the reporting month", treated_diabetes_mellistus,
            "Number of BHCPF enrollees that were treated for typhoid fever in PHCs in this LGA in the reporting month", treated_typhoid,
            "Number of BHCPF enrollees that were treated for respiratory tract infection in PHCs in this LGA in the reporting month (Under 5 years old)", treated_rti_under_5,
            "Number of BHCPF enrollees that were treated for respiratory tract infection in PHCs in this LGA in the reporting month (Above 5 years old)", treated_rti_above_5,
            "Number of BHCPF enrollees that were treated for diarrhea in PHCs in this LGA in the reporting month (Under 5 years old)", treated_diarrhea_under_5,
            "Number of BHCPF enrollees that were treated for diarrhea in PHCs in this LGA in the reporting month (Above 5 years old)", treated_diarrhea_above_5,
            "Number of BHCPF enrollees that were treated for urinary tract infection in PHCs in this LGA in the reporting month", treated_uti,
            "Number of BHCPF enrollees that were treated for gastroenteritis in PHCs in this LGA in the reporting month", treated_gastroenteritis,
            "Others", others,
            "Total deaths", total_deaths,
            "Maternal deaths", maternal_death,
            "Neonatal deaths (0-30 days)", neonatal,
            "Infant deaths (1-12 months)", infant,
            "Children deaths (1-5 years)", children,
            " ", " ",   
            
            ########## SHC ###### SERVICE UTILIZATION ###########
            "***SHC SERVICE UTILIZATION***" , "***",
            "Number of BHCPF enrollees that were referred for cesarean section to the SHCPs in this LGA in the reporting month", s_caesarean,
            "Number of BHCPF enrollees that were treated for hypertension in SHCPs in this LGA in the reporting month", s_treated_hypertension,
            "Number of BHCPF enrollees were treated for diabetes mellitus in SHCPs in this LGA in the reporting month", s_treated_diabetes_mellitus,
            "Number of BHCPF enrollees that were treated for severe malaria in SHCPs in this LGA in the reporting month (Under 5 years old)", s_treated_malaria_under_5,
            "Number of BHCPF enrollees that were treated for severe malaria in SHCPs in this LGA in the reporting month (above 5 years old)", s_treated_malaria_above_5,
            "Number of BHCPF enrollees that were treated for complicated respiratory tract infection in SHCPs in this LGA in the reporting month (Under 5 years old)", s_treated_rti_under_5,
            "Number of BHCPF enrollees that were treated for complicated respiratory tract infection in SHCPs in this LGA in the reporting month (Above 5 years old)", s_treated_rti_above_5,
            "Number of BHCPF enrollees that were treated for complicated typhoid fever in SHCPs in this LGA in the reporting month", s_treated_typhoid,
            "Others", s_others,
            "Total deaths", s_total_deaths,
            "Maternal deaths", s_maternal_death,
            "Neonatal deaths", s_neonatal,
            "Infant deaths", s_infant,
            "Children deaths", s_children
        ]
        data_list.append(data)  # append data for this record to list
        conn.close()
        return data_list 


class CustomDialog(MDDialog):
    pass

class DateTextField(MDTextField):
    def on_focus(self, instance, value):
        if value:
            date_dialog = MDDatePicker()
            date_dialog.bind(on_save=self.set_date)
            date_dialog.open()

    def set_date(self, instance, value, date_range):
        self.text = value.strftime('%d/%m/%Y')

class ADSCHMAApp(MDApp):
    def build(self):
         # Use the KivyMD theme
        self.app = MDApp.get_running_app()
        self.theme_cls.primary_palette = 'Green'
        self.theme_cls.primary_hue = "900"
        self.theme_cls.accent_palette = 'Teal'
        
        # Create the screen manager
        self.sm = ScreenManager()
        
    #     # Schedule the switch to the main screen after 60 seconds
    #     Clock.schedule_once(self.switch_to_main_screen, 6)
    #     # Switch to the main screen
    # def switch_to_main_screen(self, *args):
    #     self.sm.current = 'main_screen'

        # Add the screens to the screen manager
        self.sm.add_widget(WelcomeScreen(name='welcome_screen'))
        self.sm.add_widget(Builder.load_string(mainscreen_help))
        self.sm.add_widget(Builder.load_string(sshia_screen_help))
        self.sm.add_widget(Builder.load_string(data_input_screen_help))
        self.sm.add_widget(Builder.load_string(phcdata_input_screen_help))
        self.sm.add_widget(Builder.load_string(shcdata_input_screen_help))
        self.sm.add_widget(Builder.load_string(view_screen_help))
        self.sm.add_widget(Builder.load_string(phc_data_view_screen_help))
        self.sm.add_widget(Builder.load_string(shc_data_view_screen_help))
        self.sm.add_widget(Builder.load_string(sshia_data_view_screen_help))
        self.sm.add_widget(Builder.load_string(export_screen_help))

        # Set the current screen to the welcome screen
        self.sm.current = 'welcome_screen'
        #return the screen manager
        return self.sm
    
    #save sshia data to database 
    def save_sshia_data(self, name, rank, lga, phc, shc):
        Builder.load_string(custom_mddialog)
        if not all([name, rank, lga, phc, shc]):
            dialog = CustomDialog()
            dialog.title = "Error"
            dialog.type = "alert"
            dialog.text = "Fields cannot be empty"
            close_button = dialog.ids.close_btn
            close_button.text = "Close"
            dialog.open()
        else:
            data = {'name': name, 'rank': rank, 'lga': lga, 'phc': phc, 'shc': shc}
            with open('ASCHMA/data/user_data.json', 'w') as f:
                json.dump(data, f)
                f.write('\n')
            dialog = CustomDialog()
            close_button = dialog.ids.close_btn
            close_button.text = "Close"
            next_button = dialog.ids.next_btn
            next_button.text = "Next"
            next_button = dialog.ids.next_btn
            next_button.on_release = self.change_to_data_input_screen
            dialog.open()
            dialog.title = "Success"
            dialog.text = "Recorded successfully"
        self.sm.current = 'sshia_screen'
        
    #change the current screen to phc data screen
    def change_to_phc_screen(self):
        self.sm.current = 'phcdata_input_screen'
    #change the current screen to shc data screen
    def change_to_shc_screen(self):
        self.sm.current = 'shcdata_input_screen'
    #change the current screen to data input screen
    def change_to_data_input_screen(self):
        self.sm.current = 'data_input_screen'
    #save phc data form input  
    def save_phc_data(self, health_facility_name, report_month, received_list, total_enrollees, received_payment, payment_date, notified_payment, capitation_received, service_enrollees, utilised_services, referred_enrollees, anc_enrollees, normal_delivery, immunization_services, treated_malaria_under_5, treated_malaria_above_5, treated_hypertension, treated_diabetes_mellistus, treated_typhoid, treated_rti_under_5, treated_rti_above_5, treated_diarrhea_under_5, treated_diarrhea_above_5, treated_uti, treated_gastroenteritis, others, total_deaths, maternal_death, neonatal, infant, children):
        Builder.load_string(custom_mddialog)
        if not all([health_facility_name, report_month, received_list, total_enrollees, received_payment, notified_payment, capitation_received, service_enrollees, utilised_services, referred_enrollees, anc_enrollees, normal_delivery, immunization_services, treated_malaria_under_5, treated_malaria_above_5, treated_hypertension, treated_diabetes_mellistus, treated_typhoid, treated_rti_under_5, treated_rti_above_5, treated_diarrhea_under_5, treated_diarrhea_above_5, treated_uti, treated_gastroenteritis, others, total_deaths, maternal_death, neonatal, infant, children]):
            dialog = CustomDialog()
            close_button = dialog.ids.close_btn
            close_button.text = "Close"
            next_button = dialog.ids.next_btn
            next_button.on_release = self.change_to_phc_screen
            dialog.title = "Error"
            dialog.type = "alert"
            dialog.text = "Fields cannot be empty"
            dialog.open()
        else:
            conn = sqlite3.connect('ASCHMA/db/sshiadb.db')
            c = conn.cursor()
            c.execute('''CREATE TABLE IF NOT EXISTS phc_data
                        (health_facility_name text, report_month text, received_list text, total_enrollees text, received_payment text, payment_date text, notified_payment text, capitation_received text, service_enrollees text, utilised_services text, referred_enrollees text, anc_enrollees text, normal_delivery text, immunization_services text, treated_malaria_under_5 text, treated_malaria_above_5 text, treated_hypertension text, treated_diabetes_mellistus text, treated_typhoid text, treated_rti_under_5 text, treated_rti_above_5 text, treated_diarrhea_under_5 text, treated_diarrhea_above_5 text, treated_uti text, treated_gastroenteritis text, others text, total_deaths text, maternal_death text, neonatal text, infant text, children text)''')
            c.execute("INSERT INTO phc_data VALUES (?, ?, ?, ?, ?,?, ?, ?, ?, ?,?, ?, ?, ?, ?,?, ?, ?, ?, ?,?, ?, ?, ?, ?,?, ?, ?, ?, ?,?)",
                      (health_facility_name, report_month, received_list, total_enrollees, received_payment, payment_date, notified_payment, capitation_received, service_enrollees, utilised_services, referred_enrollees, anc_enrollees, normal_delivery, immunization_services, treated_malaria_under_5, treated_malaria_above_5, treated_hypertension, treated_diabetes_mellistus, treated_typhoid, treated_rti_under_5, treated_rti_above_5, treated_diarrhea_under_5, treated_diarrhea_above_5, treated_uti, treated_gastroenteritis, others, total_deaths, maternal_death, neonatal, infant, children))
            conn.commit()
            conn.close()
            #send success alert to the user
            dialog = CustomDialog()
            close_button = dialog.ids.close_btn
            close_button.text = "Close"
            next_button = dialog.ids.next_btn
            next_button.text = "Next"
            next_button = dialog.ids.next_btn
            next_button.on_release = self.change_to_data_input_screen
            dialog.open()
            dialog.title = "Success"
            dialog.text = "Recorded successfully"
            
    #save shc data form input   
    def save_shc_data(self,  health_facility_name, date_last_claim, month_covered, amount_requested, claim_reimbursed, imburment_month, reimbursement_amount, referred_enrollees, caesarean, treated_hypertension, treated_diabetes_mellitus, treated_malaria_under_5, treated_malaria_above_5, treated_rti_under_5, treated_rti_above_5, treated_typhoid, others, total_deaths, maternal_death, neonatal, infant, children):
        Builder.load_string(custom_mddialog)
        if not all([ health_facility_name, date_last_claim, month_covered, amount_requested,  referred_enrollees, caesarean, treated_hypertension, treated_diabetes_mellitus, treated_malaria_under_5, treated_malaria_above_5, treated_rti_under_5, treated_rti_above_5, treated_typhoid, others, total_deaths, maternal_death, neonatal, infant, children]):
            dialog = CustomDialog()
            close_button = dialog.ids.close_btn
            close_button.text = "Close"
            next_button = dialog.ids.next_btn
            next_button.on_release = self.change_to_shc_screen
            dialog.title = "Error"
            dialog.type = "alert"
            dialog.text = "Fields cannot be empty"
            dialog.open()
        else:
            conn = sqlite3.connect('ASCHMA/db/sshiadb.db')
            c = conn.cursor()
            c.execute('''CREATE TABLE IF NOT EXISTS shc_data
                        (health_facility_name text, date_last_claim text, month_covered text, amount_requested text, claim_reimbursed text, imburment_month text, reimbursement_amount text, referred_enrollees text, caesarean text, treated_hypertension text, treated_diabetes_mellitus text, treated_malaria_under_5 text, treated_malaria_above_5 text, treated_rti_under_5 text, treated_rti_above_5 text, treated_typhoid text, others text, total_deaths text, maternal_death text, neonatal text, infant text, children text)''')
            c.execute("INSERT INTO shc_data VALUES (?, ?, ?,?,?,?,?, ?, ?, ?,?,?, ?, ?, ?,?,?, ?, ?, ?,?,?)",
                      (health_facility_name, date_last_claim, month_covered, amount_requested, claim_reimbursed, imburment_month, reimbursement_amount, referred_enrollees, caesarean, treated_hypertension, treated_diabetes_mellitus, treated_malaria_under_5, treated_malaria_above_5, treated_rti_under_5, treated_rti_above_5, treated_typhoid, others, total_deaths, maternal_death, neonatal, infant, children))
            conn.commit()
            conn.close()
            #send success alert to the user
            dialog = CustomDialog()
            close_button = dialog.ids.close_btn
            close_button.text = "Close"
            next_button = dialog.ids.next_btn
            next_button.text = "Next"
            next_button = dialog.ids.next_btn
            next_button.on_release = self.change_to_data_input_screen
            dialog.open()
            dialog.title = "Success"
            dialog.text = "Recorded successfully"

    # list of months
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    # list of LGAs in ADAMAWA
    lgas = ["Demsa", "Fufore", "Ganye", "Girei", "Gombi", "Guyuk", "Hong", "Jada", "Lamurde", "Madagali", "Maiha", "Mayo-Belwa","Michika", "Mubi North", "Mubi South", "Numan", "Shelleng","Song", "Toungo", "Yola North", "Yola South"]
   
    #method to show yes or no sellection in textfield
    def show_yes_or_no(self, caller):
        menu_items = [{"text": option, "viewclass": "OneLineListItem", "on_release": lambda x=option: (setattr(caller, 'text', x), self.menu.dismiss())} for option in ["Yes", "No"]]
        self.menu = MDDropdownMenu(
            caller=caller,
            items=menu_items,
            position="center",
            width_mult=2,
        )
        self.menu.open()
        
    #method to show months as selection in textfield   
    def show_months(self, caller):
        menu_items = [{"text": month, "viewclass": "OneLineListItem", "on_release": lambda x=month: setattr(caller, 'text', x)} for month in self.months]
        self.menu = MDDropdownMenu(
            caller=caller,
            items=menu_items,
            position="center",
            width_mult=2,
        )
        self.menu.open()
    
    #method to show the list of lgas selection in textfield    
    def show_lgas(self, caller):
        menu_items = [{"text": lga, "viewclass": "OneLineListItem", "on_release": lambda x=lga: setattr(caller, 'text', x)} for lga in self.lgas]
        self.menu = MDDropdownMenu(
            caller=caller,
            items=menu_items,
            position="center",
            width_mult=2,
        )
        self.menu.open()
    
    #function to clear app user data in database 
    def del_data(self):
        try:
            # establish database connection
            conn = sqlite3.connect('ASCHMA/db/sshiadb.db')
            c = conn.cursor()
            # delete tables
            c.execute("DROP TABLE IF EXISTS phc_data")
            c.execute("DROP TABLE IF EXISTS shc_data")
            # commit changes
            conn.commit()
            # print success message
            Builder.load_string(custom_mddialog)
            dialog = CustomDialog()
            close_button = dialog.ids.close_btn
            close_button.text = "Close"
            dialog.title = "Success!"
            dialog.type = "alert"
            dialog.text = "Table data cleared successfully!"
            dialog.open()
        except sqlite3.Error as error:
            Builder.load_string(custom_mddialog)
            dialog = CustomDialog()
            close_button = dialog.ids.close_btn
            close_button.text = "Close"
            dialog.title = "Oops!"
            dialog.type = "alert"
            dialog.text = "No data available to clear"
            dialog.open()
        finally:
            # close cursor and database connection
            if c:
                c.close()
            if conn:
                conn.close()   
    
    def clear_data(self):
        Builder.load_string(custom_mddialog)
        dialog = CustomDialog()
        close_button = dialog.ids.close_btn
        close_button.text = "No"
        next_button = dialog.ids.next_btn
        next_button.text = "Yes"
        next_button.on_release = self.del_data
        dialog.title = "Warning!!!"
        dialog.type = "alert"
        dialog.text = "Do you want to clear app data?"
        dialog.open()
        
    #function to get name from JSON data
    def get_name(self):
        if not os.path.exists('ASCHMA/data/user_data.json'):
            return ""
        with open('ASCHMA/data/user_data.json', 'r') as f:
            data_list = [json.loads(line) for line in f]
        for data in data_list:
            name = data['name']
        return name
    
    #function to export data to pdf
    def export_pdf(self):
        # message not available
        Builder.load_string(custom_mddialog)
        dialog = CustomDialog()
        close_button = dialog.ids.close_btn
        close_button.text = "Close"
        dialog.title = "Oops!"
        dialog.type = "alert"
        dialog.text = "Comming Soon!"
        dialog.open()
    #function to export data to excel
    def export_excel(self):
        # message not available
        Builder.load_string(custom_mddialog)
        dialog = CustomDialog()
        close_button = dialog.ids.close_btn
        close_button.text = "Close"
        dialog.title = "Oops!"
        dialog.type = "alert"
        dialog.text = "Comming Soon!"
        dialog.open()
    #function to export data to server
    def send_to_server(self):
        # message not available
        Builder.load_string(custom_mddialog)
        dialog = CustomDialog()
        close_button = dialog.ids.close_btn
        close_button.text = "Close"
        dialog.title = "Oops!"
        dialog.type = "alert"
        dialog.text = "Comming Soon!"
        dialog.open()

### METHOD ### TO ### RUN ### APP #########       
if __name__ == '__main__':
    ADSCHMAApp().run()
