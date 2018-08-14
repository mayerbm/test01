from django.http import HttpResponse

class MyException(object):
    def process_exception(request, response, exception):
        return HttpResponse("出错啦~")
        # return HttpResponse(exception.message)