use std::sync::RwLock;

#[derive(Clone, Debug)]
pub struct Player {
    pub name: String,
    pub age: u8,
}

#[derive(Debug)]
pub struct PlayerRegistry {
    registry: RwLock<Vec<Player>>,
}

impl PlayerRegistry {
    fn new() -> PlayerRegistry {
        PlayerRegistry {
            registry: RwLock::new(Vec::new()),
        }
    }

    fn add(&self, player: Player) {
        self.registry.write().unwrap().push(player);
    }

    fn players(&self) -> Vec<Player> {
        self.registry.read().unwrap().clone()
    }
}

uniffi::include_scaffolding!("custom");
