"""Implements the :stac-ext:`Machine Learning Dataset Extension <ml-dataset>`."""


import pystac
from pystac.extensions.base import ExtensionManagementMixin

from typing import Any, Dict, List, Tuple


SCHEMA_URI: str = "https://raw.githubusercontent.com/earthpulse/ml-dataset/main/json-schema/schema.json"
PREFIX: str = "ml-dataset:"


class MLDatasetExtension(
    pystac.Catalog, ExtensionManagementMixin[pystac.Catalog]
):
    
    catalog: pystac.Catalog
    """The :class:`~pystac.Catalog` being extended."""

    properties: Dict[str, Any]
    """The :class:`~pystac.Catalog` extra fields, including extension properties."""

    links: List[pystac.Link]
    """The list of :class:`~pystac.Link` objects associated with the
    :class:`~pystac.Catalog` being extended, including links added by this extension.
    """

    def __init__(self, catalog: pystac.Catalog):
        self.catalog = catalog
        self.id = catalog.id
        self.description = catalog.description
        self.title = catalog.title if catalog.title else None
        self.stac_extensions = catalog.stac_extensions if catalog.stac_extensions else []
        self.extra_fields = self.properties = catalog.extra_fields if catalog.extra_fields else {}
        self.links = catalog.links
        
    def apply(
        self, name: str = None
    ) -> None:
        self.name = name

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, v: str) -> None:
        self.extra_fields[f'{PREFIX}name'] = v

    @property
    def tasks(self) -> List:
        return self._tasks

    @tasks.setter
    def tasks(self, v: List|Tuple) -> None:
        self.extra_fields[f'{PREFIX}tasks'] = v

    @property
    def type(self) -> str:
        return self._type

    @type.setter
    def type(self, v: str) -> None:
        self.extra_fields[f'{PREFIX}type'] = v

    @property
    def inputs_type(self) -> str:
        return self._inputs_type

    @inputs_type.setter
    def inputs_type(self, v: str) -> None:
        self.extra_fields[f'{PREFIX}inputs_type'] = v

    @property
    def annotations_type(self) -> str:
        return self._annotations_type

    @annotations_type.setter
    def annotations_type(self, v: str) -> None:
        self.extra_fields[f'{PREFIX}annotations_type'] = v

    @property
    def quality(self) -> str:
        return self._quality

    @quality.setter
    def quality(self, v: str) -> None:
        self.extra_fields[f'{PREFIX}quality'] = v

    @property
    def version(self) -> str:
        return self._version

    @version.setter
    def version(self, v: str) -> None:
        self.extra_fields[f'{PREFIX}version'] = v

    @classmethod
    def get_schema_uri(cls) -> str:
        return SCHEMA_URI

    @classmethod
    def ext(cls, obj: pystac.Catalog, add_if_missing: bool = False) -> "MLDatasetExtension":
        if isinstance(obj, pystac.Catalog):
            cls.validate_has_extension(obj, add_if_missing)
            return MLDatasetExtension(obj)
        else:
            raise pystac.ExtensionTypeError(
                f"OrderExtension does not apply to type '{type(obj).__name__}'"
            )