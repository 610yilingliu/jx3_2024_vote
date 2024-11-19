# 剑三2024同人外装投票监控

纯乐子，代码本身没有技术难点

难点在于浏览器直接访问 https://jx3.xoyo.com/p/zt/2024/10/18/tongren-clothes/index.html?activeTab=1 无法登陆，而游戏中自带cookie的浏览器是没有开发者模式的

解决方式为fiddler抓包+Chrome开发者模式强行填写fiddler中获取的cookie(session_id, session_id_)

在能用网页访问的前提下获取到排名json地址就非常简单了，西山居没有在此处设置任何反爬措施