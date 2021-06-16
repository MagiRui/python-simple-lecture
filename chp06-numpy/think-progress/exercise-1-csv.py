#!/usr/bin/env python
# coding=utf-8

import csv

NY_RowS = ["\ufeffDateTime,NY - grid,NY - EV,NY - solar\n"]
Austin_RowS = ["\ufeffDateTime,Austin - grid,Austin - EV,Austin - solar\n"]
Boulder_Rows = ["\ufeffDateTime,Boulder - grid,Boulder - EV,Boulder - solar\n"]
with open('Grid, solar, and EV data from three homes.csv', 'r', encoding="utf-8") as file:

    fileLines = csv.DictReader(file)
    for line in fileLines:

        NY_Row_Data = line["\ufeffDateTime"] + "," +line["NY - grid"] + "," + line["NY - EV"] + "," + line["NY - solar"] + "\n"
        NY_RowS.append(NY_Row_Data)

        Austin_Row_Data = line["\ufeffDateTime"] + "," +line["Austin - grid"] + "," + line["Austin - EV"] + "," + line["Austin - solar"] + "\n"
        Austin_RowS.append(Austin_Row_Data)

        Boulder_Rows_Data = line["\ufeffDateTime"] + "," +line["Boulder - grid"] + "," + line["Boulder - EV"] + "," + line["Boulder - solar"] + "\n"
        Boulder_Rows.append(Boulder_Rows_Data)

    print(NY_RowS)
    print(Austin_RowS)
    print(Boulder_Rows)

with open('NY.csv', 'w', encoding="utf8") as file1:

    file1.writelines(NY_RowS)