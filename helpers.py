#helper files
custom_mddialog = '''
<CustomDialog>:
    size_hint: .7, .2
    auto_dismiss: True
    title: 'Success'
    type: 'alert'
    BoxLayout:
        orientation: 'horizontal'
        padding: dp(2)
        spacing: '80dp'
        MDFlatButton:
            id: close_btn
            text: ''
            on_release: root.dismiss()
        MDFlatButton:
            id: next_btn
            text: ''
            on_release: root.dismiss()
'''

basescreen_help = """
Screen:
    name: 'base_screen'
    BoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title: 'ASCHMA SSHIA Data Collection Tool'
            left_action_items: [["menu", lambda x: nav_drawer.set_state('open')]]
            elevation:5
        MDLabel:
            text: 
            halign: 'center'
            size_hint_y: 0.9

    MDNavigationDrawer:
        id: nav_drawer
        
        MDBoxLayout:
            orientation: 'vertical'
            padding: '5dp'
            spacing: '10dp'
            
            Image:
                source: 'img/ADSCHMA-logo.png'
                size_hint: None, None
                size: "120dp", "120dp"
            
            ScrollView:    
                MDList:
                    OneLineIconListItem:
                        text: "Home"
                        on_release: app.root.current = 'main_screen'
                        IconLeftWidget:
                            icon: "home"
                    OneLineIconListItem:
                        text: "SSHIA"
                        on_release: app.root.current = 'sshia_screen'
                        IconLeftWidget:
                            icon: "folder"
                    OneLineIconListItem:
                        text: "Input data"
                        on_release: app.root.current = 'data_input_screen'
                        IconLeftWidget:
                            icon: "pencil"
                    OneLineIconListItem:
                        text: "View"
                        on_release: app.root.current = 'view_screen'
                        IconLeftWidget:
                            icon: "eye"
                    OneLineIconListItem:
                        text: "Export"
                        on_release: app.root.current = 'export_screen'
                        IconLeftWidget:
                            icon: "export"
                    OneLineIconListItem:
                        text: "Exit"
                        on_release: app.stop()
                        IconLeftWidget:
                            icon: "exit-to-app"
"""

mainscreen_help = """
Screen:
    name: 'main_screen'
    ScrollView:
        GridLayout:
            cols: 1
            spacing: 20
            padding: [50, 80, 50, 50]
            MDLabel:
                id: welcome_text
                text: app.get_name()
                # text: 'Welcome, [M&E OFFICER].'
                halign: 'left'
                font_style: 'H6'
            MDLabel:
                text: 'This is Big-DT, used to summarize PHCs and SHCs Data.'
                halign: 'left'
                font_style: 'Body1'
                
            MDLabel:
                text: 'When the you click on the SSHIA button, you will be directed to a screen where you can add your personal details. Clicking on the Input Data button will open a screen where you can select either add PHC data or add SHC data to add new data. Clicking on the View button will show you a list of the records you entered in the data input page and also show the summarized data. Clicking on the Export Data button will allow you to export the summarized data into various formats such as Excel, or PDF.'
                halign: 'justify'
                font_style: 'Body1'
                size_hint_y: None
                height: self.texture_size[1] + 20
            MDRectangleFlatButton:
                icon: 'trash-can'
                text: 'Clear App Data'
                font_size: '14sp'
                md_bg_color: app.theme_cls.error_color
                pos_hint: {'center_x': 0.5, 'center_y': 0.1}
                on_release: app.clear_data()
            
    BaseScreen:
                        
"""

