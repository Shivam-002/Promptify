import os
import openai
import gradio as gr

prompt = ""


def openai_create(prompt):

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.9,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6,
        stop=[" Human:", " AI:"],
    )

    return response.choices[0].text


def chatgpt_clone(input, history):
    history = history or []
    s = list(sum(history, ()))
    s.append(input)
    inp = " ".join(s)
    output = openai_create(inp)
    history.append((input, output))
    return history, history


css = """

    .home-page{
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        height: 1000px;
        width: 100vw;
        margin: 5px;
        footer {visibility: hidden}
    }

    .chat-box{
        flex: 1;
        width: 100%;
    }

    .input-submit-container{
        display: flex;
        flex-direction: row;
        justify-content: center;
        align-items: center;
    }

    .input-text{
        flex: 1;
    }
    
    .submit-btn{
        width: 100px;
        background-color: #f44336;
        color: white;
        border: none;
        cursor: pointer;
        border-radius: 5px;
        font-size: 16px;
    }
"""

js = """
function createGradioAnimation() {
    var container = document.createElement('div');
    container.id = 'gradio-animation';
    container.style.fontSize = '2em';
    container.style.fontWeight = 'bold';
    container.style.textAlign = 'center';
    container.style.marginBottom = '20px';

    var text = 'Welcome to Promptify!';
    for (var i = 0; i < text.length; i++) {
        (function(i){
            setTimeout(function(){
                var letter = document.createElement('span');
                letter.style.opacity = '0';
                letter.style.transition = 'opacity 0.5s';
                letter.innerText = text[i];

                container.appendChild(letter);

                setTimeout(function() {
                    letter.style.opacity = '1';
                }, 50);
            }, i * 50);
        })(i);
    }

    var gradioContainer = document.querySelector('.gradio-container');
    gradioContainer.insertBefore(container, gradioContainer.firstChild);

    document.querySelector('.gradio-button').classList.add('custom-button');

}
"""


with gr.Blocks(js=js, css=css) as block_main:
    with gr.Column(elem_classes="home-page"):
        output = (
            gr.Textbox(
                label="Output",
                placeholder="",
                interactive=False,
                show_label=False,
                elem_classes="chat-box",
                
            ),
        )
        with gr.Row(elem_classes="input-submit-container"):
            input = gr.Textbox(
                label="Input",
                placeholder="Enter your prompt here",
                show_label=False,
                elem_classes="input-text",
            )


block_main.launch(debug=True)
