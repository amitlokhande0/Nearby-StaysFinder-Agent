# 🏨 Nearby Stays Finder

An AI-powered web application that helps you find accommodation near any location using Google's Gemini 2.5 Flash model.

## ✨ Features

- **🔍 AI-Powered Search**: Uses Gemini 2.5 Flash to find realistic accommodation options
- **📍 Location-Based**: Search for stays near any location worldwide
- **🎯 Customizable**: Adjust search radius and maximum results
- **💡 Smart Results**: Get detailed information including prices, ratings, amenities, and descriptions
- **🔒 Secure**: API keys stored securely in environment variables
- **📱 Responsive**: Clean, mobile-friendly interface built with Streamlit

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- Google Gemini API key ([Get one here](https://aistudio.google.com/app/apikey))

### Installation

1. **Clone or download the project files**

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure environment variables**:
   - Create a `.env` file in the project root
   - Add your Gemini API key:
     ```env
     GEMINI_API_KEY=your_actual_gemini_api_key_here
     APP_NAME="Nearby Stays Finder"
     DEFAULT_RADIUS=10
     DEFAULT_MAX_RESULTS=8
     DEFAULT_LOCATION="New York"
     ```

4. **Run the application**:
   ```bash
   streamlit run app.py
   ```

5. **Open your browser** to the displayed URL (typically `http://localhost:8501`)

## 📁 Project Structure

```
nearby-stays-finder/
├── app.py                 # Main Streamlit application
├── .env                   # Environment variables (create this)
├── requirements.txt       # Python dependencies
└── README.md             # This file
```

## 🛠️ Configuration

### Environment Variables (.env)

| Variable | Description | Default |
|----------|-------------|---------|
| `GEMINI_API_KEY` | Your Google Gemini API key | **Required** |
| `APP_NAME` | Application display name | "Nearby Stays Finder" |
| `DEFAULT_RADIUS` | Default search radius in km | 10 |
| `DEFAULT_MAX_RESULTS` | Default number of results | 8 |
| `DEFAULT_LOCATION` | Default search location | "New York" |

### Search Parameters

- **Search Radius**: 1-50 km range
- **Max Results**: 1-20 accommodations
- **Location**: Any city, landmark, or address worldwide

## 💡 Usage Examples

Try searching for:
- **🗽 Landmarks**: "Times Square NYC", "Eiffel Tower Paris"
- **🏙️ City Centers**: "Tokyo Shibuya", "London Downtown"
- **🎯 Districts**: "Bangkok Sukhumvit", "Paris Latin Quarter"
- **🏖️ Destinations**: "Bali Seminyak", "Miami South Beach"

## 📊 Sample Output

The app displays accommodation information including:
- **🏨 Name & Type** (Hotel, Resort, Hostel, etc.)
- **📍 Distance** from search location
- **⭐ Rating** with visual stars
- **💰 Price Range** ($ to $$$$)
- **🛎️ Amenities** (WiFi, Pool, Parking, etc.)
- **📝 Description** of the property

## 🔧 Technical Details

### Backend Architecture
- **AI Model**: Google Gemini 2.5 Flash
- **Response Format**: Strict JSON enforcement
- **Error Handling**: Comprehensive backend validation
- **Security**: API keys isolated from frontend

### Frontend Features
- **Framework**: Streamlit
- **Layout**: Responsive grid system
- **Components**: Modular UI elements
- **State Management**: Session-free simplicity

## 🐛 Troubleshooting

### Common Issues

1. **"API key not found"**
   - Ensure `.env` file exists in the correct directory
   - Verify the `GEMINI_API_KEY` variable is set correctly

2. **"No stays found"**
   - Try a more specific location
   - Increase search radius
   - Check your internet connection

3. **JSON parsing errors**
   - The app automatically retries with cleaned responses
   - Try the search again if this occurs

### Getting Help

- Check that all dependencies are installed correctly
- Verify your Gemini API key is valid and has sufficient quota
- Ensure you're using a supported Python version (3.8+)

## 📄 License

This project is for educational and personal use. Please comply with Google's Gemini API terms of service.

## ⚠️ Disclaimer

This tool uses AI-generated content. Prices, ratings, and availability are estimates and may not reflect real-time data. Always verify accommodation details with official booking platforms before making travel arrangements.

## 🔮 Future Enhancements

- Real-time availability checking
- Integration with booking APIs
- Map visualization of results
- User reviews and photos
- Price comparison across platforms

---

**Happy travels! 🌍✈️🏨**
