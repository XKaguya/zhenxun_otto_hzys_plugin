from nonebot import on_command
from nonebot.adapters.onebot.v11.bot import Bot
from nonebot import on_command
from nonebot.adapters.onebot.v11.bot import Bot
from pathlib import Path
from utils.message_builder import image
from nonebot.adapters.onebot.v11 import Message, MessageSegment
from nonebot.adapters.onebot.v11.event import Event
from nonebot.log import logger
from .utils import otto as OTTO
from LogAnalyze import log_analyze
from configs.config import Config
import os
import json
from utils.message_builder import record

__zx_plugin_name__ = "OTTO活字印刷术"
__plugin_usage__ = """
usage：
/otto 阿米诺斯
默认开启原声大碟模式，即如果有整句直接使用整句语音。可以自定义后缀False取消。
""".strip()
__plugin_des__ = "OTTO活字印刷术"
__plugin_type__ = ("一些工具",)
__plugin_cmd__ = ["OTTO活字印刷术"]

__plugin_settings__ = {
	"level": 5,
	"default_status": True,
	"limit_superuser": False,
	"cmd": ["otto"],
}

Config.add_plugin_config("Otto", "Download_Path", None, help_="存放下载的音频文件的文件夹")


Config.add_plugin_config("Otto", "Website", "https://otto-hzys.hanayabuki.cf", help_="从哪里活字印刷")

json_path = Path(__file__).resolve().parent / "isblocked.json"

folder_path = Path("G:/PaoPao/PaoPao/log")
lines_to_read = 12
font_path = Path(__file__).parent / "msyh.ttc"

otto = on_command("otto", priority=5, block=True)
@otto.handle()
async def _(bot: Bot, ev: Event):
	if not os.path.exists(json_path):
		with open(json_path, 'w') as f:
			json.dump({'status': 'False'}, f)
	with open(json_path, 'r') as f:
		existing_data = json.load(f)
	
	status = existing_data.get('status')
 
	if (status == "False"):
		with open(json_path, 'w') as f:
			json.dump({'status': 'True'}, f)
   
		download_path = Config.get_config("Otto", "Download_Path")
		logger.info(download_path)

		website = Config.get_config("Otto", "Website")
		logger.info(website)

		user_input_pre = ev.get_plaintext().strip('/')
		user_input_after = user_input_pre.strip('otto')
		user_input = user_input_after.strip()
		logger.info(f"User input: {user_input}")

		default_bool_value = True
		
		if 'false' in user_input or 'False' in user_input:
			default_bool_value = False
		else:
			pass

		file_path = await OTTO.call_otto(user_input, default_bool_value, download_path, website)
		logger.info(f"File path: {file_path}")
		file = record(file_path)
  
		with open(json_path, 'w') as f:
			json.dump({'status': 'False'}, f)
   
		await otto.send(file)
	else:
		await otto.send("线程已锁定，请稍后再试。")
  