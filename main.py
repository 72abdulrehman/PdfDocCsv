from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

df = pd.read_csv("topics.csv")

#With header on 1 page
for index, row in df.iterrows():
    #header
    pdf.add_page()
    
    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(123,234,231)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1)
    pdf.line(10, 21, 200, 21)
    
    #footer
    pdf.ln(265)
    pdf.set_font(family="Times", style="I", size=8)
    pdf.set_text_color(120,230,170)
    pdf.cell(w=0, h=10, txt=row["Topic"], align="R", ln=1)
    
    for i in range(row["Pages"]-1):
        pdf.add_page()
        
        #footer
        pdf.ln(277)
        pdf.set_font(family="Times", style="I", size=8)
        pdf.set_text_color(120,230,170)
        pdf.cell(w=0, h=10, txt=row["Topic"], align="R", ln=1)
    
#With header on every page        
"""for index, row in df.iterrows():
    for i in range(row["Pages"]):
    #header
        pdf.add_page()
        
        pdf.set_font(family="Times", style="B", size=24)
        pdf.set_text_color(123,234,231)
        pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1)
        pdf.line(10, 21, 200, 21)
        
        #footer
        pdf.ln(265)
        pdf.set_font(family="Times", style="I", size=8)
        pdf.set_text_color(120,230,170)
        pdf.cell(w=0, h=10, txt=row["Topic"], align="R", ln=1)"""
    
pdf.output("output.pdf")
    