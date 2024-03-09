import streamlit as st
from streamlit_extras.stylable_container import stylable_container
import base64
def set_page_configuration():

    st.markdown("<h2 class='title center'>AI-Powered Medical Diagnostics</h2>", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: center;'>Unlocking Insights Through AI Vision: Redefining Medical Diagnostics 🌐🩺</h4>", unsafe_allow_html=True)

#with st.expander("Provide Your Google API Key"):
     #google_api_key = st.text_input("Google API Key", key="google_api_key", type="password")
def custom_style_english():
    # Custom CSS styling
    st.markdown(
    """
    <style>
        body {
            direction: ltr;
            text-align: ltr;
        }
        .center {
            text-align: center;
        }
        .footer {
            position: fixed;
            bottom: 10px;
            right: 10px;
            color: #808080;
            text-align: center;
        }
        .border {
            border: 2px solid #555;
            padding: 10px;
        }
        .reportview-container {
            background: url("logo.jpg")
        }
        .sidebar .sidebar-content {
            background: url("logo.jpg")
        }
    </style>
    """,
    unsafe_allow_html=True,
    )
def custom_style_arabic():
    # Custom CSS styling
    st.markdown(
    """
    <style>
        body {
            direction: rtl;
            text-align: rtl;
        }
        .center {
            text-align: center;
        }
        .footer {
            position: fixed;
            bottom: 10px;
            right: 10px;
            color: #808080;
            text-align: center;
        }
        .border {
            border: 2px solid #555;
            padding: 10px;
        }
        .reportview-container {
            background: url("logo.jpg")
        }
        .sidebar .sidebar-content {
            background: url("logo.jpg")
        }
    </style>
    """,
    unsafe_allow_html=True,
    )





def custom_style():
    # Custom CSS styling
    st.markdown(
    """
    <style>
        body {
            direction: ltr;
            text-align: ltr;
        }
        .center {
            text-align: center;
        }
        .footer {
            position: fixed;
            bottom: 10px;
            right: 10px;
            color: #808080;
            text-align: center;
        }
        .border {
            border: 2px solid #555;
            padding: 10px;
        }
        .reportview-container {
            background: url("logo.jpg")
        }
        .sidebar .sidebar-content {
            background: url("logo.jpg")
        }
    </style>
    """,
    unsafe_allow_html=True,
    )
def hide_elements():
    hide_style = '''
    <style>
        .reportview-container {
            margin-top: -2em;
        }
        #MainMenu {visibility:hidden;}
        footer {visibility:hidden;}
        stDeployButton {display:none;}
        .css-hi6a2p {padding-top: 0rem;}
        head {visibility:hidden;}
    </style>
    '''
    st.markdown(hide_style, unsafe_allow_html=True)
def footer_style_custom_position():
    # Customized footer with position: relative and higher z-index
    footer_style = '''
        <style>
        .footer {
             
              
            width: 100%;
                              

            color: black;
            text-align: center;  /* Adjusted text alignment to right */
            padding: 10px;
             
        background-color: #f1f1f1;

        }
        </style>
        <div class="footer">
            <p style="display: inline-block;">Copyright &copy; 2024 Falah.G.Salieh. All Rights Reserved.</p>
            <p style="float: right; margin-right: 0px;">Feedback? Contact me at <a href="mailto:falahgs07@gmail.com">falahgs07@gmail.com</a></p>
        </div>
    '''
    st.markdown(footer_style, unsafe_allow_html=True)
def background_style():
    page_bg_img = f"""
    <style>
    [data-testid="stAppViewContainer"] > .main {{
                background: linear-gradient(to right, #b3d9ff, #99c2ff);

        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        background-size: 180%;
        background-position: top left;
        background-repeat: no-repeat;
        background-attachment: local;
    }}

    [data-testid="stSidebar"] > div:first-child {{
        background: linear-gradient(to right, #b3d9ff, #99c2ff);
        box-shadow: 0 4px 4px rgba(0, 0, 0, 0.2);
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}

    [data-testid="stHeader"] {{
        background: linear-gradient(to right, #b3d9ff, #99c2ff);
        box-shadow: 0 4px 4px rgba(0, 0, 0, 0.2);
    }}

    [data-testid="stToolbar"] {{
        right: 2rem;
    }}
</style>

    """

    st.markdown(page_bg_img, unsafe_allow_html=True)
def hide_all():
    hide_streamlit_style = """
                <style>
                div[data-testid="stToolbar"] {
                visibility: hidden;
                height: 0%;
                position: fixed;
                }
                div[data-testid="stDecoration"] {
                visibility: hidden;
                height: 0%;
                position: fixed;
                }
                div[data-testid="stStatusWidget"] {
                visibility: hidden;
                height: 0%;
                position: fixed;
                }
                #MainMenu {
                visibility: hidden;
                height: 0%;
                }
                header {
                visibility: hidden;
                height: 0%;
                }
                footer {
                visibility: hidden;
                height: 0%;
                }
                </style>
                """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)
