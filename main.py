#SMS notification system

from twilio.rest import TwilioRestClient
from flask import *
from os import *

app = Flask(__name__)


#Twilio API
number_from = environ.get('TWILIO_NUMBER_FROM', None)
number_to = environ.get('TWILIO_NUMBER_TO', None)
account_sid = environ.get('TWILIO_SID', None)
auth_token = environ.get('TWILIO_TOKEN', None)
client = TwilioRestClient(account_sid, auth_token)


#Test data
clients = [{'case': 1087, 'name': 'John Smith', 'number': number_to},{'case': 1480, 'name': 'Pocahontas'} ]



@app.route("/")
def main():
    return render_template('form.html')


@app.route('/notify', methods=['POST'])
def notify():
    contact = request.form['contact']
    msg_type = request.form['msg_type']
    doc = (request.form['doc'])
    client = clients[int(contact)-1]

    message = "Hi, " + client['name'] + ", I would like to remind you about your appointment at HCLC regarding your case. Please bring an ID, a proof of address and a birth certificate."
    number = client['number']

    sms(number, message)

    return "Message sent to " + number + ": <br><br>" + message



def sms(number, msg):
    print("number: " + number + " | msg: " + msg)
    message = client.messages.create(to=number, from_=number_from, body=msg)



if __name__ == "__main__":
    app.run()
