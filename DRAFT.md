** 这是一个 Tom Li 使用的开发草稿。**

** 由于内容可能对它人存在误导（如未及时更新），请勿擅自阅读并以此作出决定。**

** 很多特性都已经完成实现了。**

* 忙碌图标高度不固定，导致界面抖动。
* 刷新按钮和发微博按钮，位置不友好。
* 发送对话框不能使用 C-Return。
* 每个用户时间线都应该有显示用户信息的 Widget。
* j, k 如果能滚动，Vim 用户会很高兴。而且最好 j, k 是精确跳至下一条微博，而不是向下滚动一些像素。
* 时间线内搜索功能。由于新浪不提供 API，而且手工搜索请求数超级多，所以只能废弃或等待其它思路。
* 收藏微博时选择分类，新浪 API 勉强可实现，但是问题也多。
* 阅读微博时，表情应该解析出来。
* 动态标签页。除了基础标签页，其它标签页是可打开（查看其它用户微博）、移动位置和关闭的。
* 分组支持。
* 使用代理服务器连接网络。
* 加载“中间内容”。
* 实现一个简洁的图片浏览器。
* 微博图片应支持右键另存为（可能还有其它菜单）。
* 通知栏区域应有一个托盘图标，程序应该可以隐藏到托盘。
* 主窗体的位置和大小应该可以自动记忆，保存在配置中。
* 解析 URL 为 HTML 标签时，用于匹配 URL 的正则表达式 Bug 很多。除此之外，打开链接的方式也存在问题。
* 通知不停的往外弹，太烦人了。在把通知检查时间设置到很短时，简直就是骚扰。
* 转发微博时，如果有个卷轴之类的背景，也许会更好。
* 现在程序的资源图片分散在目录各处，应该使用 QRC 统一编译为 RC 文件，便于引用和管理。
* 缺少“提及我的评论”这个标签页，是由于界面设计不决，导致未添加。
* 微博应该显示“来自某客户端”。
* 图片太小时，不应该缩放导致图片质量下降，应该填充背景色。
* 删除微博的图标太唐突，应更换一个。
* 每次登录时都会模拟浏览器，进行一次 OAuth 授权。应该保存授权码，不用重复授权。
* 界面中控件的焦点问题常常给人带来困扰：比如，添加图片后，焦点就跑到图片按钮上了，不能继续在文本框中输入。应该做些固定处理。
* 主窗体宽度太窄，会出现横向滚动条。
* 发送微博的窗台是模态对话框，这很影响体验。特别是对模态框很反感的一类用户。
* 目前的表情库很不完整，应该提供完整表情库。
* 点击一条微博评论/转发按钮时，评论和转发信息就会开始异步加载并构建界面。如果网络延迟较高或迅速关闭窗口，可能加载仍在进行中。构建界面时，由于窗口对象早就不存在了，会出现 RuntimeError 异常，暂时没有合理的解决方案。在很多场景下都有类似的问题。