# Fullstack Developer Capstone Project

This project is a fullstack application built using Django for the backend. Below are the steps to set up and run the project.

## Prerequisites

- Python 3.x
- pip (Python package installer)

## Setup Instructions

### Running Server

1. **Clone the repository:**

    ```bash
    
    git clone https://github.com/SanjaykhatiChhetri/xrwvm-fullstack_developer_capstone.git

    cd xrwvm-fullstack_developer_capstone/server
    ```
2. **Run the following to set up the Django environment:**
    - Install virtualenv:
    - Create a virtual environment:
    - Activate the virtual environment:
    ```bash
    pip install virtualenv
    virtualenv djangoenv
    source djangoenv/bin/activate
    ```
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
    python3 -m pip install -U -r requirements.txt
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
### Ruuning Backend & Database as container

1. Change to the directory
    ```
    cd /home/project/xrwvm-fullstack_developer_capstone/server/database
    ```

2. Run the following command to build the Docker app. Remember to do this every time you make changes to app.js:
    ```
    docker build . -t nodeapp
    ```

3. The docker-compose.yml has been created to run two containers, one for Mongo and the other for the Node app. Run the following command to run the server:
    ```
    docker-compose up
    ```

### Run migrations for the models.
```
python3 manage.py makemigrations
python3 manage.py migrate --run-syncdb
```
### Deploying Sentiment Analysis on Code Engine as a Microservice

1. Change to the `server/djangoapp/microservices` directory in the Code Engine CLI:
```
cd xrwvm-fullstack_developer_capstone/server/djangoapp/microservices
```

2. You have been provided with `sentiment_analyzer.py` which uses NLTK for sentiment analysis. You are also provided with a `Dockerfile` which you will use to deploy this service in Code Engine and consume it as a microservice. Take a look at these files.

3. Run the following command to build the sentiment analyzer app:
```
docker build . -t us.icr.io/${SN_ICR_NAMESPACE}/senti_analyzer
```
*Note: The Code Engine instance is transient and is attached to your lab space username.*

4. Push the Docker image by running the following command:
```
docker push us.icr.io/${SN_ICR_NAMESPACE}/senti_analyzer
```

5. Deploy the `senti_analyzer` application on Code Engine:
```
ibmcloud ce application create --name sentianalyzer --image us.icr.io/${SN_ICR_NAMESPACE}/senti_analyzer --registry-secret icr-secret --port 5000
```

6. Connect to the URL that is generated to access the microservices and check if the deployment is successful.

7. If the application deployment verification was successful, attach `/analyze/Fantastic services` to the URL in the browser to see if it returns positive. 

### Command to create a superuser.

```
python3 manage.py createsuperuser
```

### Build the client-side Application 

1. Open a New Terminal and switch to the client directory.
```
cd /home/project/xrwvm-fullstack_developer_capstone/server/frontend
```

2. Install all required packages.
```
npm install
```

3. Run the following command to build the client.
```
npm run build
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
