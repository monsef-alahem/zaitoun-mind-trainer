'''
author  :   monsef alahem
email   :   m.alahem09@gmail.com
version :   1.0
start   :   12-01-2019

'''

import math
import os
import kivy
kivy.require("1.11.1")

from kivy.animation import Animation
from kivy.properties import NumericProperty

from datetime import date
from time import time
import threading
from random import randint


from kivy.app import App
from kivy.clock import Clock
from kivy.compat import string_types
from kivy.core.window import Window
from kivy.graphics import Color, Rectangle
from kivy.lang import Builder
from kivy.metrics import sp, dp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
from kivy.core.audio import SoundLoader
from kivy.uix.progressbar import ProgressBar


eng = 0
ar = 1



# taa
# ufe90 replaced by ufe8f
# dha
# ufec8 replaced by ufec5
# ta
# ufec2 replaced by ufec1



lang = {
'ok' : [u'ok', u'\ufed5\ufed3\ufe8d\ufeed\ufee3'],
'return' : [u'return', u'\ufec9\ufeed\ufe9f\ufead'],

'*Zaitoun mind trainer*' : [u'*Zaitoun mind trainer*', u'\u002a\ufee5\ufeed\ufe98\ufef3\ufeaf\ufedf\ufe8d\u0020\ufedd\ufed8\ufecc\ufedf\ufe8d\u0020\ufe8f\ufead\ufea9\ufee3\u002a'], #\u0029
'phone number game' : [u'phone number game', u'\ufed1\ufe97\ufe8e\ufeec\ufedf\ufe8d\u0020\ufee1\ufe8e\ufed7\ufead\ufe83\u0020\ufe94\ufe92\ufecc\ufedf'],
'say 20 ! lvl 1' : [u'say 20 ! lvl 1', u'\u0031\u0020\ufeef\ufeed\ufe98\ufeb4\ufee3\u0020\u0021\u0020\u0032\u0030\u0020\ufedd\ufed7'],
'say 20 ! lvl 2' : [u'say 20 ! lvl 2', u'\u0032\u0020\ufeef\ufeed\ufe98\ufeb4\ufee3\u0020\u0021\u0020\u0032\u0030\u0020\ufedd\ufed7'],
'this is the correct answer' : [u'this is the correct answer', u'\ufea2\ufef4\ufea4\ufebc\ufedf\ufe8d\u0020\ufe8f\ufe8d\ufeed\ufea0\ufedf\ufe8d\u0020\ufeed\ufeeb\u0020\ufe8d\ufeab\ufeeb'],
'score: 0/0' : [u'score: 0/0', u'\u0030\u005c\u0030\u0020\u003a\u0020\ufec1\ufed8\ufee8\ufedf\ufe8d'],
'player: 0' : [u'player: 0', u'\u0030\u0020\u003a\u0020\ufe8f\ufecb\ufefb\ufe8d'],
'clean' : [u'clean', u'\ufecd\ufe8d\ufead\ufed3\ufe87'],
'cpu: 0' : [u'cpu: 0', u'\u0030\u0020\u003a\u0020\ufe9e\ufedf\ufe8e\ufecc\ufee4\ufedf\ufe8d']
}

    # ProgressBar:
    #     id: pb
    #     size_hint: (1, .04)
    #     pos_hint: {'x':.0, 'y':.93}
    #     height: '92dp'
    #     value: 0


            # font_size: 40
            # color: 1, 1, 0, 1



