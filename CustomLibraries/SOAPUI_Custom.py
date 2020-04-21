import requests

def getSoapResponse(requestXML,endpoint):
 
        headers = {'Content-Type': 'text/xml'}
        timeout = 90
        response = requests.post(endpoint, data=requestXML.encode('utf-8'), headers=headers, timeout=timeout).text
        return response
