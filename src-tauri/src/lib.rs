mod bridge;
mod category;
mod model;
mod app_state;
mod archive;

use crate::app_state::AppState;

pub fn run() {

    let app_state = AppState::get();

    model::run(app_state.clone());

    bridge::build(app_state);
}

