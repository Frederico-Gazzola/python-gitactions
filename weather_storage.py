from bs4 import BeautifulSoup
from google.cloud import storage
from google.oauth2 import service_account
import requests

headers = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

credentials_dict = {
  "type": "service_account",
  "project_id": "probable-quest-382223",
  "private_key_id": "02e27fabd0e691a422f0d82e9e12568eeccc1ce7",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDR2Br8z5BVkZx4\nZru2pM/pP/8Ri15VyIQNH5tlQHGVQtbYXffr4BnXUi44bsS6kUsBsJ4N794+Z1fx\n58d1H8GZx3i5HmTMq6Hd8xFeEGQqXkJuvhAoBrEhP0e+lLTW2WcjS87BKI3v3PE8\nUmtTeEnJQC+cjTWUfC+mvwE2I91xKIjaGvvTPpC1FJtbyfaKUs9T20lq1G8p8LYY\n+jyd+fz0qFyVlFJuSznPVDKqkV5uueR6dje9TYlBzo2M0ELm/KSDXmgdiRFtlEMn\na16e+Mx5r20IF/+ypyLySqeM1/NDPoFkIVAmf8kq6SK0ZFRdSzP0l1d4kcN+LZGx\n0yJKMUa7AgMBAAECggEAOxLkyg3eupAS5fw51PmBxE6tTjGXXXvk3NLsiq0BLL1T\nwTZ28FK2w5yRgXaBcGotnOytGgxQWu353pJa3riRZmq2rBqH0uxwVYyzc3EW2ayO\ndCGSZ8o2fD8VweuYGzG5rMCPFGaHyqI+0TX8m9NtpjepD5/bGRF60qzLuQOQt+Vn\n52Iv1xJDIW1GON3gjEGOlGwVE8FLeUc9gnY0MhVjrtFU3fTQpZI8NAYka2wEyE5W\nzbBqqj+h7cx1ehQktuIYakT1hubo8sJKWl1jEtc2NNFWgMKwX2bEwX8PZDhPRzqH\nC4bQk0yajL3xVPlo0qO4BIKKlL6XdIWQDcFwZn/P4QKBgQD8IqX/eLofFmQtEAQZ\nbcPE3PJ6StmbQu3a1tQpXQCEoAjZbFGumiqerYFZCIff3jfzH0t//pOsOCjjH9Pp\njaEpiFJLutZs7cvmzjholDig0utjoLEp490q+gW96O0P/jI1VyIl6P28oGYsu1Nl\n80rdF3OUnFzQnoJVAoUk9p2MWwKBgQDVD4LRFeTCYX+kSpeTVSDrJbTbwQs/GSQi\nJYi3KeQckxPWOyhPMf3EZt8PwRlGclODXOmCx3Tn1X1okGprxo/WFWKZ3ZT/ysVJ\nJG0oHcUzJp2xlUk4+ettgBgcCjoxxynOkmnnC6gyB0g3izOqP7p3ScdeU6Ayw0r1\nmFcm/Tm9IQKBgQDoON1c/AuooE3ptyufZBqAUeO+wPvFZZJ/EYhdBHx6qo8b+gkN\nYI7KkRFmOFY02Y38jaFTJN1MLHl0Hxdlr/10rErn1xCxSR+Y1+zaXVH+xeTpYNJr\nu6Qzdg4dyM+3AC+sMzGPaxVwSudwYaRBbSBRm8znXlCaELQHqgeJcN7QqwKBgQDJ\nJ8rXgvcm+oxbXb178ayRtljp/XmTyjXOM2e/nsJqpAXfhpzJIKa5rnI9Wo91bm0g\nojEpMw1R8MNlXKvNM3wLoMcmBAkv846OPuD8Nhc/8t6BkjO+ol6/VGfu2U0WQDZd\nfOiVpfDXwv5QypEt1NtE0phzmzqtkqqL85edDQldYQKBgCR1C8qEEjfy+13bsMGe\nWuliDQjX3rvn08ifVxaqafGhXaCPEG9vSO7Hkx9gbCX8Ukdu0EhsJwOqZvfL/8at\nuiQ6OMJFp4TjuylZrtBVvhtKNz54fmcEwIf9jM4osSGte5W7yPWQK+NHLBEJ0YXe\nSICMq6lNBXn18EoZNU2MHeIj\n-----END PRIVATE KEY-----\n",
  "client_email": "myaccount@probable-quest-382223.iam.gserviceaccount.com",
  "client_id": "116560735125922524795",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/myaccount%40probable-quest-382223.iam.gserviceaccount.com"

}

try:
  res = requests.get(
    f'https://www.google.com/search?q=SaoPauloCidade&oq=SaoPauloCidade&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8', headers=headers)

  print("Loading...")

  soup = BeautifulSoup(res.text, 'html.parser')

  info = soup.find_all("span", class_="LrzXr kno-fv wHYlTd z8gr9e")[0].getText()
  
  print(info)



  credentials = service_account.Credentials.from_service_account_info(credentials_dict)
  storage_client = storage.Client(credentials=credentials)
  bucket = storage_client.get_bucket('weather-saop')
  blob = bucket.blob('weather_info.txt')
  blob.upload_from_string(info + '\n')

  print('File uploaded.')
  print("Finished.")
except Exception as ex:
  print(ex)
