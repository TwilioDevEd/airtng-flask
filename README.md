# Airtng App: Part 1 - Workflow Automation with Python | Flask
> We are currently in the process of updating this sample template. If you are encountering any issues with the sample, please open an issue at [github.com/twilio-labs/code-exchange/issues](https://github.com/twilio-labs/code-exchange/issues) and we'll try to help you.

![](https://github.com/TwilioDevEd/airtng-flask/workflows/Flask/badge.svg)


Learn how to automate your workflow using Twilio's REST API and Twilio SMS. This example app is a vacation rental site, where the host can confirm a reservation via SMS.

[Read the full tutorial here](https://www.twilio.com/docs/tutorials/walkthrough/masked-numbers/python/flask)!

## Local Development


1. You will need to configure Twilio to send requests to your application when SMS are received.

   You will need to provision at least one Twilio number with sms capabilities so the application's users can make property reservations. You can buy a number [right here](https://www.twilio.com/user/account/phone-numbers/search). Once you have a number you need to configure it to work with your application. Open [the number management page](https://www.twilio.com/user/account/phone-numbers/incoming) and open a number's configuration by clicking on it.

   Remember that the number where you change the _SMS webhook_ must be the same one you set on the `TwilioPhoneNumber` setting.

   ![Configure Messaging](webhook.png)

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

1. Copy the sample configuration `.env.example` to `.env`, and then edit `.env` to match your configuration.

  ```bash
  cp .env.example .env
  ```

  You can find your `TWILIO_ACCOUNT_SID` and `TWILIO_AUTH_TOKEN` in your
   [Twilio Account Settings](https://www.twilio.com/console).
   You will also need a `TWILIO_PHONE_NUMBER`, which you may find [here](https://www.twilio.com/console/phone-numbers/incoming).

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
* The CodeExchange repository can be found [here](https://github.com/twilio-labs/code-exchange/).
* [MIT License](http://www.opensource.org/licenses/mit-license.html)
* Lovingly crafted by Twilio Developer Education.
