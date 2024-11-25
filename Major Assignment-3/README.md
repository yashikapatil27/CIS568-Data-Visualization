# Major Assignment 3: Force Layout Visualization Using D3.js

## Requirements

### 1. Data Preparation
- **JSON File**: Prepare a json file for network visualization such that,
  - Nodes should represent **Authors**.  
  - Links should represent **shared publications**.  

### 2. Hue Channel
- Color the nodes based on **affiliation country**:
  - Use distinct colors for the **top 10 countries**.  
  - Assign the color `#A9A9A9` (gray) to all other countries.  

### 3. User Interface (UI)
- **Hover Interaction**:
  - On **mouse over**:  
    - Highlight only the authors with the same affiliation.  
    - Reduce the opacity of other nodes to `0.2`.  
  - On **mouse leave**:  
    - Restore the original visualization.  
- **Click Interaction**:
  - On **click**:  
    - Display the data for the selected author using a tooltip (e.g., author affiliation information in a tooltip `div`).

### 4. Force Layout Visualization
- **Force Simulation**:
  - Use **D3.js force simulation** to create a force layout visualization.  
  - Determine the size of each node based on its degree (number of connections):
    - Use a suitable **min-max scale** for the domain.
    - Apply `d3.scaleSqrt()` with a range of `[3, 12]` for node radius.  
- **Force Parameters**:
  - Apply a charge using `d3.forceManyBody()`.  
  - Set a collision radius using `d3.forceCollide()`:
    - Choose a reasonable radius range.  
  - Add UI controls for:
    - `forceManyBody` strength.  
    - `forceCollide` radius factor.  
    - Link strength.  

### 5. Web Page Creation
- **Visualization Web Page**:  
  - Create a web page on GitHub to host the visualization.  
  - Format the page using **Flexbox** or **Bootstrap** to organize the visualization and UI.  
- **Data Filtering**:  
  - Exclude records missing the following fields:  
    - Year  
    - Affiliation  
    - Author  

---

## Example References
- Utilize the provided examples as guidance for your implementation.

---