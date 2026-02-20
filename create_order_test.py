import sender_stand_request
import data

def test_get_order_by_track_number():
    response_create = sender_stand_request.create_order(data.order_body)
    track_number = response_create.json().get('track')
    response_get = sender_stand_request.get_order_by_track_number(track_number)
    assert response_get.status_code == 200
