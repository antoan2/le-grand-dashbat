from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import Literal, Optional

DatasetName = Literal["democratie", "transition", "fiscalite", "organisation"]


class AuthorType(Enum):
    CITOYEN = "Citoyen / Citoyenne"
    ORGA_NON_LUCRATIF = "Organisation à but non lucratif"
    ELU = "Élu / élue et Institution"
    ORGA_LUCRATIF = "Organisation à but lucratif"


@dataclass
class Answer:
    id: str
    published_at: datetime
    author_id: str
    author_type: Optional[AuthorType]
    author_zip_code: str
