use std::sync::{Arc, Mutex};
use tauri::State;
use crate::app_state::AppState;
use crate::archive::{get_database_archives, Archive};
use crate::category::{get_database_categories, Category};
use crate::pyo3_bridge;

#[cfg_attr(mobile, tauri::mobile_entry_point)]
pub fn build(app_state: AppState) {
    
    tauri::Builder::default()
        .manage(app_state.categories)
        .manage(app_state.archives)
        .manage(app_state.search_input)
        .plugin(tauri_plugin_opener::init())
        .invoke_handler(tauri::generate_handler![
            greet,
            get_shared_categories,
            get_shared_archives,
            update_search_filter
        ])
        .run(tauri::generate_context!())
        .expect("error while running tauri application");

    print!("Hello world")
}

#[tauri::command]
fn greet(name: &str) -> String {
    format!("Hello, {}! You've been greeted from Rust!", name)
}

#[tauri::command]
fn get_shared_categories(
    search_input: State<'_, Arc<Mutex<String>>>
) -> Vec<Category> {

    get_database_categories(search_input.lock().unwrap().clone())
}

#[tauri::command]
fn get_shared_archives(
    search_input: State<'_, Arc<Mutex<String>>>
) -> Vec<Archive> {

    let i = pyo3_bridge::run();

    get_database_archives(search_input.lock().unwrap().clone())
}

#[tauri::command]
fn update_search_filter(
    search_input: State<'_, Arc<Mutex<String>>>,
    input: String
) {
    *search_input.lock().unwrap() = input;
}