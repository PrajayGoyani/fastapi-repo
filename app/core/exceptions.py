from fastapi import HTTPException, status


class AppException:
    @staticmethod
    def error(status_code: int, message: str):
        return HTTPException(
            status_code=status_code,
            detail={"message": message},
        )

    @staticmethod
    def conflict(message: str):
        return AppException.error(status.HTTP_409_CONFLICT, message)

    @staticmethod
    def bad_request(message: str):
        return AppException.error(status.HTTP_400_BAD_REQUEST, message)

    @staticmethod
    def not_found(message: str):
        return AppException.error(status.HTTP_404_NOT_FOUND, message)
    
    @staticmethod
    def unauthorised(message: str):
        return AppException.error(status.HTTP_401_UNAUTHORIZED, message)