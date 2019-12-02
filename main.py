'''
author  :   monsef alahem
email   :   m.alahem09@gmail.com
version :   1.0
start   :   09-08-2019

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
    
        BoxLayout:
            id: logo
            pos_hint: {'x':.35, 'y':.72}
            size_hint: (.30, .30)
            Image:
                source: 'zaitoun.png'



        Label:
            id: title
            #font_name: 'arial.ttf'
            text: "*Zaitoun mind trainer*" #utf code mean menu in arabic
            size_hint: (.66, .2)
            pos_hint: {'x':.17, 'y':.85}
            font_size: 40
            color: 1, 1, 0, 1

        Button:
            text: 'phone number game'
            size_hint: (.4, .1)
            pos_hint: {'x':.3, 'y':.66}
            on_press: root.goto_layout(phone_number)
            on_press: root.timer_start()
            on_press: root.attach_kb()
        Button:
            text: 'say 20 !'
            size_hint: (.4, .1)
            pos_hint: {'x':.3, 'y':.54}
            on_press: root.goto_layout(say_20)
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


        Button:
            id: ret_phone_btn
            # font_name: 'arial.ttf'
            font_name: 'Roboto'
            text: u'return'
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

        ScreenLabel:
            id: score
            text: 'score: 0/0'
            font_size: 40
            size_hint: (.2, .1)
            pos_hint: {'x':.7, 'y':.9}










# say 20
    FloatLayout:
        size_hint: (1, 1)
        pos_hint: {'x':0, 'y':.0}
        id: say_20
        # orientation: 'horizentale'




        Button:
            id: ret_say20_btn
            # font_name: 'arial.ttf'
            font_name: 'Roboto'
            text: u'return'
            #background_color: 0,2,1,1
            size_hint: (.2, .1)
            pos_hint: {'x':.7, 'y':.08}
            on_press: root.goto_layout(menu)
            on_press: root.detach_kb()

        ScreenLabel:
            id: score_player_say20
            font_size: 40
            text: 'player: 0'
            size_hint: (.2, .1)
            pos_hint: {'x':.7, 'y':.9}

        ScreenLabel:
            id: score_cpu_say20
            font_size: 40
            text: 'cpu: 0'
            size_hint: (.2, .1)
            pos_hint: {'x':.1, 'y':.9}


        ScreenLabel:
            id: number_say20
            text: '0'
            font_size: 70
            size_hint: (.2, .1)
            pos_hint: {'x':.4, 'y':.7}

        ScreenLabel:
            id: operation_say20
            text: ''
            size_hint: (.2, .1)
            pos_hint: {'x':.5, 'y':.7}
            font_size: 40
            color: 1, 1, 0, .5

        Button:
            id: plus1
            font_size: 40
            # font_name: 'arial.ttf'
            font_name: 'Roboto'
            text: u'+ 1'
            #background_color: 0,2,1,1
            size_hint: (.2, .1)
            pos_hint: {'x':.2, 'y':.5}
            on_press: root.increase_by1()

        Button:
            id: plus2
            font_size: 40
            # font_name: 'arial.ttf'
            font_name: 'Roboto'
            text: u'+ 2'
            #background_color: 0,2,1,1
            size_hint: (.2, .1)
            pos_hint: {'x':.6, 'y':.5}
            on_press: root.increase_by2()









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
                #font_name: 'arial.ttf'
                #text: u'ok'#means done in arabic
                text: 'ok'
                on_press: root.check_answer()
                # on_press: root.convert(kb_val)

            ScreenLabel:
                opacity:0

            Button:
                text: u'clean'
                on_press: kb_val.text = ''
                #on_press: kb_val.text = kb_val.text[:-1]

            ScreenLabel:
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
    number_say20 = 0
    score_cpu_say20 = 0
    score_player_say20 = 0
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

    def attach_kb(self):
        self.add_widget(self.ids.keyboard)
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
        na = self.ids.kb_val
        global generated_number
        # print(generated_number)
        # print(na.text)
        if na.text == generated_number:
            self.attach_ans()
            self.score += 1
            self.tries += 1
            self.load_next_question()
        else:
            self.attach_ans()
            self.tries += 1
            Clock.schedule_once(self.load_next_question, 2.)
        self.ids.score.text = "score : " + str(self.score) + "/" + str(self.tries)
        self.ids.kb_val.text = ''

    def load_next_question(self, dt):
        # randint()
        self.timer_start()
        global generated_number
        generated_number = ''
        self.generate_number()

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

    def increase_by1(self):
        self.ids.plus1.disabled = True
        self.ids.plus2.disabled = True
        self.number_say20 += 1
        self.ids.number_say20.text = str(self.number_say20)
        if self.number_say20 >= 20:
            self.ids.plus2.disabled = True
            self.ids.plus1.disabled = True
            self.score_player_say20 += 1
            self.ids.score_player_say20.text = 'player : ' + str(self.score_player_say20)
            Clock.schedule_once(self.reset_say20, 1.)
            return
        
        Clock.schedule_once(self.think_response, .3)

    def increase_by2(self):
        self.ids.plus1.disabled = True
        self.ids.plus2.disabled = True
        self.number_say20 += 2
        self.ids.number_say20.text = str(self.number_say20)
        if self.number_say20 >= 20:
            self.ids.plus1.disabled = True
            self.ids.plus2.disabled = True
            self.score_player_say20 += 1
            self.ids.score_player_say20.text = 'player : ' + str(self.score_player_say20)
            Clock.schedule_once(self.reset_say20, 1.)
            return
        # self.think_response(dt = 0)
        Clock.schedule_once(self.think_response, .4)


    def think_response(self,dt):
        tmp = 0
        if self.number_say20 % 3 == 0:
            tmp = 2
        elif self.number_say20 % 3 == 1:
            tmp = 1
        elif self.number_say20 % 3 == 2:
            tmp = randint(1, 2)
        self.number_say20 += tmp
        self.ids.number_say20.text = str(self.number_say20)
        self.ids.operation_say20.text = '+' + str(tmp)
        self.ids.operation_say20.color = (1,1,0,1)
        self.ids.operation_say20.font_size = 70
        self.ids.plus1.disabled = False  
        self.ids.plus2.disabled = False  

        if self.number_say20 >= 20:
            self.ids.plus1.disabled = True
            self.ids.plus2.disabled = True
            self.score_cpu_say20 += 1
            self.ids.score_cpu_say20.text = 'cpu : ' + str(self.score_cpu_say20)
            Clock.schedule_once(self.reset_say20, 1.)
        # Clock.schedule_once(self.fade_operator, .0)
        self.fade_operator(self.ids.operation_say20)

    # def fade_operator(self):
    #     self.operator_opacity = 0
    #     anim = Animation(operator_opacity=self.operator_opacity, duration= 10)
    #     anim.start(self)
    #     # while tmp > 0.:
    #     #     tmp -= 0.000001
    #     #     self.ids.operation_say20.color = (1, 1, 0, tmp)
    #     self.ids.operation_say20.color = (1, 1, 0, self.operator_opacity)
    #     self.ids.operation_say20.font_size = 70

    def reset_say20(self, dt):
        self.number_say20 = 0
        self.ids.number_say20.text = str(self.number_say20)
        self.fade_operator(self.ids.number_say20)
        Clock.schedule_once(self.appear_operator, 1.)


    def fade_operator(self, wdg):
        anim = Animation(color=(1,1,0,0),font_size = 100, duration= 1)
        anim.start(wdg)
    def appear_operator(self, dt):
        wdg = self.ids.number_say20
        anim = Animation(color=(1,1,1,1),font_size = 70, duration= .5)
        anim.start(wdg)
        self.ids.plus1.disabled = False
        self.ids.plus2.disabled = False


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