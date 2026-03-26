from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

def generate_welcome_kit(data):
    file_name = f"welcome_{data['name'].replace(' ', '_')}.pdf"

    doc = SimpleDocTemplate(file_name)
    styles = getSampleStyleSheet()

    content = []

    content.append(Paragraph("🏦 Welcome to Our Bank", styles['Title']))
    content.append(Spacer(1, 10))

    content.append(Paragraph(f"Name: {data['name']}", styles['Normal']))
    content.append(Paragraph(f"Account Type: Savings", styles['Normal']))
    content.append(Paragraph(f"Initial Deposit: ₹{data['amount']}", styles['Normal']))
    content.append(Spacer(1, 10))

    content.append(Paragraph("Your account has been successfully created.", styles['Normal']))
    content.append(Paragraph("Thank you for banking with us!", styles['Normal']))

    doc.build(content)

    return file_name
