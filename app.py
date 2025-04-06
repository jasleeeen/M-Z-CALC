import streamlit as st
from mzcal import calculate_mz
st.title("Peptide m/z Calculator")
st.write("Calculate the mass-to-charge (m/z) ratio of a peptide.")
sequence = st.text_input("Enter Peptide Sequence:", "PEPTIDE")
charge = st.number_input("Enter Charge State:", min_value=1, max_value=5, value=1, step=1)
if st.button("Calculate m/z"):
    mz_value = calculate_mz(sequence, charge)
    st.success(f"Mass-to-Charge Ratio (m/z): {mz_value:.5f}")