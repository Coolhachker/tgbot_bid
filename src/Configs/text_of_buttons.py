from dataclasses import dataclass


@dataclass
class TextOfButtons:
    send_bid_button_text: str = "Отправить заявку"
    response_bid_button: str = 'Принять заявку'

    url_button = 'Ссылка на чат'
    change_url_button = 'Изменить ссылку'

    comeback_button = '⏪ Вернуться'