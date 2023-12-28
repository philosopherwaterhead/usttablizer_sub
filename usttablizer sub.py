import tkinter
from tkinter import ttk
import utaupy
import tkinter
import tkinter.filedialog
import tkinter.ttk as ttk
import math

import os
import re
import ast

kanahenkan = {
        'a'  :'あ', 'i'  :'い', 'u'  :'う', 'e'  :'え', 'o'  :'お',
        'ka' :'か', 'ki' :'き', 'ku' :'く', 'ke' :'け', 'ko' :'こ',
        'sa' :'さ', 'shi':'し', 'su' :'す', 'se' :'せ', 'so' :'そ',
        'ta' :'た', 'chi':'ち', 'tsu' :'つ', 'te' :'て', 'to' :'と',
        'na' :'な', 'ni' :'に', 'nu' :'ぬ', 'ne' :'ね', 'no' :'の',
        'ha' :'は', 'hi' :'ひ', 'fu' :'ふ', 'he' :'へ', 'ho' :'ほ',
        'ma' :'ま', 'mi' :'み', 'mu' :'む', 'me' :'め', 'mo' :'も',
        'ya' :'や', 'yu' :'ゆ', 'yo' :'よ',
        'ra' :'ら', 'ri' :'り', 'ru' :'る', 're' :'れ', 'ro' :'ろ',
        'wa' :'わ', 'wo' :'を', 'n'  :'ん',
        'ga' :'が', 'gi' :'ぎ', 'gu' :'ぐ', 'ge' :'げ', 'go' :'ご',
        'za' :'ざ', 'ji' :'じ', 'zu' :'ず', 'ze' :'ぜ', 'zo' :'ぞ',
        'da' :'だ', 'di' :'ぢ', 'du' :'づ', 'de' :'で', 'do' :'ど',
        'ba' :'ば', 'bi' :'び', 'bu' :'ぶ', 'be' :'べ', 'bo' :'ぼ',
        'pa' :'ぱ', 'pi' :'ぴ', 'pu' :'ぷ', 'pe' :'ぺ', 'po' :'ぽ',
        
        'kya':'きゃ', 'kyi':'キィ', 'kyu':'きゅ', 'kye':'キェ', 'kyo':'きょ',
        'gya':'ぎゃ', 'gyi':'ギィ', 'gyu':'ぎゅ', 'gye':'ギェ', 'gyo':'ぎょ',
        'sha':'しゃ',               'shu':'しゅ', 'she':'しぇ', 'sho':'しょ',
        'ja' :'じゃ',               'ju' :'じゅ', 'je' :'じぇ', 'jo' :'じょ',
        'cha':'ちゃ',               'chu':'ちゅ', 'che':'ちぇ', 'cho':'ちょ',
        'dya':'ぢゃ', 'dyi':'ヂィ', 'dyu':'ぢゅ', 'dhe':'デェ', 'dyo':'ぢょ',
        'nya':'にゃ', 'nyi':'ニィ', 'nyu':'にゅ', 'nye':'にぇ', 'nyo':'にょ',
        'hya':'ひゃ', 'hyi':'ヒィ', 'hyu':'ひゅ', 'hye':'ひぇ', 'hyo':'ひょ',
        'bya':'びゃ', 'byi':'ビィ', 'byu':'びゅ', 'bye':'びぇ', 'byo':'びょ',
        'pya':'ぴゃ', 'pyi':'ピィ', 'pyu':'ぴゅ', 'pye':'ぴぇ', 'pyo':'ぴょ',
        'mya':'みゃ', 'myi':'ミィ', 'myu':'みゅ', 'mye':'みぇ', 'myo':'みょ',
        'rya':'りゃ', 'ryi':'リィ', 'ryu':'りゅ', 'rye':'りぇ', 'ryo':'りょ',
        'fa' :'ふぁ', 'fi' :'ふぃ',               'fe' :'ふぇ', 'fo' :'ふぉ',
        'wi' :'うぃ', 'we' :'うぇ', 
        'va' :'ヴァ', 'vi' :'ヴィ', 've' :'ヴェ', 'vo' :'ヴォ'}

def file_read():
    file_path = tkinter.filedialog.askopenfilename(defaultextension=".ust", filetypes=[("Ust Files", "*.ust"), ("All Files", "*.*")])
    if len(file_path) != 0:
        data = file_path
    else:
        data = ''
    return data

def file_save():
    file_path = tkinter.filedialog.askdirectory()
    if len(file_path) != 0:
        savedir = file_path
    else:
        savedir = ''
    return savedir

def notenumabc(a):
    if a == "R":
        b = "R"
    else:
        b = utaupy.ust.notenum_as_abc(a)
    return b

