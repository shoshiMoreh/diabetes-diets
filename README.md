# Diabetes Detection and Personalized Diet Recommendation

## Description
A full-stack project that combines **Machine Learning** with **Optimization** to help predict diabetes risk and provide a personalized diet plan.  

- Users register through the **Angular frontend** and input their medical data.  
- The system sends the data to a **Python backend** for processing:  
  - **Step 1:** A trained machine learning model predicts the probability of having diabetes.  
  - **Step 2:** If the probability is greater than 50%, the system triggers an optimization process using the **Simplex Algorithm** to generate a personalized diet plan.  
- Results (prediction & diet plan) are returned to the user in their personal dashboard.  
- Users can update their personal data at any time and review both their latest risk prediction and diet recommendations.  

---

## Technologies
| Component            | Technology |
|----------------------|------------|
| Frontend             | Angular (with personal dashboard & forms) |
| Backend (API)        | Python (Flask) |
| Machine Learning     |  TensorFlow |
| Optimization         | Simplex Algorithm (via `scipy.optimize.linprog`) |
| Data Processing      | Pandas, NumPy |
| Database             | MongoDB (NoSQL for user & medical data) |
| Database             | SQL Server / SQLite (for storing users & medical data) |
| Visualization        | Matplotlib, Seaborn |
| Architecture         | Full-stack (Angular + Python API) |

---

## Features
- **User Registration & Personal Area:**  
  - Input and update medical data (e.g., glucose, BMI, age).  
  - Secure login with personalized dashboard.  

- **Diabetes Prediction:**  
  - Machine learning model predicts the probability of diabetes.  
  - Displays clear results to the user in the dashboard.  

- **Personalized Diet Recommendation:**  
  - Triggered when prediction > 50%.  
  - Generated using the **Simplex Algorithm** for optimal nutrition balance.  
  - Results are tailored for diabetes prevention/management.  

- **User Dashboard (Angular):**  
  - View risk prediction.  
  - View and manage personal diet plan.  
  - Update data at any time to receive new predictions & recommendations.  

---

**Project Goal**

The project demonstrates how AI and optimization algorithms can be integrated into a real-world healthcare-oriented system.
It combines diabetes risk detection via ML with personalized diet planning using the Simplex algorithm, and presents it to users via a clean Angular interface.

This provides hands-on experience in:

Building a Full-Stack system (Angular + Python + MongoDB).

Applying Machine Learning models for medical prediction.

Using optimization techniques (Simplex) to generate personalized solutions.

Creating a personalized user experience with dashboards and real-time updates.
