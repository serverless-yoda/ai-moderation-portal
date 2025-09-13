import streamlit as st
import requests
from typing import Dict

# Define FastAPI backend endpoint URL
API_URL = "http://localhost:8000/api/v1/moderate"

def moderate_text(content: str) -> Dict:
    """Send content to FastAPI moderation endpoint and return JSON response."""
    try:
        response = requests.post(API_URL, json={"content": content})
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        return {"error": str(e)}

def main():
    st.title("AI Moderation Portal - Streamlit Test Client")

    content = st.text_area("Enter text to moderate:", height=150)

    if st.button("Check Moderation"):
        if not content.strip():
            st.error("Please enter some text to moderate.")
            return

        with st.spinner("Sending to moderation API..."):
            result = moderate_text(content)

        if "error" in result:
            st.error(f"API Error: {result['error']}")
        else:
            st.success(f"Is flagged: {result.get('is_flagged', False)}")
            st.write("Categories:")
            st.json(result.get("categories", {}))

if __name__ == "__main__":
    main()


# note: streamlit run streamlit_app.py