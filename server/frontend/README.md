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

p@$$word

# Getting Started with Create React App
This project was bootstrapped with [Create React App](https://github.com/facebook/create-react-app).

## Available Scripts

In the project directory, you can run:

### `npm start`

Runs the app in the development mode.\
Open [http://localhost:3000](http://localhost:3000) to view it in your browser.

The page will reload when you make changes.\
You may also see any lint errors in the console.

### `npm test`

Launches the test runner in the interactive watch mode.\
See the section about [running tests](https://facebook.github.io/create-react-app/docs/running-tests) for more information.

### `npm run build`

Builds the app for production to the `build` folder.\
It correctly bundles React in production mode and optimizes the build for the best performance.

The build is minified and the filenames include the hashes.\
Your app is ready to be deployed!

See the section about [deployment](https://facebook.github.io/create-react-app/docs/deployment) for more information.

### `npm run eject`

**Note: this is a one-way operation. Once you `eject`, you can't go back!**

If you aren't satisfied with the build tool and configuration choices, you can `eject` at any time. This command will remove the single build dependency from your project.

Instead, it will copy all the configuration files and the transitive dependencies (webpack, Babel, ESLint, etc) right into your project so you have full control over them. All of the commands except `eject` will still work, but they will point to the copied scripts so you can tweak them. At this point you're on your own.

You don't have to ever use `eject`. The curated feature set is suitable for small and middle deployments, and you shouldn't feel obligated to use this feature. However we understand that this tool wouldn't be useful if you couldn't customize it when you are ready for it.

## Learn More

You can learn more in the [Create React App documentation](https://facebook.github.io/create-react-app/docs/getting-started).

To learn React, check out the [React documentation](https://reactjs.org/).

### Code Splitting

This section has moved here: [https://facebook.github.io/create-react-app/docs/code-splitting](https://facebook.github.io/create-react-app/docs/code-splitting)

### Analyzing the Bundle Size

This section has moved here: [https://facebook.github.io/create-react-app/docs/analyzing-the-bundle-size](https://facebook.github.io/create-react-app/docs/analyzing-the-bundle-size)

### Making a Progressive Web App

This section has moved here: [https://facebook.github.io/create-react-app/docs/making-a-progressive-web-app](https://facebook.github.io/create-react-app/docs/making-a-progressive-web-app)

### Advanced Configuration

This section has moved here: [https://facebook.github.io/create-react-app/docs/advanced-configuration](https://facebook.github.io/create-react-app/docs/advanced-configuration)

### Deployment

This section has moved here: [https://facebook.github.io/create-react-app/docs/deployment](https://facebook.github.io/create-react-app/docs/deployment)

### `npm run build` fails to minify

This section has moved here: [https://facebook.github.io/create-react-app/docs/troubleshooting#npm-run-build-fails-to-minify](https://facebook.github.io/create-react-app/docs/troubleshooting#npm-run-build-fails-to-minify)
