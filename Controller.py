#!/usr/bin/python
import threading, time, subprocess, logging, minimalmodbus
# from apscheduler.schedulers import Scheduler
from time import sleep
import serial
import re
import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
import collections
import time
import csv
import sys
from threading import Thread


class Controller:
    def __init__(self, model, view):

        self.instrument_1 = None
        self.instrument_2 = None
        self.instrument_3 = None
        self.instrument_4 = None
        self.instrument_5 = None
        self.instrument_6 = None
        self.instrument_7 = None
        self.instrument_8 = None
        self.instrument_9 = None
        self.instrument_10 = None
        self.instrument_11 = None
        self.instrument_12 = None
        self.instrument_13 = None
        self.instrument_14 = None
        self.instrument_15 = None





        self.writer = None
        self.parameter = tk.StringVar()
        self.model = model
        self.view = view
        self.model.mod_1_adr_var = tk.StringVar()

        self.t1 = time.time()
        self.fig = plt.figure(figsize=(10, 5), facecolor='#DEDEDE')

        self.time_s = collections.deque(np.zeros(10))
        self.param_1 = collections.deque(np.zeros(10))
        self.param_2 = collections.deque(np.zeros(10))
        self.param_3 = collections.deque(np.zeros(10))
        self.param_4 = collections.deque(np.zeros(10))
        ###
        self.ax = plt.subplot(221)  ### set window position
        self.ax_co = self.ax.twiny()

        self.ax2 = plt.subplot(222)  ### set window position
        self.ax2_co = self.ax.twiny()

        self.ax3 = plt.subplot(223)  ### set window position
        self.ax3_co = self.ax.twiny()

        self.ax4 = plt.subplot(224)  ### set window position
        self.ax4_co = self.ax.twiny()

        self.model.save_control.set(True)

        self.conn_repeat_nr = 10

        self.n_header = 0

    def my_function(self):
        self.t2 = time.time()
        self.delta_t = (self.t2 - self.t1)
        self.time_s.popleft()
        self.time_s.append(self.delta_t)
        self.cycle_data()

        #  modbus settings

        def chart1_myfunction():
            self.instrument_1.address = int(self.model.dev_1_adr_var)
            # self.param_1.append(self.instrument_1.read_float(int(self.model.mod_1_adr_var), functioncode=4))  #adress modbus
            self.param_1.append(self.model.data_1)
            # self.param_1.append(float(self.model.data_1.get()))  # adress modbus
            self.param_1.popleft()

        chart1_myfunction()

        def chart2_myfunction():
            self.instrument_1.address = int(self.model.dev_2_adr_var)
            # self.param_2.append((self.instrument_2.read_register(int(self.model.mod_2_adr_var),0,functioncode=4))/256)  #adress modbus
            self.param_2.append(self.model.data_2)  # adress modbus
            self.param_2.popleft()

        chart2_myfunction()

        def chart3_myfunction():
            self.instrument_1.address = int(self.model.dev_3_adr_var)
            # self.param_3.append(self.instrument_1.read_float(int(self.model.mod_3_adr_var), functioncode=4))  # adress modbus
            self.param_3.append(self.model.data_3)
            # self.param_3.append(float(self.model.data_3.get()))  # adress modbus
            self.param_3.popleft()

        chart3_myfunction()

        def chart4_myfunction():
            self.instrument_1.address = int(self.model.dev_4_adr_var)
            # self.param_4.append(self.instrument_1.read_float(int(self.model.mod_4_adr_var), functioncode=4))  # adress modbus
            self.param_4.append(self.model.data_4)
            # self.param_4.append(float(self.model.data_4.get()))  # adress modbus
            self.param_4.popleft()

        chart4_myfunction()

    ##########################################################################################################################################

    def animate(self, i):
        self.my_function()

        def chart1_animate(i):
            self.ax.clear()
            self.ax.plot(self.time_s, self.param_1)
            self.ax.scatter(self.time_s[-1], self.param_1[-1])
            self.ax.text(self.time_s[-1], self.param_1[-1], f"{self.param_1[-1]}")
            self.ax.set_ylim(-1, self.param_1[-1] + 0.1 * self.param_1[-1] + 3)
            self.ax_co.set_xlim(0, 10)
            self.ax.set_xlim(right=int(self.delta_t) - 10, left=int(self.delta_t) + 1)

        chart1_animate(i)

        def chart2_animate(i):
            self.ax2.clear()
            self.ax2.plot(self.time_s, self.param_2)
            self.ax2.scatter(self.time_s[-1], self.param_2[-1])
            self.ax2.text(self.time_s[-1], self.param_2[-1], f"{self.param_2[-1]}")
            self.ax2.set_ylim(-1, self.param_2[-1] + 0.1 * self.param_2[-1] + 3)
            self.ax2_co.set_xlim(0, 10)
            self.ax2.set_xlim(right=int(self.delta_t) - 10, left=int(self.delta_t) + 1)

        chart2_animate(i)

        def chart3_animate(i):
            self.ax3.clear()
            self.ax3.plot(self.time_s, self.param_3)
            self.ax3.scatter(self.time_s[-1], self.param_3[-1])
            self.ax3.text(self.time_s[-1], self.param_3[-1], f"{self.param_3[-1]}")
            self.ax3.set_ylim(-1, self.param_3[-1] + 0.1 * self.param_3[-1] + 3)
            self.ax3_co.set_xlim(0, 10)
            self.ax3.set_xlim(right=int(self.delta_t) - 10, left=int(self.delta_t) + 1)

        chart3_animate(i)

        def chart4_animate(i):
            self.ax4.clear()
            self.ax4.plot(self.time_s, self.param_4)
            self.ax4.scatter(self.time_s[-1], self.param_4[-1])
            self.ax4.text(self.time_s[-1], self.param_4[-1], f"{self.param_4[-1]}")
            self.ax4.set_ylim(-1, self.param_4[-1] + 0.1 * self.param_4[-1] + 3)
            self.ax4_co.set_xlim(0, 10)
            self.ax4.set_xlim(right=int(self.delta_t) - 10, left=int(self.delta_t) + 1)

        chart4_animate(i)

    def make(self):
        def chart1_make():
            self.ax.set_xlim(0, -10)
            self.ax.set_facecolor('#DEDEDE')
            self.ax_co.set_xlim(0, 10)

        chart1_make()

        def chart2_make():
            self.ax2.set_xlim(0, -10)
            self.ax2.set_facecolor('#DEDEDE')
            self.ax2_co.set_xlim(0, 10)

        chart2_make()

        def chart3_make():
            self.ax3.set_xlim(0, -10)
            self.ax3.set_facecolor('#DEDEDE')
            self.ax3_co.set_xlim(0, 10)

        chart3_make()

        def chart4_make():
            self.ax4.set_xlim(0, -10)
            self.ax4.set_facecolor('#DEDEDE')
            self.ax4_co.set_xlim(0, 10)

        chart4_make()

        ani = FuncAnimation(self.fig, self.animate, interval=50, cache_frame_data=True, repeat=True, save_count=1)
        plt.show()

    ##########################################################################################################################

    def settings_1(self):
        # self.instrument_1 = minimalmodbus.Instrument("/dev/ttyUSB0", self.model.dev_1_adr_var)
        self.instrument_1 = minimalmodbus.Instrument('com4', self.model.dev_1_adr_var)
        self.instrument_1.serial.baudrate = 9600  # Baud
        self.instrument_1.serial.bytesize = 8
        self.instrument_1.serial.parity = serial.PARITY_NONE
        self.instrument_1.serial.stopbits = 1
        self.instrument_1.serial.timeout = 0.5  # seconds
        self.instrument_1.address = int(str(self.view.dev_1_adr_var.get())) # this is the slave address number

        self.instrument_1.mode = minimalmodbus.MODE_RTU  # rtu or ascii mode
        # self.instrument_1.clear_buffers_before_each_transaction = True
        # self.instrument_1.close_port_after_each_call=True

    def settings_2(self):
        # self.instrument_2 = minimalmodbus.Instrument("/dev/ttyUSB0", self.model.dev_2_adr_var)
        self.instrument_2 = minimalmodbus.Instrument('com4', self.model.dev_2_adr_var)
        self.instrument_2.serial.baudrate = 9600  # Baud
        self.instrument_2.serial.bytesize = 8
        self.instrument_2.serial.parity = serial.PARITY_NONE
        self.instrument_2.serial.stopbits = 1
        self.instrument_2.serial.timeout = 0.5  # seconds
        self.instrument_2.address = int(str(self.view.dev_2_adr_var.get()))   # this is the slave address number
        self.instrument_2.mode = minimalmodbus.MODE_RTU  # rtu or ascii mode

        # self.instrument_2.clear_buffers_before_each_transaction = True
        # self.instrument_1.close_port_after_each_call = True

    def settings_3(self):
        # self.instrument_3 = minimalmodbus.Instrument("/dev/ttyUSB0", self.model.dev_3_adr_var)
        self.instrument_3 = minimalmodbus.Instrument('com4', self.model.dev_3_adr_var)
        self.instrument_3.serial.baudrate = 9600  # Baud
        self.instrument_3.serial.bytesize = 8
        self.instrument_3.serial.parity = serial.PARITY_NONE
        self.instrument_3.serial.stopbits = 1
        self.instrument_3.serial.timeout = 0.5  # seconds
        self.instrument_3.address = int(str(self.view.dev_3_adr_var.get()))  # this is the slave address number
        self.instrument_3.mode = minimalmodbus.MODE_RTU  # rtu or ascii mode

        # self.instrument_3.clear_buffers_before_each_transaction = True
        # self.instrument_3.close_port_after_each_call = True

    def settings_4(self):
        # self.instrument_4 = minimalmodbus.Instrument("/dev/ttyUSB0", self.model.dev_4_adr_var)
        self.instrument_4 = minimalmodbus.Instrument('com4', self.model.dev_4_adr_var)
        self.instrument_4.serial.baudrate = 9600  # Baud
        self.instrument_4.serial.bytesize = 8
        self.instrument_4.serial.parity = serial.PARITY_NONE
        self.instrument_4.serial.stopbits = 1
        self.instrument_4.serial.timeout = 0.5  # seconds
        self.instrument_4.address = int(str(self.view.dev_4_adr_var.get()))  # this is the slave address number
        self.instrument_4.mode = minimalmodbus.MODE_RTU  # rtu or ascii mode

        # self.instrument_2.clear_buffers_before_each_transaction = True
        # self.instrument_1.close_port_after_each_call = True

    def settings_5(self):
        # self.instrument_5 = minimalmodbus.Instrument("/dev/ttyUSB0", self.model.dev_5_adr_var)
        self.instrument_5 = minimalmodbus.Instrument('com4', self.model.dev_5_adr_var)
        self.instrument_5.serial.baudrate = 9600  # Baud
        self.instrument_5.serial.bytesize = 8
        self.instrument_5.serial.parity = serial.PARITY_NONE
        self.instrument_5.serial.stopbits = 1
        self.instrument_5.serial.timeout = 0.5  # seconds
        self.instrument_5.address = int(str(self.view.dev_5_adr_var.get()))  # this is the slave address number
        self.instrument_5.mode = minimalmodbus.MODE_RTU  # rtu or ascii mode

        # self.instrument_2.clear_buffers_before_each_transaction = True
        # self.instrument_1.close_port_after_each_call = True

    def settings_6(self):
        # self.instrument_6 = minimalmodbus.Instrument("/dev/ttyUSB0", self.model.dev_6_adr_var)
        self.instrument_6 = minimalmodbus.Instrument('com4', self.model.dev_6_adr_var)
        self.instrument_6.serial.baudrate = 9600  # Baud
        self.instrument_6.serial.bytesize = 8
        self.instrument_6.serial.parity = serial.PARITY_NONE
        self.instrument_6.serial.stopbits = 1
        self.instrument_6.serial.timeout = 0.5  # seconds
        self.instrument_6.address = int(str(self.view.dev_6_adr_var.get())) # this is the slave address number
        self.instrument_6.mode = minimalmodbus.MODE_RTU  # rtu or ascii mode

    def settings_7(self):
        # self.instrument_7 = minimalmodbus.Instrument("/dev/ttyUSB0", self.model.dev_7_adr_var)
        self.instrument_7 = minimalmodbus.Instrument('com4', self.model.dev_7_adr_var)
        self.instrument_7.serial.baudrate = 9600  # Baud
        self.instrument_7.serial.bytesize = 8
        self.instrument_7.serial.parity = serial.PARITY_NONE
        self.instrument_7.serial.stopbits = 1
        self.instrument_7.serial.timeout = 0.5  # seconds
        self.instrument_7.address = int(str(self.view.dev_7_adr_var.get())) # this is the slave address number
        self.instrument_7.mode = minimalmodbus.MODE_RTU  # rtu or ascii mode

    def settings_8(self):
        # self.instrument_8 = minimalmodbus.Instrument("/dev/ttyUSB0", self.model.dev_8_adr_var)
        self.instrument_8 = minimalmodbus.Instrument('com4', self.model.dev_8_adr_var)
        self.instrument_8.serial.baudrate = 9600  # Baud
        self.instrument_8.serial.bytesize = 8
        self.instrument_8.serial.parity = serial.PARITY_NONE
        self.instrument_8.serial.stopbits = 1
        self.instrument_8.serial.timeout = 0.5  # seconds
        self.instrument_8.address = int(str(self.view.dev_8_adr_var.get()))  # this is the slave address number
        self.instrument_8.mode = minimalmodbus.MODE_RTU  # rtu or ascii mode



    def settings_9(self):
        # self.instrument_9 = minimalmodbus.Instrument("/dev/ttyUSB0", self.model.dev_9_adr_var)
        self.instrument_9 = minimalmodbus.Instrument('com4', self.model.dev_9_adr_var)
        self.instrument_9.serial.baudrate = 9600  # Baud
        self.instrument_9.serial.bytesize = 8
        self.instrument_9.serial.parity = serial.PARITY_NONE
        self.instrument_9.serial.stopbits = 1
        self.instrument_9.serial.timeout = 0.5  # seconds
        self.instrument_9.address = int(str(self.view.dev_9_adr_var.get()))  # this is the slave address number
        self.instrument_9.mode = minimalmodbus.MODE_RTU  # rtu or ascii mode

    def settings_10(self):
        # self.instrument_10 = minimalmodbus.Instrument("/dev/ttyUSB0", self.model.dev_10_adr_var)
        self.instrument_10 = minimalmodbus.Instrument('com4', self.model.dev_10_adr_var)
        self.instrument_10.serial.baudrate = 9600  # Baud
        self.instrument_10.serial.bytesize = 8
        self.instrument_10.serial.parity = serial.PARITY_NONE
        self.instrument_10.serial.stopbits = 1
        self.instrument_10.serial.timeout = 0.5  # seconds
        self.instrument_10.address = int(str(self.view.dev_10_adr_var.get()))  # this is the slave address number
        self.instrument_10.mode = minimalmodbus.MODE_RTU  # rtu or ascii mode

    def settings_11(self):
        # self.instrument_11 = minimalmodbus.Instrument("/dev/ttyUSB0", self.model.dev_11_adr_var)
        self.instrument_11 = minimalmodbus.Instrument('com4', self.model.dev_11_adr_var)
        self.instrument_11.serial.baudrate = 9600  # Baud
        self.instrument_11.serial.bytesize = 8
        self.instrument_11.serial.parity = serial.PARITY_NONE
        self.instrument_11.serial.stopbits = 1
        self.instrument_11.serial.timeout = 0.5  # seconds
        self.instrument_11.address = int(str(self.view.dev_11_adr_var.get()))  # this is the slave address number
        self.instrument_11.mode = minimalmodbus.MODE_RTU  # rtu or ascii mode

    def settings_12(self):
        # self.instrument_12 = minimalmodbus.Instrument("/dev/ttyUSB0", self.model.dev_12_adr_var)
        self.instrument_12 = minimalmodbus.Instrument('com4', self.model.dev_12_adr_var)
        self.instrument_12.serial.baudrate = 9600  # Baud
        self.instrument_12.serial.bytesize = 8
        self.instrument_12.serial.parity = serial.PARITY_NONE
        self.instrument_12.serial.stopbits = 1
        self.instrument_12.serial.timeout = 0.5  # seconds
        self.instrument_12.address = int(str(self.view.dev_12_adr_var.get())) # this is the slave address number
        self.instrument_12.mode = minimalmodbus.MODE_RTU  # rtu or ascii mode

    def settings_13(self):
        # self.instrument_13 = minimalmodbus.Instrument("/dev/ttyUSB0", self.model.dev_13_adr_var)
        self.instrument_13 = minimalmodbus.Instrument('com4', self.model.dev_13_adr_var)
        self.instrument_13.serial.baudrate = 9600  # Baud
        self.instrument_13.serial.bytesize = 8
        self.instrument_13.serial.parity = serial.PARITY_NONE
        self.instrument_13.serial.stopbits = 1
        self.instrument_13.serial.timeout = 0.5  # seconds
        self.instrument_13.address = int(str(self.view.dev_13_adr_var.get()))  # this is the slave address number
        self.instrument_13.mode = minimalmodbus.MODE_RTU  # rtu or ascii mode

    def settings_14(self):
        # self.instrument_14 = minimalmodbus.Instrument("/dev/ttyUSB0", self.model.dev_14_adr_var)
        self.instrument_14 = minimalmodbus.Instrument('com4', self.model.dev_14_adr_var)
        self.instrument_14.serial.baudrate = 9600  # Baud
        self.instrument_14.serial.bytesize = 8
        self.instrument_14.serial.parity = serial.PARITY_NONE
        self.instrument_14.serial.stopbits = 1
        self.instrument_14.serial.timeout = 0.5  # seconds
        self.instrument_14.address = int(str(self.view.dev_14_adr_var.get()))  # this is the slave address number
        self.instrument_14.mode = minimalmodbus.MODE_RTU  # rtu or ascii mode
    def settings_15(self):
        # self.instrument_15 = minimalmodbus.Instrument("/dev/ttyUSB0", self.model.dev_15_adr_var)
        self.instrument_15 = minimalmodbus.Instrument('com4', self.model.dev_15_adr_var)
        self.instrument_15.serial.baudrate = 9600  # Baud
        self.instrument_15.serial.bytesize = 8
        self.instrument_15.serial.parity = serial.PARITY_NONE
        self.instrument_15.serial.stopbits = 1
        self.instrument_15.serial.timeout = 0.5  # seconds
        self.instrument_15.address = int(str(self.view.dev_15_adr_var.get()))  # this is the slave address number
        self.instrument_15.mode = minimalmodbus.MODE_RTU  # rtu or ascii mode


    def transfer_data(self):
        self.model.mod_1_adr_var = self.view.mod_1_adr_var.get()
        self.model.dev_1_adr_var = self.view.dev_1_adr_var.get()

        self.model.mod_2_adr_var = self.view.mod_2_adr_var.get()
        self.model.dev_2_adr_var = self.view.dev_2_adr_var.get()

        self.model.mod_3_adr_var = self.view.mod_3_adr_var.get()
        self.model.dev_3_adr_var = self.view.dev_3_adr_var.get()

        self.model.mod_4_adr_var = self.view.mod_4_adr_var.get()
        self.model.dev_4_adr_var = self.view.dev_4_adr_var.get()

        self.model.mod_5_adr_var = self.view.mod_5_adr_var.get()
        self.model.dev_5_adr_var = self.view.dev_5_adr_var.get()

        self.model.mod_6_adr_var = self.view.mod_6_adr_var.get()
        self.model.dev_6_adr_var = self.view.dev_6_adr_var.get()

        self.model.mod_7_adr_var = self.view.mod_7_adr_var.get()
        self.model.dev_7_adr_var = self.view.dev_7_adr_var.get()

        self.model.mod_8_adr_var = self.view.mod_8_adr_var.get()
        self.model.dev_8_adr_var = self.view.dev_8_adr_var.get()

        self.model.mod_9_adr_var = self.view.mod_9_adr_var.get()
        self.model.dev_9_adr_var = self.view.dev_9_adr_var.get()

        self.model.mod_10_adr_var = self.view.mod_10_adr_var.get()
        self.model.dev_10_adr_var = self.view.dev_10_adr_var.get()

        self.model.mod_11_adr_var = self.view.mod_11_adr_var.get()
        self.model.dev_11_adr_var = self.view.dev_11_adr_var.get()

        self.model.mod_12_adr_var = self.view.mod_12_adr_var.get()
        self.model.dev_12_adr_var = self.view.dev_12_adr_var.get()

        self.model.mod_13_adr_var = self.view.mod_13_adr_var.get()
        self.model.dev_13_adr_var = self.view.dev_13_adr_var.get()

        self.model.mod_14_adr_var = self.view.mod_14_adr_var.get()
        self.model.dev_14_adr_var = self.view.dev_14_adr_var.get()

        self.model.mod_15_adr_var = self.view.mod_15_adr_var.get()
        self.model.dev_15_adr_var = self.view.dev_15_adr_var.get()

    def data_pull_from_instrument(self, device_modbus, address_modbus):
        match device_modbus:
            case self.model.dev_1_adr_var:
                return self.instrument_1.read_float(int(address_modbus), functioncode=4)
            case self.model.dev_2_adr_var:
                return self.instrument_2.read_float(int(address_modbus), functioncode=4)
            case self.model.dev_3_adr_var:
                return self.instrument_3.read_float(int(address_modbus), functioncode=4)
            case self.model.dev_4_adr_var:
                return self.instrument_4.read_float(int(address_modbus), functioncode=4)
            case self.model.dev_5_adr_var:
                return self.instrument_5.read_float(int(address_modbus), functioncode=4)
            case self.model.dev_6_adr_var:
                return self.instrument_6.read_float(int(address_modbus), functioncode=4)
            case self.model.dev_7_adr_var:
                return self.instrument_7.read_float(int(address_modbus), functioncode=4)
            case self.model.dev_8_adr_var:
                return self.instrument_8.read_float(int(address_modbus), functioncode=4)
            case self.model.dev_9_adr_var:
                return self.instrument_9.read_float(int(address_modbus), functioncode=4)
            case self.model.dev_10_adr_var:
                return self.instrument_10.read_float(int(address_modbus), functioncode=4)
            case self.model.dev_11_adr_var:
                return self.instrument_11.read_float(int(address_modbus), functioncode=4)
            case self.model.dev_12_adr_var:
                return self.instrument_12.read_float(int(address_modbus), functioncode=4)
            case self.model.dev_13_adr_var:
                return self.instrument_13.read_float(int(address_modbus), functioncode=4)
            case self.model.dev_14_adr_var:
                return self.instrument_14.read_float(int(address_modbus), functioncode=4)
            case self.model.dev_15_adr_var:
                return self.instrument_15.read_float(int(address_modbus), functioncode=4)

    def cycle_data(self):

        for i in range(self.conn_repeat_nr):

            try:
                self.model.data_1 = self.data_pull_from_instrument(self.model.dev_1_adr_var, self.model.mod_1_adr_var)
                print(self.model.data_1)
                print(f'Pobrano data_1 {i}')
                break
            except Exception:
                print(f'Błąd pobrania data_1 {i}')

        for i in range(self.conn_repeat_nr):

            try:
                self.model.data_2 = self.data_pull_from_instrument(self.model.dev_2_adr_var, self.model.mod_2_adr_var)

                print(f'Pobrano data_2 {i}')
                break
            except Exception:
                print(f'Błąd pobrania data_2 {i}')

        for i in range(self.conn_repeat_nr):
            try:
                self.model.data_3 = self.data_pull_from_instrument(self.model.dev_3_adr_var, self.model.mod_3_adr_var)

                print(f'Pobrano data_3 {i}')
                break

            except Exception:
                print(f'Błąd pobrania data_3 {i}')

        for i in range(self.conn_repeat_nr):
            try:
                self.model.data_4 = self.data_pull_from_instrument(self.model.dev_4_adr_var, self.model.mod_4_adr_var)
                print(f'Pobrano data_4 {i}')
                break
            except Exception:
                print(f'Błąd pobrania data_4 {i}')

        for i in range(self.conn_repeat_nr):
            try:
                self.model.data_5 = self.data_pull_from_instrument(self.model.dev_5_adr_var, self.model.mod_5_adr_var)
                print(f'Pobrano data_5 {i}')
                break
            except:
                print(f'Błąd pobrania data_5 {i}')

        for i in range(self.conn_repeat_nr):

            try:
                self.model.data_6 = self.data_pull_from_instrument(self.model.dev_6_adr_var, self.model.mod_6_adr_var)
                print(f'Pobrano data_6 {i}')
                break
            except:
                print(f'Błąd pobrania data_6 {i}')

        for i in range(self.conn_repeat_nr):
            try:
                self.model.data_7 = self.data_pull_from_instrument(self.model.dev_7_adr_var, self.model.mod_7_adr_var)
                print(f'Pobrano data_7 {i}')
                break
            except:
                print(f'Błąd pobrania data_7 {i}')
        for i in range(self.conn_repeat_nr):
            try:
                self.model.data_8 = self.data_pull_from_instrument(self.model.dev_8_adr_var, self.model.mod_8_adr_var)
                print(f'Pobrano data_8 {i}')
                break
            except:
                print(f'Błąd pobrania data_8 {i}')

        for i in range(self.conn_repeat_nr):

            try:
                self.model.data_9 = self.data_pull_from_instrument(self.model.dev_9_adr_var, self.model.mod_9_adr_var)
                print(f'Pobrano data_9 {i}')
                break
            except:
                print(f'Błąd pobrania data_9 {i}')

        for i in range(self.conn_repeat_nr):

            try:
                self.model.data_10 = self.data_pull_from_instrument(self.model.dev_10_adr_var,
                                                                    self.model.mod_10_adr_var)
                print(f'Pobrano data_10 {i}')
                break
            except:
                print(f'Błąd pobrania data_10 {i}')

        for i in range(self.conn_repeat_nr):
            try:
                self.model.data_11 = self.data_pull_from_instrument(self.model.dev_11_adr_var,
                                                                    self.model.mod_11_adr_var)
                print(f'Pobrano data_11 {i}')
                break
            except:
                print(f'Błąd pobrania data_11 {i}')

        for i in range(self.conn_repeat_nr):

            try:
                self.model.data_12 = self.data_pull_from_instrument(self.model.dev_12_adr_var,
                                                                    self.model.mod_12_adr_var)
                print(f'Pobrano data_12 {i}')
                break
            except:
                print(f'Błąd pobrania data_12 {i}')

        for i in range(self.conn_repeat_nr):

            try:
                self.model.data_13 = self.data_pull_from_instrument(self.model.dev_13_adr_var,
                                                                    self.model.mod_13_adr_var)
                print(f'Pobrano data_13 {i}')
                break
            except:
                print(f'Błąd pobrania data_13 {i}')

        for i in range(self.conn_repeat_nr):
            try:
                self.model.data_14 = self.data_pull_from_instrument(self.model.dev_14_adr_var,
                                                                    self.model.mod_14_adr_var)

                print(f'Pobrano data_14 {i}')
                break
            except:
                print(f'Błąd pobrania data_14 {i}')

        for i in range(self.conn_repeat_nr):
            try:
                self.model.data_15 = self.data_pull_from_instrument(self.model.dev_15_adr_var,
                                                                    self.model.mod_15_adr_var)

                print(f'Pobrano data_15 {i}')
                break
            except:
                print(f'Błąd pobrania data_15 {i}')

    def start_save(self):
        self.t2s = time.time()
        print('start')

    def fan_start(self):

        self.model.fan_signal.set(self.view.fan_signal.get())

        # for i in range(self.conn_repeat_nr):
        #   try:
        self.instrument_2.write_float(3, 100, 4)

        print((self.instrument_2.read_register(6, 1, 4)))
        print('ok')

        #          break
        #  except:
        #         print(f'Fan- failure {i}')

        print(self.model.fan_signal.get())

    def fan_stop(self):
        print('fan stop')

    def HE_start(self):

        self.model.HE_signal.set(self.view.HE_signal.get())

        # for i in range(self.conn_repeat_nr):
        #     try:
        #         self.model.data_15 = (self.instrument_2.read_float(int(self.model.mod_15_adr_var), functioncode=4))
        #         print(f'Pobrano data_15 {i}')
        #         break
        #     except:
        #         print(f'Błąd pobrania data_15 {i}')
        #
        print(self.model.HE_signal.get())

    def HE_stop(self):
        print('HE stop')

    def save_data(self):
        self.t1s = time.time()
        self.cycle_data()
        t = self.t1s - self.t2s
        t = str(round(t, 1))
        t = t.replace('.', ',')
        self.model.data_1 = round(self.model.data_1, 2)
        self.model.data_1 = str(self.model.data_1).replace('.', ',')

        self.model.data_2 = round(self.model.data_2, 2)
        self.model.data_2 = str(self.model.data_2).replace('.', ',')

        self.model.data_3 = round(self.model.data_3, 2)
        self.model.data_3 = str(self.model.data_3).replace('.', ',')

        self.model.data_4 = round(self.model.data_4, 2)
        self.model.data_4 = str(self.model.data_4).replace('.', ',')

        self.model.data_5 = round(self.model.data_5, 2)
        self.model.data_5 = str(self.model.data_5).replace('.', ',')

        self.model.data_6 = round(self.model.data_6, 2)
        self.model.data_6 = str(self.model.data_6).replace('.', ',')

        self.model.data_7 = round(self.model.data_7, 2)
        self.model.data_7 = str(self.model.data_7).replace('.', ',')

        self.model.data_8 = round(self.model.data_8, 2)
        self.model.data_8 = str(self.model.data_8).replace('.', ',')

        self.model.data_9 = round(self.model.data_9, 2)
        self.model.data_9 = str(self.model.data_9).replace('.', ',')

        self.model.data_10 = round(self.model.data_10, 2)
        self.model.data_10 = str(self.model.data_10).replace('.', ',')

        self.model.data_11 = round(self.model.data_11, 2)
        self.model.data_11 = str(self.model.data_11).replace('.', ',')

        self.model.data_12 = round(self.model.data_12, 2)
        self.model.data_12 = str(self.model.data_12).replace('.', ',')

        self.model.data_13 = round(self.model.data_13, 2)
        self.model.data_13 = str(self.model.data_13).replace('.', ',')

        self.model.data_14 = round(self.model.data_14, 2)
        self.model.data_14 = str(self.model.data_14).replace('.', ',')

        # self.model.data_15 = round(self.model.data_15,2)
        self.model.data_15 = str(self.model.data_15).replace('.', ',')

        self.data = [t, self.model.data_1, self.model.data_2, self.model.data_3,
                     self.model.data_4, self.model.data_5, self.model.data_6, self.model.data_7,
                     self.model.data_8, self.model.data_9, self.model.data_10, self.model.data_11, self.model.data_12,
                     self.model.data_13, self.model.data_14, self.model.mod_15_adr_var]

        with open('data.csv', mode='a', newline='') as file:
            header = ['t', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15']
            writer = csv.writer(file, delimiter=';')
            self.n_header += 1
            if self.n_header == 1:
                writer.writerow(header)
            writer.writerow(self.data)

        print(self.data)

    def set_save_control(self):

        self.model.save_control.set(False)

    def start_thread(self):
        self.model.save_control = True

    def stop_thread(self):
        self.model.save_control = False

        # self.settings()
        # self.make()
