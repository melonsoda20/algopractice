def backspace_compare_brute_force(s: str, t: str) -> bool:
    s_value = ""

    for s_cur_val in s:
        if s_cur_val == "#":
            s_value = s_value[:-1]
        else:
            s_value += s_cur_val

    t_value = ""

    for t_cur_val in t:
        if t_cur_val == "#":
            t_value = t_value[:-1]
        else:
            t_value += t_cur_val

    return s_value == t_value


def backspace_compare_optimized(s: str, t: str) -> bool:
    s_pointer_index = len(s) - 1
    t_pointer_index = len(t) - 1

    while(s_pointer_index >= 0 or t_pointer_index >= 0):
        if (
            (s[s_pointer_index] == "#" and s_pointer_index >= 0) or
            (t[t_pointer_index] == "#" and t_pointer_index >= 0)
        ):
            if s[s_pointer_index] == "#":
                s_backtrack_count = 2
                while s_backtrack_count > 0 and s_pointer_index > -1:
                    s_pointer_index -= 1
                    s_backtrack_count -= 1
                    print(s[s_pointer_index])
                    if s[s_pointer_index] == "#":
                        s_backtrack_count += 2

            if t[t_pointer_index] == "#":
                t_backtrack_count = 2
                while t_backtrack_count > 0 and t_pointer_index > -1:
                    t_pointer_index -= 1
                    t_backtrack_count -= 1
                    if t[t_pointer_index] == "#":
                        t_backtrack_count += 2

            if s_pointer_index < 0 and t_pointer_index < 0:
                # both string are empty after 'deletions'
                return True
        else:
            if (
                (s_pointer_index < 0 and t_pointer_index >= 0) or
                (s_pointer_index >= 0 and t_pointer_index < 0)
            ):
                return False

            if s[s_pointer_index] != t[t_pointer_index]:
                return False

            s_pointer_index -= 1
            t_pointer_index -= 1

    return True


s = "ab##"
t = "c#d#"

print(backspace_compare_optimized(s, t))
