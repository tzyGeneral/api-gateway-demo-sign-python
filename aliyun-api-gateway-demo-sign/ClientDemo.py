# -*- coding: utf-8 -*-
from com.aliyun.api.gateway.sdk import client
from com.aliyun.api.gateway.sdk.http import request
from com.aliyun.api.gateway.sdk.common import constant

# 这里为友盟一键登录接口
host = "https://verify5.market.alicloudapi.com"
url = "/api/v1/mobile/info?appkey=xxx"

cli = client.DefaultClient(app_key="appKey", app_secret="appSecret")

# GET
# req = request.Request(host=host,protocol=constant.HTTP, url=url, method="GET", time_out=30000)
# print cli.execute(req)


#post body stream

import json
req_post = request.Request(host=host, protocol=constant.HTTP, url=url, method="POST", time_out=30000)
body = {}
body["token"] = "xxx"
req_post.set_body(json.dumps(body))
req_post.set_content_type(constant.CONTENT_TYPE_STREAM)
_, _, data = cli.execute(req_post)
print(json.loads(data))


#post form

# req_post = request.Request(host=host, protocol=constant.HTTP, url=url, method="POST", time_out=30000)
# bodyMap = {}
# bodyMap["bodyForm1"] = "fwefwef"
# bodyMap["bodyForm2"] = "ffwefwef"
# req_post.set_body(bodyMap)
# req_post.set_content_type(constant.CONTENT_TYPE_FORM)
# print cli.execute(req_post)