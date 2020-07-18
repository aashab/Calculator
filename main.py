# testing variable grid system
import kivy
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.app import App
from kivy.uix.label import Label


class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)

        self.cols = 1
        self.ent = TextInput(multiline=False)
        self.add_widget(self.ent)
        


        self.inside = GridLayout()
        self.inside.cols = 4

        self.button_7 = Button(text='7')
        self.button_7.bind(on_press=self.pressed_7)

        self.button_8 = Button(text='8')
        self.button_8.bind(on_press=self.pressed_8)

        self.button_9 = Button(text='9')
        self.button_9.bind(on_press=self.pressed_9)
        
        self.button_add = Button(text='+')
        self.button_add.bind(on_press=self.add)

        self.button_4 = Button(text='4')
        self.button_4.bind(on_press=self.pressed_4)
        
        self.button_5 = Button(text='5')
        self.button_5.bind(on_press=self.pressed_5)
        
        self.button_6 = Button(text='6')
        self.button_6.bind(on_press=self.pressed_6)
        
        self.button_sub = Button(text='-')
        self.button_sub.bind(on_press=self.sub)
        
        self.button_1 = Button(text='1')
        self.button_1.bind(on_press=self.pressed_1)
        
        self.button_2 = Button(text='2')
        self.button_2.bind(on_press=self.pressed_2)
        
        self.button_3 = Button(text='3')
        self.button_3.bind(on_press=self.pressed_3)
        
        self.button_cancel = Button(text='*')
        self.button_cancel.bind(on_press=self.pressed_product)
        

        self.button_dot = Button(text='.')
        self.button_dot.bind(on_press=self.pressed_dot)

        self.button_0 = Button(text='0')
        self.button_0.bind(on_press=self.pressed_0)

        self.button_product = Button(text='C')
        self.button_product.bind(on_press=self.cancel)
        
        self.button_div = Button(text='/')
        self.button_div.bind(on_press=self.Div)






        self.inside.add_widget(self.button_7)
        self.inside.add_widget(self.button_8)
        self.inside.add_widget(self.button_9)
        self.inside.add_widget(self.button_add)
        

        self.inside.add_widget(self.button_4)
        self.inside.add_widget(self.button_5)
        self.inside.add_widget(self.button_6)
        self.inside.add_widget(self.button_sub)


        self.inside.add_widget(self.button_1)
        self.inside.add_widget(self.button_2)
        self.inside.add_widget(self.button_3)
        self.inside.add_widget(self.button_cancel)

        self.inside.add_widget(self.button_dot)
        self.inside.add_widget(self.button_0)
        self.inside.add_widget(self.button_product)
        self.inside.add_widget(self.button_div)
        

        self.add_widget(self.inside)

        self.equal = Button(text='=', font_size=40)
        self.equal.bind(on_press=self.equall)
        self.add_widget(self.equal)

    def pressed_7(self, instance):
        x = self.ent.text
        self.ent.text = x+'7'

    def pressed_8(self, instance):
        x = self.ent.text
        self.ent.text = x+'8'
    def pressed_9(self, instance):
        x = self.ent.text
        self.ent.text = x+'9'

    def pressed_4(self, instance):
        x = self.ent.text
        self.ent.text = x+'4'
    def pressed_5(self, instance):
        x = self.ent.text
        self.ent.text = x+'5'

    def pressed_6(self, instance):
        x = self.ent.text
        self.ent.text = x+'6'

    def pressed_3(self, instance):
        x = self.ent.text
        self.ent.text = x+'3'

    def pressed_2(self, instance):
        x = self.ent.text
        self.ent.text = x+'2'

    def pressed_1(self, instance):
        x = self.ent.text
        self.ent.text = x+'1'
    def pressed_0(self, instance):
        x = self.ent.text
        self.ent.text = x + '0'

   


    def add(self, instance):
        global sums
        sums=0
        global y
        y = int(self.ent.text)
        self.ent.text=''

    def sub(self, instance):
        global sums
        sums = 1
        global y
        y = int(self.ent.text)
        self.ent.text=''


    def cancel(self, instance):
        self.ent.text = ''

    
    def pressed_dot(self, instance):

        pass
    def pressed_product(self, instance):
        global sums
        sums = 2
        global y
        y = int(self.ent.text)
        self.ent.text=''
        
    def Div(self, instance):
        global sums
        sums = 3
        global y
        y = int(self.ent.text)
        self.ent.text=''
        pass


    def equall(self, instance):
        num = int(self.ent.text)
        if sums == 0:
            self.ent.text = str(y + num)
        
        elif sums == 1:
            self.ent.text = str(y - num)
        elif sums == 2:
            self.ent.text = str(y * num)
        elif sums == 3:
            self.ent.text = str(y/num)

class MyApp(App):
    def build(self):
        return MyGrid()

if __name__ == '__main__':
    MyApp().run()