from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
import os

class TEACompilerApp(App):
    def build(self):
        root = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        self.status = Label(text='Compilador Linguístico TEA\nConfigure chaves e envie mensagem', size_hint_y=None, height=80)
        root.add_widget(self.status)
        
        self.input = TextInput(hint_text='Sua mensagem', multiline=True, size_hint_y=0.3)
        root.add_widget(self.input)
        
        btn = Button(text='Processar (modo local)', size_hint_y=None, height=60)
        btn.bind(on_press=self.processar)
        root.add_widget(btn)
        
        self.output = Label(text='Resposta aparecerá aqui', size_hint_y=None, text_size=(None, None))
        scroll = ScrollView()
        scroll.add_widget(self.output)
        root.add_widget(scroll)
        
        return root
    
    def processar(self, instance):
        msg = self.input.text.strip()
        if not msg:
            self.output.text = 'Digite uma mensagem.'
            return
        # Compilador simples embutido
        resposta = f"[Intenção] Responder de forma literal e clara.\n\n{msg}\n\n[Próximo passo] Revise e confirme.\n[Confirmação: atendeu?]"
        self.output.text = resposta
        self.output.texture_update()
        self.output.height = self.output.texture_size[1]

if __name__ == '__main__':
    TEACompilerApp().run()