sshia_screen_help = """
Screen:
    name: 'sshia_screen'
    BoxLayout:
        orientation: 'vertical'
        FloatLayout:
            MDLabel:
                text: 'LGA Information'
                halign: 'center'
                font_style: 'H6'
                pos_hint: {"center_x": .5, "center_y": .8}
            MDTextField:
                id: name_field
                hint_text: 'Name'
                required: True
                helper_text: "Enter your name here"
                helper_text_mode: "on_error"
                icon_right: "account"
                pos_hint: {"center_x": .5, "center_y": .63}
                size_hint_x: .7
            MDTextField:
                id: rank_field
                hint_text: 'Rank'
                required: True
                helper_text: "Enter Rank here"
                helper_text_mode: "on_error"
                text: 'M & E Officer'
                pos_hint: {"center_x": .5, "center_y": .5}
                size_hint_x: .7
            MDTextField:
                id: lga_field
                hint_text: 'LGA'
                required: True
                helper_text: "Select your LGA here"
                helper_text_mode: "on_error"
                icon_right: "map-marker"
                pos_hint: {"center_x": .5, "center_y": .4}
                size_hint_x: .7
                on_focus: app.show_lgas(self)
            MDTextField:
                id: phc_field
                hint_text: 'No of PHCs'
                required: True
                helper_text: "Numeric field"
                helper_text_mode: "on_error"
                input_filter: 'int'
                pos_hint: {"center_x": .32, "center_y": .3}
                size_hint_x: .33   
            MDTextField:
                id: shc_field
                hint_text: 'No. of SHCs'
                required: True
                helper_text: "Numeric field"
                helper_text_mode: "on_error"
                input_filter: 'int'
                pos_hint: {"center_x": .68, "center_y": .3}
                size_hint_x: .33
            MDRectangleFlatButton:
                text: 'Save'
                on_release: app.save_sshia_data(name_field.text, rank_field.text, lga_field.text, phc_field.text, shc_field.text)
                pos_hint: {"center_x": .5, "center_y": .17}

    BaseScreen:
      
"""

