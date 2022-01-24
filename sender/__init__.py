import webbrowser as web
import time
import pyautogui as pg

from phone_utils import PhoneValidators


class Sender(PhoneValidators):
    def catch_information(self) -> dict:
        print("Código do Brasil: 55")
        print("""
==================================================================================
===_=======_====_______====_=========_====________=========____======________=====
==| |=====| |==|       |==| |=======| |==|_____  /====== / ____ \\===|  _____  \\===
==| |_____| |==| ===== |==| |===_===| |=======/ /=======| |    | |==| |     | |===
==|  ______ |==| ===== |==| |==| |==| |======/ /========| |____| |==| |_____| |===
==| |=====| |==| ===== |==| |==| |==| |=====/ /=========|  ____  |==|  ______/====
==| |=====| |==| ===== |==| |==| |==| |====/ /_______===| |    | |==| |===========
==|_|=====|_|==|_______|===\\____|____/====|__________|==|_|    |_|==|_|===========
==================================================================================
        """)
        country = input("Digite o código do país: ")
        while not self.is_valid_country(country, raise_exception=True):
            country = input("Código inválido. Digite o código do país: ")
        print(10 * "=")
        ddd = input("Digite o DDD: ")
        while not self.is_valid_ddd(ddd, raise_exception=True):
            ddd = input("DDD inválido. Código inválido. Digite o DDD: ")
        print(10 * "=")
        phone = input("Digite o número de telefone: ")
        while not self.is_valid_phone(phone, raise_exception=True):
            phone = input("Número inválido. Digite o número de telefone: ")
        print(10 * "=")
        amount = input("Digite quantas vezes quer enviar a mensagem: ")
        while not self.is_valid_amount(amount, raise_exception=True):
            amount = input("Quantidade inválida. Digite quantas vezes quer enviar a mensagem: ")
        print(10 * "=")
        wp_send = {
            "country": f'+{country}',
            "ddd": ddd,
            "phone": phone,
            "message": input("Digite a mensagem: "),
            "amount": amount,
        }

        return wp_send

    @staticmethod
    def send_what_msg_instantly(
        country: str, ddd: str, phone: str, message: str, amount
    ) -> None:
        web.open(f"https://web.whatsapp.com/send?phone={country}{ddd}{phone}")
        time.sleep(10)
        for _ in range(int(amount)):
            pg.click(1089, 1030)

            for char in message:
                pg.press(f"{char}")

            pg.press("enter")

    def send(self):
        wp = self.catch_information()
        self.send_what_msg_instantly(**wp)

        print("Obrigado por utilizar o HowZap =)")
