import streamlit as st

def calculate_mean(numbers):
    num_list = [float(num) for num in numbers.split(",")]
    mean = sum(num_list) / len(num_list)
    return mean

def main():
    st.title("Mean Calculator")
    n_input = st.text_input("Enter the X values with commas:")
    
    if n_input:
        mean = calculate_mean(n_input)
        st.write("MEAN:", mean)

    

if __name__ == "__main__":
    main()
