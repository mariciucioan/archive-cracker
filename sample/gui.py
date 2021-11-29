from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.core.clipboard import Clipboard
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.app import App

from plyer import filechooser
import utils as u

# KV Builder

Builder.load_file(u.get_resource('builder.kv'))

# Screen classes

class LogoScreen(Screen):
    def get_bg(self):
        return u.get_resource('logo.png')

class FileChooserScreen(Screen):
    def get_bg(self):
        return u.get_resource('easy.png')

class AttackMethodScreen(Screen):
    def get_bg(self):
        return u.get_resource('last_step.png')

class CrackScreen(Screen):
    def get_bg(self):
        return u.get_resource('cracking.png')

class ResultCompletedScreen(Screen):
    def get_bg(self):
        return u.get_resource('completed.png')

class ResultFailedScreen(Screen):
    def get_bg(self):
        return u.get_resource('failed.png')

# Special buttons

class PathButton(Button):
    def get_path(self):
        u.path_to_archive = filechooser.open_file(title="Pick a .ZIP archive file..",
                                     filters=[("Zip archive file", "*.zip")])

class CopyButton(Button):
    def copy(self):
        Clipboard.copy(u.found_password)

#Scene manager

sm = ScreenManager(transition=FadeTransition())
sm.add_widget(LogoScreen(name='logo'))
sm.add_widget(FileChooserScreen(name='file_chooser'))
sm.add_widget(AttackMethodScreen(name='attack_method'))
sm.add_widget(CrackScreen(name='crack'))
sm.add_widget(ResultCompletedScreen(name='completed'))
sm.add_widget(ResultFailedScreen(name='failed'))

# GUI class

class GUI(App):
    def build(self):
        Window.size = (500, 500)
        return sm