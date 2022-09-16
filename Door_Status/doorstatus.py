import requests
import json


# created get request URL from API documentation

url = "https://api.samsara.com//v1/sensors/door?sensors=278018083082629"

payload = json.dumps({
  "sensors": [
    {
      "value": "<Error: Too many levels of nesting to fake this schema>"
    },
    {
      "value": "<Error: Too many levels of nesting to fake this schema>"
    }
  ]
})

# included authenication bearer token in header (would put this is an env file and create a variable next time)

headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'Authorization': 'Bearer samsara_api_pYUL2aGihNxURsfRVPs7iVeGB1RvaW'
}

# saved response as a variable

response = requests.request("POST", url, headers=headers, data=payload)

# convert response to text to print to console
response_json = print(response.text)


# convert response to json to save to json file
response_string = print(response.json())




# function to add to JSON object to Json file

def write_json(new_data, filename= '/Users/shadae/projects/vehicle-tracking/Door_Status/doorstatus.json'):
    with open(filename,'r+') as file:
          # First we load existing data into a dict.
        file_data = json.load(file)
        # Join new_data with file_data inside emp_details
        file_data["doorstatus"].append(new_data)
        # Sets file's current position at offset.
        file.seek(0)
        # convert back to json.
        json.dump(file_data, file, indent = 4)
 
    # python object to be appended

y = {"groupId":13456,"sensors":[{"id":278018083082629,"name":"WDED-NC2-FZA","doorClosed":'True',"doorStatusTime":"2022-09-16T01:25:15Z","vehicleId":281474982422735}]}

     
write_json(response_json)

