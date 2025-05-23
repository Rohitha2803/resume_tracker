# 📄 Rezoome - AI-Powered Resume Analyzer

Rezoome is an intelligent resume analysis tool built with Google's Gemini AI. It helps job seekers optimize their resumes by providing ATS compatibility scores, missing keywords, improvement suggestions, and a resume Q&A chatbot.

##  Features

-  ATS Score: Get a 0-100 score on how well your resume matches the job description
- **Missing Keywords**: Identify crucial keywords missing from your resume
-  **Improvement Suggestions**: Receive actionable bullet-point recommendations
-  **Resume Chatbot**: Ask specific questions about resume improvements
-  **PDF Support**: Direct PDF text extraction and analysis

## Installation steps

1. **Clone the repository**

       https://github.com/Rohitha2803/resume_tracker.git

3. **Install dependencies**

       pip install -r requirements.txt
   
3. **Set up environment**

       GOOGLE_API_KEY=your_api_key_here

 4. **Run the App**

        streamlit run app.py

## Usage
  
   1. Upload your resume (PDF only).

   2. Paste a job description from LinkedIn or a careers page.

   3. Click Analyze Resume to see:

       ATS Match Score

       Missing Keywords

       Resume Improvement Tips

   4. Ask questions about resume

## Requirements
    
  .streamlit

  .PyPDF2

  .python-dotenv

  .google-generativeai

## License
        
  This project is licensed under the MIT License

##  Project Structure

     ├── app.py               # Main Streamlit application
     ├── .env                 # API key file (ignored by Git)
     ├── requirements.txt     # Python dependencies
     └── README.md            # Project documentation

     
