import time
from plyer import notification
cont = 0
if __name__ == "__main__":
    while True:
        notification.notify(
            app_name='Beber água',
            app_icon='R.ico',
            title='Hora de beber água!',
            message=f'Você bebeu {cont}ml de água hoje. Está na hora de se hidratar novamente!',
            timeout=0
        )
        confirmation = int(input('Quantos ML de água vc bebeu? '))
        cont = cont + confirmation
        time.sleep(3600)


