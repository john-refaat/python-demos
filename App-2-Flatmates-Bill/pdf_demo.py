from fpdf import FPDF

pdf = FPDF(orientation='P', unit='pt', format='A4')
pdf.add_page()
pdf.set_font('Arial', 'B', 16)
pdf.cell(0, 20, 'Hello World!', border=1, align='C', ln=1)
pdf.cell(100, 20, 'Period:', border=1)
pdf.cell(100, 20, 'March 2021', border=1, ln=1)
pdf.output('tuto1.pdf', 'F')