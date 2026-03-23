use serde::Serialize;

#[derive(Default,Serialize,Clone, Debug)]
pub struct Category {
    pub title: String,
    pub reference_image: String,
    pub threshold: i64,
}

pub fn get_default_categories() -> Vec<Category> {

    vec![
        Category { title: "Item A".to_string(), reference_image: "".to_string(), threshold: 0, },
        Category { title: "Item B".to_string(), reference_image: "".to_string(), threshold: 0, },
        Category { title: "Item C".to_string(), reference_image: "".to_string(), threshold: 0, },
        Category { title: "Item D".to_string(), reference_image: "".to_string(), threshold: 0, },
        Category { title: "Item E".to_string(), reference_image: "".to_string(), threshold: 0, },
        Category { title: "Item F".to_string(), reference_image: "".to_string(), threshold: 0, },
        Category { title: "Item G".to_string(), reference_image: "".to_string(), threshold: 0, },
        Category { title: "Item H".to_string(), reference_image: "".to_string(), threshold: 0, },
        Category { title: "Item I".to_string(), reference_image: "".to_string(), threshold: 0, },
        Category { title: "Item J".to_string(), reference_image: "".to_string(), threshold: 0, },
        Category { title: "Item K".to_string(), reference_image: "".to_string(), threshold: 0, },
        Category { title: "Item L".to_string(), reference_image: "".to_string(), threshold: 0, },
        Category { title: "Item M".to_string(), reference_image: "".to_string(), threshold: 0, },
        Category { title: "Item N".to_string(), reference_image: "".to_string(), threshold: 0, },
        Category { title: "Item O".to_string(), reference_image: "".to_string(), threshold: 0, },
        Category { title: "Item P".to_string(), reference_image: "".to_string(), threshold: 0, },
        Category { title: "Item Q".to_string(), reference_image: "".to_string(), threshold: 0, },
        Category { title: "Item R".to_string(), reference_image: "".to_string(), threshold: 0, },
        Category { title: "Item S".to_string(), reference_image: "".to_string(), threshold: 0, },
        Category { title: "Item T".to_string(), reference_image: "".to_string(), threshold: 0, },
        Category { title: "Item U".to_string(), reference_image: "".to_string(), threshold: 0, },
        Category { title: "Item V".to_string(), reference_image: "".to_string(), threshold: 0, },
        Category { title: "Item W".to_string(), reference_image: "".to_string(), threshold: 0, },
        Category { title: "Item X".to_string(), reference_image: "".to_string(), threshold: 0, },
        Category { title: "Item Y".to_string(), reference_image: "".to_string(), threshold: 0, },
        Category { title: "Item Z".to_string(), reference_image: "".to_string(), threshold: 0, },
    ]
}