import streamlit as st
import openai

openai.api_key = st.secrets['api_key']

st.title('GhatGPT!!!')

with st.form('form'):
    user_input = st.text_input('Prompt')
    size = st.selectbox("Size", ["1024X1024", "512X512", "256X256"])
    submit = st.form_submit_button('제출')

if submit and user_input:
    gpt_prompt = [{
        "role": "system",
        "content": "Imageine the detail appearence if the input. Response it shortly around 20 words."
    }]

    gpt_prompt.append({
        "role": "user",
        "content": user_input
    })

    with st.spinner("Waiting for ChatGPT..."):
        gpt_response = openai.ChatCompletion.create(
            model = "gpt-3.5-turbo",
            messages = gpt_prompt
        )

    prompt = gpt_response['choices'][0]['message']['content']

    st.write(prompt)
    st.write(size)

    # with st.spinner("Waiting for DALL-E..."):
    #     dalle_response = openai.Image.create(
    #         prompt = prompt,
    #         size = size
    #     )

    # st.image(dalle_response['data'][0]['url'])