phcdata_input_screen_help = """
Screen:
    name: 'phcdata_input_screen'
    BoxLayout:
        orientation: 'vertical'
        ScrollView:
            BoxLayout:
                orientation: 'vertical'
                padding: [30, 100, 30, 50]  # Add left and right padding
                spacing: '50px'
                size_hint_y: None
                height: max(self.minimum_height, root.height)
                MDLabel:
                    text: 'PHC DATA'
                    font_style: 'H6'
                    pos_hint: {"center_x": .9}
                MDLabel:
                    text: 
                MDLabel:
                    text: 'Name of Health Facility?'
                MDTextField:
                    id: health_facility_name
                    required: True
                    hint_text: "Please enter text"
                    mode: "rectangle"
                MDLabel:
                    text: 'Which month are you reporting for?'
                MDTextField:
                    id: report_month
                    required: True
                    hint_text: "Enter a date in the format MM"
                    mode: "rectangle"
                    on_focus: app.show_months(self)
                MDLabel:
                    text: 'Did you receive list of enrollees for this facility?'
                MDTextField:
                    id: received_list
                    required: True
                    hint_text: "Please enter Yes or No"
                    mode: "rectangle"
                    on_focus: app.show_yes_or_no(self)
                MDLabel:
                    text: 'Total number of enrollees in your facility?'
                MDTextField:
                    id: total_enrollees
                    required: True
                    hint_text: "Please enter a number"
                    input_filter: 'int'
                    mode: "rectangle"
                MDLabel:
                    text: 'Have you received payment for capitation?'
                MDTextField:
                    id: received_payment
                    required: True
                    hint_text: "Please enter Yes or No"
                    mode: "rectangle"
                    on_focus: app.show_yes_or_no(self)
                MDLabel:
                    text: 'Date you received payment for capitation?'
                DateTextField:
                    id: payment_date
                    # required: True
                    hint_text: "Enter a date in the format YYYY-MM-DD"
                    mode: "rectangle"
                MDLabel:
                    text: 'Were you notified through pay advice or any documentary means?'
                MDTextField:
                    id: notified_payment
                    required: True
                    hint_text: "Please enter Yes or No"
                    mode: "rectangle"
                    on_focus: app.show_yes_or_no(self)
                MDLabel:
                    text: 'Amount you received for capitation?'
                MDTextField:
                    id: capitation_received
                    required: True
                    hint_text: "Please enter a number"
                    input_filter: 'int'
                    mode: "rectangle"
                MDLabel:
                    text: 'Number of enrollees that access service in this facility?'
                MDTextField:
                    id: service_enrollees
                    required: True
                    hint_text: "Please enter a number"
                    input_filter: 'int'
                    mode: "rectangle"
                MDLabel:
                    text: 'Number of services utilised by enrollees in this facility?'
                MDTextField:
                    id: utilised_services
                    required: True
                    hint_text: "Please enter a number"
                    input_filter: 'int'
                    mode: "rectangle"
                MDLabel:
                    text: 'Number of referred enrollees from this facility?'
                MDTextField:
                    id: referred_enrollees
                    required: True
                    hint_text: "Please enter a number"
                    input_filter: 'int'
                    mode: "rectangle"
                MDLabel:
                    text: 'Number of enrollees that attend ANC?'
                MDTextField:
                    id: anc_enrollees
                    required: True
                    hint_text: "Please enter a number"
                    input_filter: 'int'
                    mode: "rectangle"
                MDLabel:
                    text: 'Number of the enrollees that had normal delivery?'
                MDTextField:
                    id: normal_delivery
                    required: True
                    hint_text: "Please enter a number"
                    input_filter: 'int'
                    mode: "rectangle"
                MDLabel:
                    text: 'Number of enrollees that accessed in immunization service?'
                MDTextField:
                    id: immunization_services
                    required: True
                    hint_text: "Please enter a number"
                    input_filter: 'int'
                    mode: "rectangle"
                MDLabel:
                    text: 'Number of a enrolles that were treated for malaria?'
                MDTextField:
                    id: treated_malaria_under_5
                    required: True
                    hint_text: "[Under 5yrs] Please enter a number"
                    input_filter: 'int'
                    mode: "rectangle"
                MDTextField:
                    id: treated_malaria_above_5
                    required: True
                    hint_text: "[Above 5yrs] Please enter a number"
                    input_filter: 'int'
                    mode: "rectangle"
                MDLabel:
                    text: 'Number of enrollees that were screened for hypertension?'
                MDTextField:
                    id: treated_hypertension
                    required: True
                    hint_text: "Please enter a number"
                    input_filter: 'int'
                    mode: "rectangle"
                MDLabel:
                    text: 'Number of enrollees that were screened for diabetes mellitus?'
                MDTextField:
                    id: treated_diabetes_mellistus
                    required: True
                    hint_text: "Please enter a number"
                    input_filter: 'int'
                    mode: "rectangle"
                MDLabel:
                    text: 'Number of enrollees that were treated for typhoid fever?'
                MDTextField:
                    id: treated_typhoid
                    required: True
                    hint_text: "Please enter a number"
                    mode: "rectangle"
                MDLabel:
                    text: 'Number of enrollees that were treated for respiratory tract infection?'
                MDTextField:
                    id: treated_rti_under_5
                    required: True
                    hint_text: "[Under 5yrs] Please enter a number"
                    input_filter: 'int'
                    mode: "rectangle"
                MDTextField:
                    id: treated_rti_above_5
                    required: True
                    hint_text: "[Above 5yrs] Please enter a number"
                    mode: "rectangle"
                MDLabel:
                    text: 'Number of enrollees that were treated for diarrhea?'
                MDTextField:
                    id: treated_diarrhea_under_5
                    required: True
                    hint_text: "[Under 5yrs] Please enter a number"
                    input_filter: 'int'
                    mode: "rectangle"
                MDTextField:
                    id: treated_diarrhea_above_5
                    required: True
                    hint_text: "[Above 5yrs] Please enter a number"
                    input_filter: 'int'
                    mode: "rectangle"
                MDLabel:
                    text: 'Number of enrollees that were treated for urinary tract infection?'
                MDTextField:
                    id: treated_uti
                    required: True
                    hint_text: "Please enter a number"
                    input_filter: 'int'
                    mode: "rectangle"
                MDLabel:
                    text: 'Number of enrollees that were treated for gastroenteritis?'
                MDTextField:
                    id: treated_gastroenteritis
                    required: True
                    hint_text: "Please enter a number"
                    input_filter: 'int'
                    mode: "rectangle"
                MDLabel:
                    text: 'Others'
                MDTextField:
                    id: others
                    required: True
                    hint_text: "Please enter a number"
                    input_filter: 'int'
                    mode: "rectangle"
                MDLabel:
                    text: 'Total deaths?'
                MDTextField:
                    id: total_deaths
                    required: True
                    hint_text: "Please enter a number"
                    input_filter: 'int'
                    mode: "rectangle"
                MDLabel:
                    text: 'Maternal deaths?'
                MDTextField:
                    id: maternal_death
                    required: True
                    hint_text: "Please enter a number"
                    input_filter: 'int'
                    mode: "rectangle"
                MDLabel:
                    text: 'Neonatal?'
                MDTextField:
                    id: neonatal
                    required: True
                    hint_text: "Please enter a number"
                    input_filter: 'int'
                    mode: "rectangle"
                MDLabel:
                    text: 'Infant?'
                MDTextField:
                    id: infant
                    required: True
                    hint_text: "Please enter a number"
                    input_filter: 'int'
                    mode: "rectangle"
                MDLabel:
                    text: 'Children?'
                MDTextField:
                    id: children
                    required: True
                    hint_text: "Please enter a number"
                    input_filter: 'int'
                    mode: "rectangle"
                MDRaisedButton:
                    text: 'Save'
                    on_press: app.save_phc_data(health_facility_name.text, report_month.text, received_list.text, total_enrollees.text, received_payment.text, payment_date.text, notified_payment.text, capitation_received.text, service_enrollees.text, utilised_services.text, referred_enrollees.text, anc_enrollees.text, normal_delivery.text, immunization_services.text, treated_malaria_under_5.text, treated_malaria_above_5.text, treated_hypertension.text, treated_diabetes_mellistus.text, treated_typhoid.text, treated_rti_under_5.text, treated_rti_above_5.text, treated_diarrhea_under_5.text, treated_diarrhea_above_5.text, treated_uti.text, treated_gastroenteritis.text, others.text, total_deaths.text, maternal_death.text, neonatal.text, infant.text, children.text)
                    pos_hint: {"center_x": .15, "center_y": 0}
                    
    BaseScreen:
                        
"""

