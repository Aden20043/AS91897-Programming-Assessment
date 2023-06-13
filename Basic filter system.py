#-----["Importing Services"]-----#
import re
import tkinter as tk
from tkinter import ttk

#-----["Functions"]-----#
def name_filter_system () :

    filtered_name , user_name  = '', name_entry . get ()

    match user_name :

        case '' : print ( 'Field cannot be empty.\nPlease try again.' )

        case user_name if re . search ( r'[a-zA-Z]' , user_name ) :
            for i in user_name :
                if i == ' ' : filtered_name += i
                elif i . isalpha () == False : continue
                filtered_name += i  
            if filtered_name == '' : print ( 'Please insert a proper name.' )
            else :
                if len ( filtered_name ) > 25 : print ( 'Name exceeds the 25 character limit.\nPlease try again.' )
                elif len ( filtered_name ) < 2 : print ( 'Name must contain 2 characters.\nPlease try again.' )
                else: print ( filtered_name . title () )
        
        case _ : print ( 'Error.\nPlease try again.' )
        

#-----["Creating A GUI"]-----#
window = tk . Tk ()
window . geometry ( '250x250' )
window . title ( 'customer prototype #1' )

#-----["Widgets"]-----#
title = ttk . Label ( master = window , text = "Customer prototype #1" , font = "Calibri 12" ) . pack ()
name_entry = ttk . Entry ( master = window )
name_entry . pack ()
submit_button = ttk . Button ( master = window , text = "Submit" , command = name_filter_system ) . pack ()

#-----["Run"]-----#
window . mainloop ()