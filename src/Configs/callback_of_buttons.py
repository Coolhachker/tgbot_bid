from dataclasses import dataclass


@dataclass
class CallbacksOfButtons:
    callback_of_send_bid_button = '?'
    callback_of_response_bid_button = '!'

    callback_of_change_url_button = 'change_url'