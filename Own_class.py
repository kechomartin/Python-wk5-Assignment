# Base superhero class
class Superhero:
    universe = "Digital Realm-808"  # Shared by all heroes

    def __init__(self, name, secret_id, power, base):
        # Unique attributes for each hero
        self.name = name
        self.secret_id = secret_id
        self.power = power
        self.base = base
        self.energy = 100  # Starting energy

    def use_power(self):
        # Using power costs energy
        if self.energy >= 10:
            self.energy -= 10
            return f"{self.name} uses {self.power}! Energy: {self.energy}"
        return f"{self.name} is too tired! Energy: {self.energy}"

    def rest(self):
        # Reset energy to full
        self.energy = 100
        return f"{self.name} rested! Energy: {self.energy}"

    def introduce(self):
        # Basic introduction
        return f"I'm {self.name} ({self.secret_id}). Power: {self.power}. Base: {self.base}"

# Create our main hero
kech0 = Superhero("Kech0", "Kai Thompson", "cyber-manipulation", "Neo-Tokyo Server")
print(kech0.introduce())
print(kech0.use_power())
print(kech0.rest())
print("---")

# Specialized hero that inherits from Superhero
class CyberHero(Superhero):
    def __init__(self, name, secret_id, power, base, cyberware):
        # Get everything from parent class
        super().__init__(name, secret_id, power, base)
        # Add new stuff only CyberHero has
        self.cyberware = cyberware
        self._firewall = 100  # "Private" attribute

    # Override parent method - different behavior
    def use_power(self):
        if self._firewall >= 20:
            self._firewall -= 20
            return f"{self.name} uses {self.cyberware}! Firewall: {self._firewall}%"
        return f"{self.name} system critical! Firewall: {self._firewall}%"

    # New method only CyberHero has
    def reboot(self):
        self._firewall = 100
        return f"{self.cyberware} rebooted! Firewall: 100%"

# Create cyber hero
ne0n = CyberHero("Ne0n", "Alex Chen", "neural hacking", "Shanghai Nexus", "Quantum Interface")
print(ne0n.introduce())  # Uses parent method
print(ne0n.use_power())  # Uses overridden method
print(ne0n.reboot())     # Uses new method
print("---")

# Show polymorphism - same method name, different behavior
heroes = [kech0, ne0n]
for hero in heroes:
    print(hero.use_power())  # Each hero uses power differently