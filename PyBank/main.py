import csv

# Creating variables to store values
total_months = 0
net_total = 0
previous_profit_loss = 0
changes = []
greatest_increase = {"date": "", "amount": 0}
greatest_decrease = {"date": "", "amount": 0}

# Reading CSV data
with open(
"Resources/budget_data.csv", newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)  # Skip header row

    for row in csvreader:
        date = row[0]
        profit_loss = int(row[1])

        # Total number of months & net total
        total_months += 1
        net_total += profit_loss

        # Changes in profit/loss
        if total_months > 1:
            change = profit_loss - previous_profit_loss
            changes.append(change)

            # Check for greatest increase/decrease
            if change > greatest_increase["amount"]:
                greatest_increase["date"] = date
                greatest_increase["amount"] = change
            if change < greatest_decrease["amount"]:
                greatest_decrease["date"] = date
                greatest_decrease["amount"] = change

        # Update the previous profit/loss for the next loop
        previous_profit_loss = profit_loss

# Calculate avg change in profit/loss.
average_change = round(sum(changes) / len(changes), 2)

# Printing results
print("Financial Analysis")
print("-" * 28)
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: {greatest_increase['date']} (${greatest_increase['amount']})")
print(f"Greatest Decrease in Profits: {greatest_decrease['date']} (${greatest_decrease['amount']})")

# Text file
with open("financial_analysis.txt", "w") as textfile:
    textfile.write("Financial Analysis\n")
    textfile.write("-" * 28 + "\n")
    textfile.write(f"Total Months: {total_months}\n")
    textfile.write(f"Total: ${net_total}\n")
    textfile.write(f"Average Change: ${average_change}\n")
    textfile.write(f"Greatest Increase in Profits: {greatest_increase['date']} (${greatest_increase['amount']})\n")
    textfile.write(f"Greatest Decrease in Profits: {greatest_decrease['date']} (${greatest_decrease['amount']})\n")
