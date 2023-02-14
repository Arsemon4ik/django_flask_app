SCHEDULE = [
    {
        "id": 1,
        "schedule_name": "Django лабораторна 1",
        "is_passed": False
    },
    {
        "id": 2,
        "schedule_name": "Flask лабораторна 3",
        "is_passed": False
    },
    {
        "id": 3,
        "schedule_name": "Вища математика тест 2",
        "is_passed": False
    },

]

STATE = set()


def update(ids_list) -> None:
    """ Update function takes ids_list and toggle the value of is_passed
    Args:
        ids_list: [List of checked ids]
    Returns:
    """
    global STATE
    if ids_list:
        # check if values are removed from ids_list and remain in STATE
        for id_ in sorted(STATE, key=int):
            if id_ not in ids_list:
                for subject in SCHEDULE:
                    if subject["id"] == int(id_):
                        subject['is_passed'] = 0
                        STATE.remove(int(id_))
    else:
        reset()
        STATE = set()

    # add new values to STATE
    for id_ in ids_list:
        for subject in SCHEDULE:
            if subject["id"] == int(id_):
                subject['is_passed'] = 1
                STATE.add(int(id_))


def reset():
    """ reset function reset all the values of DB
     Args:
     Returns:
     """
    for subject in SCHEDULE:
        subject['is_passed'] = False
