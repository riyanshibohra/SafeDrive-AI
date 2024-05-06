# Driver Distraction Detection Scripts

This directory contains all the essential scripts for developing and implementing the distracted driving detection system.

1. **cnn_model.ipynb**:
   - A Jupyter Notebook containing the deep learning model code. The CNN architecture is designed to detect distracted driving behavior and classify it into five distinct categories using Multi-cLass classification.

2. **route_optimization_ny.py**:
   - A Python script that provides accurate route optimization based on the driver's level of distraction. It uses Dijkstra's algorithm to suggest safer routes if the driver is distracted.

3. **predicate.py**:
   - This script contains predicate logic that assesses driver distraction levels and determines appropriate alerts. If the driver is classified as "safe driving," the script calls the route optimization algorithm.

4. **message_dict.txt**:
   - A text file containing a dictionary of classification categories and their corresponding alerts to notify the driver of their distraction status.

5. **state_dict.txt**:
   - A text file with a dictionary of the five possible driver states used as reference by the CNN model.

These scripts work together to classify driver behavior and provide actionable alerts to reduce distracted driving risks.