def notenumhz(a):
    if a == "R":
        b = "R"
    else:
        b = math.pow(2,(int(a)-69)/12)*440
    return b

def hzlog(a):
    if a == "R":
        b = "R"
    else:
        b = math.log(float(a))
    return b

def kana(a):
    hiragana_pattern = re.compile("[ぁ-ゞ]+")
    b = hiragana_pattern.findall(a)
    b = "".join(b)
    if a == "R":
        b = "R"
    elif len(a)!=0 and len(b)==0:
        b = a
    elif a in kanahenkan:
        b = kanahenkan[a]
    return b

def table(notes, glbtempo):
    l0 = [d.get('Length') for d in notes]
    l0_2 = [d.get('Tempo') for d in notes]

    l0_3 = []
    k = str(glbtempo)
    for i in range(len(l0_2)):
        if l0_2[i] != None:
            k = l0_2[i]
        l0_3.append(k)
    print(l0_3)

    l1 = [d.get('NoteNum') for d in notes]
    l2 = [d.get('Lyric') for d in notes]
    l3 = ['{:.3f}'.format((int(l0[i])/480)*(60/float(l0_3[i]))) for i in range(len(l0))] #ノート長(四分音符=240)をsecに変換(小数点以下3桁)
    l4 = [notenumabc(d) for d in l1] #音階番号を音階へ
    l5 = [notenumhz(d) for d in l1] #音階番号を周波数へ
    l5_2 = ['{:.2f}'.format(d) for d in l5] 
    l6 = [hzlog(d) for d in l5]
    l6_2 = ['{:.3f}'.format(d) for d in l6] #VOICEVOX式高さへ(周波数の自然対数)
    
    return l0, l1, l2, l3, l4, l5_2, l6_2



