from kivy.app import App
import json
import os
import time
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import StringProperty
from detectTextInImage import readImage


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

class ResultPage(Screen):
    
    yesOrNo = StringProperty()
    contains = StringProperty()

    def update_text_boxes(self,content,contains):
        if not contains:
            self.yesOrNo = "Does not contain any of the ingredients"
        else:
            self.yesOrNo = "The ingredient contains a bad ingredient"

        self.contains =  str(content)
        return 


class MyScreenManager(ScreenManager):
    pass

class CameraClick(BoxLayout):
    def capture(self):
        '''
        Function to capture the images and give them the names
        according to their captured time and date.
        '''
        camera = self.ids['camera']
        camera.export_to_png("FoodImage.png")
        contents = readImage("FoodImage.png")
        contains = App.get_running_app().checkIngredients(contents)
        App.get_running_app().myScreenManager.current = "result"
        resultScreen = App.get_running_app().myScreenManager.get_screen("result")
        resultScreen.update_text_boxes(contents,contains)

        return

class FoodScanApp(App):

    ingredientList = []

    def checkIngredients(self, content):
        
        contains = False
        for ingredient in content:
            contains = contains or self.ingredientList.__contains__(ingredient)

        return contains
    

    def build(self):
        if os.path.isfile("allergies"):
            with open("allergies", 'r') as myfile:
                self.ingredientList = json.load(myfile)
        self.myScreenManager = MyScreenManager()
        return self.myScreenManager



if __name__ == '__main__':
    FoodScanApp().run()