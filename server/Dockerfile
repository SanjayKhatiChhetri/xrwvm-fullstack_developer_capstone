FROM python:3.12.0-slim-bookworm
    # Set environment variables
    ENV PYTHONBUFFERED 1
    ENV PYTHONWRITEBYTECODE 1
    ENV APP=/app

    # Change the workdir.
    WORKDIR $APP

    # Install the requirements
    COPY requirements.txt $APP
    RUN pip3 install -r requirements.txt

    # Copy the rest of the files
    COPY . $APP

    # Expose port 8000
    EXPOSE 8000

    # Make the entrypoint script executable
    RUN chmod +x /app/entrypoint.sh

    # Set the entrypoint
    ENTRYPOINT ["/bin/bash","/app/entrypoint.sh"]

    # Command to start the application
    CMD ["gunicorn", "--bind", ":8000", "--workers", "3", "djangoproj.wsgi"]