#build app with kv language
cvrt = '''
#: import lang __main__.lang

#: import ar __main__.ar
#: import eng __main__.eng

<Zaitoun>:

    #menu
    FloatLayout:
        id: menu
        text: 'menu'
        # position and size to the parent, root in this case
        size_hint: (1, 1)
        pos_hint: {'x':0, 'y':.0}
        orientation: 'vertical'
        #opacity: 1 if root.ismenu else 0
        # Image:
        #     source: 'bg.png'
        #     # color: .2, .2, .2, .4
        #     allow_stretch: True



        canvas:
            Rectangle:
                pos: self.pos
                size: self.size
                source: 'bg.png'
    
        BoxLayout:
            id: logo
            pos_hint: {'x':.35, 'y':.72}
            size_hint: (.30, .30)
            Image:
                source: 'zaitoun.png'



        Label:
            id: title
            text: lang['*Zaitoun mind trainer*'][ar]
            font_name: 'arial.ttf'
            size_hint: (.66, .2)
            pos_hint: {'x':.17, 'y':.85}
            font_size: 40
            color: 1, 1, 0, 1

        Button:
            text: lang['phone number game'][ar]
            font_name: 'arial.ttf'
            size_hint: (.4, .1)
            pos_hint: {'x':.3, 'y':.66}
            on_press: root.attach_kb()
            on_press: root.goto_layout(phone_number)
            on_press: root.timer_start()
        Button:
            text: lang['say 20 ! lvl 1'][ar]
            font_name: 'arial.ttf'
            size_hint: (.4, .1)
            pos_hint: {'x':.3, 'y':.54}
            on_press: root.goto_layout(say_20_l1)
        Button:
            text: lang['say 20 ! lvl 2'][ar]
            font_name: 'arial.ttf'
            size_hint: (.4, .1)
            pos_hint: {'x':.3, 'y':.42}
            on_press: root.goto_layout(say_20_l2)
        # Button:
        #     text: 'mirath calculator'
        #     size_hint: (.4, .1)
        #     pos_hint: {'x':.3, 'y':.42}
        #     # on_press: root.goto_layout(date)
        # Button:
        #     text: 'zakat calculator'
        #     size_hint: (.4, .1)
        #     pos_hint: {'x':.3, 'y':.3}
        #     # on_press: root.goto_layout(date)


        Button:
            id: langage_btn
            text: 'eng'
            font_size: 30
            disabled: True
            background_color: 0,2,1,1
            size_hint: (.2, .1)
            pos_hint: {'x':.4, 'y':.08}
            on_press: root.change_langage()















# phone number page
    FloatLayout:
        size_hint: (1, 1)
        pos_hint: {'x':0, 'y':.0}
        id: phone_number
        # orientation: 'horizentale'



        canvas:
            Rectangle:
                pos: self.pos
                size: self.size
                source: 'bg.png'

        ProgressBar:
            id: pb
            size_hint: (.8, .05)
            pos_hint: {'x':.1, 'y':.90}
            orientation: 'horizontal'
            value: 0

        BoxLayout:
            id: mnemonique
            size_hint: (1, .05)
            pos_hint: {'x':0, 'y':.70}
            orientation: 'horizontal'
            # orientation: 'vertical'
            # Button:
            #     text: 'return'
            #     background_color: 0,2,1,1
            #     on_press: root.goto_layout(menu)

        BoxLayout:
            id: numbers
            size_hint: (1, .05)
            pos_hint: {'x':0, 'y':.80}
            orientation: 'horizontal'
            # Button:
            #     text: 'return'
            #     background_color: 0,2,1,1
            #     on_press: root.goto_layout(menu)

        Label:
            id: message
            text: lang['this is the correct answer'][ar]
            font_name: 'arial.ttf'
            font_size: 30
            # font_name: 'Roboto'
            size_hint: (1, .05)
            pos_hint: {'x':0, 'y':.40}
            opacity: 0



        Button:
            id: ret_phone_btn
            font_name: 'arial.ttf'
            # font_name: 'Roboto'
            text: lang['return'][ar]
            #background_color: 0,2,1,1
            size_hint: (.2, .1)
            pos_hint: {'x':.7, 'y':.08}
            on_press: root.goto_layout(menu)
            on_press: root.detach_kb()

        # Button:
        #     size_hint: (.2, .1)
        #     pos_hint: {'x':.4, 'y':.3}
        #     text: 'answer'
        #     on_press: root.check_answer()

        # ScreenLabel:
        #     id: number_answer
        #     text: '0666454237'
        #     size_hint: (.4, .1)
        #     pos_hint: {'x':.3, 'y':.4}

        Label:
            id: score
            text: lang['score: 0/0'][ar]
            font_name: 'arial.ttf'
            font_size: 40
            size_hint: (.2, .1)
            pos_hint: {'x':.7, 'y':.9}










# say 20 lvl 1
    FloatLayout:
        id: say_20_l1
        size_hint: (1, 1)
        pos_hint: {'x':0, 'y':.0}
        # orientation: 'horizentale'



        canvas:
            Rectangle:
                pos: self.pos
                size: self.size
                source: 'bg.png'


        Button:
            id: ret_say20_l1_btn
            font_name: 'arial.ttf'
            # font_name: 'Roboto'
            text: lang['return'][ar]
            #background_color: 0,2,1,1
            size_hint: (.2, .1)
            pos_hint: {'x':.7, 'y':.08}
            on_press: root.goto_layout(menu)
            on_press: root.detach_kb()

        Label:
            id: score_player_say20_l1
            font_size: 40
            text: lang['player: 0'][ar]
            font_name: 'arial.ttf'
            size_hint: (.2, .1)
            pos_hint: {'x':.7, 'y':.9}

        Label:
            id: score_cpu_say20_l1
            font_size: 40
            text: lang['cpu: 0'][ar]
            font_name: 'arial.ttf'
            size_hint: (.2, .1)
            pos_hint: {'x':.1, 'y':.9}


        Label:
            id: number_say20_l1
            text: '0'
            font_size: 70
            size_hint: (.2, .1)
            pos_hint: {'x':.4, 'y':.7}

        Label:
            id: operation_say20_l1
            text: ''
            size_hint: (.2, .1)
            pos_hint: {'x':.5, 'y':.7}
            font_size: 40
            color: 1, 1, 0, .5

        Button:
            id: plus1_l1
            font_size: 40
            # font_name: 'arial.ttf'
            # font_name: 'Roboto'
            text: u'+ 1'
            #background_color: 0,2,1,1
            size_hint: (.2, .1)
            pos_hint: {'x':.2, 'y':.5}
            on_press: root.increase_by1_l1()

        Button:
            id: plus2_l1
            font_size: 40
            # font_name: 'arial.ttf'
            # font_name: 'Roboto'
            text: u'+ 2'
            #background_color: 0,2,1,1
            size_hint: (.2, .1)
            pos_hint: {'x':.6, 'y':.5}
            on_press: root.increase_by2_l1()









# say 20 lvl 2
    FloatLayout:
        id: say_20_l2
        size_hint: (1, 1)
        pos_hint: {'x':0, 'y':.0}
        # orientation: 'horizentale'



        canvas:
            Rectangle:
                pos: self.pos
                size: self.size
                source: 'bg.png'
                

        Button:
            id: ret_say20_l2_btn
            font_name: 'arial.ttf'
            # font_name: 'Roboto'
            text: lang['return'][ar]
            #background_color: 0,2,1,1
            size_hint: (.2, .1)
            pos_hint: {'x':.7, 'y':.08}
            on_press: root.goto_layout(menu)
            on_press: root.detach_kb()

        Label:
            id: score_player_say20_l2
            font_size: 40
            text: lang['player: 0'][ar]
            font_name: 'arial.ttf'
            size_hint: (.2, .1)
            pos_hint: {'x':.7, 'y':.9}

        Label:
            id: score_cpu_say20_l2
            font_size: 40
            text: lang['cpu: 0'][ar]
            font_name: 'arial.ttf'
            size_hint: (.2, .1)
            pos_hint: {'x':.1, 'y':.9}


        Label:
            id: number_say20_l2
            text: '0'
            font_size: 70
            size_hint: (.2, .1)
            pos_hint: {'x':.4, 'y':.7}

        Label:
            id: operation_say20_l2
            text: ''
            size_hint: (.2, .1)
            pos_hint: {'x':.5, 'y':.7}
            font_size: 40
            color: 1, 1, 0, .5

        Button:
            id: plus1_l2
            font_size: 40
            # font_name: 'arial.ttf'
            # font_name: 'Roboto'
            text: u'+ 1'
            #background_color: 0,2,1,1
            size_hint: (.2, .1)
            pos_hint: {'x':.1, 'y':.5}
            on_press: root.increase_by1_l2()

        Button:
            id: plus2_l2
            font_size: 40
            # font_name: 'arial.ttf'
            # font_name: 'Roboto'
            text: u'+ 2'
            #background_color: 0,2,1,1
            size_hint: (.2, .1)
            pos_hint: {'x':.4, 'y':.5}
            on_press: root.increase_by2_l2()

        Button:
            id: plus3_l2
            font_size: 40
            # font_name: 'arial.ttf'
            # font_name: 'Roboto'
            text: u'+ 3'
            #background_color: 0,2,1,1
            size_hint: (.2, .1)
            pos_hint: {'x':.7, 'y':.5}
            on_press: root.increase_by3_l2()







#idea : set pointer to a widget then attach kb

    FloatLayout:
        id: keyboard
        ScreenLabel:
            id: kb_val
            font_size: 40
            size_hint: (.6, 0.09)
            pos_hint: {'x':.2, 'y':.6}
            text: ''
        GridLayout:
            id: kb
            size_hint: (.6, .40)
            pos_hint: {'x':.2, 'y':.2}
            rows: 6

            Button:
                text: u'1'
                on_press: root.enter_number(kb_val, 1)
            Button:
                text: u'2'
                on_press: root.enter_number(kb_val, 2)
            Button:
                text: u'3'
                on_press: root.enter_number(kb_val, 3)

            Button:
                text: u'4'
                on_press: root.enter_number(kb_val, 4)
            Button:
                text: u'5'
                on_press: root.enter_number(kb_val, 5)
            Button:
                text: u'6'
                on_press: root.enter_number(kb_val, 6)

            Button:
                text: u'7'
                on_press: root.enter_number(kb_val, 7)
            Button:
                text: u'8'
                on_press: root.enter_number(kb_val, 8)
            Button:
                text: u'9'
                on_press: root.enter_number(kb_val, 9)

            Button:
                text: u'<-'
                #on_press: kb_val.text = ''
                on_press: kb_val.text = kb_val.text[:-1]
            Button:
                text: u'0'
                on_press: root.enter_number(kb_val, 0)
            Button:
                id: goto_page_btn
                font_name: 'arial.ttf'
                text: lang['ok'][ar]
                on_press: root.check_answer()
                # on_press: root.convert(kb_val)

            Label:
                opacity:0

            Button:
                text: lang['clean'][ar]
                font_name: 'arial.ttf'
                on_press: kb_val.text = ''
                #on_press: kb_val.text = kb_val.text[:-1]

            Label:
                opacity:0

    



'''





