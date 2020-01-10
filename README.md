# Airtng App: Part 1 - Workflow Automation with Python | Flask
> We are currently in the process of updating this sample template. If you are encountering any issues with the sample, please open an issue at [github.com/twilio-labs/code-exchange/issues](https://github.com/twilio-labs/code-exchange/issues) and we'll try to help you.

[![Build Status](https://travis-ci.org/TwilioDevEd/airtng-flask.svg?branch=master)](https://travis-ci.org/TwilioDevEd/airtng-flask)


Learn how to automate your workflow using Twilio's REST API and Twilio SMS. This example app is a vacation rental site, where the host can confirm a reservation via SMS.

[Read the full tutorial here](https://www.twilio.com/docs/tutorials/walkthrough/masked-numbers/python/flask)!

## Local Development


1. You will need to configure Twilio to send requests to your application when SMS are received.

   You will need to provision at least one Twilio number with sms capabilities so the application's users can make property reservations. You can buy a number [right here](https://www.twilio.com/user/account/phone-numbers/search). Once you have a number you need to configure it to work with your application. Open [the number management page](https://www.twilio.com/user/account/phone-numbers/incoming) and open a number's configuration by clicking on it.

   Remember that the number where you change the _SMS webhook_ must be the same one you set on the `TwilioPhoneNumber` setting.

   To start using `ngrok` in our project you'll have execute to the following line in the _command prompt_.

   ```
   ngrok http 5000 -host-header="localhost:5000"
   ```

   Keep in mind that our endpoint is:

   ```
   http://<your-ngrok-subdomain>.ngrok.io/confirm
   ```

1. Clone this repository and `cd` into it.

   ```
   git clone git@github.com:TwilioDevEd/airtng-flask.git
   ```

1. Create a new virtual environment.

   - If using vanilla [virtualenv](https://virtualenv.pypa.io/en/latest/):

       ```
       virtualenv venv
       source venv/bin/activate
       ```

   - If using [virtualenvwrapper](https://virtualenvwrapper.readthedocs.org/en/latest/):

       ```
       mkvirtualenv airtng-flask
       ```

1. Install the requirements.

   ```
   pip install -r requirements.txt
   ```

1. Edit the following keys/values for the `config.py` file inside the  `airtng_flask/` directory. Be sure to replace the place holders and connection string with real information. Replace the connection string preferably under development config.

   ```
   TWILIO_ACCOUNT_SID = 'your_twilio_account_sid'
   TWILIO_AUTH_TOKEN = 'your_twilio_auth_token'
   TWILIO_NUMBER = 'your_twilio_phone_number'

   SQLALCHEMY_DATABASE_URI = 'sqlite://'
   ```

1. Run the migrations.

   ```
   python manage.py db upgrade
   ```

1. Start the development server.

   ```
   python manage.py runserver
   ```

1. Check it out at [http://localhost:5000](http://localhost:5000)


That's it!

## Run the tests

You can run the tests locally through [coverage](http://coverage.readthedocs.org/):

1. Run the tests.

    ```
    $ coverage run manage.py test
    ```

You can then view the results with `coverage report` or build an HTML report with `coverage html`.

## Meta

* No warranty expressed or implied. Software is as is. Diggity.
* [MIT License](http://www.opensource.org/licenses/mit-license.html)
* Lovingly crafted by Twilio Developer Education.
