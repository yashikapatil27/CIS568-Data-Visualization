# Homework 3: Force Layout Visualization Using D3.js

## Overview
In this assignment, a **force layout visualization** was created to represent an author network using **D3.js**. The goal was to display nodes (authors) and links (shared publications) with interactive features such as hover and click events. The size of each node was determined by the number of connections (degree), and nodes were colored based on their affiliation country, with special treatment for the top 10 countries.

Key features implemented:
- **Force simulation** with nodes sized based on degree.
- **Interactive hover** to highlight authors with the same affiliation and reduce the opacity of others.
- **Click interaction** to display author information in a tooltip.
- **Dynamic adjustment** of force parameters (charge, collision, and link strength) using UI controls.

## Findings & Results
- **GIF Output**:  
  ![Force Layout Visualization Output](/Major-Assignment-3/MA3-gif.gif)

- **Key Insights**:
  - **Nodes and Affiliation**: Nodes were successfully colored according to their affiliation country, with top 10 countries highlighted in distinct colors.
  - **Node Size**: The node sizes accurately reflected the degree (number of shared publications) with a smooth transition.
  - **Interaction**: The hover effect made it easy to focus on authors with the same affiliation, and the tooltip provided clear information about each author when clicked.
  - **Force Parameters**: Adjusting parameters like **link strength** and **collision radius** allowed for visual exploration of the network’s structure, revealing clusters and outliers.
