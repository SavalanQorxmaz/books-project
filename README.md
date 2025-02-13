Task: Build a Simple API for a Library Using Django REST Framework

Objective

Create a simple API using Django REST Framework (DRF) that allows users to retrieve a list of all books and details of a specific book.

Requirements
 1. Set up Django Project
 • Create a new Django project and a Django app named library.
 • Install and configure Django REST Framework.
 2. Create a Book Model
 • The model should include at least the following fields:
 • title (CharField)
 • author (CharField)
 • description (TextField)
 • published_date (DateField)
 • slug (SlugField, unique=True)
 3. Create API Endpoints
 • Implement the following GET endpoints:
 • GET /books/ → Returns a list of all books.
 • GET /books/{id}/ → Returns details of a specific book by its ID.
 • GET /book/{slug}/ → (Extra task) Returns details of a book by its slug.
 4. Implement Serializers
 • Create a BookSerializer to convert Book model instances into JSON format.
 5. Implement Views
 • Use Django REST Framework’s APIView or GenericAPIView with appropriate mixins for handling GET requests.
 6. Set up URLs
 • Define routes for the API endpoints in urls.py.
 7. Testing
 • Use Django’s built-in development server to test the API using tools like Postman or Django’s browsable API interface.

Bonus
 • Add pagination support for the /books/ endpoint.
 • Use ordering to allow sorting by title or published_date.
