from astrbot.api.event import filter, AstrMessageEvent
from astrbot.api.provider import ProviderRequest
from astrbot.api.star import Context, Star, register
from datetime import datetime

@register("timestamptollm", "Frieedomly", "给LLM请求加时间戳", "1.0.0")
class TimestampToLLM(Star):
    def __init__(self, context: Context):
        super().__init__(context)
        self.context = context
        self.logger = context.logger  # 使用框架提供的日志器
    
    @filter.on_llm_request()
    async def add_timestamp_hook(self, event: AstrMessageEvent, req: ProviderRequest):
        try:
            # 获取更详细的时间信息
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            weekday = datetime.now().strftime("%A")
            
            # 在prompt前添加时间戳
            original_prompt = req.prompt
            req.prompt = f"[时间: {current_time} {weekday}]\n\n{original_prompt}"
            
            # 记录日志（可选）
            self.logger.info(f"已为LLM请求添加时间戳: {current_time}")
            
        except Exception as e:
            self.logger.error(f"添加时间戳时出错: {e}")
            # 出错时不修改原始prompt
    
    async def activate(self):
        """插件激活时调用"""
        self.logger.info("时间戳插件已激活")
    
    async def terminate(self):
        """插件终止时调用"""
        self.logger.info("时间戳插件已终止")















