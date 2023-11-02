import traceback


class TopException(Exception):
    """
    项目中自定义的异常的顶层基类，包括异常堆栈的打印，error code和error msg的格式化输出
    """

    def __init__(self, code, msg):
        self.code = code
        self.msg = msg
        super().__init__(self, code, msg)

    @property
    def trace_back(self):
        return traceback.format_exc()

    def __str__(self):
        return f"error code: [{self.code}]; err msg: [{self.msg}]"


class ValidError(Exception):
    def __init__(self, *args, **kwargs):
        pass


class ArgsVerifyException(ValueError):
    def __init__(self, *args, **kwargs):
        pass


class LoginError(RuntimeError):
    def __init__(self, *args, **kwargs):
        pass


class RoleError(RuntimeError):
    def __init__(self, *args, **kwargs):
        pass
