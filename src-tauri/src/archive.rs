use serde::Serialize;

#[derive(Default,Serialize,Clone, Debug)]
pub struct Archive {
    pub title: String,
    pub reference_image: String,
    pub timestamp: String,
    pub category: String,
}


pub fn get_database_archives(filter: String) -> Vec<Archive> {

    // EXAMPLE FUNCTION PRIOR TO DATA BASE
    let categories = get_example_archives();

    let mut filtered_archives: Vec<Archive> = Vec::new();

    for c in categories {
        if c.title.to_ascii_lowercase().contains(&filter.to_ascii_lowercase()) {
            filtered_archives.push(c);
        }
        else if c.category.to_ascii_lowercase().contains(&filter.to_ascii_lowercase()) {
            filtered_archives.push(c);
        }
    }

    filtered_archives
}

pub fn get_database_archives_from_category(filter: String) -> Vec<Archive> {

    // EXAMPLE FUNCTION PRIOR TO DATA BASE
    let categories = get_example_archives();

    let mut filtered_archives: Vec<Archive> = Vec::new();

    for c in categories {
        if c.category.to_ascii_lowercase().contains(&filter.to_ascii_lowercase()) {
            filtered_archives.push(c);
        }
    }

    filtered_archives
}

pub fn get_example_archives() -> Vec<Archive> {

    vec![
        Archive { title: "Item A1".to_string(), reference_image: "".to_string(), timestamp: "Mon, 23-Mar-26 17:01:30 UTC".to_string(), category: "Item A".to_string()},
        Archive { title: "Item B1".to_string(), reference_image: "".to_string(), timestamp: "Mon, 23-Mar-26 17:01:30 UTC".to_string(), category: "Item A".to_string()},
        Archive { title: "Item C1".to_string(), reference_image: "".to_string(), timestamp: "Mon, 23-Mar-26 17:01:30 UTC".to_string(), category: "Item A".to_string()},
        Archive { title: "Item D1".to_string(), reference_image: "".to_string(), timestamp: "Mon, 23-Mar-26 17:01:30 UTC".to_string(), category: "Item A".to_string()},
        Archive { title: "Item E1".to_string(), reference_image: "".to_string(), timestamp: "Mon, 23-Mar-26 17:01:30 UTC".to_string(), category: "Item A".to_string()},
        Archive { title: "Item F1".to_string(), reference_image: "".to_string(), timestamp: "Mon, 23-Mar-26 17:01:30 UTC".to_string(), category: "Item A".to_string()},
        Archive { title: "Item G1".to_string(), reference_image: "".to_string(), timestamp: "Mon, 23-Mar-26 17:01:30 UTC".to_string(), category: "Item A".to_string()},
        Archive { title: "Item H1".to_string(), reference_image: "".to_string(), timestamp: "Mon, 23-Mar-26 17:01:30 UTC".to_string(), category: "Item A".to_string()},
        Archive { title: "Item I1".to_string(), reference_image: "".to_string(), timestamp: "Mon, 23-Mar-26 17:01:30 UTC".to_string(), category: "Item A".to_string()},
        Archive { title: "Item J1".to_string(), reference_image: "".to_string(), timestamp: "Mon, 23-Mar-26 17:01:30 UTC".to_string(), category: "Item A".to_string()},
        Archive { title: "Item K1".to_string(), reference_image: "".to_string(), timestamp: "Mon, 23-Mar-26 17:01:30 UTC".to_string(), category: "Item A".to_string()},
        Archive { title: "Item L1".to_string(), reference_image: "".to_string(), timestamp: "Mon, 23-Mar-26 17:01:30 UTC".to_string(), category: "Item A".to_string()},
        Archive { title: "Item M1".to_string(), reference_image: "".to_string(), timestamp: "Mon, 23-Mar-26 17:01:30 UTC".to_string(), category: "Item A".to_string()},
        Archive { title: "Item N1".to_string(), reference_image: "".to_string(), timestamp: "Mon, 23-Mar-26 17:01:30 UTC".to_string(), category: "Item A".to_string()},
        Archive { title: "Item O1".to_string(), reference_image: "".to_string(), timestamp: "Mon, 23-Mar-26 17:01:30 UTC".to_string(), category: "Item A".to_string()},
        Archive { title: "Item P1".to_string(), reference_image: "".to_string(), timestamp: "Mon, 23-Mar-26 17:01:30 UTC".to_string(), category: "Item A".to_string()},
        Archive { title: "Item Q1".to_string(), reference_image: "".to_string(), timestamp: "Mon, 23-Mar-26 17:01:30 UTC".to_string(), category: "Item A".to_string()},
        Archive { title: "Item R1".to_string(), reference_image: "".to_string(), timestamp: "Mon, 23-Mar-26 17:01:30 UTC".to_string(), category: "Item A".to_string()},
        Archive { title: "Item S1".to_string(), reference_image: "".to_string(), timestamp: "Mon, 23-Mar-26 17:01:30 UTC".to_string(), category: "Item A".to_string()},
        Archive { title: "Item T1".to_string(), reference_image: "".to_string(), timestamp: "Mon, 23-Mar-26 17:01:30 UTC".to_string(), category: "Item A".to_string()},
        Archive { title: "Item U1".to_string(), reference_image: "".to_string(), timestamp: "Mon, 23-Mar-26 17:01:30 UTC".to_string(), category: "Item A".to_string()},
        Archive { title: "Item V1".to_string(), reference_image: "".to_string(), timestamp: "Mon, 23-Mar-26 17:01:30 UTC".to_string(), category: "Item A".to_string()},
        Archive { title: "Item W1".to_string(), reference_image: "".to_string(), timestamp: "Mon, 23-Mar-26 17:01:30 UTC".to_string(), category: "Item A".to_string()},
        Archive { title: "Item X1".to_string(), reference_image: "".to_string(), timestamp: "Mon, 23-Mar-26 17:01:30 UTC".to_string(), category: "Item A".to_string()},
        Archive { title: "Item Y1".to_string(), reference_image: "".to_string(), timestamp: "Mon, 23-Mar-26 17:01:30 UTC".to_string(), category: "Item A".to_string()},
        Archive { title: "Item Z1".to_string(), reference_image: "".to_string(), timestamp: "Mon, 23-Mar-26 17:01:30 UTC".to_string(), category: "Item A".to_string()},
    ]
}