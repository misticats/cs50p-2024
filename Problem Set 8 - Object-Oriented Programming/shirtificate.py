from fpdf import FPDF

class PDF(FPDF):
    def __init__(self):
        super().__init__('P', 'mm', 'A4')
        self.add_page()
        self.set_auto_page_break(auto=1, margin=15)

    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'CS50 Shirtificate', 0, 1, 'C')

    def __str__(self):
        return f"PDF Object: {self.page_no()} pages"

def create_shirtificate(name):
    pdf = PDF()
    pdf.image('shirtificate.png', x=50, y=60, w=110)

    pdf.set_y(120)
    pdf.set_font('Arial', 'B', 20)
    pdf.set_text_color(255, 255, 255)
    pdf.cell(0, 10, name, 0, 1, 'C')

    pdf.output('shirtificate.pdf')
    return pdf

def main():
    name = input("Enter your name for the shirtificate: ")
    shirtificate = create_shirtificate(name)
    print("Shirtificate created successfully!")
    print(shirtificate)

if __name__ == '__main__':
    main()