shcdata_input_screen_help = """
Screen:
    name: 'shcdata_input_screen'
    BoxLayout:
        orientation: 'vertical'
        ScrollView:
            BoxLayout:
                orientation: 'vertical'
                padding: [30, 100, 30, 50]  # Add left and right padding
                spacing: '50px'
                size_hint_y: None
                height: max(self.minimum_height, root.height)
                MDLabel:
                    text: 'SHC DATA'
                    font_style: 'H6'
                    pos_hint: {"center_x": .9}
                MDLabel:
                    text: 
                MDLabel:
                    text: 'Name of Health Facility?'
                MDTextField:
                    id: health_facility_name
                    required: True
                    hint_text: "Please enter text"
                    mode: "rectangle"
                MDLabel:
                    text: 'When was the last claim submitted to SSHIA?'
                DateTextField:
                    id: date_last_claim
                    required: True
                    hint_text: "Enter a date in the format DD/MM/YYYY"
                    mode: "rectangle"
                MDLabel:
                    text: 'Which month did it cover?'
                MDTextField:
                    id: month_covered
                    required: True
                    hint_text: "Enter a date in the format MM"
                    mode: "rectangle"
                    on_focus: app.show_months(self)
                MDLabel:
                    text: 'Amount requested in the last submitted claims stated above'
                MDTextField:
                    id: amount_requested
                    required: True
                    hint_text: "Please enter a number"
                    input_filter: 'int'
                    mode: "rectangle"
                MDLabel:
                    text: 'When was the last claim reimbursement received?'
                DateTextField:
                    id: claim_reimbursed
                    required: True
                    hint_text: "Enter a date in the format DD/MM/YYYY"
                    mode: "rectangle"
                MDLabel:
                    text: 'Indicate the month for which the reimbursement covers'
                MDTextField:
                    id: imburment_month
                    required: True
                    hint_text: "Enter a date in the format MM"
                    mode: "rectangle"
                    on_focus: app.show_months(self)
                MDLabel:
                    text: 'Reimbursement received'
                MDTextField:
                    id: reimbursement_amount
                    required: True
                    hint_text: "Please enter a number"
                    input_filter: 'int'
                    mode: "rectangle"
                MDLabel:
                    text: 'Number of enrollees that were referred this facility in the reporting month'
                MDTextField:
                    id: referred_enrollees
                    required: True
                    hint_text: "Please enter a number"
                    input_filter: 'int'
                    mode: "rectangle"
                MDLabel:
                    text: 'Number of enrollees that were referred for caesarean section'
                MDTextField:
                    id: caesarean
                    required: True
                    hint_text: "Please enter a number"
                    input_filter: 'int'
                    mode: "rectangle"
                MDLabel:
                    text: 'Number of enrollees that were treated for hypertension'
                MDTextField:
                    id: treated_hypertension
                    required: True
                    hint_text: "Please enter a number"
                    input_filter: 'int'
                    mode: "rectangle"
                MDLabel:
                    text: 'Number of enrollees were treated for diabetes mellitus'
                MDTextField:
                    id: treated_diabetes_mellitus
                    required: True
                    hint_text: "Please enter a number"
                    input_filter: 'int'
                    mode: "rectangle"
                MDLabel:
                    text: 'Number of enrollees that were treated for severe malaria'
                MDTextField:
                    id: treated_malaria_under_5
                    required: True
                    hint_text: "[Under 5yrs] Please enter a number"
                    input_filter: 'int'
                    mode: "rectangle"
                MDTextField:
                    id: treated_malaria_above_5
                    required: True
                    hint_text: "[Above 5yrs] Please enter a number"
                    input_filter: 'int'
                    mode: "rectangle"
                MDLabel:
                    text: 'Number of enrollees that were treated for complicated respiratory tract infection?'
                MDTextField:
                    id: treated_rti_under_5
                    required: True
                    hint_text: "[Under 5yrs] Please enter a number"
                    input_filter: 'int'
                    mode: "rectangle"
                MDTextField:
                    id: treated_rti_above_5
                    required: True
                    hint_text: "[Above 5yrs] Please enter a number"
                    mode: "rectangle"
                MDLabel:
                    text: 'Number of enrollees that were treated for complicated typhoid fever?'
                MDTextField:
                    id: treated_typhoid
                    required: True
                    hint_text: "Please enter a number"
                    mode: "rectangle"
                MDLabel:
                    text: 'Others'
                MDTextField:
                    id: others
                    required: True
                    hint_text: "Please enter a number"
                    input_filter: 'int'
                    mode: "rectangle"
                MDLabel:
                    text: 'Total deaths?'
                MDTextField:
                    id: total_deaths
                    required: True
                    hint_text: "Please enter a number"
                    input_filter: 'int'
                    mode: "rectangle"
                MDLabel:
                    text: 'Maternal deaths?'
                MDTextField:
                    id: maternal_death
                    required: True
                    hint_text: "Please enter a number"
                    input_filter: 'int'
                    mode: "rectangle"
                MDLabel:
                    text: 'Neonatal?'
                MDTextField:
                    id: neonatal
                    required: True
                    hint_text: "Please enter a number"
                    input_filter: 'int'
                    mode: "rectangle"
                MDLabel:
                    text: 'Infant?'
                MDTextField:
                    id: infant
                    required: True
                    hint_text: "Please enter a number"
                    input_filter: 'int'
                    mode: "rectangle"
                MDLabel:
                    text: 'Children?'
                MDTextField:
                    id: children
                    required: True
                    hint_text: "Please enter a number"
                    input_filter: 'int'
                    mode: "rectangle"
                MDRaisedButton:
                    text: 'Save'
                    on_press: app.save_shc_data(health_facility_name.text, date_last_claim.text, month_covered.text, amount_requested.text, claim_reimbursed.text, imburment_month.text, reimbursement_amount.text, referred_enrollees.text, caesarean.text, treated_hypertension.text, treated_diabetes_mellitus.text, treated_malaria_under_5.text, treated_malaria_above_5.text, treated_rti_under_5.text, treated_rti_above_5.text, treated_typhoid.text, others.text, total_deaths.text, maternal_death.text, neonatal.text, infant.text, children.text)
                    pos_hint: {"center_x": .15, "center_y": 0}
                    
    BaseScreen:
                        
"""

