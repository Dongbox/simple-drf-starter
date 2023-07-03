import logging
from django.http import JsonResponse, HttpResponseServerError
from django.middleware.common import MiddlewareMixin  # type: ignore


logger = logging.getLogger("django")


class CustomExceptionMiddleware(MiddlewareMixin):
    """统一异常处理中间件"""

    def process_exception(self, request, exception):
        """
        统一异常处理
        :param request: 请求对象
        :param exception: 异常对象
        :return:
        """
        # 记录详细的异常信息
        logger.error(f"Exception: {str(exception)}", exc_info=True)

        # 返回友好的错误信息给用户
        if isinstance(exception, ValueError):
            # 对于 ValueError 类型的异常，返回 400 状态码和错误信息
            return JsonResponse({"error": "Bad Request"}, status=400)
        elif isinstance(exception, KeyError):
            # 对于 KeyError 类型的异常，返回 404 状态码和错误信息
            return JsonResponse({"error": "Not Found"}, status=404)
        else:
            # 对于其他类型的异常，返回 500 状态码和错误信息
            return HttpResponseServerError("Internal Server Error")

    def process_request(self, request):
        """处理请求"""
        # 在这里可以添加处理请求的代码
        pass

    def process_view(self, request, view_func, view_args, view_kwargs):
        """处理视图"""
        # 在这里可以添加处理视图的代码
        pass

    def process_response(self, request, response):
        """处理响应"""
        # 在这里可以添加处理响应的代码
        return response
