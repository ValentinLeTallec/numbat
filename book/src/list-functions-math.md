<!-- NOTE! This file is auto-generated -->

# Mathematical functions

### `id` (Identity function)

```nbt
fn id<A>(x: A) -> A
```
(defined in *core::functions*)

### `abs` (Absolute value)
More information [here](https://doc.rust-lang.org/std/primitive.f64.html#method.abs).

```nbt
fn abs<T: Dim>(x: T) -> T
```
(defined in *core::functions*)

### `round` (Round)
Round to the nearest integer.
More information [here](https://doc.rust-lang.org/std/primitive.f64.html#method.round).

```nbt
fn round<T: Dim>(x: T) -> T
```
(defined in *core::functions*)

### `floor` (Floor function)
More information [here](https://doc.rust-lang.org/std/primitive.f64.html#method.floor).

```nbt
fn floor<T: Dim>(x: T) -> T
```
(defined in *core::functions*)

### `ceil` (Ceil function)
More information [here](https://doc.rust-lang.org/std/primitive.f64.html#method.ceil).

```nbt
fn ceil<T: Dim>(x: T) -> T
```
(defined in *core::functions*)

### `mod` (Modulo)
More information [here](https://doc.rust-lang.org/std/primitive.f64.html#method.rem_euclid).

```nbt
fn mod<T: Dim>(a: T, b: T) -> T
```
(defined in *core::functions*)

### `unit_of`

```nbt
fn unit_of<T: Dim>(x: T) -> T
```
(defined in *core::quantities*)

### `value_of`

```nbt
fn value_of<T: Dim>(x: T) -> Scalar
```
(defined in *core::quantities*)

### `is_nan`

```nbt
fn is_nan<T: Dim>(n: T) -> Bool
```
(defined in *core::quantities*)

### `is_infinite`

```nbt
fn is_infinite<T: Dim>(n: T) -> Bool
```
(defined in *core::quantities*)

### `sqrt` (Square root)
More information [here](https://en.wikipedia.org/wiki/Square_root).

```nbt
fn sqrt<D: Dim>(x: D^2) -> D
```
(defined in *math::functions*)

### `sqr` (Square function)

```nbt
fn sqr<D: Dim>(x: D) -> D^2
```
(defined in *math::functions*)

### `exp` (Exponential function)
More information [here](https://en.wikipedia.org/wiki/Exponential_function).

```nbt
fn exp(x: Scalar) -> Scalar
```
(defined in *math::functions*)

### `ln` (Natural logarithm)
More information [here](https://en.wikipedia.org/wiki/Natural_logarithm).

```nbt
fn ln(x: Scalar) -> Scalar
```
(defined in *math::functions*)

### `log` (Natural logarithm)
More information [here](https://en.wikipedia.org/wiki/Natural_logarithm).

```nbt
fn log(x: Scalar) -> Scalar
```
(defined in *math::functions*)

### `log10` (Common logarithm)
More information [here](https://en.wikipedia.org/wiki/Common_logarithm).

```nbt
fn log10(x: Scalar) -> Scalar
```
(defined in *math::functions*)

### `log2` (Binary logarithm)
More information [here](https://en.wikipedia.org/wiki/Binary_logarithm).

```nbt
fn log2(x: Scalar) -> Scalar
```
(defined in *math::functions*)

### `sin` (Sine)
More information [here](https://en.wikipedia.org/wiki/Trigonometric_functions).

```nbt
fn sin(x: Scalar) -> Scalar
```
(defined in *math::functions*)

### `cos` (Cosine)
More information [here](https://en.wikipedia.org/wiki/Trigonometric_functions).

```nbt
fn cos(x: Scalar) -> Scalar
```
(defined in *math::functions*)

### `tan` (Tangent)
More information [here](https://en.wikipedia.org/wiki/Trigonometric_functions).

```nbt
fn tan(x: Scalar) -> Scalar
```
(defined in *math::functions*)

### `asin` (Arc sine)
More information [here](https://en.wikipedia.org/wiki/Inverse_trigonometric_functions).

```nbt
fn asin(x: Scalar) -> Scalar
```
(defined in *math::functions*)

### `acos` (Arc cosine)
More information [here](https://en.wikipedia.org/wiki/Inverse_trigonometric_functions).

```nbt
fn acos(x: Scalar) -> Scalar
```
(defined in *math::functions*)

### `atan` (Arc tangent)
More information [here](https://en.wikipedia.org/wiki/Inverse_trigonometric_functions).

```nbt
fn atan(x: Scalar) -> Scalar
```
(defined in *math::functions*)

### `atan2`
More information [here](https://en.wikipedia.org/wiki/Atan2).

```nbt
fn atan2<T: Dim>(y: T, x: T) -> Scalar
```
(defined in *math::functions*)

### `sinh` (Hyperbolic sine)
More information [here](https://en.wikipedia.org/wiki/Hyperbolic_functions).

```nbt
fn sinh(x: Scalar) -> Scalar
```
(defined in *math::functions*)

### `cosh` (Hyperbolic cosine)
More information [here](https://en.wikipedia.org/wiki/Hyperbolic_functions).

```nbt
fn cosh(x: Scalar) -> Scalar
```
(defined in *math::functions*)

### `tanh` (Hyperbolic tangent)
More information [here](https://en.wikipedia.org/wiki/Hyperbolic_functions).

```nbt
fn tanh(x: Scalar) -> Scalar
```
(defined in *math::functions*)

### `asinh` (Area hyperbolic sine)
More information [here](https://en.wikipedia.org/wiki/Hyperbolic_functions).

```nbt
fn asinh(x: Scalar) -> Scalar
```
(defined in *math::functions*)

### `acosh` (Area hyperbolic cosine)
More information [here](https://en.wikipedia.org/wiki/Hyperbolic_functions).

```nbt
fn acosh(x: Scalar) -> Scalar
```
(defined in *math::functions*)

### `atanh` (Area hyperbolic tangent )
More information [here](https://en.wikipedia.org/wiki/Hyperbolic_functions).

```nbt
fn atanh(x: Scalar) -> Scalar
```
(defined in *math::functions*)

### `gamma` (Gamma function)
More information [here](https://en.wikipedia.org/wiki/Gamma_function).

```nbt
fn gamma(x: Scalar) -> Scalar
```
(defined in *math::functions*)

### `maximum` (Maxmimum)
Get the largest element of a list

```nbt
fn maximum<D: Dim>(xs: List<D>) -> D
```
(defined in *math::functions*)

### `minimum` (Minimum)
Get the smallest element of a list

```nbt
fn minimum<D: Dim>(xs: List<D>) -> D
```
(defined in *math::functions*)

### `mean` (Arithmetic mean)
More information [here](https://en.wikipedia.org/wiki/Arithmetic_mean).

```nbt
fn mean<D: Dim>(xs: List<D>) -> D
```
(defined in *math::functions*)

### `variance` (Variance)
Calculate the population variance of a list of quantities
More information [here](https://en.wikipedia.org/wiki/Variance).

```nbt
fn variance<D: Dim>(xs: List<D>) -> D^2
```
(defined in *math::functions*)

### `stdev` (Standard deviation)
Calculate the population standard deviation of a list of quantities
More information [here](https://en.wikipedia.org/wiki/Standard_deviation).

```nbt
fn stdev<D: Dim>(xs: List<D>) -> D
```
(defined in *math::functions*)

### `median` (Median)
Calculate the median of a list of quantities
More information [here](https://en.wikipedia.org/wiki/Median).

```nbt
fn median<D: Dim>(xs: List<D>) -> D
```
(defined in *math::functions*)

### `gcd` (Greatest common divisor)
More information [here](https://en.wikipedia.org/wiki/Greatest_common_divisor).

```nbt
fn gcd(a: Scalar, b: Scalar) -> Scalar
```
(defined in *math::functions*)

### `lcm` (Least common multiple)
More information [here](https://en.wikipedia.org/wiki/Least_common_multiple).

```nbt
fn lcm(a: Scalar, b: Scalar) -> Scalar
```
(defined in *math::functions*)

### `hypot2`

```nbt
fn hypot2<T: Dim>(x: T, y: T) -> T
```
(defined in *math::functions*)

### `hypot3`

```nbt
fn hypot3<T: Dim>(x: T, y: T, z: T) -> T
```
(defined in *math::functions*)

### `circle_area`

```nbt
fn circle_area<L: Dim>(radius: L) -> L^2
```
(defined in *math::functions*)

### `circle_circumference`

```nbt
fn circle_circumference<L: Dim>(radius: L) -> L
```
(defined in *math::functions*)

### `sphere_area`

```nbt
fn sphere_area<L: Dim>(radius: L) -> L^2
```
(defined in *math::functions*)

### `sphere_volume`

```nbt
fn sphere_volume<L: Dim>(radius: L) -> L^3
```
(defined in *math::functions*)

### `cot`

```nbt
fn cot(x: Scalar) -> Scalar
```
(defined in *math::trigonometry_extra*)

### `acot`

```nbt
fn acot(x: Scalar) -> Scalar
```
(defined in *math::trigonometry_extra*)

### `coth`

```nbt
fn coth(x: Scalar) -> Scalar
```
(defined in *math::trigonometry_extra*)

### `acoth`

```nbt
fn acoth(x: Scalar) -> Scalar
```
(defined in *math::trigonometry_extra*)

### `secant`

```nbt
fn secant(x: Scalar) -> Scalar
```
(defined in *math::trigonometry_extra*)

### `arcsecant`

```nbt
fn arcsecant(x: Scalar) -> Scalar
```
(defined in *math::trigonometry_extra*)

### `cosecant`

```nbt
fn cosecant(x: Scalar) -> Scalar
```
(defined in *math::trigonometry_extra*)

### `csc`

```nbt
fn csc(x: Scalar) -> Scalar
```
(defined in *math::trigonometry_extra*)

### `acsc`

```nbt
fn acsc(x: Scalar) -> Scalar
```
(defined in *math::trigonometry_extra*)

### `sech`

```nbt
fn sech(x: Scalar) -> Scalar
```
(defined in *math::trigonometry_extra*)

### `asech`

```nbt
fn asech(x: Scalar) -> Scalar
```
(defined in *math::trigonometry_extra*)

### `csch`

```nbt
fn csch(x: Scalar) -> Scalar
```
(defined in *math::trigonometry_extra*)

### `acsch`

```nbt
fn acsch(x: Scalar) -> Scalar
```
(defined in *math::trigonometry_extra*)

### `random` (Standard uniform distribution sampling)
Uniformly samples the interval [0,1).

```nbt
fn random() -> Scalar
```
(defined in *core::random*)

### `rand_uniform` (Continuous uniform distribution sampling)
Uniformly samples the interval [a,b) if a<=b or [b,a) if b<a using inversion sampling.
More information [here](https://en.wikipedia.org/wiki/Continuous_uniform_distribution).

```nbt
fn rand_uniform<T: Dim>(a: T, b: T) -> T
```
(defined in *math::statistics*)

### `rand_int` (Discrete uniform distribution sampling)
Uniformly samples the integers in the interval [a, b].
More information [here](https://en.wikipedia.org/wiki/Discrete_uniform_distribution).

```nbt
fn rand_int(a: Scalar, b: Scalar) -> Scalar
```
(defined in *math::statistics*)

### `rand_bernoulli` (Bernoulli distribution sampling)
Samples a Bernoulli random variable, that is, 1 with probability p, 0 with probability 1-p.
              Parameter p must be a probability (0 <= p <= 1).
More information [here](https://en.wikipedia.org/wiki/Bernoulli_distribution).

```nbt
fn rand_bernoulli(p: Scalar) -> Scalar
```
(defined in *math::statistics*)

### `rand_binom` (Binomial distribution sampling)
Samples a binomial distribution by doing n Bernoulli trials with probability p.
              Parameter n must be a positive integer, parameter p must be a probability (0 <= p <= 1).
More information [here](https://en.wikipedia.org/wiki/Binomial_distribution).

```nbt
fn rand_binom(n: Scalar, p: Scalar) -> Scalar
```
(defined in *math::statistics*)

### `rand_norm` (Normal distribution sampling)
Samples a normal distribution with mean μ and standard deviation σ using the Box-Muller transform.
More information [here](https://en.wikipedia.org/wiki/Normal_distribution).

```nbt
fn rand_norm<T: Dim>(μ: T, σ: T) -> T
```
(defined in *math::statistics*)

### `rand_geom` (Geometric distribution sampling)
Samples a geometric distribution (the distribution of the number of Bernoulli trials with probability p needed to get one success) by inversion sampling.
              Parameter p must be a probability (0 <= p <= 1).
More information [here](https://en.wikipedia.org/wiki/Geometric_distribution).

```nbt
fn rand_geom(p: Scalar) -> Scalar
```
(defined in *math::statistics*)

### `rand_poisson` (Poisson distribution sampling)
Sampling a poisson distribution with rate λ, that is, the distribution of the number of events occurring in a fixed interval if these events occur with mean rate λ.
              The rate parameter λ must not be negative.
More information [here](https://en.wikipedia.org/wiki/Poisson_distribution).

```nbt
fn rand_poisson(λ: Scalar) -> Scalar
```
(defined in *math::statistics*)

### `rand_expon` (Exponential distribution sampling)
Sampling an exponential distribution (the distribution of the distance between events in a Poisson process with rate λ) using inversion sampling.
              The rate parameter λ must be positive.
More information [here](https://en.wikipedia.org/wiki/Exponential_distribution).

```nbt
fn rand_expon<T: Dim>(λ: T) -> 1 / T
```
(defined in *math::statistics*)

### `rand_lognorm` (Log-normal distribution sampling)
Sampling a log-normal distribution, that is, a distribution whose log is a normal distribution with mean μ and standard deviation σ.
More information [here](https://en.wikipedia.org/wiki/Log-normal_distribution).

```nbt
fn rand_lognorm(μ: Scalar, σ: Scalar) -> Scalar
```
(defined in *math::statistics*)

### `rand_pareto` (Pareto distribution sampling)
Sampling a Pareto distribution with minimum value min and shape parameter α using inversion sampling.
              Both parameters α and min must be positive.
More information [here](https://en.wikipedia.org/wiki/Pareto_distribution).

```nbt
fn rand_pareto<T: Dim>(α: Scalar, min: T) -> T
```
(defined in *math::statistics*)
