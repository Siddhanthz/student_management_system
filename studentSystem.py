from os import execl
import _tkinter as tk
from _tkinter import ingVar, Widget, font, messagebox
from _tkinter.constants import BOTH, BOTTOM, HORIZONTAL, RIDGE, RIGHT, VERTICAL, X, Y
import _tkinter.ttk as ttk
from typing import Text
import PIL
import mysql.connector


class Student:
    def __init__(self, win):
        self.win = win
        self.win.geometry('1300x500')
        self.win.title('Student Management System')

        self.dep_var = StringVar()
        self.year_var = StringVar()
        self.sem_var = StringVar()
        self.id_var = StringVar()
        self.fname_var = StringVar()
        self.lname_var = StringVar()
        self.roll_var = StringVar()
        self.dob_var = StringVar()
        self.gender_var = StringVar()
        self.mobile_var = StringVar()
        self.email_var = StringVar()
        self.address_var = StringVar()

        frame = tk.Frame(self.win, bd=5, relief=RIDGE)
        frame.place(x=0, y=0, height=500, width=1300)

        title = tk.Label(
            self.win, text='Student Management System', font=('arial', 25, 'bold'))
        title.place(x=10, y=10, width=1050, height=40)

        frame1 = tk.LabelFrame(frame, bd=3, padx=2, relief=RIDGE, font=('arial', 12, ),
                               text='Student Information', fg='blue')
        frame1.place(x=10, y=60, width=540, height=420)

        frame2 = tk.LabelFrame(frame, bd=3, padx=2, relief=RIDGE, font=('arial', 12, ),
                               text='Student Data', fg='blue')
        frame2.place(x=560, y=60, width=720, height=420)

        dep_label = tk.Label(frame1, text='Department', font=('arial', 12))
        dep_label.grid(row=0, column=0, padx=7, pady=7, sticky='W')

        dep_drop = ttk.Combobox(frame1, font=(
            'arial', 12), textvariable=self.dep_var, width=15, state='readonly')
        dep_drop['value'] = ('Select Department', 'IT',
                             'CSE', 'CSE', 'EC', 'Mechenical', 'Civil')
        dep_drop.current(0)
        dep_drop.grid(row=0, column=1, sticky='W')

        year_label = tk.Label(frame1, text='Year', font=('arial', 12))
        year_label.grid(row=0, column=2, padx=7, pady=7, sticky='W')

        year_drop = ttk.Combobox(frame1, font=(
            'arial', 12),  textvariable=self.year_var, width=15, state='readonly')
        year_drop['value'] = ('Current Year', '1st',
                              '2nd', '3rd', '4th')
        year_drop.current(0)
        year_drop.grid(row=0, column=3, sticky='W')

        sem_label = tk.Label(frame1, text='Semester', font=('arial', 12))
        sem_label.grid(row=1, column=0, padx=7, pady=7, sticky='W')

        sem_drop = ttk.Combobox(frame1, font=(
            'arial', 12), width=15, textvariable=self.sem_var, state='readonly')
        sem_drop['value'] = ('Current Semester', '1st',
                             '2nd')
        sem_drop.current(0)
        sem_drop.grid(row=1, column=1, sticky='W')

        id_label = tk.Label(frame1, text='Student ID', font=('arial', 12))
        id_label.grid(row=2, column=0, sticky='W')

        id_entry = ttk.Entry(frame1, font=('arial', 12),
                             textvariable=self.id_var, width=17)
        id_entry.grid(row=2, column=1, sticky='W')

        fname_label = tk.Label(frame1, text='Fname', font=('arial', 12))
        fname_label.grid(row=3, column=0, sticky='W', pady=7)

        fname_entry = ttk.Entry(frame1, font=(
            'arial', 12), textvariable=self.fname_var, width=17)
        fname_entry.grid(row=3, column=1, sticky='W', pady=7)

        lname_label = tk.Label(frame1, text='Lname', font=('arial', 12))
        lname_label.grid(row=3, column=2, sticky='W', pady=7)

        lname_entry = ttk.Entry(frame1, font=(
            'arial', 12), textvariable=self.lname_var, width=17)
        lname_entry.grid(row=3, column=3, sticky='W', pady=7)

        roll_label = tk.Label(frame1, text='Roll Number', font=('arial', 12))
        roll_label.grid(row=4, column=0, sticky='W', pady=7)

        roll_entry = ttk.Entry(frame1, font=(
            'arial', 12), textvariable=self.roll_var, width=17)
        roll_entry.grid(row=4, column=1, sticky='W', pady=7)

        dob_label = tk.Label(frame1, text='DOB', font=('arial', 12))
        dob_label.grid(row=4, column=2, sticky='W', pady=7)

        dob_entry = ttk.Entry(frame1, font=('arial', 12),
                              textvariable=self.dob_var, width=17)
        dob_entry.grid(row=4, column=3, sticky='W', pady=7)

        genderlabel = tk.Label(frame1, text='Gender', font=('arial', 12))
        genderlabel.grid(row=5, column=0, sticky='W', pady=7)

        gender_drop = ttk.Combobox(frame1, font=(
            'arial', 12), width=15, textvariable=self.gender_var, state='readonly')
        gender_drop['value'] = ('Male', 'Female')
        gender_drop.current(0)
        gender_drop.grid(row=5, column=1, sticky='W')

        mnumber_label = tk.Label(frame1, text='Mobile No.', font=('arial', 12))
        mnumber_label.grid(row=6, column=0, sticky='W', pady=7)

        mnumber_entry = ttk.Entry(frame1, font=(
            'arial', 12), textvariable=self.mobile_var, width=17)
        mnumber_entry.grid(row=6, column=1, sticky='W', pady=7)

        email_label = tk.Label(frame1, text='Email', font=('arial', 12))
        email_label.grid(row=6, column=2, sticky='W', pady=7)

        email_entry = ttk.Entry(frame1, font=(
            'arial', 12), textvariable=self.email_var, width=17)
        email_entry.grid(row=6, column=3, sticky='W', pady=7)

        add_label = tk.Label(frame1, text='Address', font=('arial', 12))
        add_label.grid(row=7, column=0, sticky='W', pady=7)

        add_entry = ttk.Entry(frame1, font=('arial', 12),
                              textvariable=self.address_var, width=41)
        add_entry.grid(row=7, column=1, sticky='W', pady=7, columnspan=4)

        btn_frame = tk.Frame(frame1, bd=3, relief=RIDGE)
        btn_frame.place(x=0, y=290, height=50, width=530)

        btn_save = tk.Button(btn_frame, text='Save', command=self.add_data,  font=(
            'arial', 12), bg='blue', fg='white', highlightthickness=0, bd=0, width=13)
        btn_save.grid(row=8, column=0, padx=5, pady=10)

        btn_update = tk.Button(btn_frame, text='Update', command=self.update_data, font=(
            'arial', 12), bg='blue', fg='white', highlightthickness=0, bd=0, width=13)
        btn_update.grid(row=8, column=1, padx=5, pady=10)

        btn_reset = tk.Button(btn_frame, text='Reset', command=self.reset_data, font=(
            'arial', 12), bg='blue', fg='white', highlightthickness=0, bd=0, width=13)
        btn_reset.grid(row=8, column=2, padx=5, pady=10)

        btn_delete = tk.Button(btn_frame, text='Delete', command=self.delete_data, font=(
            'arial', 12), bg='red', fg='white', highlightthickness=0, bd=0, width=13)
        btn_delete.grid(row=8, column=3, padx=5, pady=10)

        filter_frame = tk.LabelFrame(frame2, bd=3, padx=2, relief=RIDGE, font=('arial', 12, ),
                                     text='Filter', fg='blue')
        filter_frame.place(x=10, y=10, width=690, height=75)

        search_label = tk.Label(
            filter_frame, text='Search by:', font=('arial', 12))
        search_label.grid(row=0, column=0, sticky='W', pady=5)

        self.filter_drop_var = StringVar()

        search_drop = ttk.Combobox(filter_frame, textvariable=self.filter_drop_var, font=(
            'arial', 12), width=15, state='readonly')
        search_drop['value'] = ('Select Option', 'Student_Id',
                                'Roll_Number')
        search_drop.current(0)
        search_drop.grid(row=0, column=1, sticky='W')

        self.filter_var = StringVar()

        search_entry = ttk.Entry(
            filter_frame, textvariable=self.filter_var, font=('arial', 12), width=14)
        search_entry.grid(row=0, column=2, sticky='W', padx=5)

        btn_search = tk.Button(filter_frame, text='Search', command=self.filter, font=(
            'arial', 12), bg='blue', fg='white', highlightthickness=0, bd=0, width=15)
        btn_search.grid(row=0, column=3, padx=5, pady=10)

        btn_showall = tk.Button(filter_frame, text='Show All', command=self.fetch_data, font=(
            'arial', 12), bg='blue', fg='white', highlightthickness=0, bd=0, width=15)
        btn_showall.grid(row=0, column=4, padx=5, pady=10)

        table_frame = tk.Frame(frame2, bd=3, padx=2, relief=RIDGE)
        table_frame.place(x=10, y=100, width=690, height=285)

        x_scroll = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        y_scroll = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.student_table = ttk.Treeview(table_frame, columns=(
            'Dep', 'Year', 'Sem', 'Id', 'First', 'Last', 'Roll', 'DOB', 'Gender', 'Mobile', 'Email', 'Address'), xscrollcommand=x_scroll.set, yscrollcommand=y_scroll.set)

        x_scroll.pack(side=BOTTOM, fill=X)
        y_scroll.pack(side=RIGHT, fill=Y)

        x_scroll.config(command=self.student_table.xview)
        y_scroll.config(command=self.student_table.yview)

        self.student_table.heading('Dep', text='Department')
        self.student_table.heading('Year', text='Year')
        self.student_table.heading('Sem', text='Semester')
        self.student_table.heading('Id', text='Student Id')
        self.student_table.heading('First', text='First Name')
        self.student_table.heading('Last', text='Last Name')
        self.student_table.heading('Roll', text='Roll Number')
        self.student_table.heading('DOB', text='DOB')
        self.student_table.heading('Gender', text='Gender')
        self.student_table.heading('Mobile', text='Mobile')
        self.student_table.heading('Email', text='Email')
        self.student_table.heading('Address', text='Address')

        self.student_table['show'] = 'headings'
        self.student_table.column('Dep', width=100)
        self.student_table.column('Year', width=100)
        self.student_table.column('Sem', width=100)
        self.student_table.column('Id', width=100)
        self.student_table.column('First', width=100)
        self.student_table.column('Last', width=100)
        self.student_table.column('Roll', width=100)
        self.student_table.column('DOB', width=100)
        self.student_table.column('Gender', width=100)
        self.student_table.column('Mobile', width=100)
        self.student_table.column('Email', width=100)
        self.student_table.column('Address', width=300)

        self.student_table.pack(fill=BOTH)
        self.student_table.bind('<ButtonRelease>', self.get_cursor)
        self.fetch_data()

    def add_data(self):
        if (self.dep_var.get() == '' or self.year_var.get() == '' or self.sem_var.get() == '' or self.id_var.get() == '' or self.fname_var.get() == '' or self.lname_var.get() == '' or self.dob_var.get() == '' or self.email_var.get() == '' or self.address_var.get() == '' or self.roll_var.get() == ''):
            messagebox.showerror('Error', "All fields are required")
        else:
            try:
                conn = mysql.connector.connect(
                    host='localhost', username='root', password='root', database='student')
                cursor = conn.cursor()
                cursor.execute(
                    'insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)', (self.dep_var.get(), self.year_var.get(), self.sem_var.get(), self.id_var.get(), self.fname_var.get(), self.lname_var.get(), self.roll_var.get(), self.dob_var.get(), self.gender_var.get(), self.mobile_var.get(), self.email_var.get(), self.address_var.get()))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo(
                    'Success!!', 'Data saved!!', parent=self.win)

            except Exception as es:
                messagebox.showerror(
                    'Error', f'Due to: {str(es)}', parent=self.win)

    def fetch_data(self):
        conn = mysql.connector.connect(
            host='localhost', username='root', password='root', database='student')
        cursor = conn.cursor()
        cursor.execute('select * from student')
        data = cursor.fetchall()
        if len(data) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert('', tk.END, values=i)
            conn.commit()
        conn.close()

    def get_cursor(self, event=''):
        cursor_row = self.student_table.focus()
        content = self.student_table.item(cursor_row)
        data = content['values']

        self.dep_var.set(data[0])
        self.year_var.set(data[1])
        self.sem_var.set(data[2])
        self.id_var.set(data[3])
        self.fname_var.set(data[4])
        self.lname_var.set(data[5])
        self.roll_var.set(data[6])
        self.dob_var.set(data[7])
        self.gender_var.set(data[8])
        self.mobile_var.set(data[9])
        self.email_var.set(data[10])
        self.address_var.set(data[11])

    def update_data(self):
        if (self.dep_var.get() == '' or self.year_var.get() == '' or self.sem_var.get() == '' or self.id_var.get() == '' or self.fname_var.get() == '' or self.lname_var.get() == '' or self.dob_var.get() == '' or self.email_var.get() == '' or self.address_var.get() == '' or self.roll_var.get() == ''):
            messagebox.showerror('Error', "All fields are required")
        else:
            try:
                update = messagebox.askyesno(
                    'Update', 'Are you sure you want to update data?', parent=self.win)
                if update > 0:
                    conn = mysql.connector.connect(
                        host='localhost', username='root', password='root', database='student')
                    cursor = conn.cursor()
                    cursor.execute(
                        'update student set Dep=%s, Year=%s, Semester=%s, First_Name=%s, Last_Name=%s, Roll_Number=%s, DOB=%s, Gender=%s, Mobile=%s, Email=%s, Address=%s where Student_Id=%s', (
                            self.dep_var.get(), self.year_var.get(), self.sem_var.get(),  self.fname_var.get(), self.lname_var.get(), self.roll_var.get(
                            ), self.dob_var.get(), self.gender_var.get(), self.mobile_var.get(), self.email_var.get(), self.address_var.get(), self.id_var.get()
                        ))
                else:
                    if not update:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()

                messagebox.showinfo(
                    'Success', 'Data successfully updated', parent=self.win)
            except Exception as es:
                messagebox.showerror(
                    'Error', f'Due to: {str(es)}', parent=self.win)

    def delete_data(self):
        if self.id_var.get() == '':
            messagebox.showerror('Error', "All fields are required")
        else:
            try:
                delete = messagebox.askyesno(
                    'Delete', 'Are you sure you want to delete?')
                if delete > 0:
                    conn = mysql.connector.connect(
                        host='localhost', username='root', password='root', database='student')
                    cursor = conn.cursor()
                    sql = 'delete from student where Student_Id=%s'
                    value = (self.id_var.get(),)
                    cursor.execute(sql, value)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo(
                    'Deleted', 'Data successfully deleted!!', parent=self.win)

            except Exception as es:
                messagebox.showerror(
                    'Error', f'Due to: {str(es)}', parent=self.win)

    def reset_data(self):
        self.dep_var.set('Select Department')
        self.year_var.set('Current Year')
        self.sem_var.set('Current Semester')
        self.id_var.set('')
        self.fname_var.set('')
        self.lname_var.set('')
        self.roll_var.set('')
        self.dob_var.set('')
        self.gender_var.set('Male')
        self.mobile_var.set('')
        self.email_var.set('')
        self.address_var.set('')

    def filter(self):
        if self.filter_drop_var.get() == '' or self.filter_var.get() == '':
            messagebox.showerror(
                'Error', 'Please select option')
        else:
            try:
                conn = mysql.connector.connect(
                    host='localhost', username='root', password='root', database='student')
                cursor = conn.cursor()
                cursor.execute('select * from student where '+str(
                    self.filter_drop_var.get())+" LIKE '%"+str(self.filter_var.get()) + "%'")
                data = cursor.fetchall()
                if len(data) != 0:
                    self.student_table.delete(
                        *self.student_table.get_children())
                    for i in data:
                        self.student_table.insert("", tk.END, values=i)
                    conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showerror(
                    'Error', f'Due to: {str(es)}', parent=self.win)


if __name__ == "__main__":
    win = tk.Tk()
    object1 = Student(win)
    win.mainloop()
