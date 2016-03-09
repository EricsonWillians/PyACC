#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  PyACC.py
#  
#  Copyright 2016 Ericson Willians (Rederick Deathwill) <EricsonWRP@ERICSONWRP-PC>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

import pymysql
import tkinter as tk
import threading

class App(threading.Thread):
	
	def __init__(self):
		threading.Thread.__init__(self)
		self.start()
	
	def callback(self):
		self.root.quit()
	
	def center(self, win):
		win.update_idletasks()
		width = win.winfo_width()
		height = win.winfo_height()
		x = (win.winfo_screenwidth() // 2) - (width // 2)
		y = (win.winfo_screenheight() // 2) - (height // 2)
		win.geometry("{}x{}+{}+{}".format(width, height, x, y))
		
	def run(self):
		self.root = tk.Tk()
		self.root.protocol("WM_DELETE_WINDOW", self.callback)
		self.root.title("PyACC by Ericson Willians")
		self.root.grid()
		self.root.grid_columnconfigure(0, weight=1)
		self.root.grid_columnconfigure(1, weight=1)
		for n in range(23):
			self.root.grid_rowconfigure(n, weight=2)
		self.root.geometry("{}x{}".format(400, 800))
		self.center(self.root)
		self.create_widgets()
		self.root.mainloop()
	
	def create_widgets(self):
		self.connection_label = tk.Label(self.root, text="MySQL Connection ", font="Arial 10 bold")
		self.connection_label.grid(column=0, row=0, pady=5, sticky="w")
		self.host_label = tk.Label(self.root, text="Host: ")
		self.host_label.grid(column=0, row=1, padx=5, sticky="w")
		self.host_entry = tk.Entry(self.root, bg="#000", fg="#0F0", highlightcolor="#F00", highlightthickness=2, takefocus=1, relief="sunken")
		self.host_entry.grid(column=0, row=2, padx=5, sticky=tk.W+tk.E)
		self.host_entry.insert(0, "127.0.0.1")
		self.host_entry.grid_rowconfigure(0, weight=1)
		self.host_entry.grid_columnconfigure(0, weight=1)
		self.user_label = tk.Label(self.root, text="User: ")
		self.user_label.grid(column=0, row=3, padx=5, sticky="w")
		self.user_entry = tk.Entry(self.root, bg="#000", fg="#0F0", highlightcolor="#F00", highlightthickness=2, takefocus=1, relief="sunken")
		self.user_entry.grid(column=0, row=4, padx=5, sticky=tk.W+tk.E)
		self.user_entry.insert(0, "root")
		self.user_entry.grid_rowconfigure(0, weight=1)
		self.user_entry.grid_columnconfigure(0, weight=1)
		self.pass_label = tk.Label(self.root, text="Pass: ")
		self.pass_label.grid(column=1, row=1, padx=5, sticky="w")
		self.pass_entry = tk.Entry(self.root, bg="#000", fg="#0F0", highlightcolor="#F00", highlightthickness=2, takefocus=1, relief="sunken")
		self.pass_entry.grid(column=1, row=2, padx=5, sticky=tk.W+tk.E)
		self.pass_entry.grid_rowconfigure(0, weight=1)
		self.pass_entry.grid_columnconfigure(0, weight=1)
		self.db_label = tk.Label(self.root, text="Database: ")
		self.db_label.grid(column=1, row=3, padx=5, sticky="w")
		self.db_entry = tk.Entry(self.root, bg="#000", fg="#0F0", highlightcolor="#F00", highlightthickness=2, takefocus=1, relief="sunken")
		self.db_entry.grid(column=1, row=4, padx=5, sticky=tk.W+tk.E)
		self.db_entry.grid_rowconfigure(0, weight=1)
		self.db_entry.grid_columnconfigure(0, weight=1)
		self.acc_label = tk.Label(self.root, text="Account ", font="Arial 10 bold")
		self.acc_label.grid(column=0, row=5, pady=5, sticky="w")
		self.name_label = tk.Label(self.root, text="Name: ")
		self.name_label.grid(column=0, row=6, padx=5, sticky="w")
		self.name_entry = tk.Entry(self.root, bg="#000", fg="#0F0", highlightcolor="#F00", highlightthickness=2, takefocus=1, relief="sunken")
		self.name_entry.grid(column=0, row=7, padx=5, sticky=tk.W+tk.E)
		self.name_entry.grid_rowconfigure(0, weight=1)
		self.name_entry.grid_columnconfigure(0, weight=1)
		self.acc_pass_label = tk.Label(self.root, text="Pass: ")
		self.acc_pass_label.grid(column=0, row=8, padx=5, sticky="w")
		self.acc_pass_entry = tk.Entry(self.root, bg="#000", fg="#0F0", highlightcolor="#F00", highlightthickness=2, takefocus=1, relief="sunken")
		self.acc_pass_entry.grid(column=0, row=9, padx=5, sticky=tk.W+tk.E)
		self.acc_pass_entry.grid_rowconfigure(0, weight=1)
		self.acc_pass_entry.grid_columnconfigure(0, weight=1)
		self.type_label = tk.Label(self.root, text="Type: ")
		self.type_label.grid(column=0, row=10, padx=5, sticky="w")
		self.type_entry = tk.Entry(self.root, bg="#000", fg="#0F0", highlightcolor="#F00", highlightthickness=2, takefocus=1, relief="sunken")
		self.type_entry.grid(column=0, row=11, padx=5, sticky=tk.W+tk.E)
		self.type_entry.grid_rowconfigure(0, weight=1)
		self.type_entry.grid_columnconfigure(0, weight=1)
		self.type_entry.insert(0, "1")
		self.premdays_label = tk.Label(self.root, text="Premdays: ")
		self.premdays_label.grid(column=1, row=6, padx=5, sticky="w")
		self.premdays_entry = tk.Entry(self.root, bg="#000", fg="#0F0", highlightcolor="#F00", highlightthickness=2, takefocus=1, relief="sunken")
		self.premdays_entry.grid(column=1, row=7, padx=5, sticky=tk.W+tk.E)
		self.premdays_entry.grid_rowconfigure(0, weight=1)
		self.premdays_entry.grid_columnconfigure(0, weight=1)
		self.lastday_label = tk.Label(self.root, text="Lastday: ")
		self.lastday_label.grid(column=1, row=8, padx=5, sticky="w")
		self.lastday_entry = tk.Entry(self.root, bg="#000", fg="#0F0", highlightcolor="#F00", highlightthickness=2, takefocus=1, relief="sunken")
		self.lastday_entry.grid(column=1, row=9, padx=5, sticky=tk.W+tk.E)
		self.lastday_entry.grid_rowconfigure(0, weight=1)
		self.lastday_entry.grid_columnconfigure(0, weight=1)
		self.creation_label = tk.Label(self.root, text="Creation: ")
		self.creation_label.grid(column=1, row=10, padx=5, sticky="w")
		self.creation_entry = tk.Entry(self.root, bg="#000", fg="#0F0", highlightcolor="#F00", highlightthickness=2, takefocus=1, relief="sunken")
		self.creation_entry.grid(column=1, row=11, padx=5, sticky=tk.W+tk.E)
		self.creation_entry.grid_rowconfigure(0, weight=1)
		self.creation_entry.grid_columnconfigure(0, weight=1)
		self.creation_entry.insert(0, "1")
		self.email_label = tk.Label(self.root, text="Email: ")
		self.email_label.grid(column=0, row=12, padx=5, sticky="w")
		self.email_entry = tk.Entry(self.root, bg="#000", fg="#0F0", highlightcolor="#F00", highlightthickness=2, takefocus=1, relief="sunken")
		self.email_entry.grid(column=0, row=13, padx=5, columnspan=2, sticky=tk.W+tk.E)
		self.email_entry.grid_rowconfigure(0, weight=1)
		self.email_entry.grid_columnconfigure(0, weight=1)
		self.player_label = tk.Label(self.root, text="Player ", font="Arial 10 bold")
		self.player_label.grid(column=0, row=15, pady=5, sticky="w")
		self.player_name_label = tk.Label(self.root, text="Name: ")
		self.player_name_label.grid(column=0, row=16, padx=5, sticky="w")
		self.player_name_entry = tk.Entry(self.root, bg="#000", fg="#0F0", highlightcolor="#F00", highlightthickness=2, takefocus=1)
		self.player_name_entry.grid(column=0, row=17, padx=5, sticky=tk.W+tk.E)
		self.player_name_entry.grid_rowconfigure(0, weight=1)
		self.player_name_entry.grid_columnconfigure(0, weight=1)
		self.vocation_label = tk.Label(self.root, text="Vocation: ")
		self.vocation_label.grid(column=0, row=18, padx=5, sticky="w")
		self.vocation_entry = tk.Entry(self.root, bg="#000", fg="#0F0", highlightcolor="#F00", highlightthickness=2, takefocus=1)
		self.vocation_entry.grid(column=0, row=19, padx=5, sticky=tk.W+tk.E)
		self.vocation_entry.insert(0, "1")
		self.vocation_entry.grid_rowconfigure(0, weight=1)
		self.vocation_entry.grid_columnconfigure(0, weight=1)
		self.sex_label = tk.Label(self.root, text="Sex: ")
		self.sex_label.grid(column=1, row=16, padx=5, sticky="w")
		self.sex_entry = tk.Entry(self.root, bg="#000", fg="#0F0", highlightcolor="#F00", highlightthickness=2, takefocus=1)
		self.sex_entry.grid(column=1, row=17, padx=5, sticky=tk.W+tk.E)
		self.sex_entry.insert(0, "1")
		self.sex_entry.grid_rowconfigure(0, weight=1)
		self.sex_entry.grid_columnconfigure(0, weight=1)
		self.town_label = tk.Label(self.root, text="Town: ")
		self.town_label.grid(column=1, row=18, padx=5, sticky="w")
		self.town_entry = tk.Entry(self.root, bg="#000", fg="#0F0", highlightcolor="#F00", highlightthickness=2, takefocus=1)
		self.town_entry.grid(column=1, row=19, padx=5, sticky=tk.W+tk.E)
		self.town_entry.insert(0, "1")
		self.town_entry.grid_rowconfigure(0, weight=1)
		self.town_entry.grid_columnconfigure(0, weight=1)
		self.console_label = tk.Label(self.root, text="Console ", font="Arial 10 bold")
		self.console_label.grid(column=0, row=20, pady=5, sticky="w")
		self.console = tk.Text(self.root, width=15, height=7, bg="#000", fg="#0F0", highlightcolor="#F00", highlightthickness=2, relief="sunken")
		self.console.grid(column=0, row=21, padx=5, pady=10, columnspan=2, sticky=tk.W+tk.E+tk.N+tk.S)
		self.console.grid_rowconfigure(0, weight=1)
		self.console.grid_columnconfigure(0, weight=1)
		self.scrollbar = tk.Scrollbar(self.console, command=self.console.yview)
		self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
		self.console["yscrollcommand"] = self.scrollbar.set
		self.console.insert(tk.END, "Welcome to PyACC, an opensource account creator for OpenTibia (MySQL).\n")
		self.create_button = tk.Button(self.root, text="Create", command=self.create)
		self.create_button.grid(column=0, row=22, ipadx=15, padx=80, pady=10, columnspan=2, sticky="e")
		self.quit_button = tk.Button(self.root, text="Exit", command=self.root.quit)
		self.quit_button.grid(column=0, row=22, ipadx=15, padx=8, pady=10, columnspan=2, sticky="e")
		
	def create(self, x=None):
		self.console.insert(tk.END, "Connecting to {host}...\n".format(host=self.host_entry.get()))
		self.connection = None
		try:
			self.connection = pymysql.connect(
				host=self.host_entry.get(),
				user=self.user_entry.get(),
				password=self.pass_entry.get(),
				db=self.db_entry.get(),
				charset="utf8mb4",
				cursorclass=pymysql.cursors.DictCursor
			)
		except Exception as e:
			self.console.insert(tk.END, "Error: {err}\n".format(err=str(e)))
		try:
			with self.connection.cursor() as cursor:
				sql = "SELECT `name` FROM `accounts` where `name` = %s"
				cursor.execute(sql, self.name_entry.get())
				self.acc_result = cursor.fetchone()
			if not self.acc_result:
				self.console.insert(tk.END, "Usename is free to be used.\n")
				with self.connection.cursor() as cursor:
					sql = "INSERT INTO `accounts` (`name`, `password`, `type`, `premdays`, `lastday`, `email`, `creation`) VALUES (%s, sha1(%s), %s, %s, %s, %s, %s)"
					cursor.execute(sql, (self.name_entry.get(), self.acc_pass_entry.get(), int(self.type_entry.get()), int(self.premdays_entry.get()), int(self.lastday_entry.get()), self.email_entry.get(), int(self.creation_entry.get())))
				self.connection.commit()
				self.console.insert(tk.END, "Account successfully created.\n")
			else:
				self.console.insert(tk.END, "The username already exists, try another one.\n")
			with self.connection.cursor() as cursor:
				sql = "SELECT `name` FROM `players` where `name` = %s"
				cursor.execute(sql, self.player_name_entry.get())
				self.player_result = cursor.fetchone()
			with self.connection.cursor() as cursor:
				sql = "SELECT `id` FROM `accounts` where `name` = %s"
				cursor.execute(sql, self.name_entry.get())
				self.acc_id_result = cursor.fetchone()
			if not self.player_result:
				with self.connection.cursor() as cursor:
					sql = "INSERT INTO `players` (`name`, `account_id`, `level`, `vocation`, `sex`, `town_id`) VALUES (%s, %s, %s, %s, %s, %s)"
					cursor.execute(sql, (self.player_name_entry.get(), int(self.acc_id_result["id"]), 8, int(self.vocation_entry.get()), int(self.sex_entry.get()), int(self.town_entry.get())))
				self.connection.commit()
				self.console.insert(tk.END, "Player successfully created.\n")
			else:
				self.console.insert(tk.END, "The player name already exists, try another one.\n")
			"""
			with connection.cursor() as cursor:
				# Read a single record
				sql = "SELECT * FROM accounts where id = 1"
				cursor.execute(sql)
				result = cursor.fetchone()
				print(result)
			"""
		except Exception as e:
			self.console.insert(tk.END, "Error: {err}\n".format(err=str(e)))
		finally:
			self.connection.close()
		
if __name__ == '__main__':
	app = App()
