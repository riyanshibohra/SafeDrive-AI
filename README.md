<div align="center">
   
# SafeDrive-AI: Real-time Distracted Driving Detection with AI-powered Facial Analysis

Welcome to the SafeDriveAI project, an AI-powered system designed to enhance transportation safety by detecting distracted driving behavior in real time and providing tailored alerts to the driver.

<img width="700" alt="Screenshot 2025-02-23 at 4 58 15 PM" src="https://github.com/user-attachments/assets/7d49bf8d-adc8-467f-bb8b-3e9d61875001" />

</div>
## Project Objectives
1. **Develop and AI Model**: Implement a deep learning multi-class classification model to detect and classify distracted driving behaviors.
2. **Alert Drivers**: Generate personalized and tailored alerts based on distraction severity.
3. **Route Optimization**: Suggest safer routes if the driver is distracted.

## Components
1. **Data**:
   - The `data` directory contains categorized images of driver behaviors in five classes: `other_activities`, `texting_phone`, `talking_phone`, `turning`, and `safe_driving`.
   - Each class is crucial for training and testing the classification model.

2. **Scripts**:
   - **cnn_model.ipynb**: Contains the code for a Convolutional Neural Network (CNN) to classify driver distractions into five classes.
   - **route_optimization_ny.py**: A Python script that uses Dijkstra's algorithm to optimize routes based on distraction level.
   - **predicate.py**: Applies logical predicates to classify driver behavior and decide alerts and route changes.
   - **message_dict.txt**: Contains classification categories and the alerts associated with each.
   - **state_dict.txt**: Contains the five possible driver states.

## Methodology
1. **AI Model Framework**:
   - Developed a Convolutional Neural Network (CNN) using TensorFlow and Keras for real-time facial analysis and classification of driver behaviors.

2. **Data Processing**:
   - Trained the CNN on a diverse dataset featuring various driving behaviors to ensure accurate classification results.

3. **Alert System**:
   - Created a Python script that generates tailored safety alerts based on the AI model's classification results, seamlessly integrating with the vehicle’s onboard system.

4. **Dash Camera**:
   - Implemented algorithms to analyze live video feeds captured from dash cameras.

5. **Model Deployment**:
   - Deployed the trained model to the dash camera system for immediate analysis of live footage.

6. **User Interface**:
   - Designed a user-friendly display with bimodal feedback, ensuring alerts do not overly disturb the driver.

## Usage
1. **Training the CNN Model**:
   - Run `cnn_model.ipynb` to train the model using the data provided.
   - Save the trained model for use in distraction detection.

2. **Generating Alerts**:
   - The `predicate.py` script will analyze the driver's state and generate alerts based on the classification results.

3. **Optimizing Routes**:
   - Use `route_optimization_ny.py` to calculate optimal driving routes.

## Future Improvements
- Integration with external data sources for route optimization.
- Adding more nuanced classifications to the distracted driving categories.
- Incorporating additional sensors for broader safety coverage.
- **Incentive Program**: Develop a reward system to incentivize safe driving habits.

## Conclusion
Our deep learning model effectively classifies driver behavior into five categories, issuing tailored alerts that significantly enhance driver safety by mitigating risky behaviors in real time.

## References
- [NHTSA, Distracted Driving in 2022](https://crashstats.nhtsa.dot.gov/Api/Public/ViewPublication/813559)
- [Kaggle, Driver Behavior Dataset](https://www.kaggle.com/datasets/robinreni/revitsone-5class/data)
- Bridget, A. et al. (2017). "Effectiveness of Bimodal Versus Unimodal Alerts for Distracted Drivers," pp. 376-382. [DOI: 10.17077/DRIVINGASSESSMENT.1515](https://doi.org/10.17077/DRIVINGASSESSMENT.1515)

## Contributions
Contributions are welcome! Feel free to open an issue or submit a pull request.


