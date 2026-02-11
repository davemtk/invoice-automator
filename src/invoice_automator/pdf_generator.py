from fpdf import FPDF

class InvoicePDF :
    def __init__(self, header, footer):
        self.header = header
        self.footer = footer

    