import os
from fpdf import FPDF
from fpdf.enums import XPos, YPos

class PDF(FPDF):
    def header(self):
        self.set_font("Helvetica", "B", 16)
        self.cell(0, 10, "Vessel Operations Web Application", new_x=XPos.LMARGIN, new_y=YPos.NEXT, align="C")
        self.ln(10)

    def chapter_title(self, title):
        self.set_font("Helvetica", "B", 14)
        self.cell(0, 10, title, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.ln(4)

    def chapter_body(self, body):
        self.set_font("Helvetica", "", 12)
        self.multi_cell(0, 8, body)
        self.ln(6)

pdf = PDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()

# Title Page
pdf.set_font("Helvetica", "B", 20)
pdf.cell(0, 20, "Vessel Operations Web Application", new_x=XPos.LMARGIN, new_y=YPos.NEXT, align="C")
pdf.ln(10)
pdf.set_font("Helvetica", "", 14)
pdf.cell(0, 10, "Showcasing Agentic AI in Maritime Operations", new_x=XPos.LMARGIN, new_y=YPos.NEXT, align="C")
pdf.ln(20)

# Insert Screenshot Pages for multiple screenshots
screenshot_files = [
    "screenshot1.png",
    "screenshot2.png",
    "screenshot3.png",
    "screenshot4.png",
    "screenshot5.png"
]
for idx, screenshot_path in enumerate(screenshot_files, 1):
    pdf.add_page()
    pdf.set_font("Helvetica", "B", 16)
    pdf.cell(0, 10, f"Application Screenshot {idx}", new_x=XPos.LMARGIN, new_y=YPos.NEXT, align="C")
    pdf.ln(10)
    if os.path.exists(screenshot_path):
        try:
            # Place image at the top, below the title, and fit width to 150 (adjust y to avoid overlap)
            pdf.image(screenshot_path, x=30, y=30, w=150)
            pdf.ln(100)  # Add space after image
        except Exception as e:
            pdf.set_font("Helvetica", "B", 14)
            pdf.set_text_color(200, 0, 0)
            pdf.cell(0, 20, f"Error adding screenshot: {e}", new_x=XPos.LMARGIN, new_y=YPos.NEXT, align="C")
            pdf.set_text_color(0, 0, 0)
            pdf.ln(20)
    else:
        pdf.set_font("Helvetica", "B", 14)
        pdf.set_text_color(200, 0, 0)
        pdf.cell(0, 20, f"Screenshot '{screenshot_path}' not found in script directory.", new_x=XPos.LMARGIN, new_y=YPos.NEXT, align="C")
        pdf.set_text_color(0, 0, 0)
        pdf.ln(20)

# Start the rest of the content on a new page to avoid overlap
pdf.add_page()

# Home Page
pdf.chapter_title("Home Page")
pdf.chapter_body("The Home page provides a welcoming interface and quick access to all major features of the application.")

# Dashboard
pdf.chapter_title("Dashboard")
pdf.chapter_body("The Dashboard displays real-time and historical metrics, including vessel status, fuel consumption, emissions, and delays, using interactive charts.")

# Logistics
pdf.chapter_title("Logistics")
pdf.chapter_body("The Logistics page offers real-time tracking, predictive forecasting, and automated processing for shipments, improving supply chain visibility.")

# Sustainability
pdf.chapter_title("Sustainability")
pdf.chapter_body("The Sustainability page reports on fuel consumption, emissions, and resource allocation, supporting green shipping initiatives.")

# Vessel Operations
pdf.chapter_title("Vessel Operations")
pdf.chapter_body("This page allows users to manage and monitor vessel operations, submit feedback, and view vessel lists and maps.")

# Chatbot
pdf.chapter_title("AI Assistant (Chatbot)")
pdf.chapter_body("The Chatbot page integrates an AI assistant to answer user queries, provide operational insights, and support decision-making.")

# Agentic AI Importance
pdf.chapter_title("The Importance of Agentic AI")
pdf.chapter_body(
    "Agentic AI refers to artificial intelligence systems that can act autonomously, make decisions, and proactively optimize operations. "
    "In this application, Agentic AI enables:\n"
    "- Predictive analytics for traffic, fuel, and maintenance\n"
    "- Real-time anomaly detection and proactive alerts\n"
    "- Dynamic resource allocation and route optimization\n"
    "- Intelligent assistance via the chatbot\n\n"
    "By leveraging Agentic AI, maritime operations become more efficient, resilient, and sustainable, reducing costs and improving service quality."
)

pdf.output("Vessel_Operations_Agentic_AI_Showcase.pdf")
print("PDF created: Vessel_Operations_Agentic_AI_Showcase.pdf")