classes = ["Barbarian","Bard","Cleric","Druid","Fighter","Monk","Paladin","Ranger","Rogue","Sorcerer","Warlock","Wizard"] #Base Classes 

class_features_table = {
    "Barbarian" : {
        1:  {"Proficiency": 2, "Features": ["Rage", "Unarmored Defense", "Weapon Mastery"], "Rages": 2, "Rage Damage": 2, "Weapon Mastery": 2},
        2:  {"Proficiency": 2, "Features": ["Danger Sense", "Reckless Attack"], "Rages": 2, "Rage Damage": 2, "Weapon Mastery": 2},
        3:  {"Proficiency": 2, "Features": ["Barbarian Subclass", "Primal Knowledge"], "Rages": 3, "Rage Damage": 2, "Weapon Mastery": 2},
        4:  {"Proficiency": 2, "Features": ["Ability Score Improvement"], "Rages": 3, "Rage Damage": 2, "Weapon Mastery": 3},
        5:  {"Proficiency": 3, "Features": ["Extra Attack", "Fast Movement"], "Rages": 3, "Rage Damage": 2, "Weapon Mastery": 3},
        6:  {"Proficiency": 3, "Features": ["Subclass Feature"], "Rages": 4, "Rage Damage": 2, "Weapon Mastery": 3},
        7:  {"Proficiency": 3, "Features": ["Feral Instinct", "Instinctive Pounce"], "Rages": 4, "Rage Damage": 2, "Weapon Mastery": 3},
        8:  {"Proficiency": 3, "Features": ["Ability Score Improvement"], "Rages": 4, "Rage Damage": 2, "Weapon Mastery": 3},
        9:  {"Proficiency": 4, "Features": ["Brutal Strike"], "Rages": 4, "Rage Damage": 3, "Weapon Mastery": 3},
        10: {"Proficiency": 4, "Features": ["Subclass Feature"], "Rages": 4, "Rage Damage": 3, "Weapon Mastery": 3},
        11: {"Proficiency": 4, "Features": ["Relentless Rage"], "Rages": 4, "Rage Damage": 3, "Weapon Mastery": 4},
        12: {"Proficiency": 4, "Features": ["Ability Score Improvement"], "Rages": 5, "Rage Damage": 3, "Weapon Mastery": 4},
        13: {"Proficiency": 5, "Features": ["Improved Brutal Strike"], "Rages": 5, "Rage Damage": 3, "Weapon Mastery": 4},
        14: {"Proficiency": 5, "Features": ["Subclass Feature"], "Rages": 5, "Rage Damage": 3, "Weapon Mastery": 4},
        15: {"Proficiency": 5, "Features": ["Persistent Rage"], "Rages": 5, "Rage Damage": 3, "Weapon Mastery": 4},
        16: {"Proficiency": 5, "Features": ["Ability Score Improvement"], "Rages": 5, "Rage Damage": 4, "Weapon Mastery": 4},
        17: {"Proficiency": 6, "Features": ["Improved Brutal Strike"], "Rages": 6, "Rage Damage": 4, "Weapon Mastery": 4},
        18: {"Proficiency": 6, "Features": ["Indomitable Might"], "Rages": 6, "Rage Damage": 4, "Weapon Mastery": 4},
        19: {"Proficiency": 6, "Features": ["Epic Boon"], "Rages": 6, "Rage Damage": 4, "Weapon Mastery": 4},
        20: {"Proficiency": 6, "Features": ["Primal Champion"], "Rages": 6, "Rage Damage": 4, "Weapon Mastery": 4},

    }
}

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
        "Class Features" : class_features_table["Barbarian"],
        "Subclasses" : {"Path of Berserker":"",
                        "Path of Wild Heart":"",
                        "Path of the World Tree":"",
                        "Path of Zealot":""}
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

