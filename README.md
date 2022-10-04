# Flask backend for Evergrow PDF generator.

## Local installation steps
Install the server as a package: `pip install -e .`


Install dependencies: `pip install -r requirements.txt`


Run server locally: `flask run`


Run tests with `pytest`.


You should get test output that looks like this:
![image](https://user-images.githubusercontent.com/1471895/193717154-6605f368-6319-4190-8962-d370e7e6b254.png)

## Generating a PDF
Make a POST request to `127.0.0.1:5000/generate` with a payload that looks like `{ numbers: [123, 345] }`, with your numbers of choice in the array.