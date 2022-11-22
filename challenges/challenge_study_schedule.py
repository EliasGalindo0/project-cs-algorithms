def study_schedule(permanence_period, target_time):
    if target_time is None or not isinstance(target_time, int):
        return None

    counter = 0
    for permanence in permanence_period:
        entry_time, exit_time = permanence
        if not isinstance(entry_time, int) or not isinstance(exit_time, int):
            return None
        if entry_time <= target_time <= exit_time:
            counter += 1
    return counter
