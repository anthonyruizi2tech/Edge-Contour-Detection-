use std::sync::{Arc, Mutex};
use crate::archive::{get_default_archives, Archive};
use crate::category::{get_default_categories, Category};

#[derive(Default, Clone)]
pub struct AppState {
    pub categories: Arc<Mutex<Vec<Category>>>,
    pub archives: Arc<Mutex<Vec<Archive>>>,
}

impl AppState {

    pub fn get() -> Self {

        Self {
            categories: Arc::new(Mutex::new(get_default_categories())),
            archives: Arc::new(Mutex::new(get_default_archives())),
        }
    }
}


