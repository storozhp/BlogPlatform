# Blog Platform

This is a blog platform built using Flask, Python, and MongoDB. The platform allows users to register, login, create posts, and view posts. JWT is used for authentication without relying on the Flask-JWT library. The project includes features like flashing messages and a dynamic navbar that changes based on user login status.

## Features

### Implemented

- [x] User registration
- [x] User login with JWT authentication
- [x] User logout
- [x] Dynamic navbar that updates based on login status

### Planned

- [ ] Editing and deleting blog posts
- [ ] User profile pages
- [ ] Deployment to a production server
- [ ] Creating and viewing blog posts
- [ ] Protected routes accessible only to authenticated users

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

You need to have the following software installed on your machine:

- Python 3.12
- MongoDB
- pip (Python package installer)

### Installing

1. **Clone the repository:**

    ```bash
    git clone https://github.com/storozhp/BlogPlatform.git
    cd BlogPlatform
    ```

2. **Create a virtual environment:**

    ```bash
    python -m venv venv
    ```

3. **Activate the virtual environment:**

    - On Windows:

        ```bash
        venv\Scripts\activate
        ```

    - On macOS/Linux:

        ```bash
        source venv/bin/activate
        ```

4. **Install the required packages:**

    ```bash
    pip install -r requirements.txt
    ```

5. **Run MongoDB:**

    Make sure MongoDB is running on its default port (27017).

6. **Set up environment variables:**

    Change name file `.env.example` to `.env` and fill MongoDB link, JWT secret key

7. **Run the application:**

    ```bash
    python main.py
    ```

8. **Open your browser and navigate to:**

    ```
    http://127.0.0.1:5000/
    ```

### Usage

- To register a new user, click on the "Register" link in the navbar and fill out the form.
- To login, click on the "Login" link in the navbar and provide your credentials.
- Once logged in, you can create a new post by clicking the "New Post" link in the navbar.
- View all posts on the homepage.


## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Create a new Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

