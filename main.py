from astrbot.api.event import filter, AstrMessageEvent
from astrbot.api.provider import ProviderRequest
from datetime import datetime

@filter.on_llm_request()
async def add_timestamp_hook(self, event: AstrMessageEvent, req: ProviderRequest):
    # 获取当前时间戳
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # 在请求的消息前加上时间戳
    req.prompt = f"[时间: {current_time}] {req.prompt}"

    async def terminate(self):
        """可选择实现异步的插件销毁方法，当插件被卸载/停用时会调用。"""
