import dbhelper
from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox
class FBlike:
    def __init__(self):
        self._dbo = dbhelper.DBHelper()
        self.loginWindow()

    def loginWindow(self):
        self._root = Tk()
        self._root.configure(background="red")
        self._root.minsize(400, 600)

        self._label1 = Label(self._root, text="FBLIKE", bg="#FF6E55",fg="#fff")
        self._label1.configure(font=("Constantia", 22, "bold"))
        self._label1.pack(pady=(30, 30))

        self._label2 = Label(self._root, text="Email: ", bg="#FF6E55",fg="#fff")
        self._label2.configure(font=("Constantia", 14))
        self._label2.pack(pady=(10, 5))

        self._emailInput = Entry(self._root)
        self._emailInput.pack(pady=(0, 20), ipadx=30, ipady=7)

        self._label3 = Label(self._root, text="Password: ",bg="#FF6E55", fg="#fff")
        self._label3.configure(font=("Constantia", 14))
        self._label3.pack(pady=(10, 5))

        self._passwordInput = Entry(self._root)
        self._passwordInput.pack(pady=(0, 20), ipadx=30, ipady=7)

        self._loginBtn = Button(self._root, text="Login", bg="#fff",width=30, height=2, command=lambda:self.loginHandler(self._emailInput.get(), self._passwordInput.get()))
        self._loginBtn.pack()

        self._label4 = Label(self._root, text="Not a member? ",bg="#FF6E55", fg="#fff")
        self._label4.configure(font=("Constantia", 16))
        self._label4.pack(pady=(10, 5))

        self._regBtn = Button(self._root, text="Click Here",
                              bg="#fff", width=10, height=1, command=lambda: self.regWindow())
        self._regBtn.pack()
        self._root.mainloop()

    def regWindow(self):
        self._root1 = Tk()
        self._root1.configure(background="#FF6E55")
        self._root1.minsize(400, 700)

        self._label1 = Label(self._root1, text="Name: ", bg="#FF6E55",fg="#fff")
        self._label1.configure(font=("Constantia", 14))
        self._label1.pack(pady=(10, 5))

        self._nameInput = Entry(self._root1)
        self._nameInput.pack(pady=(0, 10), ipadx=30, ipady=7)

        self._label2 = Label(self._root1, text="Email: ",bg="#FF6E55", fg="#fff")
        self._label2.configure(font=("Constantia", 14))
        self._label2.pack(pady=(10, 5))

        self._emailInput = Entry(self._root1)
        self._emailInput.pack(pady=(0, 10), ipadx=30, ipady=7)

        self._label3 = Label(self._root1, text="Password: ",bg="#FF6E55", fg="#fff")
        self._label3.configure(font=("Constantia", 14))
        self._label3.pack(pady=(10, 5))

        self._passwordInput = Entry(self._root1)
        self._passwordInput.pack(pady=(0, 10), ipadx=30, ipady=7)

        self._label4 = Label(self._root1, text="Age: ", bg="#FF6E55",fg="#fff")
        self._label4.configure(font=("Constantia", 14))
        self._label4.pack(pady=(10, 5))

        self._ageInput = Entry(self._root1)
        self._ageInput.pack(pady=(0, 10), ipadx=30, ipady=7)

        self._label5 = Label(self._root1, text="Gender: ",bg="#FF6E55", fg="#fff")
        self._label5.configure(font=("Constantia", 14))
        self._label5.pack(pady=(10, 5))

        self._genderInput = Entry(self._root1)
        self._genderInput.pack(pady=(0, 10), ipadx=30, ipady=7)

        self._label6 = Label(self._root1, text="City: ", bg="#FF6E55",fg="#fff")
        self._label6.configure(font=("Constantia", 14))
        self._label6.pack(pady=(10, 5))

        self._cityInput = Entry(self._root1)
        self._cityInput.pack(pady=(0, 10), ipadx=30, ipady=7)

        self._label7 = Label(self._root1, text="Bio: ", bg="#FF6E55",fg="#fff")
        self._label7.configure(font=("Constantia", 14))
        self._label7.pack(pady=(10, 5))

        self._bioInput = Entry(self._root1)
        self._bioInput.pack(pady=(0, 10), ipadx=30, ipady=7)

        self._registerBtn = Button(self._root1, text="Register",bg="#fff", width=30, height=2, command=lambda:
            self.regHandler(self._nameInput.get(), self._emailInput.get(),self._passwordInput.get(),
                            self._ageInput.get(), self._genderInput.get(), self._cityInput.get(), self._bioInput.get()))
        self._registerBtn.pack()
        self._root1.mainloop()

    def loginHandler(self, email, password):

        response = self._dbo.search('email', email, 'password', password, 'users')
        if len(response) == 0:
            print("Incorrect")
        else:
            self.user_id = response[0][0]
            self.loadProfile(response)

    def loadProfile(self, response):
        self.mainWindow(response, 1)

    def mainWindow(self, response, mode, num=0):
        self.clearWindow()

        self.headerMenu()
        imageUrl = "images/y3.png"
        load = Image.open(imageUrl)
        load = load.resize((200, 200), Image.ANTIALIAS)
        render = ImageTk.PhotoImage(load)
        img = Label(image=render)
        img.image = render
        img.pack()

        name = response[0][1]
        self._label1 = Label(self._root, text=name, bg="#FF6E55",fg="#fff")
        self._label1.configure(font=("Constantia", 14))
        self._label1.pack(pady=(10, 5))

        age = response[0][4]
        self._label2 = Label(self._root, text=age, bg="#FF6E55",fg="#fff")
        self._label2.configure(font=("Constantia", 14))
        self._label2.pack(pady=(10, 5))

        gender = response[0][6]
        self._label3 = Label(self._root, text=gender, bg="#FF6E55",fg="#fff")
        self._label3.configure(font=("Constantia", 14))
        self._label3.pack(pady=(10, 5))

        city = response[0][7]
        self._label4 = Label(self._root, text=city, bg="#FF6E55", fg="#fff")
        self._label4.configure(font=("Constantia", 14))
        self._label4.pack(pady=(10, 5))

        if mode == 2:
            frame = Frame(self._root)
            frame.pack()

            btn1 = Button(frame, text="Previous", fg="#fff",bg="#fd5068", command=lambda: self.othersProfile(num - 1))
            btn1.pack(side=LEFT)

            btn2 = Button(frame, text="Purpose", fg="#fff",bg="#fd5068", command=lambda: self.propose(response[0][0]))
            btn2.pack(side=LEFT)

            btn3 = Button(frame, text="Next", fg="#fff", bg="#fd5068",command=lambda: self.othersProfile(num + 1))
            btn3.pack(side=LEFT)

    def headerMenu(self):
        menu = Menu(self._root)
        self._root.config(menu=menu)
        filemenu = Menu(menu)
        menu.add_cascade(label="Home", menu=filemenu)
        filemenu.add_command(label="My Profile")
        filemenu.add_command(label="Edit Profile")
        filemenu.add_command(label="View Profile", command=lambda: self.othersProfile(0))
        filemenu.add_command(label="LogOut")
        helpmenu = Menu(menu)
        menu.add_cascade(label="Proposals", menu=helpmenu)
        helpmenu.add_command(label="My Proposals")
        helpmenu.add_command(label="My Requests")
        helpmenu.add_command(label="My Matches")

    def clearWindow(self):
        for i in self._root.pack_slaves():
            i.destroy()

    def regHandler(self, name, email, password, age, gender, city, bio):
        mydict = {
            'user_id': 'NULL',
            'name': name,
            'email': email,
            'password': password,
            'age': age,
            'bg': 'avatar.jpg',
            'gender': gender,
            'city': city,
            'bio': bio
        }
        flag = self._dbo.insert(mydict, 'users')
        if flag == 0:
            print("Error")
        else:
            print("Reg successful")

    def othersProfile(self, num):
        send_data = []

        data = self._dbo.searchOne('user_id', self.user_id, 'users', 'NOTLIKE')
        if num < 0:
            self.errorMessage("Error", "first one")
        elif num > len(data) - 1:
            self.errorMessage("Error", "End")
        else:
            send_data.append(data[num])
        self.mainWindow(send_data, 2, num)

    def propose(self, juliet_id):

        data = self._dbo.search('romeo_id', self.user_id, 'juliet_id', juliet_id, 'proposals')
        if len(data) == 0:
            mydict = {
                'proposal_id': 'NULL',
                'romeo_id': self.user_id,
                'juliet_id': juliet_id
            }
            flag = self._dbo.insert(mydict, 'proposals')
            if flag == 1:
                self.errorMessage("Success", "request sent")
            else:
                self.errorMessage("Failure", "something went wrong")
        else:
            self.errorMessage("Error", "Despo sala")

    def errorMessage(self, title, message):
        messagebox.showerror(title, message)


t=FBlike()


