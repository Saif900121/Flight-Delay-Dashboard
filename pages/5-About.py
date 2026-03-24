
import streamlit as st

# Page configuration
st.set_page_config(page_title="About Me", page_icon="👤", layout="centered")

# Page title
st.title("👤 About Me")

# Display profile picture 
st.image("6.PNG" , width=200)

# introduction
st.markdown("""
Hi! I'm **Ahmed Saif**, a passionate Data Scientist and Python developer with a strong interest in flight data analysis and visualization.

---

### 🧑‍🎓 Background
- Bachelor's degree in Pharmaceutical Science.
- Certified Data Scientist Professional (CDSP) from Epsilon AI.
- Certified Data Analysis Professional (CDAP) from Epsilon AI.
- Experienced in data analysis, visualization, and deploying interactive dashboards using Streamlit .
- Experienced in Sales & Operations | Marketing | Medical Insurance | Pharmaceutical Industry.
---

### 🛠 Skills & Tools
- Python (Pandas, NumPy, Sklearn)  
- Data Visualization (Plotly, Seaborn, Matplotlib)  
- Dashboarding with Streamlit  
- Machine Learning basics & Data Preprocessing  
- GitHub for version control

---

### 📫 Contact Me
- **Email:** [drahmed.saif90@gmail.com](mailto:drahmed.saif90@gmail.com)  
- **LinkedIn:** [linkedin.com/in/ahmed-saif-1bb820192/](https://www.linkedin.com/in/ahmed-saif-1bb820192/)  
- **GitHub:** [github.com/Saif900121](https://github.com/Saif900121)

---

Thank you for visiting my project! Feel free to reach out for collaboration or questions.
""")

# foter
st.markdown("---")
st.markdown("""
<p style='text-align:center; font-size: 14px; color: #555;'>
    © 2025 | Developed by Ahmed Saif | 📧 <a href="mailto:drahmed.saif90@gmail.com">Contact Me</a>
</p>
""", unsafe_allow_html=True)
