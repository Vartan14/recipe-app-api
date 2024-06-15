# Recipe App API

This repository contains a backend API for managing recipes using Python, Django REST framework, PostgreSQL, and Docker. The API supports user authentication, CRUD operations for recipes, ingredient handling, tagging, and is developed following Test-Driven Development (TDD) principles. Swagger is integrated for clear API documentation.

## Features

- User authentication (registration, login, logout)
- CRUD operations for recipes (Create, Read, Update, Delete)
- Management of ingredients associated with recipes
- Tagging system for categorizing recipes
- Comprehensive unit tests following Test-Driven Development (TDD)
- API documentation using Swagger

## Technologies Used

- Python
- Django REST framework
- PostgreSQL
- Docker

## Getting Started

To get the project up and running on your local machine, follow these steps:

### Prerequisites

- Docker
- Git

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Vartan14/recipe-app-api.git
   cd recipe-app-api
   ```

2. Build and run the Docker containers:

   ```bash
   docker-compose up --build
   ```

3. The API should now be accessible at `http://localhost:8000`.

### Usage

- Access the Swagger UI documentation at `http://localhost:8000/swagger/` to explore available endpoints, request/response formats, and authentication methods.
- Use tools like Postman or cURL to interact with the API endpoints for managing recipes, ingredients, and user authentication.

### Running Tests

To run the unit tests:

```bash
docker-compose run --rm app sh -c "python manage.py test && flake8"
```

This command will execute the unit tests and lint the codebase using Flake8.

### Deployment

For deployment, ensure that you have Docker and a production-ready database setup. Update the necessary environment variables in `docker-compose.yml` and `settings.py` files as per your deployment environment.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any enhancements, bug fixes, or new features. Ensure that your code is well-tested and follows the project's coding standards.

## Contact

For any questions or feedback, feel free to reach out:

- Email: vartankaramian1414@gmail.com
- GitHub: Vartan14 (https://github.com/Vartan14)
