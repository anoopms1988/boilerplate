import logging

from core import errors as err, helper
from wkhtmltopdf.views import PDFTemplateResponse

logger = logging.getLogger(__name__)

def generate_wkhtml_response(data, template, orientation='landscape', header="pdf_header.html",
                             footer='pdf_footer.html'):
    """

    :param data:
    :param template:
    :param orientation:
    :param header:
    :param footer:
    :return:
    """
    try:
        response = PDFTemplateResponse(request=None,
                                 template=template,
                                 header_template=header,
                                 footer_template=footer,
                                 context={'data': data},
                                 show_content_in_browser=False,
                                 cmd_options={'orientation': orientation, 'header-spacing': 5, 'footer-spacing': 5,
                                              'javascript-delay': 1000})
        return response
    except Exception as e:
        logger.error(e.message)
        raise err.ValidationError(*(e.message, 400))
