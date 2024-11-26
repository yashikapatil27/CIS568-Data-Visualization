# CIS568: Data-Visualization

This repository contains interactive data visualizations built using **D3.js**, developed as part of the course *CIS568: Data Visualization*. The assignments showcase key concepts in data representation, interactivity, and geospatial analysis. 

## Table of Contents  
1. [Assignment 1: Multiline Chart and Table](#assignment-1-multiline-chart-and-table)  
2. [Assignment 2: Geospatial Visualizations](#assignment-2-geospatial-visualizations)  
3. [Assignment 3: Force Layout Visualization](#assignment-3-force-layout-visualization)  
4. [Assignment 4: Contour Map Visualization](#assignment-4-contour-map-visualization)  

---

## Assignment 1: Multiline Chart and Table  
**Objective**: Visualize supply chain data using a table and multiline chart in a single HTML file.  

### Features:  
- **Table**: Displays calculated metrics (`ActualCost`, `SoldPrice`, `MarginOfProfit`) along with original data.  
- **Chart**: Plots `EstimatedCost`, `ActualCost`, `SoldPrice`, and `MarginOfProfit` over time using D3.js.  
- **Styling**: Transitions, color schemes (`d3.schemeCategory10` or ColorBrewer), and responsive layout.  

---

## Assignment 2: Geospatial Visualizations  
**Objective**: Visualize population data across Massachusetts counties using choropleth maps.  

### Features:  
1. **Map 1**: Population in 1980.  
2. **Map 2**: Population change (2010 vs. 2000).  
3. **Map 3**: Color-coded counties with hover interactions and tooltips.  
- **Interactivity**: Mouse hover highlights counties and displays data.  
- **Styling**: Clean layout with HTML and CSS.  

---

## Assignment 3: Force Layout Visualization  
**Objective**: Create an interactive author network visualization using a force-directed graph.  

### Features:  
- **Node Size**: Based on the number of connections.  
- **Node Color**: By affiliation country, with distinct colors for the top 10 countries.  
- **Interactivity**:  
  - **Hover**: Highlights authors from the same affiliation.  
  - **Click**: Displays author details in a tooltip.  
  - **Dynamic Controls**: Adjust force simulation parameters (e.g., link strength).  

---

## Assignment 4: Contour Map Visualization  
**Objective**: Visualize CT scan data with interactive contour maps.  

### Features:  
- **Dynamic Contours**: Update contours based on user-defined value ranges.  
- **Color Mapping**: Diverging color scale (`d3.interpolateRdBu`) for intensity representation.  
- **Interactivity**:  
  - Slider (`jQuery UI`) for range selection.  
  - Brush slider (`d3.brushX`) for focused exploration.  

---
