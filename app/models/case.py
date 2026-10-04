from pydantic import BaseModel

class TroubleshootingCase(BaseModel):
    category: str
    error_code: str | None = None
    description: str