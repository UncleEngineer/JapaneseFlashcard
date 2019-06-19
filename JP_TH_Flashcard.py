from tkinter import *
from tkinter import ttk,messagebox
from tkinter.font import Font
import webbrowser as web
from tkinter import simpledialog
from tkinter.ttk import Notebook
from tkinter import filedialog
import random
import sqlite3
import time
from PIL import Image
from PIL import ImageTk

# PIL is pillow libray
# pip install pillow

import csv

from googletrans import Translator
import webbrowser
import pyperclip

def Trans0(event=None):
    #print('We are Ready to Trans')
    Lam = Translator()
    txt = texttrans.get() # .get() คือ ดึงค่าในตัวแปรนั้นออกมา
    mytext = Lam.translate(txt,dest='en')
    print(mytext.text)

    textset = ''
    xx = 0
    for i in mytext.text:
        if xx < 50:
            textset += i
            xx += 1
        else:
            textset += '\n' + i
            xx = 0

    meaning.set(textset)
    print('-----------')

def Trans1(event=None):
    #print('We are Ready to Trans')
    Lam = Translator()
    txt = texttrans.get() # .get() คือ ดึงค่าในตัวแปรนั้นออกมา
    mytext = Lam.translate(txt,dest='th')
    print(mytext.text)
    textset = ''
    xx = 0
    for i in mytext.text:
        if xx < 50:
            textset += i
            xx += 1
        else:
            textset += '\n' + i
            xx = 0

    meaning.set(textset)
    print('-----------')



def Trans2(event=None):
    #print('We are Ready to Trans')
    Lam = Translator()
    txt = texttrans.get()
    mytext = Lam.translate(txt,dest='zh-cn')
    print(mytext.text)
    print(mytext.pronunciation)
    try:
        textset = ''
        xx = 0
        for i in mytext.text:
            if xx < 10:
                textset += i
                xx += 1
            else:
                textset += '\n' + i
                xx = 0

        xx = 0
        textset += '\n'
        for i in mytext.pronunciation:
            if xx < 50:
                textset += i
                xx += 1
            else:
                textset += '\n' + i
                xx = 0



        meaning.set(textset)
    except:
        textset = ''
        xx = 0
        for i in mytext.text:
            if xx < 20:
                textset += i
                xx += 1
            else:
                textset += '\n' + i
                xx = 0
        meaning.set(textset)

    print('-----------')

def Trans3(event=None):
    #print('We are Ready to Trans')
    Lam = Translator()
    txt = texttrans.get()
    mytext = Lam.translate(txt,dest='ja')
    print(mytext.text)
    print(mytext.pronunciation)
    try:
        textset = ''
        xx = 0
        for i in mytext.text:
            if xx < 20:
                textset += i
                xx += 1
            else:
                textset += '\n' + i
                xx = 0

        xx = 0
        textset += '\n'
        for i in mytext.pronunciation:
            if xx < 50:
                textset += i
                xx += 1
            else:
                textset += '\n' + i
                xx = 0



        meaning.set(textset)
    except:
        textset = ''
        xx = 0
        for i in mytext.text:
            if xx < 20:
                textset += i
                xx += 1
            else:
                textset += '\n' + i
                xx = 0
        meaning.set(textset)

def Trans4(event=None):
    #print('We are Ready to Trans')
    Lam = Translator()
    txt = texttrans.get() # .get() คือ ดึงค่าในตัวแปรนั้นออกมา
    mytext = Lam.translate(txt,dest='de')
    print(mytext.text)

    textset = ''
    xx = 0
    for i in mytext.text:
        if xx < 50:
            textset += i
            xx += 1
        else:
            textset += '\n' + i
            xx = 0

    meaning.set(textset)
    print('-----------')


