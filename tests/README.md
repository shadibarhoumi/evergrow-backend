# Evergrow PDF Generator

## Local installation steps
Install the server as a package: `pip install -e .`

Install dependencies: `pip install -r requirements.txt`

Run the server: `flask --app evergrowpdf --debug run `

To run tests: `pytest`

## To generate a pdf
Make a `POST` request to `127.0.0.1/generate` with a payload of `{ numbers: [123, 345]}`, with your numbers of choice in the array.