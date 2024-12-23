from kivy.app import App
import json
import os
import time
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import StringProperty

class AddIngredientButton(Button):
    def on_press(self):
        App.get_running_app().ingredientList.append(self.parent.ingredient)
        with open("allergies", 'w') as myfile:
            myfile.write(json.dumps(App.get_running_app().ingredientList))
        
class AnswerInput(BoxLayout):
    ingredient = StringProperty()

class StartPage(Screen):
    pass

class PhotoPage(Screen):
    pass

class SettingsPage(Screen):
    pass

class MyScreenManager(ScreenManager):
    pass

class CameraClick(BoxLayout):
    def capture(self):
        '''
        Function to capture the images and give them the names
        according to their captured time and date.
        '''
        camera = self.ids['camera']
        timestr = time.strftime("%Y%m%d_%H%M%S")
        camera.export_to_png("IMG_{}.png".format(timestr))
        print("Captured")


class FoodScanApp(App):

    ingredientList = []

    def read_input(self,obj):
        print("was here")
        return 
    
    def update_allergies(self,obj,string):
        print(string)
        return
    def build(self):
        if os.path.isfile("allergies"):
            with open("allergies", 'r') as myfile:
                self.ingredientList = json.load(myfile)
                
        return MyScreenManager()



if __name__ == '__main__':
    FoodScanApp().run()