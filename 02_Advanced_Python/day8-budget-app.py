def create_spend_chart(categories):

    total_spent = 0
    spent = []

    for category in categories:
        category_spent = 0

        for item in category.ledger:
            if item["amount"] < 0:
                category_spent += abs(item["amount"])

        spent.append(category_spent)
        total_spent += category_spent


    percentages = []

    for amount in spent:
        percentage = int((amount / total_spent) * 100)
        percentage = percentage - (percentage % 10)
        percentages.append(percentage)


    chart = "Percentage spent by category\n"


    # Create bars
    for i in range(100, -1, -10):

        chart += str(i).rjust(3) + "|"

        for percent in percentages:

            if percent >= i:
                chart += " o "
            else:
                chart += "   "

        chart += " \n"


    # Horizontal line
    chart += "    " + "-" * (len(categories) * 3 + 1)


    # Vertical category names
    max_length = max(len(category.name) for category in categories)

    for i in range(max_length):

        chart += "\n     "

        for category in categories:

            if i < len(category.name):
                chart += category.name[i] + "  "
            else:
                chart += "   "

    return chart