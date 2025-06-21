import webbrowser

from fpdf import FPDF


class PdfReport:
    """
    Creates a Pdf file that contains data about the flatmates such as their names, their due amount, and the period of the bill.
    """
    def __init__(self, filename):
        self.filename = filename

    def generate(self, bill):
        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()
        pdf.image("files/house.png", w=30, h=30)
        pdf.set_font('Arial', 'B', 16)
        pdf.cell(0, 20, 'Flatmate Bill', align='C', ln=1)
        pdf.set_font('Arial', 'B', 14)
        pdf.cell(100, 20, 'Period:')
        pdf.cell(100, 20, bill.period, ln=1)
        pdf.set_font('Arial', size=12)
        for flatmate in bill.flatmates:
            pdf.cell(100, 20, flatmate.name)
            pdf.cell(100, 20, f"{flatmate.pays(bill):.4}", ln=1)
        pdf.output(self.filename, 'F')
