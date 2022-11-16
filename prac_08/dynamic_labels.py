"""
Estimate: 30 minutes
Actual:  35 minutes
"""
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabels(App):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.names = ["Mike", "Stella", "David", "Kate", "Rory", "Alex"]

    def build(self):
        self.title = "Dynamic Labels"
        self.root = Builder.load_file("dynamic_labels.kv")
        for name in self.names:
            name_label = Label(text=name)
            self.root.ids.names_box.add_widget(name_label)
        return self.root

    def create_name_label(self):
        name = self.root.ids.name_input.text
        self.root.ids.names_box.add_widget(Label(text=name))
        self.root.ids.name_input.text = ""


if __name__ == '__main__':
    DynamicLabels().run()
