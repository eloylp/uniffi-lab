type Result<T, E = ArithmeticError> = std::result::Result<T, E>;

#[derive(Debug, thiserror::Error)]
pub enum ArithmeticError {
    #[error("Integer overflow for {a} and {b}")]
    IntegerOverflow { a: u32, b: u32 },
}

pub fn add(a: u32, b: u32) -> Result<u32, ArithmeticError> {
    a.checked_add(b)
        .ok_or(ArithmeticError::IntegerOverflow { a: a, b: b })
}

uniffi::include_scaffolding!("basic");