class Application(tkinter.Tk):
    def __init__(self):
        super().__init__()

        self.title("USTtablizer")
        self.geometry("600x400")
        self.lylist = None
        self.querylist = []
        self.seqlist = []

        self.adjustlist = None
        self.queryblocklist = None
        self.query_data = None
        self.extlist = []
        self.exl = 0.100
        self.pitmax = 6.50
        self.pitmin = 3.00
        self.key = 0
        self.sid = 8

        ''' ここからメニュータブ用の仮のコマンド '''

        # Create a menubar
        self.menubar = tkinter.Menu(self)
        self.config(menu=self.menubar)

        # Create a File menu
        self.file_menu = tkinter.Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="ファイル", menu=self.file_menu)
        self.file_menu.add_command(label="新規プロジェクト", command=self.new_file)       
        self.file_menu.add_command(label="USTインポート", command=self.ust_import)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="プロジェクト読込", command=self.load_file) 
        self.file_menu.add_command(label="名前を付けて保存", command=self.save_file) 
        self.file_menu.add_separator()
        self.file_menu.add_command(label="終了", command=self.quit)

        self.soft_menu = tkinter.Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="USTtableizerについて", menu=self.soft_menu)
        self.soft_menu.add_command(label="クレジット", command=self.credit)

        '''仮コマンドは関数定義が下にまだある'''

        self.tree = ttk.Treeview(
            self, 
            columns=("sec", "読み", "高さ(VOICEVOX)", "音名", "高さ(Hz)"),
            show='headings',
            height=15  # Reduce the height of the treeview to make space for the scrollbar
        )

        self.tree.column("sec", width=100, anchor='center')
        self.tree.column("読み", width=100, anchor='center')
        self.tree.column("高さ(VOICEVOX)", width=100, anchor='center')
        self.tree.column("音名", width=100, anchor='center')
        self.tree.column("高さ(Hz)", width=100, anchor='center')

        self.tree.heading("sec", text='sec')
        self.tree.heading("読み", text='読み')
        self.tree.heading("高さ(VOICEVOX)", text='高さ(VOICEVOX)')
        self.tree.heading("音名", text='音名')
        self.tree.heading("高さ(Hz)", text='高さ(Hz)')

        self.tree.pack()

        self.vsb = ttk.Scrollbar(self, orient='vertical', command=self.tree.yview)

        # Pack the Treeview to the RIGHT and the Scrollbar to the RIGHT as well.
        self.tree.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=True)
        self.vsb.pack(side=tkinter.RIGHT, fill=tkinter.Y)

        # スクロールバーとTreeviewを連動させる設定
        self.tree.configure(yscrollcommand=self.vsb.set)
        self.vsb.configure(command=self.tree.yview)

    def new_file(self):
        #表示されたtableとlistたちの内容をすべてクリア
        self.lylist = None
        self.pilist = None
        self.lelist = None
        self.adjustlist = None
        self.queryblocklist = None
        self.querylist = []
        self.extlist = []
        self.exl = 0.100
        self.pitmax = 6.50
        self.pitmin = 3.00
        self.key = 0
        self.clear_table()

    def load_file(self):
        '''loadをうまくやる'''
        file_path = tkinter.filedialog.askopenfilename(defaultextension=".nsp", filetypes=[("Project Files", "*.nsp"), ("All Files", "*.*")])

        if file_path:
            with open(file_path, "r", encoding = "shift-JIS") as file:
                content = file.readlines()

            #ここからは文字列で保存されているプロジェクトファイルをリストに戻す
            for i in range(len(content)):
                content[i] = content[i].strip()

            adjustliststr = content[0:-9]
            al = []
            for i in range(len(adjustliststr)):
                a = ast.literal_eval(adjustliststr[i])
                al.append(a)
            self.adjustlist = al

            #load結果を表に直す
            alrev = al[::-1]
            for i in range(0, len(alrev)):
                self.tree.insert('', '0', values=(alrev[i][1],alrev[i][3],alrev[i][2],alrev[i][4],alrev[i][5]))


            queryblockliststr = content[-8]
            self.queryblocklist = ast.literal_eval(queryblockliststr)

            queryliststr = content[-7]
            self.querylist = ast.literal_eval(queryliststr)

            if self.querylist != None:
                for i in range(len(self.querylist)):
                    self.querylist[i] = ast.literal_eval(str(self.querylist[i]))

            extliststr = content[-6]
            self.extlist = ast.literal_eval(extliststr)

            self.exl = float(content[-5])

            self.pitmax = float(content[-4])

            self.pitmin = float(content[-3])

            self.key = float(content[-2])

            self.sid = int(content[-1])

            #print("Project successfully loaded from:", file_path)
        #print("Load file")

    def save_file(self):
        saver = ''
        if self.adjustlist == None:
            saver = saver + 'None' + '\n'
        else:
            for i in range(len(self.adjustlist)):
                saver = saver + str(self.adjustlist[i]) + '\n'

        if self.queryblocklist == None:
            saver = saver + 'None' + '\n'
        else:
            saver = saver + str(self.queryblocklist) + '\n' 

        if self.querylist == None:
            saver = saver + 'None' + '\n'
        else:
            saver = saver + str(self.querylist) + '\n'

        if self.extlist == []:
            saver = saver + '[]' + '\n'
        else:
            saver = saver + str(self.extlist) + '\n'

        saver = saver + str(self.exl) + '\n'

        saver = saver + str(self.pitmax) + '\n'

        saver = saver + str(self.pitmin) + '\n'

        saver = saver + str(self.key) + '\n'

        saver = saver + str(self.sid) 
        
        project_data = str(saver)
        file_path = tkinter.filedialog.asksaveasfilename(defaultextension=".nsp", filetypes=[("Project Files", "*.nsp"), ("All Files", "*.*")])

        if file_path:
            with open(file_path, "w", encoding = "shift-JIS") as file:
                file.write(project_data)
            #print("Project saved to:", file_path)

    def ust_import(self):
        data = file_read()
        filename = os.path.basename(data)
        self.title("USTtablizer - " + filename)
        self.new_file()
        x = utaupy.ust.load(data)
        xtempo = x.tempo
        xnotes = str(x.notes)

        et = table(x.notes, xtempo)

        l2_2 = [kana(d) for d in et[2]]

        self.lylist = l2_2
        self.pilist = et[6]
        self.lelist = et[3]

        et0 = et[0][::-1]
        et1 = et[1][::-1]
        et2_2 = l2_2[::-1]
        et3 = et[3][::-1]
        et4 = et[4][::-1]
        et5 = et[5][::-1]
        et6 = et[6][::-1]

        self.show_table(et3,et2_2,et6,et4,et5)

        self.show_message('最高音: ' + str(notenumabc(max(et[1]))) + '    ' + '{:.2f}'.format(notenumhz(max(et[1]))) + 'Hz    ' + str(max(et6)) + '\n最低音: '+ str(notenumabc(min(et[1]))) + '    ' + '{:.2f}'.format(notenumhz(min(et[1]))) + 'Hz    ' + str(min(et6)))

    def show_table(self,r1,r2,r3,r4,r5):
        for i in range(0, len(r1)):
            self.tree.insert('', '0', values=(r1[i], r2[i], r3[i], r4[i], r5[i]))

    def clear_table(self):
        for i in self.tree.get_children():
            self.tree.delete(i)

    def show_message(self, message):
        message_window = tkinter.Toplevel(self)
        message_window.title("メッセージ")
        message_window.geometry("400x100")

        message_label = tkinter.Label(message_window, text=message)
        message_label.pack(pady=20)

    def credit(self):
        self.show_message("VOICEVOX API - Hiroshiba様\nutaupy - oatsu-gh様\npy2exe for Python 3")


app = Application()

app.mainloop()
