class JsonResponse:
    def __init__(self, data, is_error, status, error_message):
        self.status = status
        self.is_error = is_error
        self.error_message = error_message
        self.data = data

    def __str__(self):
        return "status: "+self.status+", error_message: "+self.error_message