# Builder.load_string(kbrd, filename ="kbrd.kv")
Builder.load_string(cvrt, filename ="cvrt.kv")

# Builder.unload_file("cvrt.kv")
# Builder.unload_file("kbrd.kv")


generated_number = "0000000000"
last_time = time()


# class Keyboard(Popup):
#     target_widget = None

#     def __init__(self, target_widget, **kwargs):
#         super(Keyboard, self).__init__(**kwargs)
#         self.target_widget = target_widget

#     def enter_number(self, kb_val, number):
#         kb_val.text += (str)(number)
#         # if len(kb_val.text) == 2 or len(kb_val.text) == 5:
#         #     kb_val.text += (str)('-')

#     def validate(self, value):
#         self.target_widget.text = value
#         self.dismiss()




#custom label with solid background
class ZaitounLabel(Label):

    image = ''

    def __init__(self, image, **kwargs):
        super(ZaitounLabel, self).__init__(**kwargs)
        self.image = image

    def on_size(self, *args):
        self.canvas.before.clear()
        with self.canvas.before:
            Color(1.0, 1.0, 1.0, 1)
            Rectangle(pos= self.pos, size= self.size, source= self.image)

#same here with black color
class ScreenLabel(Label):
    def on_size(self, *args):
        self.canvas.before.clear()
        with self.canvas.before:
            Color(0, 0, 0, 1)
            Rectangle(pos=self.pos, size=self.size)

