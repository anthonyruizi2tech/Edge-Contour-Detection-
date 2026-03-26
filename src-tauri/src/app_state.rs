use std::sync::{Arc, Mutex};
use crate::archive::{get_example_archives, Archive};
use crate::category::{get_example_categories, Category};

#[derive(Default, Clone)]
pub struct AppState {
    pub categories: Arc<Mutex<Vec<Category>>>,
    pub archives: Arc<Mutex<Vec<Archive>>>,
    pub search_input: Arc<Mutex<String>>,
}

impl AppState {

    pub fn get() -> Self {

        Self {
            categories: Arc::new(Mutex::new(get_example_categories())),
            archives: Arc::new(Mutex::new(get_example_archives())),
            search_input: Arc::new(Mutex::new(String::default())),
        }
    }
}


