import streamlit as st
import google.generativeai as genai
import json
from typing import List, Dict
import os
from dotenv import load_dotenv

# 1. Load environment variables
load_dotenv()

# 2. Configure the page layout
st.set_page_config(
    page_title=os.getenv('APP_NAME', 'Nearby Stays Finder'),
    page_icon="🏨",
    layout="wide"
)

# 3. Get configuration from environment
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
DEFAULT_RADIUS = int(os.getenv('DEFAULT_RADIUS', '10'))
DEFAULT_MAX_RESULTS = int(os.getenv('DEFAULT_MAX_RESULTS', '8'))
DEFAULT_LOCATION = os.getenv('DEFAULT_LOCATION', 'New York')

# --- UI HEADER ---
st.title("🏨 Nearby Stays Finder")
st.markdown("Find accommodation near your location using AI.")

# --- SIDEBAR CONFIGURATION ---
with st.sidebar:
    st.header("Settings")
    
    # API Key Status Indicator
    if GEMINI_API_KEY:
        st.success("✅ API key loaded")
    else:
        st.error("❌ API key missing")
        st.info("Add GEMINI_API_KEY to your .env file")
    
    st.divider()
    
    st.subheader("Search Parameters")
    radius = st.slider("Search Radius (km)", 1, 50, DEFAULT_RADIUS)
    max_results = st.slider("Max Results", 1, 20, DEFAULT_MAX_RESULTS)
    
    st.divider()
    st.caption("⚠️ **Disclaimer:** This tool uses AI. Prices, ratings, and availability are estimates and may not be real-time. Always verify with booking platforms.")

# --- CORE FUNCTIONS ---

def configure_gemini():
    """Configure the Gemini AI client."""
    if not GEMINI_API_KEY:
        st.error("API key not configured. Please check your .env file.")
        return None
    try:
        genai.configure(api_key=GEMINI_API_KEY)
        # Use flash for speed, or pro for better reasoning
        return genai.GenerativeModel('gemini-2.5-flash')
    except Exception as e:
        st.error(f"Error configuring Gemini: {str(e)}")
        return None

def generate_stays_prompt(location: str, radius: int, max_results: int) -> str:
    """Generate the prompt for the AI."""
    return f"""
    Act as a travel specialist. Find {max_results} accommodation options around "{location}" within {radius} km.
    
    Strictly return a JSON array of objects. Do not include markdown formatting like ```json ... ```.
    
    Each object must have:
    - "name": string
    - "type": string (e.g. Hotel, Hostel, Resort)
    - "distance_km": number (estimated)
    - "price_range": string (e.g. "$", "$$", "$$$")
    - "rating": number (0-5)
    - "amenities": list of strings (max 5 items)
    - "description": string (short marketing blurb)
    """

def get_gemini_response(model, prompt):
    """
    Send request to Gemini with JSON enforcement.
    This is the critical stability fix.
    """
    try:
        response = model.generate_content(
            prompt,
            generation_config=genai.types.GenerationConfig(
                response_mime_type="application/json"  # Forces JSON output
            )
        )
        return response.text
    except Exception as e:
        st.error(f"API Error: {e}")
        return None

def parse_stays_response(response_text: str) -> List[Dict]:
    """
    Robust parsing to handle potential markdown wrapping.
    """
    try:
        # Clean string if the model accidentally adds markdown backticks
        clean_text = response_text.replace("```json", "").replace("```", "").strip()
        return json.loads(clean_text)
    except json.JSONDecodeError:
        st.error("Failed to parse AI response. Please try again.")
        return []

def display_stays(stays: List[Dict], location: str):
    """Render the results in nice cards."""
    st.success(f"Found {len(stays)} stays near {location}")
    
    for i, stay in enumerate(stays):
        with st.container():
            col1, col2 = st.columns([3, 1])
            
            with col1:
                st.subheader(stay.get('name', 'Unknown Stay'))
                st.caption(f"**{stay.get('type', 'Hotel')}** • {stay.get('distance_km', 0)} km from center")
                
                # Rating stars
                rating = stay.get('rating', 0)
                st.write(f"{'⭐' * int(rating)} ({rating}/5)")
                
                st.write(stay.get('description', ''))
                
                # Amenities chips
                amenities = stay.get('amenities', [])
                if amenities:
                    st.write("**Amenities:** " + " • ".join(amenities))
            
            with col2:
                st.markdown("###") # Spacer
                st.metric("Price", stay.get('price_range', 'N/A'))
            
            if i < len(stays) - 1:
                st.divider()

# --- MAIN APP LOOP ---

def main():
    col1, col2 = st.columns([3, 1])
    with col1:
        location = st.text_input(
            "Enter location:", 
            placeholder=f"e.g., {DEFAULT_LOCATION}",
            value=DEFAULT_LOCATION
        )
    with col2:
        st.markdown("###")
        search_clicked = st.button("Find Stays", use_container_width=True, type="primary")
    
    if search_clicked and location:
        if not GEMINI_API_KEY:
            st.error("❌ API key missing.")
            return
            
        with st.spinner(f"🔍 AI is scanning for stays in {location}..."):
            model = configure_gemini()
            if not model:
                return
                
            prompt = generate_stays_prompt(location, radius, max_results)
            raw_response = get_gemini_response(model, prompt)
            
            if raw_response:
                stays_data = parse_stays_response(raw_response)
                if stays_data:
                    display_stays(stays_data, location)
                else:
                    st.warning("No data returned. Try a different location.")

    elif not location:
        st.info("💡 **Try searching for:** Kyoto, Downtown Chicago, Paris Latin Quarter")

if __name__ == "__main__":
    main()