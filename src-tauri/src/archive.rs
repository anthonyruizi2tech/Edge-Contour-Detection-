use serde::Serialize;

#[derive(Default,Serialize,Clone, Debug)]
pub struct Archive {
    pub title: String,
    pub reference_image: String,
    pub timestamp: String,
}

pub fn get_default_archives() -> Vec<Archive> {

    vec![
        Archive { title: "Item A1".to_string(), reference_image: "".to_string(), timestamp: "Monday, 23-Mar-26 17:01:30 UTC".to_string(), },
        Archive { title: "Item B1".to_string(), reference_image: "".to_string(), timestamp: "Monday, 23-Mar-26 17:01:30 UTC".to_string(), },
        Archive { title: "Item C1".to_string(), reference_image: "".to_string(), timestamp: "Monday, 23-Mar-26 17:01:30 UTC".to_string(), },
        Archive { title: "Item D1".to_string(), reference_image: "".to_string(), timestamp: "Monday, 23-Mar-26 17:01:30 UTC".to_string(), },
        Archive { title: "Item E1".to_string(), reference_image: "".to_string(), timestamp: "Monday, 23-Mar-26 17:01:30 UTC".to_string(), },
        Archive { title: "Item F1".to_string(), reference_image: "".to_string(), timestamp: "Monday, 23-Mar-26 17:01:30 UTC".to_string(), },
        Archive { title: "Item G1".to_string(), reference_image: "".to_string(), timestamp: "Monday, 23-Mar-26 17:01:30 UTC".to_string(), },
        Archive { title: "Item H1".to_string(), reference_image: "".to_string(), timestamp: "Monday, 23-Mar-26 17:01:30 UTC".to_string(), },
        Archive { title: "Item I1".to_string(), reference_image: "".to_string(), timestamp: "Monday, 23-Mar-26 17:01:30 UTC".to_string(), },
        Archive { title: "Item J1".to_string(), reference_image: "".to_string(), timestamp: "Monday, 23-Mar-26 17:01:30 UTC".to_string(), },
        Archive { title: "Item K1".to_string(), reference_image: "".to_string(), timestamp: "Monday, 23-Mar-26 17:01:30 UTC".to_string(), },
        Archive { title: "Item L1".to_string(), reference_image: "".to_string(), timestamp: "Monday, 23-Mar-26 17:01:30 UTC".to_string(), },
        Archive { title: "Item M1".to_string(), reference_image: "".to_string(), timestamp: "Monday, 23-Mar-26 17:01:30 UTC".to_string(), },
        Archive { title: "Item N1".to_string(), reference_image: "".to_string(), timestamp: "Monday, 23-Mar-26 17:01:30 UTC".to_string(), },
        Archive { title: "Item O1".to_string(), reference_image: "".to_string(), timestamp: "Monday, 23-Mar-26 17:01:30 UTC".to_string(), },
        Archive { title: "Item P1".to_string(), reference_image: "".to_string(), timestamp: "Monday, 23-Mar-26 17:01:30 UTC".to_string(), },
        Archive { title: "Item Q1".to_string(), reference_image: "".to_string(), timestamp: "Monday, 23-Mar-26 17:01:30 UTC".to_string(), },
        Archive { title: "Item R1".to_string(), reference_image: "".to_string(), timestamp: "Monday, 23-Mar-26 17:01:30 UTC".to_string(), },
        Archive { title: "Item S1".to_string(), reference_image: "".to_string(), timestamp: "Monday, 23-Mar-26 17:01:30 UTC".to_string(), },
        Archive { title: "Item T1".to_string(), reference_image: "".to_string(), timestamp: "Monday, 23-Mar-26 17:01:30 UTC".to_string(), },
        Archive { title: "Item U1".to_string(), reference_image: "".to_string(), timestamp: "Monday, 23-Mar-26 17:01:30 UTC".to_string(), },
        Archive { title: "Item V1".to_string(), reference_image: "".to_string(), timestamp: "Monday, 23-Mar-26 17:01:30 UTC".to_string(), },
        Archive { title: "Item W1".to_string(), reference_image: "".to_string(), timestamp: "Monday, 23-Mar-26 17:01:30 UTC".to_string(), },
        Archive { title: "Item X1".to_string(), reference_image: "".to_string(), timestamp: "Monday, 23-Mar-26 17:01:30 UTC".to_string(), },
        Archive { title: "Item Y1".to_string(), reference_image: "".to_string(), timestamp: "Monday, 23-Mar-26 17:01:30 UTC".to_string(), },
        Archive { title: "Item Z1".to_string(), reference_image: "".to_string(), timestamp: "Monday, 23-Mar-26 17:01:30 UTC".to_string(), },
    ]
}