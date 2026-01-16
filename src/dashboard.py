import streamlit as st
from src.password_generator import PinGenerator, RandomPasswordGenerator, MemorablePasswordGenerator     


st.title(":zap: Password Generator Dashboard")
col1, col2, col3 = st.columns(3)

generator_type = st.radio("Select Generator Type:", ("PIN Generator", "Random Password Generator", "Memorable Password Generator"))


disabled_pin = generator_type != "PIN Generator"
disabled_rand = generator_type != "Random Password Generator"
disabled_mem = generator_type != "Memorable Password Generator"

with col1:
    st.subheader("PIN Generator")
    pin_length = st.slider("PIN Length", min_value=4, max_value=12, value=8, disabled=disabled_pin)
    if st.button("Generate PIN", disabled=disabled_pin):        
        pin_gen = PinGenerator(length=pin_length)
        st.write(f"Generated PIN: ``` {pin_gen.generate()} ```")        
        
with col2:      
    st.subheader("Random Password Generator")
    rand_length = st.slider("Password Length", min_value=6, max_value=20, value=10, disabled=disabled_rand)
    include_symbols = st.checkbox("Include Symbols", disabled=disabled_rand)
    include_numbers = st.checkbox("Include Numbers", disabled=disabled_rand)
    if st.button("Generate Random Password", disabled=disabled_rand):        
        random_pass_gen = RandomPasswordGenerator(length=rand_length, include_symbols=include_symbols, include_numbers=include_numbers)
        st.write(f"Generated Random Password: ``` {random_pass_gen.generate()} ```")    
        
with col3:  
    st.subheader("Memorable Password Generator")
    num_words = st.slider("Number of Words", min_value=2, max_value=6, value=4, disabled=disabled_mem)
    separator = st.text_input("Separator", value='-', disabled=disabled_mem)
    capitalize = st.checkbox("Capitalize Random Words", disabled=disabled_mem)
    if st.button("Generate Memorable Password", disabled=disabled_mem):        
        memorable_pass_gen = MemorablePasswordGenerator(num_words=num_words, separator=separator, capitalize=capitalize)
        st.write(f"Generated Memorable Password: ``` {memorable_pass_gen.generate()} ```")



