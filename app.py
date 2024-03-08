import streamlit as st
import json
import random
from docx import Document
from docx.shared import Pt
from docx.shared import Inches
from datetime import datetime
import base64
import io
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT
st.set_page_config(
    page_title="Random Prompts Generator",
    page_icon='⚡️',
    layout="wide"
)
import style_functions as sf
sf.hide_all()
#sf.button_color()
#sf.footer_style_custom_position()
sf.custom_style()
def load_categories_from_json(file_path):
    with open(file_path, 'r') as file:
        categories = json.load(file)
    return categories

# Function to generate random choice from a category
def generate_random_item(category):
    if category in categories:
        items = categories[category]["random"]
        return random.choice(items)
    else:
        return None
#pip install urllib3==1.26.6
#documnet
def document_sd(prompts):

    doc = Document()
    # Set margins for the document (in inches)
    sections = doc.sections
    for section in sections:
        section.left_margin = Inches(0.8)
        section.right_margin = Inches(0.8)
        section.top_margin = Inches(0.5)
        section.bottom_margin = Inches(0.5)

    # Title
    title = doc.add_heading("Prompts", level=1)
    title.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER

    # Header
    header = doc.sections[0].header
    header_paragraph = header.paragraphs[0]
    header_paragraph.text = "Header - Your Company Name"

    # Footer
    footer = doc.sections[0].footer
    footer_paragraph = footer.paragraphs[0]
    footer_paragraph.text = "Footer - Copyright © Your Company"

    # Adding numbered prompts manually
    for i, prompt in enumerate(prompts, start=1):
        para = doc.add_paragraph()
        #para.add_run(f"{i}. ").bold = True
        #para.add_run(f"{i}. ").bold = True
        para.add_run(prompt)

    # Save the document
    #doc.save("prompts.docx")
    stamp_time = datetime.now().strftime("%Y%m%d%H%M%S")
    docx_file = f"{stamp_time}_SD_Prompts.docx"
    docx_content = io.BytesIO()
    doc.save(docx_content)
    docx_content.seek(0)
        
    st.download_button('Download file', docx_content, key='download_button2', file_name=f"{docx_file}", mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document")

    st.write(f"Prompts saved to prompts.docx: {len(prompts)}")

# Streamlit UI
st.title("Choose Items")

json_file_path = "categories.json"
categories = load_categories_from_json(json_file_path)

category1 = st.selectbox("Select Type of Photography", categories["Type of photography"]["random"])
category2 = st.selectbox("Select Ethnicity", categories["Ethnicity"]["random"])
category3 = st.selectbox("Select Age", categories["Age"]["random"])
category4 = st.selectbox("Select Genre", categories["Genre"]["random"])
category5 = st.selectbox("Select Hair | Length", categories["Hair | Length"]["random"])
category6 = st.selectbox("Select Hair | Woman style", categories["Hair | Woman style"]["random"])
category7 = st.selectbox("Select Hair | man style", categories["Hair | Man style"]["random"])
category8 = st.selectbox("Select Hair | Color", categories["Hair | Color"]["random"])
category9 = st.selectbox("Select Hair | Accessories", categories["Hair | Accessories"]["random"])
category10 = st.selectbox("Select Eyes | Shape", categories["Eyes | Shape"]["random"])
category11 = st.selectbox("Select Eyes | Color", categories["Eyes | Color"]["random"])
category12 = st.selectbox("Select Eyes | Accessories", categories["Eyes | Accessories"]["random"])
category13 = st.selectbox("Select Lips | Shape", categories["Lips | Shape"]["random"])
category14 = st.selectbox("Select Lips | Color", categories["Lips | Color"]["random"])
category15 = st.selectbox("Select Face | Shape", categories["Face | Shape"]["random"])
category16 = st.selectbox("Select Face | Make-up", categories["Face | Make-up"]["random"])
category17 = st.selectbox("Select Face | Emotion", categories["Face | Emotion"]["random"])
category18 = st.selectbox("Select Body | Shape", categories["Body | Shape"]["random"])
category19 = st.selectbox("Select Body | Pose", categories["Body | Pose"]["random"])
category20 = st.selectbox("Select Body | Action", categories["Body | Action"]["random"])
category21 = st.selectbox("Select Clothes style", categories["Clothes style"]["random"])
category22 = st.selectbox("Select Lighting | Directional", categories["Lighting | Directional"]["random"])
category23 = st.selectbox("Select Lighting | Effect", categories["Lighting | Effect"]["random"])
category24 = st.selectbox("Select Time of day", categories["Time of day"]["random"])
category25 = st.selectbox("Select Weather", categories["Weather"]["random"])
category26 = st.selectbox("Select Photo backdrop", categories["Photo backdrop"]["random"])
category27 = st.selectbox("Select Environment | Background", categories["Environment | Background"]["random"])
category28 = st.selectbox("Select Camera", categories["Camera"]["random"])
category29 = st.selectbox("Select Camera distance", categories["Camera distance"]["random"])
category30 = st.selectbox("Select Camera angle", categories["Camera angle"]["random"])



choice_type = st.radio("Select choice type", ("Specific", "Random"))

num_prompts = st.number_input("Enter the number of prompts to generate", min_value=1, step=1, value=1)

prompts = []

if category1 and category2 and category3:
    for i in range(num_prompts):
        if choice_type == "Specific":
            prompts.append(f"{i+1}. Prompt: {category1}, {category2}, {category3}, {category4}, {category5}, {category6}, {category7}, {category8}, {category9}, {category10}, {category11}, {category12}, {category13}, {category14}, {category15}, {category16}, {category17}, {category18}, {category19}, {category20}, {category21}, {category22}, {category23}, {category24}, {category25}, {category26}, {category27}, {category28}, {category29}, {category30}")
        elif choice_type == "Random":
            random_category1 = generate_random_item("Type of photography")
            random_category2 = generate_random_item("Ethnicity")
            random_category3 = generate_random_item("Age")
            random_category4 = generate_random_item("Genre")
            random_category5 = generate_random_item("Hair | Length")
            random_category6 = generate_random_item("Hair | Woman style")
            random_category7 = generate_random_item("Hair | Man style")
            random_category8 = generate_random_item("Hair | Color")
            random_category9 = generate_random_item("Hair | Accessories")
            random_category10 = generate_random_item("Eyes | Shape")
            random_category11 = generate_random_item("Eyes | Color")
            random_category12 = generate_random_item("Eyes | Accessories")
            random_category13 = generate_random_item("Lips | Shape")
            random_category14 = generate_random_item("Lips | Color")
            random_category15 = generate_random_item("Face | Shape")
            random_category16 = generate_random_item("Face | Make-up")
            random_category17 = generate_random_item("Face | Emotion")
            random_category18 = generate_random_item("Body | Shape")
            random_category19 = generate_random_item("Body | Pose")
            random_category20 = generate_random_item("Body | Action")
            random_category21 = generate_random_item("Clothes style")
            random_category22 = generate_random_item("Lighting | Directional")
            random_category23 = generate_random_item("Lighting | Effect")
            random_category24 = generate_random_item("Time of day")
            random_category25 = generate_random_item("Weather")
            random_category26 = generate_random_item("Photo backdrop")
            random_category27 = generate_random_item("Environment | Background")
            random_category28 = generate_random_item("Camera")
            random_category29 = generate_random_item("Camera distance")
            random_category30 = generate_random_item("Camera angle")


            
                
            prompts.append(f"{random_category1}, {random_category2}, {random_category3}, {random_category4}, {random_category5}, {random_category6}, {random_category7}, {random_category8}, {random_category9}, {random_category10}, {random_category11}, {random_category12}, {random_category13}, {random_category14}, {random_category15}, {random_category16}, {random_category17}, {random_category18}, {random_category19}, {random_category20}, {random_category21}, {random_category22}, {random_category23}, {random_category24}, {random_category25}, {random_category26}, {random_category27}, {random_category28}, {random_category29}, {random_category30}")
document_sd(prompts)
# Save prompts to Word document
