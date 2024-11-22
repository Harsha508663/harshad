import streamlit as st

st.title("2305a21L35-PS 6")
st.write("Calculate the Efficiency of the transformer and copper losses at various loads")

def Tran_Eff(va, cl, fcl, k, pf):
    # Efficiency formula
    eff = ((k * va * pf) * 100) / (k * va * pf + cl + (k**2) * fcl)
    
    # Copper losses formula
    cul = (k**2) * fcl
    
    return eff, cul

# Create two columns for input and output
col1, col2 = st.columns(2)

with col1:
    # Input fields for user to enter transformer parameters
    va = st.number_input("Rating of transformer (VA):", value=5000)
    cl = st.number_input("Core Losses (W):", value=50)
    fcl = st.number_input("Full Load Copper Losses (W):", value=100)
    k = st.number_input("Loading of transformer (0-1):", value=0.5)
    pf = st.number_input("Power Factor (0-1):", value=0.8)
    
    # Compute button to trigger calculations
    compute = st.button("Compute")

with col2:
    # Only display results after the 'compute' button is clicked
    if compute:
        # Call the Tran_Eff function to get efficiency and copper losses
        eff, cul = Tran_Eff(va, cl, fcl, k, pf)
        
        # Display the results
        st.write(f"Efficiency of Transformer: {eff:.2f} %")
        st.write(f"Copper Losses of Transformer: {cul:.2f} Watts")
