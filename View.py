import re
import tkinter as tk
from tkinter import ttk
from Controller import Controller
from Model import Model

import time
window = tk.Tk()

window.title("EVOT_printer")
window.geometry('800x760')

tab_parent = ttk.Notebook(window)
tab0 = ttk.Frame(tab_parent)
tab2 = ttk.Frame(tab_parent)
from tkinter.filedialog import asksaveasfile



class View(ttk.Frame):
    def __init__(self, parent):

        super().__init__(parent)

        self.file_name = None

        self.dev_1_adr_var = tk.StringVar()
        self.mod_1_adr_var = tk.StringVar()

        self.dev_2_adr_var = tk.StringVar()
        self.mod_2_adr_var = tk.StringVar()

        self.dev_3_adr_var = tk.StringVar()
        self.mod_3_adr_var = tk.StringVar()

        self.dev_4_adr_var = tk.StringVar()
        self.mod_4_adr_var = tk.StringVar()

        self.dev_5_adr_var = tk.StringVar()
        self.mod_5_adr_var = tk.StringVar()

        self.dev_6_adr_var = tk.StringVar()
        self.mod_6_adr_var = tk.StringVar()

        self.dev_7_adr_var = tk.StringVar()
        self.mod_7_adr_var = tk.StringVar()

        self.dev_8_adr_var = tk.StringVar()
        self.mod_8_adr_var = tk.StringVar()

        self.dev_9_adr_var = tk.StringVar()
        self.mod_9_adr_var = tk.StringVar()

        self.dev_10_adr_var = tk.StringVar()
        self.mod_10_adr_var = tk.StringVar()

        self.dev_11_adr_var = tk.StringVar()
        self.mod_11_adr_var = tk.StringVar()

        self.dev_12_adr_var = tk.StringVar()
        self.mod_12_adr_var = tk.StringVar()

        self.dev_13_adr_var = tk.StringVar()
        self.mod_13_adr_var = tk.StringVar()

        self.dev_14_adr_var = tk.StringVar()
        self.mod_14_adr_var = tk.StringVar()

        self.dev_15_adr_var = tk.StringVar()
        self.mod_15_adr_var = tk.StringVar()



        self.dist = ttk.Label(tab0, width=5)
        self.dist.grid(row=0, column=0)

        self.labelframe01 = tk.LabelFrame(tab0, text="")
        self.labelframe01.grid(row=1, column=1, sticky=tk.NSEW)

        self.stop_check = tk.BooleanVar()

        self.rpm = tk.StringVar()

        self.HE_signal = tk.StringVar()
        self.fan_signal = tk.StringVar()

        self.rpm.set('10')



        #######################################################################################################################

        self.label = ttk.Label(self.labelframe01, text='Zapis/Wykres 01 - adres modbus')
        self.label.grid(row=6, column=2)

        self.dist = ttk.Label(self.labelframe01)
        self.dist.grid(row=1, column=0)

        self.mod_1_adr_entry = ttk.Entry(self.labelframe01, textvariable=self.mod_1_adr_var)
        self.mod_1_adr_entry.grid(row=6, column=3)

        self.mod_1_adr_entry.insert(0, "0")

        self.dist = ttk.Label(self.labelframe01, width=5)
        self.dist.grid(row=6, column=4)

        self.label = ttk.Label(self.labelframe01, text='adres urządzenia')
        self.label.grid(row=6, column=5)

        self.dev_1_adr_entry = ttk.Entry(self.labelframe01, textvariable=self.dev_1_adr_var)
        self.dev_1_adr_entry.grid(row=6, column=6)
        self.dev_1_adr_entry.insert(0, "2")

        self.dist = ttk.Label(self.labelframe01)
        self.dist.grid(row=7, column=0)

        ########################################################################################################################

        self.label = ttk.Label(self.labelframe01, text='Zapis/Wykres 02 - adres modbus')
        self.label.grid(row=10, column=2)

        self.mod_2_adr_entry = ttk.Entry(self.labelframe01, textvariable=self.mod_2_adr_var)
        self.mod_2_adr_entry.grid(row=10, column=3)

        self.mod_2_adr_entry.insert(0, "2")

        self.dist = ttk.Label(self.labelframe01, width=5)
        self.dist.grid(row=10, column=4)

        self.label = ttk.Label(self.labelframe01, text='adres urządzenia')
        self.label.grid(row=10, column=5)

        self.dev_2_adr_entry = ttk.Entry(self.labelframe01, textvariable=self.dev_2_adr_var)
        self.dev_2_adr_entry.grid(row=10, column=6)
        self.dev_2_adr_entry.insert(0, "2")

        self.dist = ttk.Label(self.labelframe01)
        self.dist.grid(row=11, column=0)

        #######################################################################################################################

        self.label = ttk.Label(self.labelframe01, text='Zapis/Wykres 03 - adres modbus')
        self.label.grid(row=15, column=2)

        self.mod_3_adr_entry = ttk.Entry(self.labelframe01, textvariable=self.mod_3_adr_var)
        self.mod_3_adr_entry.grid(row=15, column=3)
        self.mod_3_adr_entry.insert(0, "4")

        self.dist = ttk.Label(self.labelframe01, width=5)
        self.dist.grid(row=15, column=4)

        self.label = ttk.Label(self.labelframe01, text='adres urządzenia')
        self.label.grid(row=15, column=5)

        self.dev_3_adr_entry = ttk.Entry(self.labelframe01, textvariable=self.dev_3_adr_var)
        self.dev_3_adr_entry.grid(row=15, column=6)
        self.dev_3_adr_entry.insert(0, "2")

        self.dist = ttk.Label(self.labelframe01)
        self.dist.grid(row=16, column=0)

        #######################################################################################################################
        self.label = ttk.Label(self.labelframe01, text='Zapis/Wykres 04 - adres modbus')
        self.label.grid(row=20, column=2)

        self.mod_4_adr_entry = ttk.Entry(self.labelframe01, textvariable=self.mod_4_adr_var)
        self.mod_4_adr_entry.grid(row=20, column=3)

        self.mod_4_adr_entry.insert(0, "342")

        self.dist = ttk.Label(self.labelframe01, width=5)
        self.dist.grid(row=20, column=4)

        self.label = ttk.Label(self.labelframe01, text='adres urządzenia')
        self.label.grid(row=20, column=5)

        self.dev_4_adr_entry = ttk.Entry(self.labelframe01, textvariable=self.dev_4_adr_var)
        self.dev_4_adr_entry.grid(row=20, column=6)
        self.dev_4_adr_entry.insert(0, "1")

        self.dist = ttk.Label(self.labelframe01)
        self.dist.grid(row=21, column=0)

        ###########################################################################################################################

        self.label = ttk.Label(self.labelframe01, text='Zapis 05 - adres modbus')
        self.label.grid(row=30, column=2)

        self.mod_5_adr_entry = ttk.Entry(self.labelframe01, textvariable=self.mod_5_adr_var)
        self.mod_5_adr_entry.grid(row=30, column=3)
        self.mod_5_adr_entry.insert(0, "0")

        self.dist = ttk.Label(self.labelframe01, width=5)
        self.dist.grid(row=30, column=4)

        self.label = ttk.Label(self.labelframe01, text='adres urządzenia')
        self.label.grid(row=30, column=5)

        self.dev_5_adr_entry = ttk.Entry(self.labelframe01, textvariable=self.dev_5_adr_var)
        self.dev_5_adr_entry.grid(row=30, column=6)
        self.dev_5_adr_entry.insert(0, "1")

        self.dist = ttk.Label(self.labelframe01)
        self.dist.grid(row=31, column=0)
        ########################################################################################################################

        self.label = ttk.Label(self.labelframe01, text='Zapis 06 - adres modbus')
        self.label.grid(row=40, column=2)

        self.mod_6_adr_entry = ttk.Entry(self.labelframe01, textvariable=self.mod_6_adr_var)
        self.mod_6_adr_entry.grid(row=40, column=3)
        self.mod_6_adr_entry.insert(0, "2")

        self.dist = ttk.Label(self.labelframe01, width=5)
        self.dist.grid(row=40, column=4)

        self.label = ttk.Label(self.labelframe01, text='adres urządzenia')
        self.label.grid(row=40, column=5)

        self.dev_6_adr_entry = ttk.Entry(self.labelframe01, textvariable=self.dev_6_adr_var)
        self.dev_6_adr_entry.grid(row=40, column=6)
        self.dev_6_adr_entry.insert(0, "1")

        self.dist = ttk.Label(self.labelframe01)
        self.dist.grid(row=41, column=0)

        ############################################################################################################################

        self.label = ttk.Label(self.labelframe01, text='Zapis 07 - adres modbus')
        self.label.grid(row=50, column=2)

        self.mod_7_adr_entry = ttk.Entry(self.labelframe01, textvariable=self.mod_7_adr_var)
        self.mod_7_adr_entry.grid(row=50, column=3)

        self.dist = ttk.Label(self.labelframe01, width=5)
        self.dist.grid(row=50, column=4)

        self.label = ttk.Label(self.labelframe01, text='adres urządzenia')
        self.label.grid(row=50, column=5)

        self.mod_7_adr_entry.insert(0, "4")

        self.dev_7_adr_entry = ttk.Entry(self.labelframe01, textvariable=self.dev_7_adr_var)
        self.dev_7_adr_entry.grid(row=50, column=6)

        self.dev_7_adr_entry.insert(0, "1")

        self.dist = ttk.Label(self.labelframe01)
        self.dist.grid(row=51, column=0)

        ############################################################################################################################

        self.label = ttk.Label(self.labelframe01, text='Zapis 08 - adres modbus')
        self.label.grid(row=60, column=2)

        self.mod_8_adr_entry = ttk.Entry(self.labelframe01, textvariable=self.mod_8_adr_var)
        self.mod_8_adr_entry.grid(row=60, column=3)
        self.mod_8_adr_entry.insert(0, "6")

        self.dist = ttk.Label(self.labelframe01, width=5)
        self.dist.grid(row=60, column=4)

        self.label = ttk.Label(self.labelframe01, text='adres urządzenia')
        self.label.grid(row=60, column=5)

        self.dev_8_adr_entry = ttk.Entry(self.labelframe01, textvariable=self.dev_8_adr_var)
        self.dev_8_adr_entry.grid(row=60, column=6)

        self.dev_8_adr_entry.insert(0, "1")

        self.dist = ttk.Label(self.labelframe01)
        self.dist.grid(row=61, column=0)

        ############################################################################################################################

        self.label = ttk.Label(self.labelframe01, text='Zapis 09 - adres modbus')
        self.label.grid(row=70, column=2)

        self.mod_9_adr_entry = ttk.Entry(self.labelframe01, textvariable=self.mod_9_adr_var)
        self.mod_9_adr_entry.grid(row=70, column=3)
        self.mod_9_adr_entry.insert(0, "8")

        self.dist = ttk.Label(self.labelframe01, width=5)
        self.dist.grid(row=70, column=4)

        self.label = ttk.Label(self.labelframe01, text='adres urządzenia')
        self.label.grid(row=70, column=5)

        self.dev_9_adr_entry = ttk.Entry(self.labelframe01, textvariable=self.dev_9_adr_var)
        self.dev_9_adr_entry.grid(row=70, column=6)
        self.dev_9_adr_entry.insert(0, "1")

        self.dist = ttk.Label(self.labelframe01)
        self.dist.grid(row=71, column=0)

        ############################################################################################################################

        self.label = ttk.Label(self.labelframe01, text='Zapis 10 - adres modbus')
        self.label.grid(row=80, column=2)

        self.mod_10_adr_entry = ttk.Entry(self.labelframe01, textvariable=self.mod_10_adr_var)
        self.mod_10_adr_entry.grid(row=80, column=3)
        self.mod_10_adr_entry.insert(0, "10")

        self.dist = ttk.Label(self.labelframe01, width=5)
        self.dist.grid(row=80, column=4)

        self.label = ttk.Label(self.labelframe01, text='adres urządzenia')
        self.label.grid(row=80, column=5)

        self.dev_10_adr_entry = ttk.Entry(self.labelframe01, textvariable=self.dev_10_adr_var)
        self.dev_10_adr_entry.grid(row=80, column=6)
        self.dev_10_adr_entry.insert(0, "1")

        self.dist = ttk.Label(self.labelframe01)
        self.dist.grid(row=81, column=0)

        ############################################################################################################################

        self.label = ttk.Label(self.labelframe01, text='Zapis 11 - adres modbus')
        self.label.grid(row=90, column=2)

        self.mod_11_adr_entry = ttk.Entry(self.labelframe01, textvariable=self.mod_11_adr_var)
        self.mod_11_adr_entry.grid(row=90, column=3)
        self.mod_11_adr_entry.insert(0, "358")

        self.dist = ttk.Label(self.labelframe01, width=5)
        self.dist.grid(row=90, column=4)

        self.label = ttk.Label(self.labelframe01, text='adres urządzenia')
        self.label.grid(row=90, column=5)

        self.dev_11_adr_entry = ttk.Entry(self.labelframe01, textvariable=self.dev_11_adr_var)
        self.dev_11_adr_entry.grid(row=90, column=6)
        self.dev_11_adr_entry.insert(0, "1")

        self.dist = ttk.Label(self.labelframe01)
        self.dist.grid(row=91, column=0)



        ###########################################################################################################################



        self.label = ttk.Label(self.labelframe01, text='Zapis 12 - adres modbus')
        self.label.grid(row=100, column=2)

        self.mod_12_adr_entry = ttk.Entry(self.labelframe01, textvariable=self.mod_12_adr_var)
        self.mod_12_adr_entry.grid(row=100, column=3)
        self.mod_12_adr_entry.insert(0, "360")

        self.dist = ttk.Label(self.labelframe01, width=5)
        self.dist.grid(row=100, column=4)

        self.label = ttk.Label(self.labelframe01, text='adres urządzenia')
        self.label.grid(row=100, column=5)

        self.dev_12_adr_entry = ttk.Entry(self.labelframe01, textvariable=self.dev_12_adr_var)
        self.dev_12_adr_entry.grid(row=100, column=6)
        self.dev_12_adr_entry.insert(0, "1")

        self.dist = ttk.Label(self.labelframe01)
        self.dist.grid(row=101, column=0)








        ###########################################################################################################################


        self.label = ttk.Label(self.labelframe01, text='Zapis 13 - adres modbus')
        self.label.grid(row=120, column=2)

        self.mod_13_adr_entry = ttk.Entry(self.labelframe01, textvariable=self.mod_13_adr_var)
        self.mod_13_adr_entry.grid(row=120, column=3)
        self.mod_13_adr_entry.insert(0, "362")

        self.dist = ttk.Label(self.labelframe01, width=5)
        self.dist.grid(row=120, column=4)

        self.label = ttk.Label(self.labelframe01, text='adres urządzenia')
        self.label.grid(row=120, column=5)

        self.dev_13_adr_entry = ttk.Entry(self.labelframe01, textvariable=self.dev_13_adr_var)
        self.dev_13_adr_entry.grid(row=120, column=6)
        self.dev_13_adr_entry.insert(0, "1")

        self.dist = ttk.Label(self.labelframe01)
        self.dist.grid(row=121, column=0)


        ###########################################################################################################################


        self.label = ttk.Label(self.labelframe01, text='Zapis 14 - adres modbus')
        self.label.grid(row=130, column=2)

        self.mod_14_adr_entry = ttk.Entry(self.labelframe01, textvariable=self.mod_14_adr_var)
        self.mod_14_adr_entry.grid(row=130, column=3)
        self.mod_14_adr_entry.insert(0, "14")

        self.dist = ttk.Label(self.labelframe01, width=5)
        self.dist.grid(row=130, column=4)

        self.label = ttk.Label(self.labelframe01, text='adres urządzenia')
        self.label.grid(row=130, column=5)

        self.dev_14_adr_entry = ttk.Entry(self.labelframe01, textvariable=self.dev_14_adr_var)
        self.dev_14_adr_entry.grid(row=130, column=6)
        self.dev_14_adr_entry.insert(0, "2")

        self.dist = ttk.Label(self.labelframe01)
        self.dist.grid(row=131, column=0)

        ###########################################################################################################################

        self.label = ttk.Label(self.labelframe01, text='Wysterowanie')
        self.label.grid(row=140, column=2)

        self.mod_15_adr_entry = ttk.Entry(self.labelframe01, textvariable=self.mod_15_adr_var)
        self.mod_15_adr_entry.grid(row=140, column=3)
        self.mod_15_adr_entry.insert(0, "wpisz")

        self.dist = ttk.Label(self.labelframe01, width=5)
        self.dist.grid(row=140, column=4)

        self.label = ttk.Label(self.labelframe01, text='adres urządzenia')
        self.label.grid(row=140, column=5)

        self.dev_15_adr_entry = ttk.Entry(self.labelframe01, textvariable=self.dev_15_adr_var)
        self.dev_15_adr_entry.grid(row=140, column=6)
        self.dev_15_adr_entry.insert(0, "1")

        self.dist = ttk.Label(self.labelframe01)
        self.dist.grid(row=141, column=0)


        ###########################################################################################################################

        self.draw_window_button = ttk.Button(self.labelframe01, text="wykresy", width=5, command=self.draw_chart)
        self.draw_window_button.config(state = "disabled")
        self.draw_window_button.grid(row=200, columnspan=7, sticky=tk.W + tk.E)

        self.cfg_button = ttk.Button(self.labelframe01, text="cfg", width=2, command=self.stop_save)
        self.cfg_button.grid(row=205, column=3, ipadx=50)

        ########################################################################################################################
        self.change_file_button = ttk.Button(self.labelframe01, text="wybierz plik", width=2, command=self.choose_file)
        self.change_file_button.grid(row=205, column=5, ipadx=50)

        #######################################################################################################################


        self.start_save_button = ttk.Button(self.labelframe01, text="start -zapis", width=2, command=self.start_save)
        self.start_save_button.grid(row=210, column=3, ipadx=50)


        ######################################################################################################################



        self.stop_save_button = ttk.Button(self.labelframe01, text="stop - zapis", width=2, command=self.stop_save)
        self.stop_save_button.grid(row=210, column=5, ipadx=50)

        ##########################################################################################################################
        ########################################################################################################################


        self.labelframe02 = tk.LabelFrame(tab2, text="")
        self.labelframe02.grid(row=1, column=1, sticky=tk.NSEW)


        self.dist = ttk.Label(self.labelframe02, text ="0-10V")
        self.dist.grid(row=10, column=15)

        self.fan_start_button = ttk.Button(self.labelframe02, text="Wentylator - ON", width=10, command=self.fan_start)
        self.fan_start_button.grid(row=20, column=5, ipadx=50)



        self.fan_signal_entry = ttk.Entry(self.labelframe02, textvariable=self.fan_signal)
        self.fan_signal_entry.grid(row=20, column=15)

        self.dist = ttk.Label(self.labelframe02)
        self.dist.grid(row=20, column=20)

        self.fan_stop_button = ttk.Button(self.labelframe02, text="Wentylator - OFF", width=10, command=self.fan_stop)
        self.fan_stop_button.grid(row=20, column=25, ipadx=50)



        self.rpm_label = ttk.Label(self.labelframe02,text='rpm')
        self.rpm_label.grid(row=25, column=10)

        self.rpm_label = ttk.Label(self.labelframe02, text=self.rpm.get())
        self.rpm_label.config(text=self.rpm.get())
        self.rpm_label.grid(row=25, column=15)

        self.dist = ttk.Label(self.labelframe02)
        self.dist.grid(row=30, column=10)

        self.he_start_button = ttk.Button(self.labelframe02, text="Nagrzewnica - ON", width=10, command=self.HE_start)
        self.he_start_button.grid(row=40, column=5, ipadx=50)

        self.he_signal_entry = ttk.Entry(self.labelframe02, textvariable=self.HE_signal)
        self.he_signal_entry.grid(row=40, column=15)

        self.he_stop_button = ttk.Button(self.labelframe02, text="Nagrzewnica - OFF", width=10, command=self.HE_stop)
        self.he_stop_button.grid(row=40, column=25, ipadx=50)

        self.dist = ttk.Label(self.labelframe02, text ="0-10V")
        self.dist.grid(row=50, column=15)


    def choose_file(self):
        self.file_name = asksaveasfile(initialdir='C:\\Users\oljar\PycharmProjects\jupiter02', defaultextension='*.csv',
                               mode='w', filetypes=[('CSV Files', '*.csv')])

        print(self.file_name.name)




    def draw_chart(self):
        self.controller.settings_1()
        self.controller.settings_2()
        self.controller.transfer_data()
        self.controller.make()


    def start_save(self):
        self.stop_check.set(False)
        self.controller.settings_1()
        self.controller.settings_2()
        self.controller.settings_3()
        self.controller.settings_4()
        self.controller.settings_5()
        self.controller.settings_6()
        self.controller.settings_7()
        self.controller.settings_8()
        self.controller.settings_9()
        self.controller.settings_10()
        self.controller.settings_11()
        self.controller.settings_12()
        self.controller.settings_13()
        self.controller.settings_14()
        self.controller.settings_15()









        self.controller.transfer_data()
        #
        self.controller.start_save()
        self.start_loop()
        self.start_save_button.config(state="disabled")
        self.stop_save_button.config(state="enabled")
        self.controller.save_data()


    def start_loop(self):
        time.sleep(0.1)
        self.controller.save_data()
        if self.stop_check.get() :
            return
        self.labelframe01.after(1000, self.start_loop)



        # self.start_save_button.config(state= "disabled")
        # self.stop_save_button.config(state = "enabled")

    def stop_save(self):

        self.stop_check.set(True)
        self.stop_save_button.config(state="disabled")
        self.start_save_button.config(state="enabled")

        # self.start_save_button.config(state="enabled")
        # self.stop_save_button.config(state="disabled")

    def fan_start(self):
        self.controller.settings_1()
        self.controller.settings_2()
        self.controller.fan_start()

    def fan_stop(self):
        self.controller.settings_1()
        self.controller.settings_2()
        self.controller.fan_stop()

    def HE_start(self):
        self.controller.settings_1()
        self.controller.settings_2()
        self.controller.HE_start()

    def HE_stop(self):
        self.controller.settings_1()
        self.controller.settings_2()
        self.controller.HE_stop()



    def set_controller(self, controller):
        """
        Set the controller
        :param controller:
        :return:
        """
        self.controller = controller

    def save_button_clicked(self):
        """
        Handle button click event
        :return:
        """
        if self.controller:
            self.controller.save(self.email_var.get())




















    def show_error(self, message):
        """
        Show an error message
        :param message:
        :return:
        """
        self.message_label['text'] = message
        self.message_label['foreground'] = 'red'
        self.message_label.after(3000, self.hide_message)
        self.email_entry['foreground'] = 'red'

    def show_success(self, message):
        """
        Show a success message
        :param message:
        :return:
        """
        self.message_label['text'] = message
        self.message_label['foreground'] = 'green'
        self.message_label.after(3000, self.hide_message)

        # reset the form
        self.email_entry['foreground'] = 'black'
        self.email_var.set('')

    def hide_message(self):
        """
        Hide the message
        :return:
        """
        self.message_label['text'] = ''
