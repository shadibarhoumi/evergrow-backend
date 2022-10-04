from flask import Blueprint, request, make_response, render_template, current_app
import pdfkit, os, subprocess

bp = Blueprint('pdf_generation', __name__)

@bp.route("/generate", methods=['POST'])
def generate_pdf():
    content = request.get_json()
    pdf = generate_numbers_pdf(content['numbers'])
    response = make_response(pdf)

    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = 'inline'
    return response

# helper that generates a pdf given a list of numbers
def generate_numbers_pdf(input_numbers):
    rendered = render_template('numbers_pdf_template.html', numbers=input_numbers)
    pdf = pdfkit.from_string(rendered, False, configuration=get_pdfkit_config(current_app.config['ENV']))
    return pdf

# helper that creates a config object for pdf generation library
def get_pdfkit_config(environment):
    binary_name = 'wkhtmltopdf' if environment == 'development' else 'wkhtmltopdf-pack'
    WKHTMLTOPDF_CMD = subprocess.Popen(['which', os.environ.get('WKHTMLTOPDF_BINARY', binary_name)], stdout=subprocess.PIPE).communicate()[0].strip()
    return pdfkit.configuration(wkhtmltopdf=WKHTMLTOPDF_CMD)
