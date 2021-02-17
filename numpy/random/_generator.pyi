import sys
from typing import Any, Callable, Dict, Literal, Optional, Sequence, Tuple, Type, Union, overload

from numpy import (
    bool_,
    double,
    dtype,
    float32,
    float64,
    int8,
    int16,
    int32,
    int64,
    int_,
    ndarray,
    single,
    uint,
    uint8,
    uint16,
    uint32,
    uint64,
)
from numpy.random import BitGenerator, SeedSequence
from numpy.typing import (
    ArrayLike,
    _ArrayLikeFloat_co,
    _ArrayLikeInt_co,
    _BoolCodes,
    _DoubleCodes,
    _DTypeLikeBool,
    _DTypeLikeInt,
    _DTypeLikeUInt,
    _Float32Codes,
    _Float64Codes,
    _Int8Codes,
    _Int16Codes,
    _Int32Codes,
    _Int64Codes,
    _IntCodes,
    _ShapeLike,
    _SingleCodes,
    _SupportsDType,
    _UInt8Codes,
    _UInt16Codes,
    _UInt32Codes,
    _UInt64Codes,
    _UIntCodes,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

_DTypeLikeFloat32 = Union[
    dtype[float32],
    _SupportsDType[dtype[float32]],
    Type[float32],
    _Float32Codes,
    _SingleCodes,
]

_DTypeLikeFloat64 = Union[
    dtype[float64],
    _SupportsDType[dtype[float64]],
    Type[float],
    Type[float64],
    _Float64Codes,
    _DoubleCodes,
]

class Generator:
    # COMPLETE
    def __init__(self, bit_generator: BitGenerator) -> None: ...
    def __repr__(self) -> str: ...
    def __str__(self) -> str: ...
    # Pickling support:
    def __getstate__(self) -> Dict[str, Any]: ...
    def __setstate__(self, state: Dict[str, Any]) -> None: ...
    def __reduce__(self) -> Tuple[Callable[[str], BitGenerator], Tuple[str], Dict[str, Any]]: ...
    @property
    def bit_generator(self) -> BitGenerator: ...
    def bytes(self, length: int) -> str: ...
    @overload
    def standard_normal(  # type: ignore[misc]
        self,
        size: None = ...,
        dtype: Union[_DTypeLikeFloat32, _DTypeLikeFloat64] = ...,
        out: None = ...,
    ) -> float: ...
    @overload
    def standard_normal(  # type: ignore[misc]
        self,
        size: _ShapeLike = ...,
        dtype: Union[_DTypeLikeFloat32, _DTypeLikeFloat64] = ...,
        out: Optional[ndarray[Any, dtype[Union[float32, float64]]]] = ...,
    ) -> ndarray[Any, dtype[Union[float32, float64]]]: ...
    @overload
    def permutation(self, x: int, axis: int = ...) -> ndarray[Any, dtype[int64]]: ...
    @overload
    def permutation(self, x: ArrayLike, axis: int = ...) -> ndarray[Any, Any]: ...
    @overload
    def standard_cauchy(self, size: None = ...) -> float: ...  # type: ignore[misc]
    @overload
    def standard_cauchy(self, size: Optional[_ShapeLike] = ...) -> ndarray[Any, dtype[float64]]: ...
    @overload
    def standard_exponential(  # type: ignore[misc]
        self,
        size: None = ...,
        dtype: Union[_DTypeLikeFloat32, _DTypeLikeFloat64] = ...,
        method: Literal["zig", "inv"] = ...,
        out: None = ...,
    ) -> float: ...
    @overload
    def standard_exponential(
        self,
        size: _ShapeLike = ...,
        dtype: Union[_DTypeLikeFloat32, _DTypeLikeFloat64] = ...,
        method: Literal["zig", "inv"] = ...,
        out: Optional[ndarray[Any, dtype[Union[float32, float64]]]] = ...,
    ) -> ndarray[Any, dtype[Union[float32, float64]]]: ...
    @overload
    def standard_exponential(
        self,
        size: Optional[_ShapeLike] = ...,
        dtype: Union[_DTypeLikeFloat32, _DTypeLikeFloat64] = ...,
        method: Literal["zig", "inv"] = ...,
        out: ndarray[Any, dtype[Union[float32, float64]]] = ...,
    ) -> ndarray[Any, dtype[Union[float32, float64]]]: ...
    @overload
    def random(  # type: ignore[misc]
        self,
        size: None = ...,
        dtype: Union[_DTypeLikeFloat32, _DTypeLikeFloat64] = ...,
        out: None = ...,
    ) -> float: ...
    @overload
    def random(
        self,
        size: _ShapeLike = ...,
        dtype: Union[_DTypeLikeFloat32, _DTypeLikeFloat64] = ...,
        out: Optional[ndarray[Any, dtype[Union[float32, float64]]]] = ...,
    ) -> ndarray[Any, dtype[Union[float32, float64]]]: ...
    @overload
    def beta(self, a: float, b: float, size: None = ...) -> float: ...  # type: ignore[misc]
    @overload
    def beta(
        self, a: _ArrayLikeFloat_co, b: _ArrayLikeFloat_co, size: Optional[_ShapeLike] = ...
    ) -> ndarray[Any, dtype[float64]]: ...
    @overload
    def exponential(self, scale: float = ..., size: None = ...) -> float: ...  # type: ignore[misc]
    @overload
    def exponential(
        self, scale: _ArrayLikeFloat_co = ..., size: Optional[_ShapeLike] = ...
    ) -> ndarray[Any, dtype[float64]]: ...
    @overload
    def integers(  # type: ignore[misc]
        self,
        low: int,
        high: Optional[int] = ...,
        size: None = ...,
        dtype: _DTypeLikeBool = ...,
        endpoint: bool = ...,
    ) -> bool: ...
    @overload
    def integers(  # type: ignore[misc]
        self,
        low: int,
        high: Optional[int] = ...,
        size: None = ...,
        dtype: Union[_DTypeLikeInt, _DTypeLikeUInt] = ...,
        endpoint: bool = ...,
    ) -> int: ...
    @overload
    def integers(  # type: ignore[misc]
        self,
        low: _ArrayLikeInt_co,
        high: Optional[_ArrayLikeInt_co] = ...,
        size: Optional[_ShapeLike] = ...,
        dtype: Union[
            dtype[bool_], Type[bool], Type[bool_], _BoolCodes, _SupportsDType[dtype[bool_]]
        ] = ...,
        endpoint: bool = ...,
    ) -> ndarray[Any, dtype[bool_]]: ...
    @overload
    def integers(  # type: ignore[misc]
        self,
        low: _ArrayLikeInt_co,
        high: Optional[_ArrayLikeInt_co] = ...,
        size: Optional[_ShapeLike] = ...,
        dtype: Union[
            dtype[int_], Type[int], Type[int_], _IntCodes, _SupportsDType[dtype[int_]]
        ] = ...,
        endpoint: bool = ...,
    ) -> ndarray[Any, dtype[int_]]: ...
    @overload
    def integers(  # type: ignore[misc]
        self,
        low: _ArrayLikeInt_co,
        high: Optional[_ArrayLikeInt_co] = ...,
        size: Optional[_ShapeLike] = ...,
        dtype: Union[dtype[uint], Type[uint], _UIntCodes, _SupportsDType[dtype[uint]]] = ...,
        endpoint: bool = ...,
    ) -> ndarray[Any, dtype[uint]]: ...
    @overload
    def integers(  # type: ignore[misc]
        self,
        low: _ArrayLikeInt_co,
        high: Optional[_ArrayLikeInt_co] = ...,
        size: Optional[_ShapeLike] = ...,
        dtype: Union[dtype[int8], Type[int8], _Int8Codes, _SupportsDType[dtype[int8]]] = ...,
        endpoint: bool = ...,
    ) -> ndarray[Any, dtype[int8]]: ...
    @overload
    def integers(  # type: ignore[misc]
        self,
        low: _ArrayLikeInt_co,
        high: Optional[_ArrayLikeInt_co] = ...,
        size: Optional[_ShapeLike] = ...,
        dtype: Union[dtype[int16], Type[int16], _Int16Codes, _SupportsDType[dtype[int16]]] = ...,
        endpoint: bool = ...,
    ) -> ndarray[Any, dtype[int16]]: ...
    @overload
    def integers(  # type: ignore[misc]
        self,
        low: _ArrayLikeInt_co,
        high: Optional[_ArrayLikeInt_co] = ...,
        size: Optional[_ShapeLike] = ...,
        dtype: Union[dtype[int32], Type[int32], _Int32Codes, _SupportsDType[dtype[int32]]] = ...,
        endpoint: bool = ...,
    ) -> ndarray[Any, dtype[Union[int32]]]: ...
    @overload
    def integers(  # type: ignore[misc]
        self,
        low: _ArrayLikeInt_co,
        high: Optional[_ArrayLikeInt_co] = ...,
        size: Optional[_ShapeLike] = ...,
        dtype: Optional[
            Union[dtype[int64], Type[int64], _Int64Codes, _SupportsDType[dtype[int64]]]
        ] = ...,
        endpoint: bool = ...,
    ) -> ndarray[Any, dtype[int64]]: ...
    @overload
    def integers(  # type: ignore[misc]
        self,
        low: _ArrayLikeInt_co,
        high: Optional[_ArrayLikeInt_co] = ...,
        size: Optional[_ShapeLike] = ...,
        dtype: Union[dtype[uint8], Type[uint8], _UInt8Codes, _SupportsDType[dtype[uint8]]] = ...,
        endpoint: bool = ...,
    ) -> ndarray[Any, dtype[uint8]]: ...
    @overload
    def integers(  # type: ignore[misc]
        self,
        low: _ArrayLikeInt_co,
        high: Optional[_ArrayLikeInt_co] = ...,
        size: Optional[_ShapeLike] = ...,
        dtype: Union[
            dtype[uint16], Type[uint16], _UInt16Codes, _SupportsDType[dtype[uint16]]
        ] = ...,
        endpoint: bool = ...,
    ) -> ndarray[Any, dtype[Union[uint16]]]: ...
    @overload
    def integers(  # type: ignore[misc]
        self,
        low: _ArrayLikeInt_co,
        high: Optional[_ArrayLikeInt_co] = ...,
        size: Optional[_ShapeLike] = ...,
        dtype: Union[
            dtype[uint32], Type[uint32], _UInt32Codes, _SupportsDType[dtype[uint32]]
        ] = ...,
        endpoint: bool = ...,
    ) -> ndarray[Any, dtype[uint32]]: ...
    @overload
    def integers(  # type: ignore[misc]
        self,
        low: _ArrayLikeInt_co,
        high: Optional[_ArrayLikeInt_co] = ...,
        size: Optional[_ShapeLike] = ...,
        dtype: Union[
            dtype[uint64], Type[uint64], _UInt64Codes, _SupportsDType[dtype[uint64]]
        ] = ...,
        endpoint: bool = ...,
    ) -> ndarray[Any, dtype[uint64]]: ...
    # TODO: Use a TypeVar _T here to get away from Any output?  Should be int->ndarray[Any,dtype[int64]], ArrayLike[_T] -> Union[_T, ndarray[Any,Any]]
    def choice(
        self,
        a: ArrayLike,
        size: Optional[_ShapeLike] = ...,
        replace: bool = ...,
        p: Optional[_ArrayLikeFloat_co] = ...,
        axis: Optional[int] = ...,
        shuffle: bool = ...,
    ) -> Any: ...
    @overload
    def uniform(self, low: float = ..., high: float = ..., size: None = ...) -> float: ...  # type: ignore[misc]
    @overload
    def uniform(
        self,
        low: _ArrayLikeFloat_co = ...,
        high: _ArrayLikeFloat_co = ...,
        size: Optional[_ShapeLike] = ...,
    ) -> ndarray[Any, dtype[float64]]: ...
    @overload
    def normal(self, loc: float = ..., scale: float = ..., size: None = ...) -> float: ...  # type: ignore[misc]
    @overload
    def normal(
        self,
        loc: _ArrayLikeFloat_co = ...,
        scale: _ArrayLikeFloat_co = ...,
        size: Optional[_ShapeLike] = ...,
    ) -> ndarray[Any, dtype[float64]]: ...
    @overload
    def standard_gamma(  # type: ignore[misc]
        self,
        shape: float,
        size: None = ...,
        dtype: Union[_DTypeLikeFloat32, _DTypeLikeFloat64] = ...,
        out: None = ...,
    ) -> float: ...
    @overload
    def standard_gamma(
        self,
        shape: _ArrayLikeFloat_co,
        size: Optional[_ShapeLike] = ...,
        dtype: Union[_DTypeLikeFloat32, _DTypeLikeFloat64] = ...,
        out: Optional[ndarray[Any, dtype[Union[float32, float64]]]] = ...,
    ) -> ndarray[Any, dtype[float64]]: ...
    @overload
    def gamma(self, shape: float, scale: float = ..., size: None = ...) -> float: ...  # type: ignore[misc]
    @overload
    def gamma(
        self,
        shape: _ArrayLikeFloat_co,
        scale: _ArrayLikeFloat_co = ...,
        size: Optional[_ShapeLike] = ...,
    ) -> ndarray[Any, dtype[float64]]: ...
    @overload
    def f(self, dfnum: float, dfden: float, size: None = ...) -> float: ...  # type: ignore[misc]
    @overload
    def f(
        self, dfnum: _ArrayLikeFloat_co, dfden: _ArrayLikeFloat_co, size: Optional[_ShapeLike] = ...
    ) -> ndarray[Any, dtype[float64]]: ...
    @overload
    def noncentral_f(self, dfnum: float, dfden: float, nonc: float, size: None = ...) -> float: ...  # type: ignore[misc]
    @overload
    def noncentral_f(
        self,
        dfnum: _ArrayLikeFloat_co,
        dfden: _ArrayLikeFloat_co,
        nonc: _ArrayLikeFloat_co,
        size: Optional[_ShapeLike] = ...,
    ) -> ndarray[Any, dtype[float64]]: ...
    @overload
    def chisquare(self, df: float, size: None = ...) -> float: ...  # type: ignore[misc]
    @overload
    def chisquare(
        self, df: _ArrayLikeFloat_co, size: Optional[_ShapeLike] = ...
    ) -> ndarray[Any, dtype[float64]]: ...
    @overload
    def noncentral_chisquare(self, df: float, nonc: float, size: None = ...) -> float: ...  # type: ignore[misc]
    @overload
    def noncentral_chisquare(
        self, df: _ArrayLikeFloat_co, nonc: _ArrayLikeFloat_co, size: Optional[_ShapeLike] = ...
    ) -> ndarray[Any, dtype[float64]]: ...
    @overload
    def standard_t(self, df: float, size: None = ...) -> float: ...  # type: ignore[misc]
    @overload
    def standard_t(
        self, df: _ArrayLikeFloat_co, size: None = ...
    ) -> ndarray[Any, dtype[float64]]: ...
    @overload
    def standard_t(
        self, df: _ArrayLikeFloat_co, size: _ShapeLike = ...
    ) -> ndarray[Any, dtype[float64]]: ...
    @overload
    def vonmises(self, mu: float, kappa: float, size: None = ...) -> float: ...  # type: ignore[misc]
    @overload
    def vonmises(
        self, mu: _ArrayLikeFloat_co, kappa: _ArrayLikeFloat_co, size: Optional[_ShapeLike] = ...
    ) -> ndarray[Any, dtype[float64]]: ...
    @overload
    def pareto(self, a: float, size: None = ...) -> float: ...  # type: ignore[misc]
    @overload
    def pareto(
        self, a: _ArrayLikeFloat_co, size: Optional[_ShapeLike] = ...
    ) -> ndarray[Any, dtype[float64]]: ...
    @overload
    def weibull(self, a: float, size: None = ...) -> float: ...  # type: ignore[misc]
    @overload
    def weibull(
        self, a: _ArrayLikeFloat_co, size: Optional[_ShapeLike] = ...
    ) -> ndarray[Any, dtype[float64]]: ...
    @overload
    def power(self, a: float, size: None = ...) -> float: ...  # type: ignore[misc]
    @overload
    def power(
        self, a: _ArrayLikeFloat_co, size: Optional[_ShapeLike] = ...
    ) -> ndarray[Any, dtype[float64]]: ...
    @overload
    def laplace(self, loc: float = ..., scale: float = ..., size: None = ...) -> float: ...  # type: ignore[misc]
    @overload
    def laplace(
        self,
        loc: _ArrayLikeFloat_co = ...,
        scale: _ArrayLikeFloat_co = ...,
        size: Optional[_ShapeLike] = ...,
    ) -> ndarray[Any, dtype[float64]]: ...
    @overload
    def gumbel(self, loc: float = ..., scale: float = ..., size: None = ...) -> float: ...  # type: ignore[misc]
    @overload
    def gumbel(
        self,
        loc: _ArrayLikeFloat_co = ...,
        scale: _ArrayLikeFloat_co = ...,
        size: Optional[_ShapeLike] = ...,
    ) -> ndarray[Any, dtype[float64]]: ...
    @overload
    def logistic(self, loc: float = ..., scale: float = ..., size: None = ...) -> float: ...  # type: ignore[misc]
    @overload
    def logistic(
        self,
        loc: _ArrayLikeFloat_co = ...,
        scale: _ArrayLikeFloat_co = ...,
        size: Optional[_ShapeLike] = ...,
    ) -> ndarray[Any, dtype[float64]]: ...
    @overload
    def lognormal(self, mean: float = ..., sigma: float = ..., size: None = ...) -> float: ...  # type: ignore[misc]
    @overload
    def lognormal(
        self,
        mean: _ArrayLikeFloat_co = ...,
        sigma: _ArrayLikeFloat_co = ...,
        size: Optional[_ShapeLike] = ...,
    ) -> ndarray[Any, dtype[float64]]: ...
    @overload
    def rayleigh(self, scale: float = ..., size: None = ...) -> float: ...  # type: ignore[misc]
    @overload
    def rayleigh(
        self, scale: _ArrayLikeFloat_co = ..., size: Optional[_ShapeLike] = ...
    ) -> ndarray[Any, dtype[float64]]: ...
    @overload
    def wald(self, mean: float, scale: float, size: None = ...) -> float: ...  # type: ignore[misc]
    @overload
    def wald(
        self, mean: _ArrayLikeFloat_co, scale: _ArrayLikeFloat_co, size: Optional[_ShapeLike] = ...
    ) -> ndarray[Any, dtype[float64]]: ...
    @overload
    def triangular(self, left: float, mode: float, right: float, size: None = ...) -> float: ...  # type: ignore[misc]
    @overload
    def triangular(
        self,
        left: _ArrayLikeFloat_co,
        mode: _ArrayLikeFloat_co,
        right: _ArrayLikeFloat_co,
        size: Optional[_ShapeLike] = ...,
    ) -> ndarray[Any, dtype[float64]]: ...
    # Complicated, discrete distributions:
    @overload
    def binomial(self, n: int, p: float, size: None = ...) -> int: ...  # type: ignore[misc]
    @overload
    def binomial(
        self, n: _ArrayLikeInt_co, p: _ArrayLikeFloat_co, size: Optional[_ShapeLike] = ...
    ) -> ndarray[Any, dtype[int64]]: ...
    @overload
    def negative_binomial(self, n: float, p: float, size: None = ...) -> int: ...  # type: ignore[misc]
    @overload
    def negative_binomial(
        self, n: _ArrayLikeFloat_co, p: _ArrayLikeFloat_co, size: Optional[_ShapeLike] = ...
    ) -> ndarray[Any, dtype[int64]]: ...
    @overload
    def poisson(self, lam: float = ..., size: None = ...) -> int: ...  # type: ignore[misc]
    @overload
    def poisson(
        self, lam: _ArrayLikeFloat_co = ..., size: Optional[_ShapeLike] = ...
    ) -> ndarray[Any, dtype[int64]]: ...
    @overload
    def zipf(self, a: float, size: None = ...) -> int: ...  # type: ignore[misc]
    @overload
    def zipf(
        self, a: _ArrayLikeFloat_co, size: Optional[_ShapeLike] = ...
    ) -> ndarray[Any, dtype[int64]]: ...
    @overload
    def geometric(self, p: float, size: None = ...) -> int: ...  # type: ignore[misc]
    @overload
    def geometric(
        self, p: _ArrayLikeFloat_co, size: Optional[_ShapeLike] = ...
    ) -> ndarray[Any, dtype[int64]]: ...
    @overload
    def hypergeometric(self, ngood: int, nbad: int, nsample: int, size: None = ...) -> int: ...  # type: ignore[misc]
    @overload
    def hypergeometric(
        self,
        ngood: _ArrayLikeInt_co,
        nbad: _ArrayLikeInt_co,
        nsample: _ArrayLikeInt_co,
        size: Optional[_ShapeLike] = ...,
    ) -> ndarray[Any, dtype[int64]]: ...
    @overload
    def logseries(self, p: float, size: None = ...) -> int: ...  # type: ignore[misc]
    @overload
    def logseries(
        self, p: _ArrayLikeFloat_co, size: Optional[_ShapeLike] = ...
    ) -> ndarray[Any, dtype[int64]]: ...
    # Multivariate distributions:
    def multivariate_normal(
        self,
        mean: _ArrayLikeFloat_co,
        cov: _ArrayLikeFloat_co,
        size: Optional[_ShapeLike] = ...,
        check_valid: Literal["warn", "raise", "ignore"] = ...,
        tol: float = ...,
        *,
        method: Literal["svd", "eigh", "cholesky"] = ...
    ) -> ndarray[Any, dtype[float64]]: ...
    def multinomial(
        self, n: _ArrayLikeInt_co, pvals: _ArrayLikeFloat_co, size: Optional[_ShapeLike] = ...
    ) -> ndarray[Any, dtype[int64]]: ...
    def multivariate_hypergeometric(
        self,
        colors: _ArrayLikeInt_co,
        nsample: int,
        size: Optional[_ShapeLike] = ...,
        method: Literal["marginals", "count"] = ...,
    ) -> ndarray[Any, dtype[int64]]: ...
    def dirichlet(
        self, alpha: _ArrayLikeFloat_co, size: Optional[_ShapeLike] = ...
    ) -> ndarray[Any, dtype[float64]]: ...
    def permuted(
        self, x: ArrayLike, *, axis: Optional[int] = ..., out: Optional[ndarray[Any, Any]] = ...
    ) -> ndarray[Any, Any]: ...
    def shuffle(self, x: ArrayLike, axis: int = ...) -> Sequence[Any]: ...

def default_rng(seed: Union[None, _ArrayLikeInt_co, SeedSequence] = ...) -> Generator: ...
