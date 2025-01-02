backfill_prompt, translation_methods, comfyd_active_checkbox, preselector = [None] * 4

def set_all_enhanced_parameters(*args):
    global backfill_prompt, translation_methods, comfyd_active_checkbox, preselector

    backfill_prompt, translation_methods, comfyd_active_checkbox, preselector = args

    return
