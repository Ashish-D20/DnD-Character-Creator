classes = ["Barbarian","Bard","Cleric","Druid","Fighter","Monk","Paladin","Ranger","Rogue","Sorcerer","Warlock","Wizard"] #Base Classes 
class_traits = {
    "Barbarian":{
        "Description" : "Barbarians are powered by primal forces of the multiverse that manifest as a Rage. More than a mere emotion and not limited to anger, this Rage is an incarnation of a predator's ferocity, a storm's fury, and a sea's turmoil.",
        "Primary Ability" : "Strength",
        "Hitpoint Die" : "D12",
        "Saving Throw Proficiencies" : ["Strength","Constitution"],
        "Skill Proficiencies" : ["Animal Handling", "Athletics", "Intimidation", "Nature", "Perception", "Survival"],
        "Weapon Proficiencies" : ["Simple", "Martial"],
        "Armor Training" : ["Light", "Medium", "Shields"],
        "Tool Proficiencies" : "None",
        "Starting Equipment" : [["Greataxe","Handaxe","Handaxe","Handaxe","Handaxe","Explorer's Pack", "GP 15"],["GP 75"]],
        "Class Features" : {}
    },

    "Bard":{
        "Primary Ability" : "Charisma",
        "Hitpoint Die" : "D8",
        "Saving Throw Proficiencies" : ["Strength","Constitution"],
        "Skill Proficiencies" : ["Animal Handling", "Athletics", "Intimidation", "Nature", "Perception", "Survival"],
        "Weapon Proficiencies" : ["Simple", "Martial"],
        "Armor Training" : ["Light", "Medium", "Shields"],
        "Starting Equipment" : [["Greataxe","Handaxe","Handaxe","Handaxe","Handaxe","Explorer's Pack", "GP 15"],["GP 75"]]
    }

}