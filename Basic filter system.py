#-----["Importing Services"]-----#
import re
import tkinter as tk
from tkinter import ttk

#-----["Functions"]-----#
def name_filter_system () :
    
    filtered_name = ''
    user_name = name_entry . get ()

    match user_name :

        case '' if user_name == '' : print ( 'Field cannot be empty.\nPlease try again.' )

        case _ if re . search ( r'\d' , user_name ) :
            for i in user_name :
                if i . isdigit () :
                    continue
                filtered_name += i
            if filtered_name == '' : print ( 'Please insert a proper name.' )
            else : print ( filtered_name )

        case _ if len ( user_name ) > 25 or len ( user_name ) == 1 :
            if len ( user_name ) > 25 : print ( 'Username exceeds the 25 character limit.\nPlease try again.' )
            else : print ( 'Username must contain at least 2 characers.\nPlease try again.' )
        
        case str if user_name == str : print ( user_name )

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