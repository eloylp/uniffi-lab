use std::sync::{Arc, RwLock};

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
    pub fn new() -> PlayerRegistry {
        PlayerRegistry {
            registry: RwLock::new(Vec::new()),
        }
    }

    pub fn add(&self, player: Player) {
        self.registry.write().unwrap().push(player);
    }

    pub fn players(&self) -> Vec<Player> {
        self.registry.read().unwrap().clone()
    }

    pub fn first(&self) -> Option<Player> {
        if let Some(player) = self.registry.read().unwrap().first() {
            return Some(player.clone());
        }
        None
    }

    pub fn merge(&self, registry: &PlayerRegistry) {
        let mut reg = self.registry.write().unwrap();
        registry.players().iter().for_each(|player| {
            reg.push(player.clone());
        });
    }
}

pub struct Race {
    player_registry: Arc<PlayerRegistry>,
}

impl Race {
    pub fn new(player_registry: Arc<PlayerRegistry>) -> Race {
        Race { player_registry }
    }

    pub fn player_registry(&self) -> Arc<PlayerRegistry> {
        Arc::clone(&self.player_registry)
    }
}

pub fn winners(registry_a: &PlayerRegistry, registry_b: &PlayerRegistry) -> Vec<Player> {
    let mut winners = Vec::new();

    if let Some(player) = registry_a.first() {
        winners.push(player)
    }
    if let Some(player) = registry_b.first() {
        winners.push(player)
    }
    winners
}

uniffi::include_scaffolding!("custom");
