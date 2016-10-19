#!/usr/bin/env python
# coding:utf-8

import tornado.web
import application


url = [(r"^/(favicon\.ico)", tornado.web.StaticFileHandler,
         dict(path=application.settings['static_path']))]
url += [(r"^/", "handlers.huobi.LoginHandler")]
url += [(r"^/main","handlers.huobi.HuobiHandler")]
url += [(r"^/login", "handlers.huobi.LoginHandler")]
url += [(r"^/account", "handlers.huobi.HuobiHandler")]
url += [(r"^/trade", "handlers.huobi.TradeHandler")]
url += [(r"^/entrust", "handlers.huobi.entrustHandler")]
url += [(r"^/logout", "handlers.huobi.LogoutHandler")]
url += [(r"^/api/accountInfo", "handlers.ApiHandler.accountInfo")]
url += [(r"^/api/Profit", "handlers.ApiHandler.ProfitHandler")]
url += [(r"^/api/entrust", "handlers.ApiHandler.entrustInfo")]
url += [(r"^/api/entrustCancel", "handlers.ApiHandler.entrustCancel")]
url += [(r"^/api/tradeSetting", "handlers.ApiHandler.tradeSetting")]
url += [(r"^/api/tradeSetInfo", "handlers.ApiHandler.tradeSetInfo")]
url += [(r"^/api/APIInfo", "handlers.ApiHandler.APIInfo")]
url += [(r"^/api/dealMessage", "handlers.ApiHandler.dealMessage")]
url += [(r"^/api/avatarInfo", "handlers.ApiHandler.avatarInfo")]



