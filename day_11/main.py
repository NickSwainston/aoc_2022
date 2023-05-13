from pprint import pprint

if __name__ == "__main__":
    monkey_i = 0
    monkeys = {}
    with open('input.txt') as data_file:
        for line in data_file:
            line = line.strip()
            if line.startswith("Monkey"):
                monkey_i = line.split("Monkey ")[1].split(":")[0]
                monkeys[monkey_i] = { "passes": 0 }
            elif line.startswith("Starting items: "):
                items = line.split("Starting items: ")[1].split(", ")
                items = [ int(i) for i in items ]
                monkeys[monkey_i]["items"] = items
            elif line.startswith("Operation: new = old"):
                operation, value = line.split("Operation: new = old ")[1].split(" ")
                monkeys[monkey_i]["operation"] = operation
                monkeys[monkey_i]["value"] = value
            elif line.startswith("Test: divisible by"):
                value = int(line.split("Test: divisible by ")[1])
                monkeys[monkey_i]["divisible"] = value
            elif line.startswith("If true: throw to monkey"):
                value = line.split("If true: throw to monkey ")[1]
                monkeys[monkey_i]["true"] = value
            elif line.startswith("If false: throw to monkey"):
                value = line.split("If false: throw to monkey ")[1]
                monkeys[monkey_i]["false"] = value

    pprint(monkeys)

    # Part 1
    # for round_i in range(20):
    #     for monkey_i in monkeys.keys():
    #         monkey = monkeys[monkey_i]
    #         for item in list(monkey["items"]):
    #             if monkey["value"] == "old":
    #                 worry = (item * item) // 3
    #             elif monkey["operation"] == "*":
    #                 worry = (item * int(monkey["value"])) // 3
    #             else:
    #                 worry = (item + int(monkey["value"])) // 3
    #             monkey["passes"] += 1

    #             if worry % monkey["divisible"] == 0:
    #                 throw_to = monkey["true"]
    #             else:
    #                 throw_to = monkey["false"]

    #             # do the throw
    #             print(f"Throw {worry} to {throw_to}")
    #             monkeys[monkey_i]["items"].remove(item)
    #             monkeys[throw_to]["items"].append(worry)

    # pprint(monkeys)

    # monkey_business = []
    # for monkey_i in monkeys.keys():
    #     monkey_business.append(monkeys[monkey_i]["passes"])
    # monkey_business.sort()
    # print(monkey_business)
    # print(f"Part 1: {monkey_business[-1] * monkey_business[-2]}")

    # Part 2
    divisable_prime = 1
    for monkey_i in monkeys.keys():
        divisable_prime *= monkeys[monkey_i]["divisible"]
    print(f"divisable prime: {divisable_prime}")
    for round_i in range(1, 10001):
        for monkey_i in monkeys.keys():
            monkey = monkeys[monkey_i]
            for item in list(monkey["items"]):
                if monkey["value"] == "old":
                    worry = (item * item)
                elif monkey["operation"] == "*":
                    worry = (item * int(monkey["value"]))
                else:
                    worry = (item + int(monkey["value"]))
                worry = worry % divisable_prime
                monkey["passes"] += 1

                if worry % monkey["divisible"] == 0:
                    throw_to = monkey["true"]
                else:
                    throw_to = monkey["false"]

                # do the throw
                monkeys[monkey_i]["items"].remove(item)
                monkeys[throw_to]["items"].append(worry)
        if round_i in ( 1, 20 ) or round_i % 1000 == 0:
            print(f"\n== After round {round_i} ==")
            for monkey_i in monkeys.keys():
                print(f"Monkey {monkey_i} inspected items {monkeys[monkey_i]['passes']} times.")

    pprint(monkeys)

    monkey_business = []
    for monkey_i in monkeys.keys():
        monkey_business.append(monkeys[monkey_i]["passes"])
    monkey_business.sort()
    print(monkey_business)
    print(f"Part 2: {monkey_business[-1] * monkey_business[-2]}")