class Zaitoun(FloatLayout):

    isfirsttime = 1
    current_layout = None
    show_answer = True
    score = 0
    tries = 0

    number_say20_l1 = 0
    score_cpu_say20_l1 = 0
    score_player_say20_l1 = 0

    number_say20_l2 = 0
    score_cpu_say20_l2 = 0
    score_player_say20_l2 = 0

    operator_opacity = 1.
    isstop = True
    timer_val = 0

    
    #ti = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(Zaitoun, self).__init__(**kwargs)
        

    def timer_reset(self):
        global last_time
        self.ids.pb.value = 0
        last_time = time()
        # self.timer_val = time() - last_time


    def timer_start(self):
        self.isstop = False
        self.timer_reset()

    def timer_stop(self):
        self.isstop = True


    def update(self, dt):
        global last_time


        if self.isfirsttime:
            self.current_layout = self.ids.menu
            # p = Keyboard(self)
            # p.open()
            # p.dismiss()
            self.clear_widgets()
            self.add_widget(self.ids.menu)
            # genrated_number = ['0','6','6','6','4','5','4','2','3','7']
            global generated_number
            # generated_number = '0666454237'
            generated_number = ''
            self.generate_number()
            # print(self.ids.ret_phone_btn.font_name)

            self.isfirsttime = 0
        # self.ids.operation_say20.color = (1, 1, 0, self.operator_opacity)
        # print(self.operator_opacity)
        
        if self.isstop == False:
            self.timer_val = time() - last_time
            self.ids.pb.value = self.timer_val * 100 / 30
            if self.ids.pb.value == 100:
                self.detach_ans()







    #functions for buttons


    # def show_kb(self):
    #     if not self.iskb:
    #         self.ids.kb.opacity = 1
    #         self.ids.kb.size_hint_x = .6
    #         self.iskb = 1

    # def hide_kb(self):
    #     if self.iskb:
    #         self.ids.kb.opacity = 0
    #         self.ids.kb.size_hint_x = .0
    #         self.iskb = 0

    def goto_layout(self, layout):
        self.remove_widget(self.current_layout)
        self.current_layout = layout
        self.add_widget(self.current_layout)

        self.ids.kb_val.canvas.before.clear()
        with self.ids.kb_val.canvas.before:
            Color(0, 0, 0, 1)
            Rectangle(pos=self.ids.kb_val.pos, size=self.ids.kb_val.size)

    def disable_kb(self):
        l = len(self.ids.kb.children)
        for i in range(l):
            self.ids.kb.children[i].disabled = True
    def enable_kb(self):
        l = len(self.ids.kb.children)
        for i in range(l):
            self.ids.kb.children[i].disabled = False

    def attach_kb(self):
        self.add_widget(self.ids.keyboard)
        # self.add_widget(self.ids.keyboard, len(self.children))
    def detach_kb(self):
        self.remove_widget(self.ids.keyboard)
    
    def attach_ans(self):
        if not self.show_answer:
            self.ids.phone_number.add_widget(self.ids.numbers)
            self.ids.phone_number.add_widget(self.ids.mnemonique)
            self.show_answer = True
    def detach_ans(self):
        if self.show_answer:
            self.ids.phone_number.remove_widget(self.ids.numbers)
            self.ids.phone_number.remove_widget(self.ids.mnemonique)
            self.show_answer = False




    def enter_number(self, page_val, number):
        page_val.text += (str)(number)
        self.detach_ans()
        if len(page_val.text) == 10:
            page_val.color = 0,1,0,1
        # if len(page_val.text) == 2 or len(page_val.text) == 5:
        #     page_val.text += (str)('-')



    # def show_popup(self, target_widget):
    #     p = Keyboard(target_widget)
    #     p.open()












    def auto_destruct(self, instance):
        if self.isdelete :
            converted_date.pop(int(instance.id))
            self.ids.hist_box.remove_widget(instance)
            print(instance.id + ' deleted')

    def activate_delete(self):
        if self.isdelete:
            self.isdelete = 0
            self.ids.delete_btn.background_color = 1,1,1,1
        else :
            self.isdelete = 1
            self.ids.delete_btn.background_color = 3,0,0,1


    def check_answer(self):
        self.attach_ans()
        na = self.ids.kb_val
        global generated_number
        # print(generated_number)
        # print(na.text)
        self.timer_reset()
        if na.text == generated_number:
            self.score += 1
            self.tries += 1
            self.load_next_question(0)
        else:
            self.tries += 1
            self.disable_kb()
            self.ids.message.opacity = 1
            Clock.schedule_once(self.load_next_question, 5.)
        # self.ids.score.text = "score : " + str(self.score) + "/" + str(self.tries)
        self.ids.score.text = str(self.tries) + "/" + str(self.score) + u'\u0020\u003a\u0020\ufec1\ufed8\ufee8\ufedf\ufe8d'

    def load_next_question(self,dt):
        # randint()
        self.timer_start()
        global generated_number
        generated_number = ''
        self.generate_number()
        self.enable_kb()
        self.ids.message.opacity = 0
        self.attach_ans()
        self.ids.kb_val.text = ''
        self.ids.kb_val.color = 1,1,1,1

    def generate_number(self):
        global generated_number
        for n in range(10):
            generated_number += str(randint(0,9))
        self.ids.mnemonique.clear_widgets()
        for i in range(len(generated_number)):
            tmp = generated_number[i] + ".png"
            lbl = ZaitounLabel(tmp)
            self.ids.mnemonique.add_widget(lbl)

        self.ids.numbers.clear_widgets()
        for i in range(len(generated_number)):
            tmp = "n" + generated_number[i] + ".png"
            lbl = ZaitounLabel(tmp)
            self.ids.numbers.add_widget(lbl)



