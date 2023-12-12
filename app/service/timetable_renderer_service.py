from jinja2 import Environment, PackageLoader, select_autoescape
from io import BytesIO
from xhtml2pdf import pisa

from app.model import TimeTable


class TimeTableRendererService:
    timetable: TimeTable
    enable_logging: bool

    def __init__(self, timetable: TimeTable, enable_logging: bool = False):
        self.timetable = timetable
        self.enable_logging = enable_logging

    def render(self, template: str, output_filename: str = "") -> None:
        source_html = self._render_html(template)
        self._render_pdf(source_html, output_filename or f"{self.timetable.timetable_id}.pdf")

    def _render_html(self, template: str) -> str:
        env = Environment(
            loader=PackageLoader("app", "template"),
            autoescape=select_autoescape()
        )

        template = env.get_template(f"{template}.jinja")
        data = {
            'teacher': self.timetable.teacher,
            'week_a': self.timetable.week_a,
            'week_b': self.timetable.week_b,
        }

        return template.render(**data)

    def _render_pdf(self, source_html: str, output_filename: str) -> None:
        with open(output_filename, "w+b") as result_file:
            pisa.CreatePDF(BytesIO(source_html.encode('utf-8')), dest=result_file, encoding='utf-8')
            pisa.showLogging() if self.enable_logging else None
