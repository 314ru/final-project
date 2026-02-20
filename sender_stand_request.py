import configuration
import requests
import data 

def create_order(order_body):
      return requests.post(
        configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
        json=order_body,
        headers=data.headers
    )

def get_order_by_track_number(track_number):
    params = {'t': track_number}
    return requests.get(
        configuration.URL_SERVICE + configuration.ORDER_TRACK_PATH,
        params=params
    )