#============================ lvl 1 ===================================


    def increase_by1_l1(self):
        self.ids.plus1_l1.disabled = True
        self.ids.plus2_l1.disabled = True
        self.number_say20_l1 += 1
        self.ids.number_say20_l1.text = str(self.number_say20_l1)
        if self.number_say20_l1 >= 20:
            self.ids.plus2_l1.disabled = True
            self.ids.plus1_l1.disabled = True
            self.score_player_say20_l1 += 1
            # self.ids.score_player_say20_l1.text = 'player : ' + str(self.score_player_say20_l1)
            self.ids.score_player_say20_l1.text = str(self.score_player_say20_l1) + u'\u0020\u003a\u0020\ufe8f\ufecb\ufefb\ufe8d'
            Clock.schedule_once(self.reset_say20_l1, 1.)
            return
        
        Clock.schedule_once(self.think_response_l1, .3)

    def increase_by2_l1(self):
        self.ids.plus1_l1.disabled = True
        self.ids.plus2_l1.disabled = True
        self.number_say20_l1 += 2
        self.ids.number_say20_l1.text = str(self.number_say20_l1)
        if self.number_say20_l1 >= 20:
            self.ids.plus1_l1.disabled = True
            self.ids.plus2_l1.disabled = True
            self.score_player_say20_l1 += 1
            self.ids.score_player_say20_l1.text = str(self.score_player_say20_l1)  + u'\u0020\u003a\u0020\ufe8f\ufecb\ufefb\ufe8d'
            Clock.schedule_once(self.reset_say20_l1, 1.)
            return
        # self.think_response(dt = 0)
        Clock.schedule_once(self.think_response_l1, .4)





