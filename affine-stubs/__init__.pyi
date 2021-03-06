from typing import NoReturn, Optional, Tuple, TypeVar, Union

class AffineError(Exception): ...
class TransformNotInvertibleError(AffineError): ...
class UndefinedRotationError(AffineError): ...

T = TypeVar("T", "Affine", Tuple[float, float])

# We don't subclass from NamedTuple because the implementation of Affine breaks some
# typing requirements, especially
# https://mypy.readthedocs.io/en/stable/common_issues.html#incompatible-overrides
# Because the typing of `__mul__` of NamedTuple is tuple input, tuple output, we can't
# provide a case where input is Affine and output is Affine, as that would break the
# Liskov principle.
class Affine:
    a: float
    b: float
    c: float
    d: float
    e: float
    f: float
    g: float = ...
    h: float = ...
    i: float = ...

    precision: float = ...
    def __new__(cls, a: float, b: float, c: float, d: float, e: float, f: float): ...
    @classmethod
    def from_gdal(
        cls, c: float, a: float, b: float, f: float, d: float, e: float
    ) -> "Affine": ...
    @classmethod
    def identity(cls) -> "Affine": ...
    @classmethod
    def translation(cls, xoff: float, yoff: float) -> "Affine": ...
    @classmethod
    def scale(cls, *scaling: Union[float, Tuple[float, float]]) -> "Affine": ...
    @classmethod
    def shear(cls, x_angle: float = ..., y_angle: float = ...) -> "Affine": ...
    @classmethod
    def rotation(
        cls, angle: float, pivot: Optional[Tuple[float, float]] = ...
    ) -> "Affine": ...
    @classmethod
    def permutation(cls, *scaling: Union[float, Tuple[float, float]]) -> "Affine": ...
    def to_gdal(self) -> Tuple[float, float, float, float, float, float]: ...
    def to_shapely(self) -> Tuple[float, float, float, float, float, float]: ...
    @property
    def xoff(self) -> float: ...
    @property
    def yoff(self) -> float: ...
    @property
    def determinant(self) -> float: ...
    @property
    def eccentricity(self) -> float: ...
    @property
    def rotation_angle(self) -> float: ...
    @property
    def is_identity(self) -> bool: ...
    @property
    def is_rectilinear(self) -> bool: ...
    @property
    def is_conformal(self) -> bool: ...
    @property
    def is_orthonormal(self) -> bool: ...
    @property
    def is_degenerate(self) -> bool: ...
    @property
    def is_proper(self) -> bool: ...
    @property
    def column_vectors(
        self,
    ) -> Tuple[Tuple[float, float], Tuple[float, float], Tuple[float, float]]: ...
    def almost_equals(self, other: "Affine", precision: float = ...) -> bool: ...
    def __gt__(self, other: "Affine") -> NoReturn: ...
    def __ge__(self, other: "Affine") -> NoReturn: ...
    def __lt__(self, other: "Affine") -> NoReturn: ...
    def __le__(self, other: "Affine") -> NoReturn: ...
    def __add__(self, other: "Affine") -> NoReturn: ...
    def __iadd__(self, other: "Affine") -> NoReturn: ...
    def __mul__(self, other: T) -> T: ...
    def __rmul__(self, other: T) -> T: ...
    def __imul__(self, other: T) -> T: ...
    def itransform(self, seq: Tuple[float, float]) -> None: ...
    def __invert__(self) -> "Affine": ...
    # __hash__: Any
    def __getnewargs__(self) -> Tuple[float, float, float, float, float, float]: ...

def loadsw(s: str) -> "Affine": ...
def dumpsw(obj: "Affine") -> str: ...
