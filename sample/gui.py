from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.core.clipboard import Clipboard
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.app import App

from plyer import filechooser

from utils import get_image, get_resource

# KV Builder

Builder.load_file(get_resource('builder.kv'))


# Screen classes


class LogoScreen(Screen):
    @staticmethod
    def get_bg():
        return get_image('logo.png')


class FileChooserScreen(Screen):
    @staticmethod
    def get_bg():
        return get_image('easy.png')


class AttackMethodScreen(Screen):
    @staticmethod
    def get_bg():
        return get_image('last_step.png')


class CrackScreen(Screen):
    @staticmethod
    def get_bg():
        return get_image('cracking.png')


class ResultCompletedScreen(Screen):
    @staticmethod
    def get_bg():
        return get_image('completed.png')


class ResultFailedScreen(Screen):
    @staticmethod
    def get_bg():
        return get_image('failed.png')


# Special buttons


path_to_archive = ''


class PathButton(Button):
    @staticmethod
    def get_path():
        global path_to_archive
        path_to_archive = filechooser.open_file(title="Pick a .ZIP archive file..",
                                                filters=[("Zip archive file", "*.zip")])


class CopyButton(Button):
    @staticmethod
    def copy():
        Clipboard.copy('password')


# Scene manager

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
