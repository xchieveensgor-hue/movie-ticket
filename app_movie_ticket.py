"""
Movie Ticket Booking System
DFK50083: Python Programming - Practical Work 3
"""

import streamlit as st

def main():
    # Page configuration
    st.set_page_config(
        page_title="Movie Ticket Booking System",
        page_icon="🎬",
        layout="centered"
    )
    
    # Title and header
    st.title("🎬 Movie Ticket Booking System")
    st.markdown("---")
    
    # Initialize session state for booking confirmation
    if 'booking_made' not in st.session_state:
        st.session_state.booking_made = False
    
    # Create input fields using Streamlit widgets
    st.subheader("📝 Booking Details")
    
    # Customer Name input with text_input
    customer_name = st.text_input("Customer Name", placeholder="Enter your full name")
    
    # Movie Title selection with selectbox
    movie_title = st.selectbox(
        "Movie Title",
        options=["Avengers", "Kung Fu Panda", "Frozen"]
    )
    
    # Show Time selection with selectbox
    show_time = st.selectbox(
        "Show Time",
        options=["10:00 AM", "2:00 PM", "8:00 PM"]
    )
    
    # Seat Type selection with radio button
    seat_type = st.radio(
        "Seat Type",
        options=["Standard", "Premium"]
    )
    
    st.markdown("---")
    
    # Book Ticket button
    if st.button("🎟️ Book Ticket", type="primary"):
        # Exception handling block
        try:
            # Validate customer name (not empty)
            if not customer_name or customer_name.strip() == "":
                st.error("❌ Error: Customer name cannot be empty! Please enter your name.")
            else:
                # Display booking information
                st.success("✅ Ticket booked successfully!")
                
                st.subheader("📋 Booking Information")
                
                # Create a nice formatted display
                col1, col2 = st.columns(2)
                
                with col1:
                    st.write("**Customer Name:**")
                    st.write("**Movie Title:**")
                    st.write("**Show Time:**")
                    st.write("**Seat Type:**")
                
                with col2:
                    st.write(f"{customer_name.strip()}")
                    st.write(f"{movie_title}")
                    st.write(f"{show_time}")
                    st.write(f"{seat_type}")
                
                st.markdown("---")
                st.info("🎉 Thank you for booking with us! Enjoy your movie!")
                
                # Mark booking as made
                st.session_state.booking_made = True
                
        except Exception as e:
            # Handle unexpected errors
            st.error(f"❌ An unexpected error occurred: {str(e)}")
            st.info("Please try again or contact support if the problem persists.")
    
    # Reset button to clear booking
    if st.session_state.booking_made:
        if st.button("🔄 New Booking"):
            st.session_state.booking_made = False
            st.rerun()
    
    # Footer
    st.markdown("---")
    st.caption("© Movie Ticket Booking System | Streamlit GUI")

if __name__ == "__main__":
    main()