def create_character(character_name, strength, intelligence, charisma):
    # 1. CHARACTER NAME VALIDATION
    if type(character_name) is not str:
        return 'The character name should be a string'
    
    elif character_name == '':
        return 'The character should have a name'
        
    elif len(character_name) > 10:
        return 'The character name is too long'
        
    elif ' ' in character_name:
        return 'The character name should not contain spaces'
        
    # 2. STATS VALIDATION
    stats = (strength, intelligence, charisma)
    
    # Check if they are pure integers (blocks booleans and strings)
    if not all(type(s) is int for s in stats):
        return 'All stats should be integers'
        
    elif strength < 1 or intelligence < 1 or charisma < 1:
        return 'All stats should be no less than 1'
        
    elif strength > 4 or intelligence > 4 or charisma > 4:
        return 'All stats should be no more than 4'
        
    elif sum(stats) != 7:
        return 'The character should start with 7 points'
        
    # 3. VISUAL GENERATION (Passed perfectly!)
    else:
        full_dot = '●'
        empty_dot = '○'
        
        str_dots = (full_dot * strength) + (empty_dot * (10 - strength))
        int_dots = (full_dot * intelligence) + (empty_dot * (10 - intelligence))
        cha_dots = (full_dot * charisma) + (empty_dot * (10 - charisma))
        
        return f"{character_name}\nSTR {str_dots}\nINT {int_dots}\nCHA {cha_dots}"
