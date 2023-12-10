from io import BytesIO
from xhtml2pdf import pisa
import chevron

render_pdf = True

with open('./template/timetable1.mustache', 'r') as template_file:
    data = {}
    source_html = chevron.render(template_file, data)

with open('./tmp/timetable1.html', 'w') as rendered_template_file:
    rendered_template_file.write(source_html)

if render_pdf:
    result_file = open("out.pdf", "w+b")

    pisa_status = pisa.CreatePDF(BytesIO(source_html.encode('utf-8')), dest=result_file, encoding='utf-8')
    pisa.showLogging()

    result_file.close()
