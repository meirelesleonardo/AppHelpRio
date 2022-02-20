from multiprocessing.connection import Client


from django.test import Client

def test_home_satatus_code(client:Client):
    resposta = client.get('/')
    assert resposta.status_code == 200