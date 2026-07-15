from fastapi import HTTPException


class AppException:
    @staticmethod
    def error(status_code: int, message: str):
        return HTTPException(
            status_code=status_code,
            detail={"message": message},
        )

    @staticmethod
    def conflict(message: str):
        return AppException.error(409, message)

    @staticmethod
    def bad_request(message: str):
        return AppException.error(400, message)

    @staticmethod
    def not_found(message: str):
        return AppException.error(404, message)
    
    
    @staticmethod
    def unauthorised(message: str):
        return AppException.error(401, message)