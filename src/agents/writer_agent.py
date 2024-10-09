from langchain_core.messages import AIMessage  # 导入 AI 消息类
import random
from .session_history import get_session_history  # 导入用于处理会话历史的方法
from .agent_base import AgentBase  # 导入基础代理类
from utils.logger import LOG  # 导入日志记录模块

class WriterAgent(AgentBase):
    """
    词汇学习代理类，负责处理与用户的对话。
    继承自 AgentBase 基类。
    """
    def __init__(self,session_id=None):
        # 调用父类的构造函数，初始化代理名称、提示文件路径以及可选的会话 ID
        prompt_file= f"prompts/writer_study_prompt.txt"  # 提示词文件的路径
        intro_file = f"content/intro/writer_study.json"
        super().__init__(
            name="writer_study",
            prompt_file=prompt_file,
            intro_file=intro_file,
            session_id=session_id
        )

    def restart_session(self, session_id=None):
        """
        重新启动会话，清除会话历史。

        参数:
            session_id (str, optional): 会话的唯一标识符。如果未提供，将使用当前会话 ID。

        返回:
            str: 返回清空后的会话历史，作为初始的 AI 消息。
        """
        # 如果没有传递 session_id，则使用实例中的 session_id
        if session_id is None:
            session_id = self.session_id

        # 获取该会话的历史记录对象
        history = get_session_history(session_id)
        # 清除该会话的历史记录
        history.clear()

        # 记录清除后的会话历史到日志中
        LOG.debug(f"[history][{session_id}]:{history}")

        if not history.messages:
            initial_ai_message = random.choice(self.intro_messages)  # 随机选择初始AI消息
            history.add_message(AIMessage(content=initial_ai_message))  # 添加初始AI消息到历史记录
            return initial_ai_message
        else:
            return history.messages[-1].content  # 返回历史记录中的最后一条消息
            
        # 返回清空后的会话历史记录
        #return history
