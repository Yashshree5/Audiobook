import pyttsx3
import PyPDF2
pdf_book = open('Harry Potter and The Sorcerer’s Stone.pdf','rb')
reading_pdf = PyPDF2.PdfFileReader(pdf_book)
pdf_pages = reading_pdf.numPages
pdf_speaker = pyttsx3.init()
speaker.say("hello prakash pattana sir i am ur audio book  perusaling a book named the ultimate secrets of total self confidence by robert anthony lets start")
for num in range(2, pdf_pages):
    choose_page = reading_pdf.getPage(num)
    pdf_text = choose_page.extractText()
speaker.say()
    pdf_speaker.runAndWait()