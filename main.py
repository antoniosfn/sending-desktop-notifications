#Importando e iniciando a biblioteca
from win10toast import ToastNotifier
toaster = ToastNotifier()

#Recebe os parâmetros e exibe a notificação
toaster.show_toast(
  "Notificação", "Seja bem-vindo ao portfolio do Antonio Neto",
  threaded=True, icon_path=None, duration=3 
)
