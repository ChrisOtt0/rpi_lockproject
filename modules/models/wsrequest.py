class WsRequest(object):
    def __init__(self, action: str, args: dict):
        self.action = action
        self.args = args