def openweb1(event=None):
    txt = texttrans.get()
    print(txt)

    splittext = txt.split(' ')

    print(splittext)

    url = 'https://translate.google.co.th/?hl=th#view=home&op=translate&sl=auto&tl=en&text='
    url2 = ''

    for sp in splittext:
        url2 = url2 + sp + '%20'
        print(url2)

    allurl = url + url2
    webbrowser.open(allurl)

def openweb2(event=None):
    txt = texttrans.get()
    print(txt)

    splittext = txt.split(' ')

    print(splittext)

    url = 'https://translate.google.co.th/?hl=th#view=home&op=translate&sl=auto&tl=th&text='
    url2 = ''

    for sp in splittext:
        url2 = url2 + sp + '%20'
        print(url2)

    allurl = url + url2
    webbrowser.open(allurl)

def openweb3(event=None):
    txt = texttrans.get()
    print(txt)

    splittext = txt.split(' ')

    print(splittext)

    url = 'https://translate.google.co.th/?hl=th#view=home&op=translate&sl=auto&tl=zh-CN&text='
    url2 = ''

    for sp in splittext:
        url2 = url2 + sp + '%20'
        print(url2)

    allurl = url + url2
    webbrowser.open(allurl)

def openweb4(event=None):
    txt = texttrans.get()
    print(txt)

    splittext = txt.split(' ')

    print(splittext)

    url = 'https://translate.google.co.th/?hl=th#view=home&op=translate&sl=auto&tl=ja&text='
    url2 = ''

    for sp in splittext:
        url2 = url2 + sp + '%20'
        print(url2)

    allurl = url + url2
    webbrowser.open(allurl)

def openweb5(event=None):
    txt = texttrans.get()
    print(txt)

    splittext = txt.split(' ')

    print(splittext)

    url = 'https://translate.google.co.th/?hl=th#view=home&op=translate&sl=auto&tl=de&text='
    url2 = ''

    for sp in splittext:
        url2 = url2 + sp + '%20'
        print(url2)

    allurl = url + url2
    webbrowser.open(allurl)

def EnterTrans(event=None):

    if v_radio.get() == 'en':
        Trans0()
    elif v_radio.get() == 'th':
        Trans1()
    elif v_radio.get() == 'zh-CN':
        Trans2()
    elif v_radio.get() == 'de':
        Trans4()
    else :
        Trans3()

def copytoclipboard(event=None):
    pyperclip.copy(meaning.get())

conn = sqlite3.connect('vocab.db')
c = conn.cursor()

c.execute(""" CREATE TABLE IF NOT EXISTS japanese (

			ID INTEGER PRIMARY KEY AUTOINCREMENT,
			vc_jp TEXT,
			vc_th TEXT,
			vc_desc TEXT,
			vc_img TEXT

			) """)

#CRUD Create Read Update Delete

def insert_vocab(vc_jp,vc_th,vc_desc,vc_img):
	ID = None
	with conn:
		c.execute("""INSERT INTO japanese VALUES (?,?,?,?,?)""",

			(ID,vc_jp,vc_th,vc_desc,vc_img)	)

	conn.commit()
	print('Data was inserted')



def delete_vocab(vocab):
	with conn:
		c.execute("DELETE FROM japanese WHERE vc_jp = ?",([vocab]))
	conn.commit()

def update_vocab(vocab,new_vocab):
	with conn:
		c.execute("UPDATE japanese SET vc_jp = ? WHERE vc_jp = ?",([new_vocab,vocab]))
	conn.commit()


def select_one(vocab):
	with conn:
		c.execute("SELECT * FROM japanese WHERE vc_jp = ?",([vocab]))
		allvocab = c.fetchall()

	#print(allvocab)
	return allvocab[0][1:]

def view_data():
	with conn:
		c.execute("SELECT * FROM japanese")
		allvocab = c.fetchall()

	#print(allvocab)
	return allvocab

def writecsv(filename='log.csv',header='Winner',score=0):
	with open(filename,'w',newline='') as f:
		fw = csv.writer(f)
		dt = [header,score]
		fw.writerow(dt)

