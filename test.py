print("Hello world")



# main.py
from telegram.ext import ApplicationBuilder, CommandHandler
from core import start, load_config, load_plugins, connect_to_mysql
from tqdm import tqdm

# 读取配置文件
config = load_config()

TOKEN = config["telegram"]["token"]
proxy_url = config["telegram"]["proxy_url"]

# 初始化数据库

db = connect_to_mysql()

application = (
    ApplicationBuilder()
    .token(TOKEN)
    .proxy(proxy_url)
    .get_updates_proxy(proxy_url)
    .build()
)

# 加载基本处理程序
print("正在启动...")
start_handler = CommandHandler("start", start)
application.add_handler(start_handler)


# 动态加载插件
plugins = load_plugins(config)
for plugin in tqdm(plugins, desc="少女折寿中..."):
    plugin.register(application)

print("就绪！")
# 运行
application.run_polling()
