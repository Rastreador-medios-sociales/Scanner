from fpdf import FPDF


class PEDEFE:

    def __init__(self):
        self.pdf = FPDF()
        self.nombre = ""


    def exportaPDF(self, titulo, contenido):
        self.pdf.add_page()
        self.pdf.set_font('Arial', 'B', 16)
        for x in range(0,len(contenido)):
            self.pdf.cell(40, 10, contenido[x])
            self.pdf.ln()

        self.nombre = titulo
        self.pdf.output(titulo, 'F')
        return self.nombre