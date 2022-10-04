import pytest
from evergrowpdf.pdf_generation import generate_numbers_pdf, get_pdfkit_config
import pdfkit

PDF_HEADER_LENGTH = 296

def test_generate_numbers_pdf_equal(client, app):
    with app.app_context():
        generated_pdf = generate_numbers_pdf([123, 456])
        body = '''
        <!DOCTYPE html>
        <html lang="en">
          <head>
            <title>Document</title>
          </head>
          <body>
            <h2>Your Numbers</h2>
            <ul>
              <li>123</li>
              <li>456</li>
            </ul>
          </body>
        </html>
        '''
        reference_pdf = pdfkit.from_string(body, False, configuration=get_pdfkit_config('development'))
        # we omit the header from the comparison because it contains a creation timestamp which
        # changes on each invocation of the pdf generation function
        assert generated_pdf[PDF_HEADER_LENGTH:] == reference_pdf[PDF_HEADER_LENGTH:]

def test_generate_numbers_pdf_not_equal(client, app):
    with app.app_context():
        generated_pdf = generate_numbers_pdf([123, 456])
        body = '''
        <!DOCTYPE html>
        <html lang="en">
          <head>
            <title>Document</title>
          </head>
          <body>
            <h2>Your Numbers</h2>
            <ul>
              <li>888</li>
              <li>999</li>
            </ul>
          </body>
        </html>
        '''
        reference_pdf = pdfkit.from_string(body, False, configuration=get_pdfkit_config('development'))
        # we omit the header from the comparison because it contains a creation timestamp which
        # changes on each invocation of the pdf generation function
        assert generated_pdf[PDF_HEADER_LENGTH:] != reference_pdf[PDF_HEADER_LENGTH:]
