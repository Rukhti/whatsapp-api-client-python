from whatsapp_api_client_python import API as API

ID_INSTANCE = '1101824950'
API_TOKEN_INSTANCE = 'd527a190b4a441e08687ed6ac7d658725edfe214649b4cb49d'

greenAPI = API.GreenApi(ID_INSTANCE, API_TOKEN_INSTANCE)

def main():
    result = greenAPI.sending.sendMessage('923479811551@c.us', 'G')
    print(result.data)

if __name__ == "__main__":
    main()
