# Assignment 1 – Multiline Chart and Table Using D3.js

## Data: `data_sample.csv`

The `data_sample.csv` file contains data related to a supply chain. Your task is to create a **table** and a **multiline chart** using **D3.js**. Both the table and the chart should be displayed side by side in the same HTML file.

---

## Part 1: Table of Data (40 Points)

### Description
The data includes the following columns:
- **EstimatedCost**: Estimated cost provided by supply chain consultants (e.g., $1000 per ton).  
- **RawMaterial**, **Workmanship**, and **Storage**: Actual costs for these categories.  

### Calculations
Using JavaScript or Python, derive the following columns:
1. **ActualCost** = `RawMaterial + Workmanship + Storage`
2. **SoldPrice** = `EstimatedCost × 1.1`
3. **MarginOfProfit** = `SoldPrice - ActualCost`

### Final Table Columns
`Date`, `EstimatedCost`, `RawMaterial`, `Workmanship`, `Storage`, `ActualCost`, `SoldPrice`, `MarginOfProfit`

---

## Part 2: Multiline Chart (60 Points)

### Description
Create a **multiline chart** using **D3.js**. The chart should include four lines in one plot (SVG):
1. **EstimatedCost**  
2. **ActualCost**  
3. **SoldPrice**  
4. **MarginOfProfit**  

### Requirements
- Use `d3.scaleLinear()` and `d3.scaleTime()` for axes.  
- Parse the `Date` column into the correct date format.  
- Color the lines using:
  - `d3.scaleOrdinal(d3.schemeCategory10)` or  
  - Colors from **ColorBrewer**: [https://colorbrewer2.org/#type=qualitative&scheme=Paired&n=4](https://colorbrewer2.org/#type=qualitative&scheme=Paired&n=4)  
- Use **transitions** and **styling** to enhance the chart appearance.  
- Set the SVG dimensions to `viewBox(0 0 1000 800)`.  
