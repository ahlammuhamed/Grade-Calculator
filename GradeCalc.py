import streamlit as st
import statistics

def app():

    st.markdown(
    """
     <style>
     
    .stApp {
        background-image: url("https://taylorinstitute.ucalgary.ca/sites/default/files/styles/ucws_hero_cta_large_desktop/public/2022-04/22-TAY-Consistent-Effective-Grading-Graphics-01.webp?itok=AscfM_uI");
        background-size: cover;
        background-repeat: no-repeat;
        background-position: center center;
        background-attachment: fixed;
        min-height: 100vh;
    }
    .block-container {
    margin-right: 40rem;
    padding-left: 2rem;
    text-align: left;
    margin-top: -4.7rem;
   
}
 .block-container * {
        font-size: 18px !important;
        color: brown;
    }
.center-output {
    text-align: center;
    margin-left: 200rem;
    font-size: 18px !important;
    color : #00826E;
}

    </style>
    """,
    unsafe_allow_html=True
)


    
    subjects = ['Arabic', 'English', 'Math']
    degrees = []

    st.title("Grade Calculator")

    for subject in subjects:
        degree = st.number_input(f"Enter your degree for {subject}:", min_value=0, max_value=100, step=1)
        degrees.append(degree)

    if st.button("Calculate"):
        fails = len([d for d in degrees if d < 50])
        if fails >= 2:
            st.markdown("<p class='center-output'>You are failed!</p>", unsafe_allow_html=True)
        else:
            avg = round(statistics.mean(degrees), 2)
            st.write(f"Your Average degrees: {avg}")
            for subject, degree in zip(subjects, degrees):
                if degree < 50:
                    grade = 'F'
                elif 50 <= degree <= 64:
                    grade = 'D'
                elif 65 <= degree <= 79:
                    grade = 'C'
                elif 80 <= degree <= 89:
                    grade = 'B'
                else:
                    grade = 'A'
                st.markdown(f"<p class='center-output'>Your grade in {subject} is {grade}</p>", unsafe_allow_html=True)


if __name__ == "__main__":
    app()
