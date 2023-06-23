# dependencies
import requests

def line_notify(token, msg):
  requests.post(
      'https://notify-api.line.me/api/notify',
      headers={'Authorization': f'Bearer {token}'},
      data={'message': f'message: {msg}'})
