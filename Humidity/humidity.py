import requests
import json

url = "https://api.samsara.com//v1/sensors/humidity?sensors=278018084737978"

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
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'Authorization': 'Bearer samsara_api_pYUL2aGihNxURsfRVPs7iVeGB1RvaW'
}

response = requests.request("POST", url, headers=headers, data=payload)

# convert response to text to print to console
response_json = print(response.text)


# convert response to json to save to json file
response_string = print(response.json())



# function to add to JSON
def write_json(new_data, filename= '/Users/shadae/projects/vehicle-tracking/Humidity/humidity_data.json'):
    with open(filename,'r+') as file:
          # First we load existing data into a dict.
        file_data = json.load(file)
        # Join new_data with file_data inside emp_details
        file_data["humidity"].append(new_data)
        # Sets file's current position at offset.
        file.seek(0)
        # convert back to json.
        json.dump(file_data, file, indent = 4)
 
    # python object to be appended

y = {"groupId":108155,"sensors":[{"id":278018084737978,"name":"W32X-WMB-S5S","humidity":28,"humidityTime":"2022-09-16T02:58:26Z","vehicleId":281474982422735}]}

     
write_json(y)
