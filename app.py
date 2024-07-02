import streamlit as st
import json
from datafog_instructor import DataFog
from datafog_instructor.models import EntityType

            
# Initialize DataFog
datafog = DataFog()

# Function to map returned entity types to EntityType enum values
def map_entity_type(entity_type: str) -> str:
    try:
        return EntityType(entity_type).value
    except ValueError:
        # If the exact match fails, try to find a close match
        for enum_type in EntityType:
            if entity_type.lower().replace(" ", "") in enum_type.value.lower().replace(" ", ""):
                return enum_type.value
        # If no match is found, default to ORG
        return EntityType.ORG.value

st.title("PII Detection using Ollama and Microsoft Phi-3")

st.write("""
This demo showcases the named entity recognition capabilities of the DataFog Instructor SDK using Ollama and Microsoft Phi-3 for custom entity detection.
Enter some text below and click 'Detect Entities' to see the results in structured JSON format.
""")

# Text input
text_input = st.text_area("Enter text for entity detection:", height=150)

# Button to trigger entity detection
if st.button("Detect Entities"):
    if text_input:
        with st.spinner("Detecting entities..."):
            result = datafog.detect_entities(text_input)
        
        # Display results
        st.subheader("Detected Entities:")
        for entity in result.entities:
            mapped_type = map_entity_type(entity.type)
            st.write(f"- **{entity.text}**: {mapped_type}")
        
        # JSON Output
        st.subheader("JSON Output:")
        json_output = json.dumps({
            "entities": [
                {
                    "text": entity.text,
                    "type": map_entity_type(entity.type),
                    "start": entity.start,
                    "end": entity.end
                } for entity in result.entities
            ]
        }, indent=2)
        st.code(json_output, language="json")
    else:
        st.warning("Please enter some text to analyze.")

# Display entity types
st.sidebar.subheader("Available Entity Types")
for entity_type in EntityType:
    st.sidebar.write(f"- **{entity_type.name}**: {entity_type.value}")

# Add custom entity type
st.sidebar.subheader("Add Custom Entity Type")
new_type = st.sidebar.text_input("Entity Type Name")
new_description = st.sidebar.text_input("Entity Type Description")
if st.sidebar.button("Add Entity Type"):
    if new_type and new_description:
        datafog.add_entity_type(new_type, new_description)
        st.sidebar.success(f"Added new entity type: {new_type}")
    else:
        st.sidebar.warning("Please provide both name and description.")

# Footer
st.markdown("---")
st.markdown("Powered by [DataFog Instructor](https://github.com/datafog/datafog-instructor)")
st.markdown("For any questions, please contact [sid@datafog.ai](mailto:sid@datafog.ai).")
