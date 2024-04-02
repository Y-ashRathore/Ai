def pour_water(jug1, jug2, target):
    while jug1 != target and jug2 != target:
        print(f'Jug 1: {jug1}L, Jug 2: {jug2}L')

        if jug1 == 0:
            jug1 = 4
        elif jug2 == 3:
            jug2 = 0
        else:
            amount_poured = min(jug1, 3 - jug2)
            jug1 -= amount_poured
            jug2 += amount_poured

    print(f'Jug 1: {jug1}L, Jug 2: {jug2}L')
    print('Done')


# Initial state: Both jugs are empty
jug1_capacity = 4
jug2_capacity = 3
target_amount = 2

jug1_current = 0
jug2_current = 0

print('Starting:')
pour_water(jug1_current, jug2_current, target_amount)