def button_color():
    m = st.markdown("""
    <style>
    div.stButton > button:first-child {
        background-color: #0099ff;
        color:#ffffff;
                background: linear-gradient(to right, #b3d9ff, #99c2ff);
border:2px solid;
    }
    div.stButton > button:hover {
        background-color: #00ff00;
        background: linear-gradient(to right, #b3d9ff, #99c2ff);

        color:#b3d9ff;
        }
        div.uploadedFiles {
    
    visibility: hidden;}
    </style>""", unsafe_allow_html=True)
def slidebar_color():
    slidebar_bg_img = f"""
    <style>
    [data-testid="stSidebar"] > div:first-child {{
            background: linear-gradient(to right, #b3d9ff, #99c2ff);
            box-shadow: 0 4px 4px rgba(0, 0, 0, 0.2);
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
</style>

    """
    st.markdown(slidebar_bg_img, unsafe_allow_html=True)

def upload():
    css = '''
    <style>
    [data-testid='stFileUploader'] {
        width: max-content;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        border-radius: 8px;
        padding: 4px;
        color:#b3d9ff;
        border:2px solid;
         
    }

    [data-testid='stFileUploader'] section {
        padding: 0;
        
    }

    [data-testid='stFileUploader'] section > input + div {
        display: none;
    }

    [data-testid='stFileUploader'] section + div {
        float: right;
        padding-top: 0;
    }
</style>

    '''

    st.markdown(css, unsafe_allow_html=True)
def upload_file():
    st.markdown('''
            <style>
                .uploadedFile {display: none}
            <style>''',
            unsafe_allow_html=True)
def hide_chat_input():
    with stylable_container(
        key="bottom_content",
        css_styles="""
            {
                position: fixed;
                bottom: 50px;
            }
            """,
    ):
        st.markdown("")  # this appears above the chat_input() element.

    st.markdown(
        """
        <style>
            .stChatFloatingInputContainer {
                bottom: 20px;
                background-color: rgba(0, 0, 0, 0)
            }
        </style>
        """,
        unsafe_allow_html=True,
    )
def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://images.unsplash.com/photo-1542281286-9e0a16bb7366");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )
import base64

#@st.cache(allow_output_mutation=True)
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_png_as_page_bg(png_file):
    bin_str = get_base64_of_bin_file(png_file)
    page_bg_img = '''
    <style>
    body {
    background-image: url("data:image/jpg;base64,%s");
    background-size: cover;
    }
    </style>
    ''' % bin_str
    
    st.markdown(page_bg_img, unsafe_allow_html=True)
    return

#set_png_as_page_bg('background.png')

def slid_bar_image():
    st.markdown(
        """
        <style>
       
       .sidebar .sidebar-content {
            background: url("https://images.unsplash.com/photo-1542281286-9e0a16bb7366")
        }
          
         .stApp {{
             background-image: url("https://images.unsplash.com/photo-1542281286-9e0a16bb7366");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )
         
def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"jpg"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )


