# TickIt Backend API

TickIt is a backend API built using Django and Django REST Framework that allows users to manage venues and events. It provides endpoints to create, retrieve, update, and delete venues and events.

## Installation and Setup

To run the TickIt Backend API locally, follow these steps:

1. Clone the repository:

    ```bash
    git clone <repository_url>
    cd tick-it-backend
    ```

2. Create and activate a virtual environment:

    ```bash
    pipenv shell
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Apply database migrations:

    ```bash
    python manage.py migrate
    ```

5. Create a superuser (admin) to access the Django admin interface:

    ```bash
    python manage.py createsuperuser
    ```

6. Run the development server:

    ```bash
    python manage.py runserver
    ```

The API will be available at [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

## API Endpoints

The TickIt API provides the following endpoints:

### Venues:

- GET /api/venues/: List all venues.
- POST /api/venues/: Create a new venue.
- GET /api/venues/<venue_id>/: Retrieve a specific venue.
- PUT /api/venues/<venue_id>/: Update a specific venue.
- DELETE /api/venues/<venue_id>/: Delete a specific venue.

### Events:

- GET /api/events/: List all events.
- POST /api/events/: Create a new event.
- GET /api/events/<event_id>/: Retrieve a specific event.
- PUT /api/events/<event_id>/: Update a specific event.
- DELETE /api/events/<event_id>/: Delete a specific event.



## Django Admin Interface

You can access the Django admin interface at [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/). Use your superuser credentials to log in and manage venues and events through the admin panel.

## Contributing

Contributions to the TickIt Backend API are welcome! If you find a bug, have a feature request, or want to improve the code, feel free to open an issue or submit a pull request.