def Addvocab_jp():

	try:

		vcjp = vocab_jp.get()
		vcth = vocab_th.get()
		vcdesc = desc_th.get()
		imgpath = img_path.get()

		insert_vocab(vcjp,vcth,vcdesc,imgpath)

		text = 'JP: {} TH: {} Desc: {}\nImg Path: {}'.format(vcjp,vcth,vcdesc,imgpath)
		result.set(text)
		vocab_jp.set('')
		vocab_th.set('')
		desc_th.set('')
		img_path.set('')
		EVocab.focus()
		

	except Exception as e:
		print(e)
		messagebox.showerror('ERROR','มีปัญหาเรื่องการกรอกข้อมูล')

	img_path.set('vocab\\default.png')
	update_data()

def vocabfocus(event=None):
	EVocab_th.focus()


try:
	count = view_data()
	if len(count) <= 0:
		insert_vocab('こんいちわ','สวัสดี','konnichiwa','vocab\\default.png')
		insert_vocab('魚','ปลา','sakana (さかな)','vocab\\fish.jpg')
except:
	pass

GUI = Tk()
GUI.title('JP-TH Flashcard by Uncle Engineer')
GUI.geometry('800x650+100+20')
GUI.state('zoomed')
GUI.iconbitmap('flashcard.ico')
GUI.wm_iconbitmap('flashcard.ico')
GUI.bind('<F6>',vocabfocus)



menubar = Menu(GUI)


def Exit():
	GUI.withdraw()


menufile = Menu(menubar, tearoff=0)
menufile.add_command(label='Exit',command=Exit)
menubar.add_cascade(label='File', menu=menufile) #Add menufile to menubar

def About():
	url = 'https://www.facebook.com/UncleEngineer'
	web.open(url)

def Version():
	messagebox.showinfo('Version','This is JP-TH Flashcard v.1.0\nby Uncle Engineer')

menuhelp = Menu(menubar, tearoff=0)
menuhelp.add_command(label='About Us',command=About)
menuhelp.add_command(label='Version',command=Version)
menubar.add_cascade(label='Help', menu=menuhelp)

GUI.config(menu=menubar)

tab = Notebook(GUI)

AllVocab = Frame(tab)
TAdd = Frame(tab)
TLearn = Frame(tab)
TTrans = Frame(tab)
TSummary = Frame(tab)

img_learning = PhotoImage(file='learning.png')


tab.add(TLearn, text='Learning',image=img_learning, compound='left')

img_vocab = PhotoImage(file='vocab.png')
tab.add(AllVocab, text='All Vocab',image=img_vocab, compound='left')


img_add = PhotoImage(file='add.png')
tab.add(TAdd, text='Add',image=img_add, compound='left')

img_trans = PhotoImage(file='translate.png')
tab.add(TTrans, text='Translate',image=img_trans, compound='left')


img_summary = PhotoImage(file='summary.png')
tab.add(TSummary, text='Summary',image=img_summary, compound='left')
tab.pack(fill=BOTH,expand=1)

###############################

############################TRANSLATE########################

GUI.bind('<F1>',openweb1)
GUI.bind('<F2>',openweb2)
GUI.bind('<F3>',openweb3)
GUI.bind('<F4>',openweb4)
GUI.bind('<F5>',openweb5)
GUI.bind('<Return>',EnterTrans)
GUI.bind('<Control-c>',copytoclipboard)


def AddtoFlashcard():
	tab.select(TAdd)
	vocab_jp.set(texttrans.get())
	vocab_th.set(meaning.get())

E1 = ttk.Label(TTrans, text = 'กรุณาใส่คำที่ต้องการแปล',font=('Angsana New',20))
E1.pack(pady=10)

F0 = Frame(TTrans)
F0.pack()

v_radio = StringVar()

