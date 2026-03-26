use std::ffi::CString;
use std::fs;
use pyo3::prelude::*;
use pyo3::types::IntoPyDict;

pub fn run() -> PyResult<()> {

    let code = fs::read_to_string("script.py")?;
    let code_c = CString::new(code)?;

    Python::attach(|py| {
        py.run(code_c.as_c_str(), None, None)?;
        Ok(())
    })
}