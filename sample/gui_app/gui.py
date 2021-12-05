import pyzipper
from kivy.clock import Clock
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.core.clipboard import Clipboard
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.app import App

from plyer import filechooser
from sample.utils import get_image, get_resource

import sample.cracker as cracker

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

    @staticmethod
    def dictionary_attack():
        Clock.schedule_once(dictionary_atk, 1)

    @staticmethod
    def brute_force_attack():
        Clock.schedule_once(brute_force, 1)


def dictionary_atk(dt):
    global password
    password = cracker.dictionary_attack(path_to_archive)

    if password is None:
        sm.current = 'failed'
    else:
        sm.current = 'completed'


def brute_force(dt):
    global password

    password = cracker.brute_force_attack_multi_thread(path_to_archive)

    if password is None:
        sm.current = 'failed'
    else:
        sm.current = 'completed'
        sm.get_screen('completed').update_pwd(password)


class CrackScreen(Screen):
    @staticmethod
    def get_bg():
        return get_image('cracking.png')


class ResultCompletedScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.ids.label.text = 'Archive password: ' + '' if password is None else password

    def update_pwd(self, pwd):
        self.ids.label.text = 'Archive password: ' + pwd

    @staticmethod
    def get_bg():
        return get_image('completed.png')


class ResultFailedScreen(Screen):
    @staticmethod
    def get_bg():
        return get_image('failed.png')


# Special buttons


path_to_archive = ''
attack_method = None
password = None


class PathButton(Button):
    @staticmethod
    def get_path():
        global path_to_archive
        while not pyzipper.is_zipfile(path_to_archive):
            path_to_archive = str(filechooser.open_file(title="Pick a .ZIP archive file..",
                                                        filters=[("Zip archive file", "*.zip")]))

            file_path = ''
            for char in path_to_archive:
                if char == '[' or char == "'" or char == ']':
                    continue

                file_path += char

            path_to_archive = file_path

        sm.current = 'attack_method'


class CopyButton(Button):
    @staticmethod
    def copy():
        Clipboard.copy(password)


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