RB1 = ttk.Radiobutton(F0,text='English',variable=v_radio,value='en')
RB1.invoke()
RB2 = ttk.Radiobutton(F0,text='Thai',variable=v_radio,value='th')
RB3 = ttk.Radiobutton(F0,text='Chinese',variable=v_radio,value='zh-CN')
RB4 = ttk.Radiobutton(F0,text='Japanese',variable=v_radio,value='ja')
RB5 = ttk.Radiobutton(F0,text='German',variable=v_radio,value='de')

RB1.grid(row=0,column=1)
RB2.grid(row=0,column=2)
RB3.grid(row=0,column=3)
RB4.grid(row=0,column=4)
RB5.grid(row=0,column=5)

texttrans = StringVar() #เก็บสิ่งที่เราพิมพ์ไว้

#FE1 = Frame(TTrans)
#FE1.pack(ipadx=200,pady=10)

E1 = ttk.Entry(F0, textvariable = texttrans,font=('Angsana New',20))
E1.grid(row=2,column=0,ipadx=200,columnspan=5,padx=10)

EB1 = ttk.Button(F0,text='Add to Flashcard',command=AddtoFlashcard)
EB1.grid(ipadx=20,ipady=10,pady=10,row=2,column=5)


F1 = Frame(TTrans)
F1.pack()

B1 = ttk.Button(F1,text='English',command=Trans0)
B1.grid(ipadx=20,ipady=10,pady=10,row=0,column=0)

B1 = ttk.Button(F1,text='Thai',command=Trans1)
B1.grid(ipadx=20,ipady=10,pady=10,row=0,column=1)

B2 = ttk.Button(F1,text='Chinese',command=Trans2)
B2.grid(ipadx=20,ipady=10,pady=10,row=0,column=2)

B3 = ttk.Button(F1,text='Japanese',command=Trans3)
B3.grid(ipadx=20,ipady=10,pady=10,row=0,column=3)

B4 = ttk.Button(F1,text='German',command=Trans4)
B4.grid(ipadx=20,ipady=10,pady=10,row=0,column=4)

meaning = StringVar()
meaning.set('----------Result----------')

Result = ttk.Label(TTrans,textvariable=meaning,font=('Angsana New',20))
Result.pack()

E1.focus()

#################################################################

global pvc
pvc = None
def NextVocab():

	try:
		all_vc = view_data()
		vc = random.choice(all_vc)
		global pvc
		
		while vc == pvc:
			vc = random.choice(all_vc)
			
		
		pvc = vc

		img = pvc[4]
		image = Image.open(img)

		image_size = list(image.size)
		#print(image_size)

		resize = 350
		cal = resize / image_size[0]
		pixels_x = int(image_size[0] * cal)
		pixels_y = int(image_size[1] * cal)
		global bg
		bg = ImageTk.PhotoImage(image.resize((pixels_x, pixels_y)))

		Vocab_Image['image'] =bg

		lvocab.set(vc[1])
		text = "TH: {}\nReading: {}".format('-','-')
		lvocab2.set(text)
	except:
		messagebox.showinfo('Please add Vocab','กรุณาเพิ่มคำศัพท์เพื่อเริ่มต้นใช้งาน เข้า Tab (Add) ได้เลยจร้าา')

		
