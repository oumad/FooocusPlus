backfill_prompt, translation_methods, comfyd_active_checkbox = [None] * 3

def set_all_enhanced_parameters(*args):
    global backfill_prompt, translation_methods, comfyd_active_checkbox, preselector
    if preselector == '':
        if lang=='cn':
            preselector='Topbar Menu'
        else:    
            preselector='Dropdown Menu'

    backfill_prompt, translation_methods, comfyd_active_checkbox, preselector = args

    return

def set_preselector():
    global preselector
    if preselector == '':
        if lang=='cn':
            preselector='Topbar Menu'
        else:    
            preselector='Dropdown Menu'
    return
