mod tauri_bridge;
mod category;
mod model;
mod app_state;
mod archive;
mod pyo3_bridge;

use crate::app_state::AppState;

pub fn run() {

    let app_state = AppState::get();

    model::run(app_state.clone());

    tauri_bridge::build(app_state);
}