def Translate(event=None):

	try:
		user_ans = ans.get()
		
		th = pvc[2]
		rd = pvc[3]
		text = "TH: {}\nReading: {}".format(th,rd)
		lvocab2.set(text)

		if th == user_ans:

			correct_list = ['คำตอบถูกต้องจร้าาาา ลุงตู่สอนมาแน่เลยอะไรจะเก่งปานนั้น',
							'ตอบถูกอีกแล้ว แบบนี้ซื้อรถถังให้สักคัน',
							'จะเทพไปไหน',
							'ถั่วต้ม เก่งมาก']

			last_score = user_score.get()
			last_score = int(last_score[7:-3])
			print(last_score)
			score_text = 'Score: {} XP'.format(last_score+1)
			user_score.set(score_text)

			rand_msg = random.choice(correct_list)

			messagebox.showinfo('Correct',rand_msg)
			ans.set('')
		else:
			wrong_list = ['ไปเรียนภาษาญี่ปุ่นกับลุงป้อมมาหรอ 555\nลุงป้อมสอนได้เฉพาะเทคนิคการซื้อนาฬิกา',
						  'ตั้งใจฝึกหน่อย เดี๋ยวจับไปปรับทัศนคติซะเลย...ปัดโถ่!']
			wrong_word = random.choice(wrong_list)
			messagebox.showerror('Wrong!',wrong_word)
	except:
		messagebox.showinfo('Please Click Next','กดปุ่ม Next ได้เลย')

########## IMAGE ##########

show_img = StringVar()
show_img.set('default.png')


# Resize image

image = Image.open('vocab\\default.png')

bg = ImageTk.PhotoImage(image)
#

#bg = PhotoImage(file=img, width=500)
# Image Label
global Vocab_Image

Vocab_Image = ttk.Label(TLearn, image=bg)
Vocab_Image.place(x=400,y=50)

lvocab = StringVar()
lvocab.set('Click Next to Start')

LLearning_Vocab = ttk.Label(TLearn,font=('Angsana New',40),textvariable=lvocab)
LLearning_Vocab.place(x=20,y=50)

lvocab2 = StringVar()
text = "TH: {}\nReading: {}".format('-','-')
lvocab2.set(text)

LLearning_Vocab2 = ttk.Label(TLearn,font=('TH Sarabun New',20),textvariable=lvocab2)
LLearning_Vocab2.place(x=20,y=200)

ans = StringVar()

LAns = ttk.Label(TLearn,font=('TH Sarabun New',20),text='Ans: ')
LAns.place(x=20,y=300)

# Input Text
EAns = ttk.Entry(TLearn,font=('TH Sarabun New',20),textvariable=ans)
EAns.place(x=60,y=300)

EAns.bind('<Return>',Translate)

user_score = StringVar()
user_score.set('0')
score_text = 'Score: {} XP'.format(user_score.get())
user_score.set(score_text)

EScore = ttk.Label(TLearn,font=('TH Sarabun New',20),textvariable=user_score)
EScore.place(x=60,y=350)

### Button ###

LFrame = Frame(TLearn)
LFrame.place(x=100,y=500)

BNext = ttk.Button(LFrame,text='Translate',command=Translate)
BNext.pack(ipadx=20,ipady=10)


LFrame2 = Frame(TLearn)
LFrame2.place(x=250,y=500)

BNext2 = ttk.Button(LFrame2,text='Next',command=NextVocab)
BNext2.pack(ipadx=20,ipady=10)


FAddvocab = Frame(TAdd)
FAddvocab.place(x=50,y=20)

LVocab = ttk.Label(FAddvocab,text='Vocab Japanese',font=('Angsana New',15))
LVocab.grid(row=0,column=0,sticky='w')

vocab_jp = StringVar()

EVocab = ttk.Entry(FAddvocab,textvariable=vocab_jp,font=('Angsana New',15))
EVocab.grid(row=0,column=1,padx=10,pady=10,sticky='w')


LVocab_th = ttk.Label(FAddvocab,text='Translate',font=('Angsana New',15))
LVocab_th.grid(row=1,column=0,sticky='w')

vocab_th = StringVar()

EVocab_th = ttk.Entry(FAddvocab,textvariable=vocab_th,font=('Angsana New',15))
EVocab_th.grid(row=1,column=1,padx=10,pady=10,sticky='w')


LDesc = ttk.Label(FAddvocab,text='Description',font=('Angsana New',15))
LDesc.grid(row=2,column=0,sticky='w')

desc_th = StringVar()