#============================ lvl 2 ===================================

    def increase_by1_l2(self):
        self.ids.plus1_l2.disabled = True
        self.ids.plus2_l2.disabled = True
        self.ids.plus3_l2.disabled = True
        self.number_say20_l2 += 1
        self.ids.number_say20_l2.text = str(self.number_say20_l2)
        if self.number_say20_l2 >= 20:
            self.ids.plus1_l2.disabled = True
            self.ids.plus2_l2.disabled = True
            self.ids.plus3_l2.disabled = True
            self.score_player_say20_l2 += 1
            # self.ids.score_player_say20_l2.text = 'player : ' + str(self.score_player_say20_l2)
            self.ids.score_player_say20_l2.text = str(self.score_player_say20_l2) + u'\u0020\u003a\u0020\ufe8f\ufecb\ufefb\ufe8d'
            Clock.schedule_once(self.reset_say20_l2, 1.)
            return
        
        Clock.schedule_once(self.think_response_l2, .3)


    def increase_by2_l2(self):
        self.ids.plus1_l2.disabled = True
        self.ids.plus2_l2.disabled = True
        self.ids.plus3_l2.disabled = True
        self.number_say20_l2 += 2
        self.ids.number_say20_l2.text = str(self.number_say20_l2)
        if self.number_say20_l2 >= 20:
            self.ids.plus1_l2.disabled = True
            self.ids.plus2_l2.disabled = True
            self.ids.plus3_l2.disabled = True
            self.score_player_say20_l2 += 1
            # self.ids.score_player_say20_l2.text = 'player : ' + str(self.score_player_say20_l2)
            self.ids.score_player_say20_l2.text = str(self.score_player_say20_l2) + u'\u0020\u003a\u0020\ufe8f\ufecb\ufefb\ufe8d'
            Clock.schedule_once(self.reset_say20_l2, 1.)
            return
        # self.think_response(dt = 0)
        Clock.schedule_once(self.think_response_l2, .4)


    def increase_by3_l2(self):
        self.ids.plus1_l2.disabled = True
        self.ids.plus2_l2.disabled = True
        self.ids.plus3_l2.disabled = True
        self.number_say20_l2 += 3
        self.ids.number_say20_l2.text = str(self.number_say20_l2)
        if self.number_say20_l2 >= 20:
            self.ids.plus1_l2.disabled = True
            self.ids.plus2_l2.disabled = True
            self.ids.plus3_l2.disabled = True
            self.score_player_say20_l2 += 1
            # self.ids.score_player_say20_l2.text = 'player : ' + str(self.score_player_say20_l2)
            self.ids.score_player_say20_l2.text = str(self.score_player_say20_l2) + u'\u0020\u003a\u0020\ufe8f\ufecb\ufefb\ufe8d'
            Clock.schedule_once(self.reset_say20_l2, 1.)
            return
        # self.think_response(dt = 0)
        Clock.schedule_once(self.think_response_l2, .4)













    def think_response_l1(self,dt):
        tmp = 0
        if self.number_say20_l1 % 3 == 0:
            tmp = 2
        elif self.number_say20_l1 % 3 == 1:
            tmp = 1
        elif self.number_say20_l1 % 3 == 2:
            tmp = randint(1, 2)
        self.number_say20_l1 += tmp
        self.ids.number_say20_l1.text = str(self.number_say20_l1)
        self.ids.operation_say20_l1.text = '+' + str(tmp)
        self.ids.operation_say20_l1.color = (1,1,0,1)
        self.ids.operation_say20_l1.font_size = 70
        self.ids.plus1_l1.disabled = False  
        self.ids.plus2_l1.disabled = False  

        if self.number_say20_l1 >= 20:
            self.ids.plus1_l1.disabled = True
            self.ids.plus2_l1.disabled = True
            self.score_cpu_say20_l1 += 1
            # self.ids.score_cpu_say20_l1.text = 'cpu : ' + str(self.score_cpu_say20_l1)
            self.ids.score_cpu_say20_l1.text = str(self.score_cpu_say20_l1) + u'\u0020\u003a\u0020\ufe9e\ufedf\ufe8e\ufecc\ufee4\ufedf\ufe8d'
            Clock.schedule_once(self.reset_say20_l1, 1.)
        # Clock.schedule_once(self.fade_operator, .0)
        self.fade_operator(self.ids.operation_say20_l1)

