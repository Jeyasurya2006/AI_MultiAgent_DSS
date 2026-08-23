from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet


def generate_pdf(analysis, recommendations, prediction, next_month):

    doc = SimpleDocTemplate("reports/Sales_Report.pdf")

    styles = getSampleStyleSheet()

    story = []

    story.append(
        Paragraph(
            "<b>AI Multi-Agent Decision Support System</b>",
            styles["Title"]
        )
    )

    story.append(
        Paragraph(
            f"Total Sales: Rs. {analysis['Total Sales']:,.0f}",
            styles["BodyText"]
        )
    )

    story.append(
        Paragraph(
            f"Average Sales: Rs. {analysis['Average Sales']:,.2f}",
            styles["BodyText"]
        )
    )

    story.append(
        Paragraph(
            f"Highest Sale: Rs. {analysis['Highest Sale']:,.0f}",
            styles["BodyText"]
        )
    )

    story.append(
        Paragraph(
            f"Lowest Sale: Rs. {analysis['Lowest Sale']:,.0f}",
            styles["BodyText"]
        )
    )

    story.append(
        Paragraph(
            "<br/><b>Recommendations</b>",
            styles["Heading2"]
        )
    )

    for rec in recommendations:
        story.append(
            Paragraph(
                "• " + rec,
                styles["BodyText"]
            )
        )

    story.append(
        Paragraph(
            "<br/><b>Prediction</b>",
            styles["Heading2"]
        )
    )

    story.append(
        Paragraph(
            f"Predicted Month {next_month} Sales: Rs. {prediction:,.2f}",
            styles["BodyText"]
        )
    )

    doc.build(story)