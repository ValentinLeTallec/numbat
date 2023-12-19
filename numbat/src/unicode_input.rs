// We are following Julia here [1], but we only support
// a small (useful) subset of sequences for now.
// [1] https://docs.julialang.org/en/v1/manual/unicode-input/
pub const UNICODE_INPUT: &[(&[&str], &str)] = &[
    // Superscript symbols
    (&["^-"], "⁻"),
    (&["pm"], "±"),
    (&["^1"], "¹"),
    (&["^2"], "²"),
    (&["^3"], "³"),
    (&["^4"], "⁴"),
    (&["^5"], "⁵"),
    (&["^6"], "⁶"),
    (&["^7"], "⁷"),
    (&["^8"], "⁸"),
    (&["^9"], "⁹"),
    // Numbers
    (&["1/2"], "½"),
    // Operators
    (&["cdot"], "⋅"),
    (&["cdotp"], "·"),
    (&["times"], "×"),
    (&["div"], "÷"),
    (&["to", "rightarrow"], "→"),
    (&["ge"], "≥"),
    (&["le"], "≤"),
    (&["dots", "ldots"], "…"),
    // Greek alphabet
    (&["Gamma"], "Γ"),
    (&["Delta"], "Δ"),
    (&["Theta"], "Θ"),
    (&["Lambda"], "Λ"),
    (&["Pi"], "Π"),
    (&["Sigma"], "Σ"),
    (&["Phi"], "Φ"),
    (&["Psi"], "Ψ"),
    (&["Omega"], "Ω"),
    (&["alpha"], "α"),
    (&["beta"], "β"),
    (&["gamma"], "γ"),
    (&["delta"], "δ"),
    (&["epsilon"], "ε"),
    (&["varepsilon"], "ϵ"),
    (&["zeta"], "ζ"),
    (&["eta"], "η"),
    (&["theta"], "θ"),
    (&["vartheta"], "ϑ"),
    (&["iota"], "ι"),
    (&["kappa"], "κ"),
    (&["lambda"], "λ"),
    (&["mu"], "μ"),
    (&["nu"], "ν"),
    (&["xi"], "ξ"),
    (&["pi"], "π"),
    (&["rho"], "ρ"),
    (&["sigma"], "σ"),
    (&["tau"], "τ"),
    (&["upsilon"], "υ"),
    (&["phi"], "ϕ"),
    (&["varphi"], "φ"),
    (&["chi"], "χ"),
    (&["psi"], "ψ"),
    (&["omega"], "ω"),
    // Units
    (&["sterling"], "£"),
    (&["yen"], "¥"),
    (&["euro"], "€"),
    (&["degree"], "°"),
    (&["ohm"], "Ω"),
    (&["Angstrom"], "Å"),
    (&["percent"], "%"),
    (&["perthousand"], "‰"),
    (&["pertenthousand"], "‱"),
    // Constants
    (&["hbar"], "ℏ"),
    (&["planck"], "ℎ"),
];