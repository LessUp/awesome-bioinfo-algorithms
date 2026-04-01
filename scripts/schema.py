"""
Data models for Awesome Bioinformatics Algorithms.
Defines Category, Reference, and AlgorithmEntry dataclasses.
"""

from dataclasses import dataclass, field
from typing import Optional

VALID_DIFFICULTIES = ("beginner", "intermediate", "advanced")
VALID_REFERENCE_TYPES = ("tutorial", "blog", "video", "book", "documentation", "slides")


@dataclass
class Reference:
    """Represents an extended reference (tutorial, blog, video, etc.)."""

    url: str
    title: str = ""
    type: str = ""

    def to_dict(self) -> dict:
        """Convert to dictionary for serialization."""
        result: dict = {"url": self.url}
        if self.title:
            result["title"] = self.title
        if self.type:
            result["type"] = self.type
        return result

    @classmethod
    def from_dict(cls, data: dict) -> "Reference":
        """Create Reference from dictionary."""
        return cls(
            url=data["url"],
            title=data.get("title", ""),
            type=data.get("type", ""),
        )


@dataclass
class Category:
    """Represents an algorithm category with optional subcategories."""

    id: str
    name: str
    name_en: str
    description: str = ""
    subcategories: list["Category"] = field(default_factory=list)
    parent_id: Optional[str] = None

    def to_dict(self) -> dict:
        """Convert to dictionary for serialization."""
        result: dict = {
            "id": self.id,
            "name": self.name,
            "name_en": self.name_en,
            "description": self.description,
        }
        if self.subcategories:
            result["subcategories"] = [sub.to_dict() for sub in self.subcategories]
        return result

    @classmethod
    def from_dict(cls, data: dict, parent_id: Optional[str] = None) -> "Category":
        """Create Category from dictionary."""
        subcategories = []
        if "subcategories" in data:
            subcategories = [
                cls.from_dict(sub, parent_id=data["id"]) for sub in data["subcategories"]
            ]
        return cls(
            id=data["id"],
            name=data["name"],
            name_en=data["name_en"],
            description=data.get("description", ""),
            subcategories=subcategories,
            parent_id=parent_id,
        )


@dataclass
class AlgorithmEntry:
    """Represents a single algorithm entry."""

    # Required fields
    id: str
    name: str
    description: str
    purpose: str
    time_complexity: str
    category: str

    # Optional fields
    space_complexity: str = ""
    year: int = 0
    paper_url: str = ""
    implementation_url: str = ""
    related_tools: list[str] = field(default_factory=list)
    tags: list[str] = field(default_factory=list)
    subcategory: str = ""
    difficulty: str = ""
    language: list[str] = field(default_factory=list)
    references: list[Reference] = field(default_factory=list)

    def to_dict(self) -> dict:
        """Convert to dictionary for serialization."""
        result: dict = {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "purpose": self.purpose,
            "time_complexity": self.time_complexity,
            "category": self.category,
        }
        # Include optional fields only if they have values
        if self.space_complexity:
            result["space_complexity"] = self.space_complexity
        if self.year:
            result["year"] = self.year
        if self.paper_url:
            result["paper_url"] = self.paper_url
        if self.implementation_url:
            result["implementation_url"] = self.implementation_url
        if self.related_tools:
            result["related_tools"] = self.related_tools
        if self.tags:
            result["tags"] = self.tags
        if self.subcategory:
            result["subcategory"] = self.subcategory
        if self.difficulty:
            result["difficulty"] = self.difficulty
        if self.language:
            result["language"] = self.language
        if self.references:
            result["references"] = [ref.to_dict() for ref in self.references]
        return result

    @classmethod
    def from_dict(cls, data: dict) -> "AlgorithmEntry":
        """Create AlgorithmEntry from dictionary."""
        return cls(
            id=data["id"],
            name=data["name"],
            description=data["description"],
            purpose=data["purpose"],
            time_complexity=data["time_complexity"],
            category=data["category"],
            space_complexity=data.get("space_complexity", ""),
            year=data.get("year", 0),
            paper_url=data.get("paper_url", ""),
            implementation_url=data.get("implementation_url", ""),
            related_tools=data.get("related_tools", []),
            tags=data.get("tags", []),
            subcategory=data.get("subcategory", ""),
            difficulty=data.get("difficulty", ""),
            language=data.get("language", []),
            references=[Reference.from_dict(r) for r in data.get("references", [])],
        )

    def __hash__(self) -> int:
        """Hash based on algorithm ID for use in sets and dicts."""
        return hash(self.id)
