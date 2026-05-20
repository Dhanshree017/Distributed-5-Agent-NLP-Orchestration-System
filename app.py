import streamlit as st
from groq import Groq
import json

# Initialize Groq Client (Kept exactly as requested)
client = Groq(api_key=" add your api key")

# Constant to ensure all agents target the exact same model engine uniformly
MODEL_NAME = "llama-3.1-8b-instant"

# =====================================================================
# 🧠 CORE GENUINE AGENT LOGIC FUNCTIONS (DECOUPLED PIPELINE ARCHITECTURE)
# =====================================================================

def run_poet_agent(keywords):
    """
    Agent 1: The Core Text Generator
    Takes user-defined keywords and handles comprehensive, multi-stanza creative text generation.
    """
    system_prompt = """You are PoetAgent, a master of creative writing and literature. 
    Your task is to write an extended, deep, and meaningful poem based strictly on the user's keywords.
    
    CRITICAL STRUCTURE: The poem must be exactly 3 stanzas long, with 4 lines per stanza (total 12 lines). 
    Separate each stanza with a clean line break. Do not add titles, preambles, stanza numbers, notes, or explanations. 
    Return ONLY the raw lines of poetry."""
    
    completion = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": f"Keywords to build upon: {keywords}"}
        ],
        temperature=0.75  # Higher temperature allowed for artistic variation
    )
    return completion.choices[0].message.content.strip()


def run_translator_agent_french(poem_text):
    """
    Agent 2: The French Lingual Expert
    Receives an extended text block from Agent 1 and executes stanza-by-stanza translation.
    """
    system_prompt = """You are TranslatorAgent (French), a professional bilingual literary expert. 
    Your sole task is to translate the provided multi-stanza English poem into beautiful, classical French. 
    Maintain the emotional core, stanza formatting (keep the 3 distinct stanzas separated by line breaks), meter, and structure perfectly. 
    Do not include conversational filler or meta-remarks. Return ONLY the translated French text."""
    
    completion = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": f"Poem to translate:\n{poem_text}"}
        ],
        temperature=0.25  # Lower temperature guarantees translation accuracy
    )
    return completion.choices[0].message.content.strip()


def run_translator_agent_hindi(poem_text):
    """
    Agent 5: The Hindi Lingual Expert
    Receives an extended text block from Agent 1 and executes lyrical poetic translation into Devanagari script.
    """
    system_prompt = """You are TranslatorAgent (Hindi), an expert in Hindi literature and poetry. 
    Your sole task is to translate the provided multi-stanza English poem into deep, expressive, and rhythmic Hindi using Devanagari script. 
    Maintain the exact 3-stanza structural layout. Ensure it reads like natural, moving Hindi poetry rather than a rigid literal translation. 
    Do not include English words, transliterated text, or chatty commentary. Return ONLY the translated Hindi text."""
    
    completion = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": f"Poem to translate:\n{poem_text}"}
        ],
        temperature=0.3  # Keeps translation faithful but allows lyrical flexibility in Hindi phrasing
    )
    return completion.choices[0].message.content.strip()


def run_title_agent(poem_text):
    """
    Agent 3: The Editorial Evaluator
    Analyzes the complete 12-line poetic structure to synthesize a comprehensive title.
    """
    system_prompt = """You are TitleAgent, an artistic editorial designer. 
    Analyze the provided multi-stanza poem and invent a short, striking, metaphorical, and highly artistic title that summarizes its full journey. 
    Do not wrap the title inside quotes or markdown formatting blocks. Return ONLY the title phrase."""
    
    completion = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": f"Poem context:\n{poem_text}"}
        ],
        temperature=0.45
    )
    return completion.choices[0].message.content.strip()


