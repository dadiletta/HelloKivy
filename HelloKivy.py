from kivy.uix.popup import Popup
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.stacklayout import StackLayout
from kivy.config import Config

# I think the grid layout does a lot of the work for me
class OptionsDisplay(GridLayout):


    def __init__(self, menu, **kwargs):
        root_menu = menu
        super(OptionsDisplay, self).__init__(**kwargs)
        self.cols = 3
        if(len(menu) % 3 == 0):
            self.row = len(menu)/3
        else:
            self.row = (len(menu) / 3)+1
        #self.add_widget(Label(text='User Name'))
        for x in range(len(menu)):
            self.btn = Button(text=menu[x][0])
            self.btn.bind(on_press=menu[x][1])
            self.add_widget(self.btn)


    def lights(self):
        '''menu = [("Back", OptionsDisplay.lights),
                ("Rotate", OptionsDisplay.lights),
                ("Demo", OptionsDisplay.demo),
                ("Calibrate servo", OptionsDisplay.lights),
                ("Forward", OptionsDisplay.lights),
                ("Quit", OptionsDisplay.lights)
                ]
        return OptionsDisplay(menu)'''

    def demo(self):
        print('Tra la la')


class MyApp(App):
    root_menu = []

    def build(self):
        # window settings
        Config.set('kivy', 'exit_on_escape', '1')
        Config.set('graphics', 'borderless', '1')
        Config.set('graphics', 'window_state', 'maximized')
        Config.set('graphics', 'fullscreen', 'auto')
        Config.set('graphics', 'resizable', '0')
        # event handler
        self.root_menu = [("Navigate forward", OptionsDisplay.lights),
                ("Rotate", OptionsDisplay.lights),
                ("Demo", OptionsDisplay.demo),
                ("Calibrate servo", OptionsDisplay.lights),
                ("Forward", OptionsDisplay.lights),
                ("Quit", OptionsDisplay.lights)
                ]
        return OptionsDisplay(self.root_menu)


if __name__ == '__main__':
    MyApp().run()