data_input_screen_help = """
Screen:
    name: 'data_input_screen'
    BoxLayout:
        orientation: 'vertical'
        size_hint: None, None
        pos_hint: {'center_x': 0.6, 'center_y': 0.5}
        padding: [30, 100, 30, 50]  # Add left and right padding
        spacing: '80px'
        # MDLabel:
        #     text: 'Tab on the below button to add either PHC or SHC record'
        #     halign: 'left'
        MDRectangleFlatIconButton:
            icon: 'plus-box'
            text: 'Add PHC Data'
            theme_text_color: 'Custom'
            text_color: app.theme_cls.primary_color
            on_release: app.root.current = 'phcdata_input_screen'
            pos_hint: {'center_x': 0.3, 'center_y': 1}
        MDRectangleFlatIconButton:
            icon: 'plus-box'
            text: 'Add SHC Data'
            theme_text_color: 'Custom'
            text_color: app.theme_cls.primary_color
            on_release: app.root.current = 'shcdata_input_screen'
            pos_hint: {'center_x': 0.3, 'center_y': 0}

    BaseScreen:
                        
"""
view_screen_help = """
Screen:
    name: 'view_screen'
    BoxLayout:
        orientation: 'vertical'
        size_hint: None, None
        padding: [30, 100, 30, 50]  # Add left and right padding
        spacing: '80px'
        pos_hint: {'center_x': 0.6, 'center_y': 0.3}
        MDRectangleFlatIconButton:
            icon: 'eye'
            text: 'View PHC Data'
            theme_text_color: 'Custom'
            text_color: app.theme_cls.primary_color
            on_release: app.root.current = 'phc_data_view_screen'
            pos_hint: {'center_x': 0.3, 'center_y': 6}
        MDRectangleFlatIconButton:
            icon: 'eye'
            text: 'View SHC Data'
            theme_text_color: 'Custom'
            text_color: app.theme_cls.primary_color
            on_release: app.root.current = 'shc_data_view_screen'
            pos_hint: {'center_x': 0.3, 'center_y': 0.6}
        MDRectangleFlatIconButton:
            icon: 'eye'
            text: 'View SSHIA Data'
            theme_text_color: 'Custom'
            text_color: app.theme_cls.primary_color
            on_release: app.root.current = 'sshia_data_view_screen'
            pos_hint: {'center_x': 0.3, 'center_y': 0}
    BaseScreen:
"""


