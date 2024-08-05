# Django PDF Vector Database Slack Bot

## Overview
This project aims to create a Slack bot that utilizes Llamaindex and OpenAI to convert PDFs into a vector database. The vector database is powered by Upstash, and the backend is built with Django and Celery.

## Features
- Convert PDFs into vectors using Llamaindex and OpenAI.
- Store and manage vector data in Upstash.
- Backend management with Django.
- Task scheduling and background processing using Celery.
- Integration with Slack for easy interaction.

## Tech Stack

![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![Celery](https://img.shields.io/badge/Celery-37814A?style=for-the-badge&logo=celery&logoColor=white)
![OpenAI](https://img.shields.io/badge/OpenAI-412991?style=for-the-badge&logo=openai&logoColor=white)
![Llamaindex](https://img.shields.io/badge/Llamaindex-FFB800?style=for-the-badge&logo=llamaindex&logoColor=black)
![Upstash](https://img.shields.io/badge/Upstash-09ACBD?style=for-the-badge&logo=upstash&logoColor=white)
![Slack](https://img.shields.io/badge/Slack-4A154B?style=for-the-badge&logo=slack&logoColor=white)

## Prerequisites
Before you begin, ensure you have the following installed:
- Python 3.8+
- Django 3.2+
- Celery 5.1+
- Redis (for Celery broker)
- Upstash account and API key
- OpenAI API key
- Slack API key

## Installation

1. **Clone the repository:**
    ```bash
    git clone <repository_url>
    cd <repository_name>
    ```

2. **Create a virtual environment:**
    ```bash
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up environment variables:**
    Create a `.env` file in the project root and add the following:
    ```env
    DJANGO_SECRET_KEY=<your_django_secret_key>
    OPENAI_API_KEY=<your_openai_api_key>
    UPSTASH_REDIS_URL=<your_upstash_redis_url>
    SLACK_BOT_TOKEN=<your_slack_bot_token>
    SLACK_SIGNING_SECRET=<your_slack_signing_secret>
    ```

## Configuration

1. **Django settings:**
    Ensure that your `settings.py` is configured to use the environment variables and includes necessary configurations for Upstash and Celery.

    ```python
    import os
    from dotenv import load_dotenv

    load_dotenv()

    SECRET_KEY = os.getenv('DJANGO_SECRET_KEY')
    DEBUG = True
    ALLOWED_HOSTS = []

    INSTALLED_APPS = [
        # Your apps here
    ]

    MIDDLEWARE = [
        # Your middleware here
    ]

    ROOT_URLCONF = '<your_project_name>.urls'

    TEMPLATES = [
        # Your templates here
    ]

    WSGI_APPLICATION = '<your_project_name>.wsgi.application'

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / "db.sqlite3",
        }
    }

    # Celery Configuration
    CELERY_BROKER_URL = os.getenv('UPSTASH_REDIS_URL')
    CELERY_RESULT_BACKEND = os.getenv('UPSTASH_REDIS_URL')

    # Static files (CSS, JavaScript, Images)
    STATIC_URL = '/static/'
    ```

2. **Celery Configuration:**
    Ensure your `celery.py` file in the Django project is configured correctly.

    ```python
    from __future__ import absolute_import, unicode_literals
    import os
    from celery import Celery

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', '<your_project_name>.settings')

    app = Celery('<your_project_name>')
    app.config_from_object('django.conf:settings', namespace='CELERY')
    app.autodiscover_tasks()
    ```

## Usage

1. **Run migrations:**
    ```bash
    python manage.py migrate
    ```

2. **Run the Django development server:**
    ```bash
    python manage.py runserver
    ```

3. **Start Celery worker:**
    ```bash
    celery -A <your_project_name> worker --loglevel=info
    ```

4. **Start Celery beat:**
    ```bash
    celery -A <your_project_name> beat --loglevel=info
    ```

## Slack Bot Integration

1. **Create a Slack App:**
    - Go to the [Slack API](https://api.slack.com/) and create a new app.
    - Enable necessary permissions and event subscriptions.
    - Obtain the bot token and signing secret and add them to your `.env` file.

2. **Integrate Slack with Django:**
    Use a Slack SDK or library to handle interactions between your Django backend and Slack.

    ```python
    import os
    from slack_sdk import WebClient
    from slack_sdk.errors import SlackApiError
    from django.views.decorators.csrf import csrf_exempt
    from django.http import JsonResponse

    slack_client = WebClient(token=os.getenv('SLACK_BOT_TOKEN'))

    @csrf_exempt
    def slack_events(request):
        if request.method == 'POST':
            event_data = json.loads(request.body.decode('utf-8'))
            if 'challenge' in event_data:
                return JsonResponse({'challenge': event_data['challenge']})
            handle_event(event_data)
        return JsonResponse({'status': 'ok'})

    def handle_event(event_data):
        event = event_data['event']
        if event['type'] == 'message' and 'subtype' not in event:
            try:
                slack_client.chat_postMessage(
                    channel=event['channel'],
                    text=f"Received your message: {event['text']}"
                )
            except SlackApiError as e:
                print(f"Error posting message: {e.response['error']}")
    ```

## Contributing

1. **Fork the repository**
2. **Create a new branch:**
    ```bash
    git checkout -b feature/your-feature-name
    ```
3. **Commit your changes:**
    ```bash
    git commit -m 'Add some feature'
    ```
4. **Push to the branch:**
    ```bash
    git push origin feature/your-feature-name
    ```
5. **Open a pull request**

## License
This project is licensed under the MIT License.

## Acknowledgments
- [Llamaindex](https://llamaindex.ai/)
- [OpenAI](https://openai.com/)
- [Upstash](https://upstash.com/)
- [Django](https://www.djangoproject.com/)
- [Celery](https://docs.celeryproject.org/en/stable/)
- [Slack](https://slack.com/)
