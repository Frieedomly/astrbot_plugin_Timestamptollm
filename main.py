from astrbot.api.event import filter, AstrMessageEvent
from astrbot.api.provider import ProviderRequest
from astrbot.api.star import Context, Star, register
from datetime import datetime

@register("timestamp_plugin", "你的名字", "给LLM请求加时间戳", "1.0.0")
class TimestampPlugin(Star):
    def __init__(self, context: Context):
        super().__init__(context)
    
    @filter.on_llm_request()
    async def add_timestamp_hook(self, event: AstrMessageEvent, req: ProviderRequest):
        # 获取当前时间戳
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # 在请求的消息前加上时间戳
        req.prompt = f"[时间: {current_time}] {req.prompt}"
    
    async def terminate(self):
        '''插件卸载时调用'''
        pass
