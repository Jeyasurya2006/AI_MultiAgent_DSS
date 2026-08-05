from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

def generate_pdf(analysis, recommendations, prediction):
    doc = SimpleDocTemplate("reports/Sales_Report.pdf")
    styles = getSampleStyleSheet()
    story = []

    story.append(Paragraph("<b>AI Multi-Agent Decision Support System</b>", styles["Title"]))

    story.append(Paragraph(f"Total Sales: {analysis['Total Sales']}", styles["BodyText"]))
    story.append(Paragraph(f"Average Sales: {analysis['Average Sales']}", styles["BodyText"]))
    story.append(Paragraph(f"Highest Sale: {analysis['Highest Sale']}", styles["BodyText"]))
    story.append(Paragraph(f"Lowest Sale: {analysis['Lowest Sale']}", styles["BodyText"]))

    story.append(Paragraph("<br/><b>Recommendations</b>", styles["Heading2"]))

    for rec in recommendations:
        story.append(Paragraph("• " + rec, styles["BodyText"]))

    story.append(Paragraph("<br/><b>Prediction</b>", styles["Heading2"]))
    story.append(Paragraph(f"Predicted Month 13 Sales: {prediction}", styles["BodyText"]))

    doc.build(story)