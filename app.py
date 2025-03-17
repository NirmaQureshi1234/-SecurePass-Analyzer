# import streamlit as st
# from utils.password_analyzer import analyze_password

# # Custom CSS for dark theme
# def load_css():
#     with open("assets/styles.css") as f:
#         st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# # Main app
# def main():
#     # Load custom CSS
#     load_css()

#     # App title
#     st.markdown(
#         """
#         <div class="main-header">
#             🔐 Password Strength Meter
#         </div>
#         <div class="sub-header">
#             Check the strength of your password and get tips to improve it.
#         </div>
#         """,
#         unsafe_allow_html=True
#     )

#     # Password input
#     password = st.text_input("Enter your password:", type="password", key="password_input", help="Your password is never stored or transmitted.")

#     if password:
#         # Analyze password
#         result = analyze_password(password)

#         # Display strength
#         st.markdown(
#             f"""
#             <div class="result-section">
#                 <div class="strength-header">Password Strength</div>
#                 <div class="strength-result {result['strength'].lower()}">
#                     {result['strength']} Password
#                 </div>
#             </div>
#             """,
#             unsafe_allow_html=True
#         )

#         # Display feedback
#         if result["feedback"]:
#             st.markdown(
#                 """
#                 <div class="result-section">
#                     <div class="strength-header">Improvement Tips</div>
#                 </div>
#                 """,
#                 unsafe_allow_html=True
#             )
#             for tip in result["feedback"]:
#                 st.markdown(f"<div class='tip-item'>⚠️ {tip}</div>", unsafe_allow_html=True)

#         # Password strength meter (visual)
#         st.markdown(
#             """
#             <div class="result-section">
#                 <div class="strength-header">Strength Meter</div>
#             </div>
#             """,
#             unsafe_allow_html=True
#         )
#         strength_score = result["score"]
#         st.progress(strength_score / 5)

# # Run the app
# if __name__ == "__main__":
#     main()




 



import streamlit as st
from utils.password_analyzer import analyze_password

# Custom CSS for advanced black theme
def load_css():
    with open("assets/styles.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Main app
def main():
    # Load custom CSS
    load_css()

    # App title with animation
    st.markdown(
        """
        <div class="main-header">
            <span class="animated-text">🔐 Password Strength Meter</span>
        </div>
        <div class="sub-header">
            Check the strength of your password and get tips to improve it.
        </div>
        """,
        unsafe_allow_html=True
    )

    # Password input
    password = st.text_input("Enter your password:", type="password", key="password_input", help="Your password is never stored or transmitted.")

    if password:
        # Analyze password
        result = analyze_password(password)

        # Display strength with animation
        st.markdown(
            f"""
            <div class="result-section">
                <div class="strength-header">Password Strength</div>
                <div class="strength-result {result['strength'].lower()} animated-strength">
                    {result['strength']} Password
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

        # Display feedback
        if result["feedback"]:
            st.markdown(
                """
                <div class="result-section">
                    <div class="strength-header">Improvement Tips</div>
                </div>
                """,
                unsafe_allow_html=True
            )
            for tip in result["feedback"]:
                st.markdown(f"<div class='tip-item'>⚠️ {tip}</div>", unsafe_allow_html=True)

        # Password strength meter (visual)
        st.markdown(
            """
            <div class="result-section">
                <div class="strength-header">Strength Meter</div>
            </div>
            """,
            unsafe_allow_html=True
        )
        strength_score = result["score"]
        st.progress(strength_score / 5)

        # Add a fun animation for strong passwords
        if result["strength"] == "Strong":
            st.markdown(
                """
                <div class="celebration">
                    🎉 Your password is strong! Keep it safe!
                </div>
                """,
                unsafe_allow_html=True
            )

# Run the app
if __name__ == "__main__":
    main()