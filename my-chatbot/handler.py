import datetime
import requests

def handle(req):
    # Convert the input string to lowercase for case-insensitive matching
    input_data = req.lower()

    if 'name' in input_data:
        names = ["ChatBot", "Bot", "Chatty"]
        response = "My name is {}. But you can call me {} or {}.".format(names[0], names[1], names[2])
    elif 'time' in input_data:
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        response = "The current date and time is {}.".format(current_time)
    elif 'figlet' in input_data:
        start_index = input_data.find("for ")
        if start_index != -1:
            figlet_text = input_data[start_index + 4:].strip()
            if figlet_text:
                # Make HTTP request to invoke figlet function
                figlet_response = requests.post("http://10.62.0.13:8080/function/figlet", data=figlet_text)
                if figlet_response.status_code == 200:
                    response = figlet_response.text
                else:
                    response = "Error invoking figlet function."
            else:
                response = "Please provide text for the figlet."
        else:
            response = "Please provide text for the figlet."
    else:
        response = "Sorry, I didn't understand the question."

    return response

