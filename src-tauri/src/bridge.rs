use std::sync::{Arc, Mutex};
use tauri::State;
use crate::app_state::AppState;
use crate::archive::Archive;
use crate::category::Category;

#[cfg_attr(mobile, tauri::mobile_entry_point)]
pub fn build(app_state: AppState) {
    
    tauri::Builder::default()
        .manage(app_state.categories)
        .manage(app_state.archives)
        .plugin(tauri_plugin_opener::init())
        .invoke_handler(tauri::generate_handler![greet,get_shared_categories, get_shared_archives])
        .run(tauri::generate_context!())
        .expect("error while running tauri application");

    print!("Hello world")
}

#[tauri::command]
fn greet(name: &str) -> String {
    format!("Hello, {}! You've been greeted from Rust!", name)
}

#[tauri::command]
fn get_shared_categories(categories: State<'_, Arc<Mutex<Vec<Category>>>>) -> Vec<Category> {
    categories.lock().unwrap().clone()
}

#[tauri::command]
fn get_shared_archives(categories: State<'_, Arc<Mutex<Vec<Archive>>>>) -> Vec<Archive> {
    categories.lock().unwrap().clone()
}