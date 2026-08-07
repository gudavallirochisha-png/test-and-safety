from fastapi import HTTPException, status


class EntityNotFoundException(HTTPException):
    def __init__(self, entity_name: str, entity_id: str):
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"{entity_name} with ID '{entity_id}' was not found.",
        )


class DatabaseConnectionException(HTTPException):
    def __init__(self, message: str = "Database connection error"):
        super().__init__(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail=message,
        )