EDesc = ttk.Entry(FAddvocab,textvariable=desc_th,font=('Angsana New',15))
EDesc.grid(row=2,column=1,padx=10,pady=10,sticky='w')


LImg = ttk.Label(FAddvocab,text='Image',font=('Angsana New',15))
LImg.grid(row=3,column=0,sticky='w')

img_path = StringVar()
img_path.set('vocab\\default.png')

LImg_path = ttk.Label(FAddvocab,textvariable=img_path,font=('Angsana New',15))
LImg_path.grid(row=3,column=1,padx=10,pady=5,sticky='w')

def Browse():
	ipth = filedialog.askopenfilename()
	ipth = ipth.replace('/','\\\\')
	print(ipth)
	img_path.set(ipth)

BBrowse = ttk.Button(FAddvocab, text='Browse Vocab Image',command=Browse)
BBrowse.grid(row=4,column=1,sticky='w')

FB = Frame(TAdd)
FB.place(x=150,y=260)

BAdd = ttk.Button(FB, text='Add',command=Addvocab_jp)
BAdd.pack(ipadx=10,ipady=10)

result = StringVar()
result.set('----Result----')

LResult = ttk.Label(TAdd, textvariable=result,font=('Angsana New',20,'bold'))
LResult.place(x=50,y=320)


def update_data():

	vocablist.delete(*vocablist.get_children())

	alldata = view_data()
	for row in alldata:
		print(row[1:])
		vocablist.insert('','end',values=row[1:])


header = ['Vocab JP','Vocab Thai','Description','Image']


vocablist = ttk.Treeview(AllVocab, columns=header, show='headings',height=10)
vocablist.pack(fill=BOTH)


for hd in header:
	vocablist.heading(hd,text=hd)


font=Font(family='Angsana New', size=20)
font.metrics()
fontheight=font.metrics()['linespace']

style = ttk.Style()
style.configure("Treeview.Heading", font=('Arial',15))
style.configure("Treeview",font=font,rowheight=fontheight)

BUpdate = ttk.Button(AllVocab, text='Update',command=update_data)
BUpdate.pack()


def del_item():

	q = messagebox.askyesno('Confirm','คุณต้องการลบใช่หรือไม่?')
	print(q)


	if q == True:
		select = vocablist.selection()
		item = vocablist.item(select)
		print(item['values'])

		vocab_jp = item['values'][0]
		delete_vocab(vocab_jp)
		update_data()
	else:
		pass

rightclick = Menu(GUI,tearoff=0)
rightclick.add_command(label='Delete',command=del_item)


def popup(event):
	rightclick.post(event.x_root,event.y_root)

vocablist.bind('<Button-3>',popup)


def fullscreen(event):
	GUI.attributes('-fullscreen',True)


def fullscreen2(event):
	GUI.attributes('-fullscreen',False)

GUI.bind('<F12>',fullscreen)
GUI.bind('<F11>',fullscreen2)

#username = StringVar()
#un = simpledialog.askstring('Enter Your Name','ลื้อชื่ออาลายย?')
#messagebox.showinfo('Welcome','สวักลี '+un)
#username.set(un)

def Askname():

	GUI2 = Toplevel()
	GUI2.geometry('300x200+100+100')
	global name
	ename = StringVar()

	ename.set('')

	Lname = ttk.Label(GUI2,text='นายชื่ออะไรว่ะ? พิมพ์ชื่อก่อน',font=('TH Sarabun New',20))
	Lname.pack(pady=10)

	Ename = ttk.Entry(GUI2,textvariable=ename,font=('TH Sarabun New',20))
	Ename.pack(pady=10)

	GUI2.mainloop()

try:
	update_data()
except:
	messagebox.showinfo('Add Vocab','กรุณาเพิ่มคำศัพท์เพื่อเริ่มต้นใช้งาน')
#Askname()

tab.select(TTrans)

GUI.mainloop()