export_screen_help = """
Screen:
    name: 'export_screen'
    BoxLayout:
        orientation: 'vertical'
        size_hint: None, None
        padding: [30, 100, 30, 50]  # Add left and right padding
        spacing: '80px'
        pos_hint: {'center_x': 0.6, 'center_y': 0.3}
        MDRectangleFlatIconButton:
            icon: 'file-pdf-box'
            text: 'Export as PDF'
            theme_text_color: 'Custom'
            text_color: app.theme_cls.primary_color
            on_release: app.export_pdf()
            pos_hint: {'center_x': 0.3, 'center_y': 1}
        MDRectangleFlatIconButton:
            icon: 'file-excel'
            text: 'Export as Excel'
            theme_text_color: 'Custom'
            text_color: app.theme_cls.primary_color
            on_release: app.export_excel()
            pos_hint: {'center_x': 0.3, 'center_y': 0.5}
        MDRectangleFlatIconButton:
            icon: 'web'
            text: 'Send to Server'
            theme_text_color: 'Custom'
            text_color: app.theme_cls.primary_color
            on_release: app.send_to_server()
            pos_hint: {'center_x': 0.3, 'center_y': 0}
                
    BaseScreen:
"""


phc_data_view_screen_help = """
Screen:
    name: 'phc_data_view_screen'
    BoxLayout:
        orientation: 'vertical'
        PHCDataViewScreen:
            pos_hint: {'center_x': 0.5, 'center_y': 1}
            
    BaseScreen:
                        
"""

shc_data_view_screen_help = """
Screen:
    name: 'shc_data_view_screen'
    BoxLayout:
        orientation: 'vertical'
        SHCDataViewScreen:
            pos_hint: {'center_x': 0.5, 'center_y': 1}
            
    BaseScreen:
                        
"""

sshia_data_view_screen_help = """
Screen:
    name: 'sshia_data_view_screen'
    BoxLayout:
        orientation: 'vertical'
        SSHIADataViewScreen:
            pos_hint: {'center_x': 0.5, 'center_y': 1}
            
    BaseScreen:
                        
"""

