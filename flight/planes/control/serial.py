from concurrent.futures import Future


class SerialCP:
    def __call__(self, fn, /, *args, **kwargs) -> Future:  # noqa
        future: Future = Future()
        try:
            result = fn(*args, **kwargs)
            future.set_result(result)
        except Exception as exception:
            future.set_exception(exception)
        return future
