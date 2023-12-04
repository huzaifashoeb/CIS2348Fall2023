# Name: Huzaifa Shoeb, ID: 1925670

num_calls = 0


def partition(ids_user, i, k):
    global num_calls
    midpoint = i + (k - i) // 2
    pivot = ids_user[midpoint]
    done = False
    l_id = i
    h = k
    while not done:
        while ids_user[l_id] < pivot:
            l_id = l_id + 1
        while pivot < ids_user[h]:
            h = h - 1
        if l_id >= h:
            done = True
        else:
            ids_user[l_id], ids_user[h] = ids_user[h], ids_user[l_id]
            l_id = l_id + 1
            h = h - 1
    return h


def quicksort(ids_user, i, k):
    global num_calls
    num_calls += 1
    j_id = 0
    if i < k:
        j_id = partition(ids_user, i, k)
        quicksort(ids_user, i, j_id)
        quicksort(ids_user, j_id + 1, k)


if __name__ == "__main__":
    user_ids = []
    user_id = input()
    while user_id != "-1":
        user_ids.append(user_id)
        user_id = input()

    quicksort(user_ids, 0, len(user_ids) - 1)

    print(num_calls)

    for user_id in user_ids:
        print(user_id)