# 16 12 8 4 
    def think_response_l2(self,dt):
        tmp = 0
        if self.number_say20_l2 % 4 == 0:
            tmp = randint(1, 3)
        elif self.number_say20_l2 % 4 == 1:
            tmp = 3
        elif self.number_say20_l2 % 4 == 2:
            tmp = 2
        elif self.number_say20_l2 % 4 == 3:
            tmp = 1
        self.number_say20_l2 += tmp
        self.ids.number_say20_l2.text = str(self.number_say20_l2)
        self.ids.operation_say20_l2.text = '+' + str(tmp)
        self.ids.operation_say20_l2.color = (1,1,0,1)
        self.ids.operation_say20_l2.font_size = 70
        self.ids.plus1_l2.disabled = False  
        self.ids.plus2_l2.disabled = False  
        self.ids.plus3_l2.disabled = False  

        if self.number_say20_l2 >= 20:
            self.ids.plus1_l2.disabled = True
            self.ids.plus2_l2.disabled = True
            self.ids.plus3_l2.disabled = True
            self.score_cpu_say20_l2 += 1
            # self.ids.score_cpu_say20_l2.text = 'cpu : ' + str(self.score_cpu_say20_l2)
            self.ids.score_cpu_say20_l2.text = str(self.score_cpu_say20_l2) + u'\u0020\u003a\u0020\ufe9e\ufedf\ufe8e\ufecc\ufee4\ufedf\ufe8d'
            Clock.schedule_once(self.reset_say20_l2, 1.)
        # Clock.schedule_once(self.fade_operator, .0)
        self.fade_operator(self.ids.operation_say20_l2)




