# **LLM - Invoice Extractor**

## Overview
This Streamlit app allows users to upload an image of an invoice and receive a response generated by a generative model. The model is trained to understand invoices and provide insights based on the uploaded image.

[![Streamlit App](https://img.shields.io/badge/Streamlit_App_-Invoice_Details_Extractor-ff69b4.svg?style=for-the-badge&logo=Streamlit)](https://llm-invoice-details-finder-sc5ctm3t7kepdd2g9cappdf.streamlit.app/)


## How to Use
1. Input Prompt: Enter your prompt or question related to the invoice.
2. Choose an image of the invoice: Upload an image file (JPEG, JPG, or PNG format) containing the invoice.
3. Click the "Tell Me about the Invoice" button to generate a response based on the input prompt and uploaded image.
4. View the generated response below the button.

## Installation
1. Clone this repository.
2. Install the required Python packages:
   ```
   pip install streamlit pillow generativeai
   ```
3. Run the Streamlit app:
   ```
   streamlit run app.py
   ```

## Dependencies
- Streamlit: Web application framework for Python.
- Pillow: Python Imaging Library for image processing.
- Google GenerativeAI: Library for accessing generative models.

## Configuration
1. Obtain an API key for the Google GenerativeAI service.
2. Set up the API key as a secret in Streamlit (if using Streamlit Sharing or a similar platform).
3. Configure the API key in the Streamlit app.

## Notes
- Ensure that the uploaded image file is clear and contains the invoice details prominently for accurate results.
- The response generated by the model may vary based on the input prompt and the content of the uploaded image.
- For best results, provide clear and specific input prompts related to the invoice.


## About the Author

This project was developed by Parthebhan Pari as a demonstration of Large Language Model (LLM) techniques using Streamlit.


## `Highlights:`

    1. This app uses the Gemini Pro visiion model from Google's GenerativeAI API to generate responses.
    2. Ensure that you have a stable internet connection to interact with the Gemini Pro model.
    3. For security reasons, make sure to handle and store your API key securely.



## 🔗 Connect with Me

Feel free to connect with me on :

[![portfolio](https://img.shields.io/badge/my_portfolio-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://parthebhan143.wixsite.com/datainsights)

[![LinkedIn Profile](https://img.shields.io/badge/LinkedIn_Profile-000?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/parthebhan)

[![Kaggle Profile](https://img.shields.io/badge/Kaggle_Profile-000?style=for-the-badge&logo=kaggle&logoColor=white)](https://www.kaggle.com/parthebhan)

[![Tableau Profile](https://img.shields.io/badge/Tableau_Profile-000?style=for-the-badge&logo=tableau&logoColor=white)](https://public.tableau.com/app/profile/parthebhan.pari/vizzes)



