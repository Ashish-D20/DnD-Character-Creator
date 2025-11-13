import streamlit as st  

classes = ["Barbarian","Bard","Cleric","Druid","Fighter","Monk","Paladin","Ranger","Rogue","Sorcerer","Warlock","Wizard"] #Base Classes 

species = ["Aasimar","Dragonborn","Dwarf","Elf","Gnome","Goliath","Halfling","Human","Orc","Tiefling"] # Base Species 

subclass = {"Barbarian":["Path of Berserker","Path of Wild Heart","Path of World Tree","Path of Zealot"],
            "Bard":["College of Dance","College of Glamour","Collge of Lore","Collge of Valour"],
            "Cleric":["Life Domain","Light Domain","Trickery Domain","War Domain"],
            "Druid":["Circle of the Land","Circle of the Moon","Circle of the Sea","Circle of the Stars"],
            "Fighter":["Battle Master","Champion","Eldritch Knight","Psi Warrior"],
            "Monk":["Warrior of Mercy","Warrior of Shadow","Warrior of Mercy","Warrior of The Elements","Warrior of The Open Hand"],
            "Paladin":["Oath of Devotion","Oath of Glory","Oath of The Ancients","Oath of Vengeance"],
            "Ranger":["Beast Master","Fey Wanderer","Gloom Stalker","Hunter"],
            "Rogue":["Arcane Trickster","Assasin","Soulknife","Thief"],
            "Sorcerer":["Aberrant Sorcery","Clockwork Sorcery","Draconic Sorcery","Wild Magic"],
            "Warlock":["The Archfey","The Celestial","The Fiend","The Great Old One"],
            "Wizard":["Abjurer","Diviner","Evoker","Illusionist"]
            } # Subclasses Dictionary

background = ["Acolyte","Artisan","Charlatan","Criminal","Criminal",
              "Entertainer","Farmer","Guard","Guide","Hermit","Merchant",
              "Noble","Sage","Sailor","Scribe","Soldier","Wayfarer"] # Base Backgrounds 