def run_artist_agent(poem_text):
    """
    Agent 4: The Visual Metaphor Constructor
    Transmutes the complex progression of the multi-stanza poem into a cohesive canvas description.
    """
    system_prompt = """You are ArtistAgent, a visual concept director specializing in classical watercolor mediums. 
    Analyze the narrative and imagery of the complete poem provided. Describe a comprehensive watercolor painting that captures its evolving essence. 
    Focus deeply on environmental elements, lighting transitions across the scene, specific bleeding color palettes, edge behaviors, and brushstroke techniques. 
    Do not explicitly state titles or text in the response. Return ONLY a single, highly detailed descriptive paragraph."""
    
    completion = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": f"Poem to visually capture:\n{poem_text}"}
        ],
        temperature=0.65
    )
    return completion.choices[0].message.content.strip()


# --- STREAMLIT USER INTERFACE LAYOUT ---
st.set_page_config(page_title="Multi-Agent Suite", layout="wide")

# Custom CSS Injection to enforce a beautiful light pale yellow background across the entire app
st.markdown(
    """
    <style>
    .stApp {
        background-color: #FEFBF0;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🎨 Genuine Multi-Agent Poetry Suite")
st.write("Decoupled Inferences ⮕ Directed Sequential State Flows ⮕ 5 Collaborative Agents")

user_input = st.text_input("Enter keywords (e.g., 'golden sunset, quiet waves, passing time'):")

if st.button("Start Agents"):
    if user_input:
        # Using Streamlit's native status wrapper to visually track the execution of our graph
        with st.status("🧠 Activating Independent Agents...", expanded=True) as status:
            try:
                # Step 1: Agent 1 acts as the root node of our network graph, outputting an extended 12-line payload
                st.write("🤖 **PoetAgent** running... processing input keywords and composing an extended 3-stanza poem structure.")
                poem_output = run_poet_agent(user_input)
                
                # Step 2: Downstream translation nodes process the core text in parallel tracks
                st.write("🌐 **TranslatorAgent (French)** running... ingesting source text and executing stanza-by-stanza French mapping.")
                french_output = run_translator_agent_french(poem_output)
                
                st.write("🧡 **TranslatorAgent (Hindi)** running... ingesting source text and crafting Hindi poetic script.")
                hindi_output = run_translator_agent_hindi(poem_output)
                
                # Step 3: Structural evaluation nodes
                st.write("🏷️ **TitleAgent** running... reading core text layout and brainstorming artistic headers.")
                title_output = run_title_agent(poem_output)
                
                st.write("🎨 **ArtistAgent** running... transforming underlying literary themes into visual rendering logic.")
                visual_output = run_artist_agent(poem_output)
                
                # Close the visual trace bar smoothly on completion
                status.update(label="Distributed Agent Operations Finalized!", state="complete", expanded=False)
                
                # --- LAYOUT PRESENTATION FRAMEWORK ---
                # 1. Output Header Title
                st.markdown(f"<h1 style='text-align: center; color: #1E3A8A;'>{title_output}</h1>", unsafe_allow_html=True)
                st.divider()

                # 2. Three-Column Setup for Lingual Processing Outputs (Adjusts cleanly to multi-stanza blocks)
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.subheader("🤖 Poet Agent (Source)")
                    st.info(poem_output)
                with col2:
                    st.subheader("🌐 Translator Agent (French)")
                    st.success(french_output)
                with col3:
                    st.subheader("🧡 Translator Agent (Hindi)")
                    st.warning(hindi_output)

                # 3. Dedicated Container for the Visual Prompt Synthesis Agent
                st.divider()
                st.subheader("🎨 Artist Agent (Visual Concept)")
                st.write(visual_output)
                
                st.caption("Architecture Update: 5-Node Multi-Inference Directed Acyclic Graph (DAG) Pipeline")
                
            except Exception as e:
                status.update(label="Pipeline Execution Errored out", state="error", expanded=True)
                st.error(f"An internal error occurred during the multi-agent execution loop: {str(e)}")
                st.info("Check if your Groq API key variable is empty or if your billing limit has been reached.")
    else:
        st.warning("Please enter keywords first.")