from kivy.app import App
from kivy.uix.button import Button

class MyApp(App):
    def build(self):
        # Crear un botón con un mensaje
        button = Button(text='Presiona aquí')
        button.bind(on_press=self.on_button_press)
        # Retornar el botón como widget raíz
        return button

    def on_button_press(self, instance):
        print('¡Hola desde Kivy!')

if __name__ == '__main__':
    MyApp().run()