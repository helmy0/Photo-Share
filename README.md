# PhotoShare

Welcome to PhotoShare! PhotoShare is a containarized Django-based web application that allows users to manage photos by adding, deleting, viewing, and organizing them into categories. The application stores photos on AWS for efficient management and accessibility.

## Features

- Add photos: Users can upload their photos to the platform.
- Delete photos: Users can remove photos they no longer want to share.
- View photos: Users can browse through the collection of photos.
- Categorize photos: Users can attach photos to specific categories for better organization.

## Technologies Used

- Python Django: Backend framework for developing the web application.
- AWS: Cloud storage service used for storing photos.
- Docker: Containerization technology used for packaging the application and its dependencies.

## Dockerization

To run the PhotoShare application using Docker, follow these steps:

1. Clone the PhotoShare repository to your local machine:
```
git clone https://github.com/helmy0/photoshare.git
```

2. Navigate to the project directory:
```
cd photoshare
```

3. Build the Docker image

```
docker build -t photoshare .
```


4. Run the Docker container:
```
docker run -p 8000:8000 photoshare
```


5. Access the application in your web browser at `http://localhost:8000`.

Thank you for considering PhotoShare! 📷
