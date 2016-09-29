<a href="https://www.twilio.com">
  <img src="https://static0.twilio.com/marketing/bundles/marketing/img/logos/wordmark-red.svg" alt="Twilio" width="250" />
</a>

# Airtng App: Part 2 - Workflow Automation with Twilio Python | Flask

[![Build Status](https://travis-ci.org/TwilioDevEd/airtng-flask.svg?branch=masked-numbers)]
(https://travis-ci.org/TwilioDevEd/airtng-flask)

Protect your customers' privacy by creating a seamless interaction by provisioning Twilio numbers on the fly. Route all voice calls and messages through your very own 3rd party. This allows you to control the interaction between your customers, while putting your customer's privacy first.

## Configure Twilio to call your webhooks

You will need to configure Twilio to send requests to your application when SMSs are received.

You will need to provision at least one Twilio number with SMS capabilities so the application's users can make property reservations. You can buy a number [right here](https://www.twilio.com/user/account/phone-numbers/search). Once you have a number you need to configure it to work with your application. Open [the number management page](https://www.twilio.com/user/account/phone-numbers/incoming) and open a number's configuration by clicking on it.

Remember that the number where you change the _SMS webhook_ must be the same one you set on the `TwilioPhoneNumber` settings.

![Configure Voice](http://howtodocs.s3.amazonaws.com/twilio-number-config-all-med.gif)

 To start using `ngrok` in our project you'll have execute to the following line in the _command prompt_.

```bash
ngrok http 5000 -host-header="localhost:5000"
```

Keep in mind that our endpoint is:

```
http://<your-ngrok-subdomain>.ngrok.io/confirm
```


## Create a TwiML App

This project is configured to use a _TwiML App_ that allows us to easily set the voice URLs for all Twilio phone numbers we purchase in this app.

Create a new TwiML app at https://www.twilio.com/user/account/apps/add and use its `Sid` as the `TwiMLApplicationSID` application setting.

![Creating a TwiML App](http://howtodocs.s3.amazonaws.com/call-tracking-twiml-app.gif)

Once you have created your TwiML app, configure your Twilio phone number to use it ([instructions here](https://www.twilio.com/help/faq/twilio-client/how-do-i-create-a-twiml-app)).

If you don't have a Twilio phone number yet, you can purchase a new number in your [Twilio Account Dashboard](https://www.twilio.com/user/account/phone-numbers/incoming).

You'll need to update your TwiML app's voice and SMS URL setting to use your `ngrok` hostname. It will look something like this:

```
http://<your-ngrok-subdomain>.ngrok.io/exchange/sms
http://<your-ngrok-subdomain>.ngrok.io/exchange/voice
```

## Local Development

1. Clone this repository and `cd` into it.

   ```bash
   git clone git@github.com:TwilioDevEd/airtng-flask.git
   ```

1. Switch to `masked-numbers` branch.

    ```bash
    git checkout masked-numbers
    ```

1. Create a new virtual environment.

   - If using vanilla [virtualenv](https://virtualenv.pypa.io/en/latest/):

       ```bash
       virtualenv venv
       source venv/bin/activate
       ```

   - If using [virtualenvwrapper](https://virtualenvwrapper.readthedocs.org/en/latest/):

       ```bash
       mkvirtualenv airtng-flask
       ```

1. Install the requirements.

   ```bash
   pip install -r requirements.txt
   ```

1. Edit the following keys/values for the `config.py` file inside the  `airtng_flask/` directory. Be sure to replace the place holders and connection strings with real information or reuse the provided one, like the connection string.

   ```
   TWILIO_ACCOUNT_SID = 'your_twilio_account_sid'
   TWILIO_AUTH_TOKEN = 'your_twilio_auth_token'
   TWILIO_NUMBER = 'your_twilio_phone_number'
   APPLICATION_SID = 'your_application_sid'

   SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'dev.sqlite')
   ```

1. Run the migrations.

   ```bash
   python manage.py db upgrade
   ```

1. Start the development server.

   ```bash
   python manage.py runserver
   ```

1. Check it out at [http://localhost:5000](http://localhost:5000)


## Run the tests

You can run the tests locally through [coverage](http://coverage.readthedocs.org/):

1. Run the tests.

    ```bash
    $ coverage run manage.py test
    ```

You can then view the results with `coverage report` or build an HTML report with `coverage html`.

## Meta

* No warranty expressed or implied. Software is as is. Diggity.
* [MIT License](http://www.opensource.org/licenses/mit-license.html)
* Lovingly crafted by Twilio Developer Education.
