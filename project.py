from pypdf import PdfReader, PdfWriter
import glob
pdfs = [f for f in glob.glob("*.pdf") if f != 'abc.pdf']
writer = PdfWriter()
for pdf in pdfs:
    search = input(f"which word to search in {pdf}(all lowercase pls): ")
    reader = PdfReader(pdf)
    cover = reader.pages[0]
    writer.add_page(cover)
    writer.add_outline_item(title=pdf, page_number=writer.pages[-1])
    for page in reader.pages:
        if search in page.extract_text().lower():
                p = writer.add_page(page=page)
writer.write("abc.pdf")