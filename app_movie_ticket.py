import streamlit as st

st.set_page_config(page_title="Movie Ticket Booking", layout="centered")

st.title("Movie Ticket Booking System")
st.markdown("---")

if 'booking_done' not in st.session_state:
    st.session_state.booking_done = False

st.subheader("Booking Details")

customer_name = st.text_input("Customer Name", placeholder="Enter your full name")

movie_title = st.selectbox("Movie Title", options=["Avengers", "Kung Fu Panda", "Frozen"])

show_time = st.selectbox("Show Time", options=["10:00 AM", "2:00 PM", "8:00 PM"])

seat_type = st.radio("Seat Type", options=["Standard", "Premium"])

if st.button("Book Ticket"):
    try:
        if not customer_name or customer_name.strip() == "":
            st.error("Error: Customer name cannot be empty! Please enter your name.")
        else:
            st.success("Ticket booked successfully!")
            
            st.subheader("Booking Information")
            
            col1, col2 = st.columns(2)
            with col1:
                st.write("**Customer Name:**")
                st.write("**Movie Title:**")
                st.write("**Show Time:**")
                st.write("**Seat Type:**")
            with col2:
                st.write(customer_name.strip())
                st.write(movie_title)
                st.write(show_time)
                st.write(seat_type)
            
            st.info("Thank you for booking!")
            st.session_state.booking_done = True
    
    except Exception as e:
        st.error(f"An unexpected error occurred: {str(e)}")

if st.session_state.booking_done:
    if st.button("New Booking"):
        st.session_state.booking_done = False
        st.rerun()

st.markdown("---")
st.caption("DFK50083 Practical Work 3 - Question 1")