# def think_response(self,dt):
#         tmp = 0
#         if self.number_say20_l2 % 3 == 0:
#             tmp = 2
#         elif self.number_say20_l2 % 3 == 1:
#             tmp = 1
#         elif self.number_say20_l2 % 3 == 2:
#             tmp = randint(1, 2)
#         self.number_say20_l2 += tmp
#         self.ids.number_say20_l2.text = str(self.number_say20_l2)
#         self.ids.operation_say20_l2.text = '+' + str(tmp)
#         self.ids.operation_say20_l2.color = (1,1,0,1)
#         self.ids.operation_say20_l2.font_size = 70
#         self.ids.plus1.disabled = False  
#         self.ids.plus2.disabled = False  

#         if self.number_say20_l2 >= 20:
#             self.ids.plus1.disabled = True
#             self.ids.plus2.disabled = True
#             self.score_cpu_say20_l2 += 1
#             self.ids.score_cpu_say20_l2.text = 'cpu : ' + str(self.score_cpu_say20_l2)
#             Clock.schedule_once(self.reset_say20_l2, 1.)
#         # Clock.schedule_once(self.fade_operator, .0)
#         self.fade_operator(self.ids.operation_say20_l2)

#     # def fade_operator(self):
#     #     self.operator_opacity = 0
#     #     anim = Animation(operator_opacity=self.operator_opacity, duration= 10)
#     #     anim.start(self)
#     #     # while tmp > 0.:
#     #     #     tmp -= 0.000001
#     #     #     self.ids.operation_say20.color = (1, 1, 0, tmp)
#     #     self.ids.operation_say20.color = (1, 1, 0, self.operator_opacity)
#     #     self.ids.operation_say20.font_size = 70




    def reset_say20_l1(self, dt):
        self.number_say20_l1 = 0
        self.ids.number_say20_l1.text = str(self.number_say20_l1)
        self.fade_operator(self.ids.number_say20_l1)
        Clock.schedule_once(self.appear_operator_l1, 1.)
        tmp = randint(0,1)
        # if tmp == 1:
        #     Clock.schedule_once(self.think_response_l1, 1.)


    def reset_say20_l2(self, dt):
        self.number_say20_l2 = 0
        self.ids.number_say20_l2.text = str(self.number_say20_l2)
        self.fade_operator(self.ids.number_say20_l2)
        Clock.schedule_once(self.appear_operator_l2, 1.)
        tmp = randint(0,1)
        if tmp == 1:
            Clock.schedule_once(self.think_response_l2, 1.)


    def fade_operator(self, wdg):
        anim = Animation(color=(1,1,0,0),font_size = 100, duration= 1)
        anim.start(wdg)
    
    def appear_operator_l1(self, dt):
        wdg = self.ids.number_say20_l1
        anim = Animation(color=(1,1,1,1),font_size = 70, duration= .5)
        anim.start(wdg)
        self.ids.plus1_l1.disabled = False
        self.ids.plus2_l1.disabled = False

    def appear_operator_l2(self, dt):
        wdg = self.ids.number_say20_l2
        anim = Animation(color=(1,1,1,1),font_size = 70, duration= .5)
        anim.start(wdg)
        self.ids.plus1_l2.disabled = False
        self.ids.plus2_l2.disabled = False
        self.ids.plus3_l2.disabled = False


    # def fade_operator(self, wdg):
    #     anim = Animation(color=(1,1,0,0),font_size = 100, duration= 1)
    #     anim.start(self.ids.operation_say20)




class ZaitounApp(App):

    #window object of the app
    global Window
    #principal widget of the app
    global wdg
    needle_angle = NumericProperty(0)

    _anim = None


    def build(self):
        Window.set_title('Zaitoun')
        self.title = 'Zaitoun'
        self.icon = 'Zaitoun.png'
        self.wdg = Zaitoun(size= Window.size)
        main_wdg = self.wdg 
        
    # initializing graphic objects that can't be on kv language

        Clock.schedule_interval(main_wdg.update, 1.0 / 30.0)
        # Clock.schedule_interval(self.update, 1.0 / 30.0)
        return main_wdg



    # def update():
    #     self.needle_angle = 134


    #when user exit the app auto-save his session
    def on_stop(self):
        pass

if __name__ == '__main__':
    ZaitounApp().run()
