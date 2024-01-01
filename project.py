from pypdf import PdfReader, PdfWriter
import glob
pdfs = [f for f in glob.glob("*.pdf") if f != 'abc.pdf']
writer = PdfWriter()
for pdf in pdfs:
    reader = PdfReader(pdf)
    cover = reader.pages[0]
    writer.add_page(cover)
    writer.add_outline_item(title=pdf, page_number=writer.pages[-1])
    if pdf == "Nikhil Menon - Planning Democracy_ Modern India's Quest for Development-Cambridge University Press (2022).pdf":
        for page in reader.pages:
            if 'women' in page.extract_text().lower():
                    p = writer.add_page(page=page)
    else:
        for page in reader.pages:
            if 'rukmini' in page.extract_text().lower():
                    p = writer.add_page(page=page)
writer.write("abc.pdf")