#!/usr/bin/env python3
import random
import io
from reportlab.pdfgen import canvas
from pypdf import PdfWriter, PdfReader


def congruencia(dsc_pdf_name, multiplicand):
    '''
    Create a file with Congruence exercises using a random function
    dsc_pdf_name - name of output pdf file
    multiplicand - max number in exercises
    '''

    packet = io.BytesIO()
    can = canvas.Canvas(packet)

    lines_count = 16
    axis_y = 800
    axis_x = 20
    while lines_count > 0:
        for _column in range(5):
            can.drawString(axis_x, axis_y, f'{random.randint(0, multiplicand)}   {random.randint(0, multiplicand)}')
            axis_x += 120

        lines_count -= 1
        axis_y -= 50
        axis_x = 20
    can.save()

    # move to the beginning of the StringIO buffer
    packet.seek(0)

    # create a new PDF with Reportlab
    new_pdf = PdfReader(packet)
    output = PdfWriter()
    output.add_page(new_pdf.pages[0])

    # finally, write "output" to a real file
    output_stream = open(dsc_pdf_name, "wb")
    output.write(output_stream)
    output_stream.close()


if __name__ == '__main__':
    congruencia('tabla_de_congruencia.pdf', 100)

