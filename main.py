import streamlit as st

def main():
    # Set page configuration
    st.set_page_config(page_title="Unit Converter", layout="centered")
    
    # Sidebar
    with st.sidebar:
        st.title("About")
        st.info("This is a unit converter application that helps you convert between different units of measurement.")
        
        st.markdown("### Features")
        st.markdown("- Length Conversion")
        st.markdown("- Weight Conversion")
        st.markdown("- Temperature Conversion")
        
        st.markdown("### How to Use")
        st.markdown("1. Select conversion type")
        st.markdown("2. Choose input unit")
        st.markdown("3. Enter value")
        st.markdown("4. Choose output unit")
        st.markdown("5. Click Convert")
        
        # Enhanced Theme Selection
        st.markdown("### Settings")
        theme = st.selectbox("Select Theme:", 
                           ["Light", "Dark", "Blue", "Green", "Gradient"])
        
        if theme == "Dark":
            primary_color = "#2e2e2e"
            secondary_color = "#ffffff"
            background_color = "#1a1a1a"
            container_color = "#3e3e3e"
            accent_color = "#4287f5"
            gradient = "linear-gradient(135deg, #1a1a1a 0%, #2e2e2e 100%)"
        elif theme == "Blue":
            primary_color = "#1f618d"
            secondary_color = "#ffffff"
            background_color = "#e6f3ff"
            container_color = "#ffffff"
            accent_color = "#2980b9"
            gradient = "linear-gradient(135deg, #1c92d2 0%, #f2fcfe 100%)"
        elif theme == "Green":
            primary_color = "#2ecc71"
            secondary_color = "#ffffff"
            background_color = "#e8f8f5"
            container_color = "#ffffff"
            accent_color = "#27ae60"
            gradient = "linear-gradient(135deg, #43cea2 0%, #185a9d 100%)"
        elif theme == "Gradient":
            primary_color = "#2c3e50"
            secondary_color = "#ffffff"
            background_color = "#ffffff"
            container_color = "#ffffff"
            accent_color = "#3498db"
            gradient = "linear-gradient(135deg, #ff6b6b 0%, #556270 100%)"
        else:  # Light theme
            primary_color = "#1f618d"
            secondary_color = "#2c3e50"
            background_color = "#f0f2f6"
            container_color = "#ffffff"
            accent_color = "#3498db"
            gradient = "linear-gradient(135deg, #E0EAFC 0%, #CFDEF3 100%)"

    # Add this enhanced CSS for sidebar styling
    st.markdown(f"""
        <style>
        /* Sidebar styling */
        .css-1d391kg, .css-1q1n0ol {{
            background: {gradient};
        }}
        
        section[data-testid="stSidebar"] {{
            background: {gradient};
            border-right: 1px solid rgba(255,255,255,0.1);
        }}
        
        section[data-testid="stSidebar"] .stMarkdown {{
            color: {secondary_color};
        }}
        
        section[data-testid="stSidebar"] h1 {{
            color: {secondary_color};
            font-size: 2em;
            font-weight: bold;
            padding: 20px 0;
            text-align: center;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
            background: linear-gradient(45deg, {primary_color}, {accent_color});
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }}
        
        section[data-testid="stSidebar"] h3 {{
            color: {secondary_color};
            font-size: 1.3em;
            font-weight: bold;
            margin-top: 30px;
            padding: 10px 0;
            border-bottom: 2px solid {accent_color};
        }}
        
        section[data-testid="stSidebar"] .stSelectbox > div > div {{
            background-color: rgba(255,255,255,0.1);
            border: 1px solid {accent_color};
            border-radius: 10px;
            color: {secondary_color};
            transition: all 0.3s ease;
        }}
        
        section[data-testid="stSidebar"] .stSelectbox > div > div:hover {{
            border-color: {primary_color};
            box-shadow: 0 0 10px rgba(0,0,0,0.2);
        }}
        
        /* Info box styling in sidebar */
        section[data-testid="stSidebar"] .stAlert {{
            background: rgba(255,255,255,0.1);
            border: 1px solid {accent_color};
            border-radius: 10px;
            color: {secondary_color};
            padding: 15px;
            margin: 15px 0;
            backdrop-filter: blur(5px);
        }}
        
        /* Sidebar list items */
        section[data-testid="stSidebar"] ul {{
            list-style-type: none;
            padding-left: 0;
        }}
        
        section[data-testid="stSidebar"] li {{
            margin: 10px 0;
            padding: 8px 15px;
            border-radius: 5px;
            background: rgba(255,255,255,0.05);
            transition: all 0.3s ease;
        }}
        
        section[data-testid="stSidebar"] li:hover {{
            background: rgba(255,255,255,0.1);
            transform: translateX(5px);
        }}
        
        /* Numbered list in How to Use section */
        section[data-testid="stSidebar"] ol {{
            counter-reset: item;
            list-style-type: none;
            padding-left: 0;
        }}
        
        section[data-testid="stSidebar"] ol li {{
            position: relative;
            padding-left: 30px;
            margin: 10px 0;
        }}
        
        section[data-testid="stSidebar"] ol li::before {{
            content: counter(item);
            counter-increment: item;
            position: absolute;
            left: 0;
            top: 50%;
            transform: translateY(-50%);
            background: {accent_color};
            color: {secondary_color};
            width: 20px;
            height: 20px;
            border-radius: 50%;
            text-align: center;
            line-height: 20px;
            font-size: 12px;
        }}
        
        /* Hover effects for interactive elements */
        section[data-testid="stSidebar"] .stMarkdown a:hover {{
            color: {accent_color};
            text-decoration: none;
        }}
        
        /* Animation for sidebar elements */
        @keyframes slideIn {{
            from {{
                opacity: 0;
                transform: translateX(-10px);
            }}
            to {{
                opacity: 1;
                transform: translateX(0);
            }}
        }}
        
        section[data-testid="stSidebar"] .element-container {{
            animation: slideIn 0.3s ease-out forwards;
        }}
        
        /* Custom scrollbar for sidebar */
        section[data-testid="stSidebar"] ::-webkit-scrollbar {{
            width: 6px;
        }}
        
        section[data-testid="stSidebar"] ::-webkit-scrollbar-track {{
            background: rgba(255,255,255,0.1);
        }}
        
        section[data-testid="stSidebar"] ::-webkit-scrollbar-thumb {{
            background: {accent_color};
            border-radius: 3px;
        }}
        
        section[data-testid="stSidebar"] ::-webkit-scrollbar-thumb:hover {{
            background: {primary_color};
        }}
        </style>
    """, unsafe_allow_html=True)

    # Enhanced CSS with background patterns and animations
    st.markdown(f"""
        <style>
        /* Main container and background styling */
        .main {{
            background: {gradient};
            min-height: 100vh;
            background-attachment: fixed;
            position: relative;
        }}
        
        .main::before {{
            content: '';
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: url("data:image/svg+xml,%3Csvg width='60' height='60' viewBox='0 0 60 60' xmlns='http://www.w3.org/2000/svg'%3E%3Cg fill='none' fill-rule='evenodd'%3E%3Cg fill='%23ffffff' fill-opacity='0.1'%3E%3Cpath d='M36 34v-4h-2v4h-4v2h4v4h2v-4h4v-2h-4zm0-30V0h-2v4h-4v2h4v4h2V6h4V4h-4zM6 34v-4H4v4H0v2h4v4h2v-4h4v-2H6zM6 4V0H4v4H0v2h4v4h2V6h4V4H6z'/%3E%3C/g%3E%3C/g%3E%3C/svg%3E");
            opacity: 0.1;
            z-index: 0;
            pointer-events: none;
        }}
        
        /* Title styling with enhanced effects */
        .title {{
            color: {primary_color};
            text-align: center;
            margin-bottom: 30px;
            font-size: 2.8em;
            font-weight: bold;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
            background: linear-gradient(45deg, {primary_color}, {accent_color});
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            animation: titleGlow 2s ease-in-out infinite;
        }}
        
        /* Converter container with glass effect */
        .converter-container {{
            background: rgba({container_color.replace('#', '')}, 0.9);
            backdrop-filter: blur(10px);
            padding: 30px;
            border-radius: 20px;
            box-shadow: 0 8px 32px rgba(0,0,0,0.1);
            border: 1px solid rgba(255,255,255,0.2);
            transition: all 0.3s ease;
            margin: 20px 0;
            position: relative;
            overflow: hidden;
        }}
        
        .converter-container:hover {{
            transform: translateY(-5px);
            box-shadow: 0 15px 45px rgba(0,0,0,0.2);
        }}
        
        .converter-container::before {{
            content: '';
            position: absolute;
            top: -50%;
            left: -50%;
            width: 200%;
            height: 200%;
            background: radial-gradient(circle, rgba(255,255,255,0.1) 0%, transparent 60%);
            transform: rotate(45deg);
            pointer-events: none;
        }}
        
        /* Button styling with gradient */
        .stButton > button {{
            background: linear-gradient(45deg, {accent_color}, {primary_color});
            color: white;
            border: none;
            border-radius: 25px;
            padding: 12px 30px;
            font-weight: bold;
            transition: all 0.3s ease;
            width: 100%;
            margin-top: 20px;
            text-transform: uppercase;
            letter-spacing: 1px;
        }}
        
        .stButton > button:hover {{
            transform: scale(1.05);
            box-shadow: 0 10px 20px rgba(0,0,0,0.2);
            background: linear-gradient(45deg, {primary_color}, {accent_color});
        }}
        
        /* Animations */
        @keyframes titleGlow {{
            0%, 100% {{ opacity: 1; }}
            50% {{ opacity: 0.8; }}
        }}
        
        /* Select box styling */
        .stSelectbox > div > div {{
            background-color: {container_color};
            border-radius: 10px;
            border: 2px solid {accent_color};
            transition: all 0.3s ease;
        }}
        
        .stSelectbox > div > div:hover {{
            border-color: {primary_color};
        }}
        
        /* Number input styling */
        .stNumberInput > div > div > input {{
            border-radius: 10px;
            border: 2px solid {accent_color};
            padding: 10px;
            transition: all 0.3s ease;
        }}
        
        .stNumberInput > div > div > input:focus {{
            border-color: {primary_color};
            box-shadow: 0 0 0 2px rgba(41, 128, 185, 0.2);
        }}
        
        /* Success message styling */
        .stSuccess {{
            background-color: #d4edda;
            color: #155724;
            padding: 15px;
            border-radius: 10px;
            border-left: 5px solid #28a745;
            margin-top: 20px;
            animation: slideIn 0.5s ease-out;
        }}
        
        /* Sidebar styling */
        .css-1d391kg {{
            background-color: {container_color};
        }}
        
        .sidebar .sidebar-content {{
            background-color: {container_color};
        }}
        
        /* Animations */
        @keyframes slideIn {{
            from {{
                opacity: 0;
                transform: translateY(20px);
            }}
            to {{
                opacity: 1;
                transform: translateY(0);
            }}
        }}
        
        /* Additional responsive design */
        @media (max-width: 768px) {{
            .title {{
                font-size: 2em;
            }}
            .converter-container {{
                padding: 20px;
                margin: 10px;
            }}
        }}
        </style>
    """, unsafe_allow_html=True)

    # Title
    st.markdown("<h1 class='title'>Unit Converter</h1>", unsafe_allow_html=True)

    # Create conversion dictionaries
    length_units = {
        'Meter': 1,
        'Kilometer': 0.001,
        'Centimeter': 100,
        'Millimeter': 1000,
        'Mile': 0.000621371,
        'Yard': 1.09361,
        'Foot': 3.28084,
        'Inch': 39.3701
    }

    weight_units = {
        'Kilogram': 1,
        'Gram': 1000,
        'Milligram': 1000000,
        'Pound': 2.20462,
        'Ounce': 35.274
    }

    temperature_units = ['Celsius', 'Fahrenheit', 'Kelvin']

    # Create container
    with st.container():
        st.markdown("<div class='converter-container'>", unsafe_allow_html=True)
        
        # Select conversion type
        conversion_type = st.selectbox('Select Conversion Type:', 
                                     ['Length', 'Weight', 'Temperature'])

        # Input fields
        col1, col2 = st.columns(2)

        with col1:
            if conversion_type == 'Length':
                from_unit = st.selectbox('From:', length_units.keys())
                value = st.number_input('Enter Value:', value=0.0)
            elif conversion_type == 'Weight':
                from_unit = st.selectbox('From:', weight_units.keys())
                value = st.number_input('Enter Value:', value=0.0)
            else:  # Temperature
                from_unit = st.selectbox('From:', temperature_units)
                value = st.number_input('Enter Value:', value=0.0)

        with col2:
            if conversion_type == 'Length':
                to_unit = st.selectbox('To:', length_units.keys())
            elif conversion_type == 'Weight':
                to_unit = st.selectbox('To:', weight_units.keys())
            else:  # Temperature
                to_unit = st.selectbox('To:', temperature_units)

        # Conversion logic
        if st.button('Convert'):
            if conversion_type == 'Length':
                # Convert to meters first, then to target unit
                meters = value / length_units[from_unit]
                result = meters * length_units[to_unit]
                st.success(f'{value} {from_unit} = {result:.4f} {to_unit}')

            elif conversion_type == 'Weight':
                # Convert to kilograms first, then to target unit
                kilos = value / weight_units[from_unit]
                result = kilos * weight_units[to_unit]
                st.success(f'{value} {from_unit} = {result:.4f} {to_unit}')

            else:  # Temperature
                if from_unit == 'Celsius':
                    if to_unit == 'Fahrenheit':
                        result = (value * 9/5) + 32
                    elif to_unit == 'Kelvin':
                        result = value + 273.15
                    else:
                        result = value

                elif from_unit == 'Fahrenheit':
                    if to_unit == 'Celsius':
                        result = (value - 32) * 5/9
                    elif to_unit == 'Kelvin':
                        result = (value - 32) * 5/9 + 273.15
                    else:
                        result = value

                else:  # Kelvin
                    if to_unit == 'Celsius':
                        result = value - 273.15
                    elif to_unit == 'Fahrenheit':
                        result = (value - 273.15) * 9/5 + 32
                    else:
                        result = value

                st.success(f'{value} {from_unit} = {result:.2f} {to_unit}')

        st.markdown("</div>", unsafe_allow_html=True)

if __name__ == '__main__':
    main() 