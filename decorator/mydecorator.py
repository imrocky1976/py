import functools

## 登录状态检查

def user_is_authed(request):
    if (request["name"] == "xiaoming"):
        return True
    else:
        return False

def auth(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        request = args[0]
        if user_is_authed(request):
            return func(*args, **kwargs)
        else:
            raise Exception(f"user is not authed. request: {request}")
    return wrapper


@auth
def order(request):
    print(f"order called. order info: {request}")


if __name__ == '__main__':
    request = {"name": "xiaoming", "goods": "toy", "num": 1}
    try:
        order(request)
    except Exception as e:
        print(f"Exception catched: {e}")

    request = {"name": "xiaomei", "goods": "toy", "num": 1}
    try:
        order(request)
    except Exception as e:
        print(f"Exception catched: {e}")


## 日志记录，性能监视
import time
import functools

def log_execution_time(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        res = func(*args, **kwargs)
        end = time.perf_counter()
        print('{} took {} ms'.format(func.__name__, (end - start) * 1000))
        return res
    return wrapper
    
@log_execution_time
def calculate_similarity(items):
    print(i for i in range(1000000))


## 输入合理性检查
import functools

def validation_check(input):
    @functools.wraps(func)
    def wrapper(*args, **kwargs): 
        ... # 检查输入是否合法
    
@validation_check
def neural_network_training(param1, param2, ...):
    ...
