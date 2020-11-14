class NotFound(Exception):
    def __init__(*args, **kwargs):
        Exception.__init__(*args, **kwargs)

class LibraryUpdateAvailable(Exception):
    def __init__(*args, **kwargs):
        Exception.__init__(*args, **kwargs)


def CheckException(data):
    errorCode: int = data["code"]
    errorMessage: str = data["message"]

    if errorCode == 404: raise NotFound(errorMessage)
    else: raise Exception(errorMessage)