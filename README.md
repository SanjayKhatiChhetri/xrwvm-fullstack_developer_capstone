# run locally 

# Fullstack Developer Capstone Project

This project is a fullstack application built using Django for the backend. Below are the steps to set up and run the project.

## Prerequisites

- Python 3.x
- pip (Python package installer)

## Setup Instructions

1. **Clone the repository:**

    ```bash
    
    git clone https://github.com/SanjaykhatiChhetri/xrwvm-fullstack_developer_capstone.git

    cd xrwvm-fullstack_developer_capstone/server
    ```

2. **Install virtualenv:**

    ```bash
    pip install virtualenv
    ```

3. **Create a virtual environment:**

    ```bash
    virtualenv djangoenv
    ```

4. **Activate the virtual environment:**

    - On Windows:

        ```bash
        djangoenv\Scripts\activate
        ```

    - On macOS and Linux:

        ```bash
        source djangoenv/bin/activate
        ```

5. **Install the required packages:**

    ```bash
    pip install -r requirements.txt
    ```

6. **Apply migrations:**

    ```bash
    python3 manage.py makemigrations
    python3 manage.py migrate
    ```

7. **Run the development server:**

    ```bash
    python3 manage.py runserver
    ```

## Project Structure

- `server/`: Contains the Django backend code.
- `requirements.txt`: Lists the Python dependencies for the project.

## Usage

After starting the development server, you can access the application at `http://127.0.0.1:8000/`.

## Contributing

If you would like to contribute to this project, please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License.
