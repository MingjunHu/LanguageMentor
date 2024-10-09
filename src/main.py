import gradio as gr
from tabs.scenario_tab import create_scenario_tab
from tabs.conversation_tab import create_conversation_tab
from tabs.vocab_tab import create_vocab_tab
from tabs.writer_tab import create_writer_tab
from utils.logger import LOG

def main():
    with gr.Blocks(title="CYOL助手园地") as language_mentor_app:
        #create_scenario_tab()
        #create_conversation_tab()
        #create_vocab_tab()
        create_writer_tab()
    
    # 启动应用
    # 设置登录密码
    username_password_list = [("cyol", "cyol5152000"), ("zqb", "cyol5152000")]
    language_mentor_app.launch(share=False,auth=username_password_list, server_name="0.0.0.0",server_port=8888)

if __name__ == "__main__":
    main()
