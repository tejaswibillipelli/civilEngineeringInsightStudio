import streamlit as st
from PIL import Image

# ---------- Gemini Simulation ----------
# def get_gemini_response(prompt):
#     return f"Analysis Result:\nBased on input '{prompt}', the system predicts a construction-related project requiring safety monitoring and proper material management."

def get_gemini_response(prompt):
    return (
        "Project appears to be a building construction site.\n"
        "Materials: Concrete and steel observed.\n"
        "Stage: Mid construction phase.\n"
        "Safety: Workers should use helmets and safety gear.\n"
        "Suggestion: Improve site safety monitoring."
    )


# ---------- Prompt ----------
def build_civil_prompt():
    return "Analyze construction image and give insights."


# ---------- Image Handling ----------
def prepare_image(uploaded_file):
    image = Image.open(uploaded_file)
    return image


# ---------- Streamlit UI ----------
st.title("🏗 Civil Engineering Insight Studio")

uploaded_file = st.file_uploader(
    "Upload Construction Image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file:
    image = prepare_image(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    if st.button("Analyze Image"):
        prompt = build_civil_prompt()
        response = get_gemini_response(prompt)

        st.subheader("Analysis Result")
        st.write(response)

# ---------- Landmark Description ----------
st.subheader("Generate Landmark Description")

landmark_name = st.text_input("Enter Landmark / Project Name")

if st.button("Generate Description"):
    if landmark_name:
        prompt = f"Describe the civil engineering landmark: {landmark_name}"

        description = get_gemini_response(prompt)

        st.subheader("Landmark Description")
        st.write(description)
    else:
        st.warning("Please enter a landmark name.")

