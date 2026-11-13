EXPERIMENT 2: PROGRESSIVE ELECTRICITY BILLING
. Problem Statement
Write a Python program to calculate electricity bills using different consumption slabs, fixed charges, surcharges, and rebates. Compare monthly electricity bills and identify unusual increases.

Assumed billing rates:
- First 100 units: ₹2 per unit.
- Next 100 units: ₹3 per unit.
- Above 200 units: ₹5 per unit.
- Fixed charge: ₹50.
- Surcharge: 5%.
- Rebate: ₹20 for consumption below 50 units.
- Unusual increase: More than 20%.
2. Algorithm
1. Start.
2. Read the number of months.
3. Initialize an empty list for storing bills.
4. For each month:
   - Read electricity units.
   - Calculate charges using consumption slabs.
   - Add fixed charges.
   - Calculate and add surcharge.
   - Apply rebate if consumption is below 50 units.
   - Store the final bill.
5. Display all monthly bills.
6. Compare consecutive monthly bills.
7. If the increase is greater than 20%, display an unusual increase warning.
8. Stop.
3. Flowchart (Mermaid)
4. ```flowchart TD
    A([Start]) --> B[/Enter number of months/]
    B --> C[Initialize bills list]
    C --> D[/Enter electricity units/]
    D --> E{Units <= 100?}
    E -->|Yes| F[Bill = Units * 2]
    E -->|No| G{Units <= 200?}
    G -->|Yes| H[Bill = 200 + Remaining * 3]
    G -->|No| I[Bill = 500 + Remaining * 5]
    F --> J[Add fixed charge]
    H --> J
    I --> J
    J --> K[Add 5 percent surcharge]
    K --> L{Units < 50?}
    L -->|Yes| M[Apply 20 rupees rebate]
    L -->|No| N[Store bill]
    M --> N
    N --> O{More months?}
    O -->|Yes| D
    O -->|No| P[Display monthly bills]
    P --> Q[Compare consecutive bills]
    Q --> R{Increase greater than 20 percent?}
    R -->|Yes| S[Display unusual increase]
    R -->|No| T([Stop])
    S --> T```



5. Sample Input
Enter number of months: 3

Month 1
Enter units consumed: 80

Month 2
Enter units consumed: 120

Month 3
Enter units consumed: 250

6. Sample Output
Monthly Electricity Bills

Month 1 : 218.0
Month 2 : 438.0
Month 3 : 1212.5

Unusual increase in month 2
Unusual increase in month 3
