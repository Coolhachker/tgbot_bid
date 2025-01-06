from dataclasses import dataclass


@dataclass
class TextOfButtons:
    send_bid_button_text: str = "<b>Отправить заявку</b>"
    response_bid_button: str = '<b>Принять заявку</b>'