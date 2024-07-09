#!/usr/bin/env python3
import random
import io
from reportlab.pdfgen import canvas
from pypdf import PdfWriter, PdfReader


def tabla_de_multiplicar(dsc_pdf_name):

    packet = io.BytesIO()
    can = canvas.Canvas(packet)

    lines_count = 15
    axis_y = 800
    axis_x = 20
    while lines_count > 0:
        for i in range(5):
            can.drawString(axis_x, axis_y, f'{random.randint(0, 10)} x {random.randint(0, 10)}=')
            axis_x += 120
            print(f'{i}x{random.randint(0, 10)}')

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
    tabla_de_multiplicar('tabla_de_multiplicar.pdf')