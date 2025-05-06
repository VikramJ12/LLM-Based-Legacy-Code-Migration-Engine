import streamlit as st
import subprocess
import os
import shutil
from pathlib import Path

EXAMPLES_DIR = Path("../examples")
PYTHON_DIR = Path("../src/python")

st.set_page_config(page_title="Legacy Code Migration Engine", layout="wide")
st.title("Legacy Code Migration Engine")

# File uploader
uploaded_file = st.file_uploader("Upload a C file:", type=["c"])

if uploaded_file:
    filename = uploaded_file.name
    c_file_path = EXAMPLES_DIR / filename
    py_file_path = c_file_path.with_suffix(".py")

    # Save uploaded file
    with open(c_file_path, "wb") as f:
        f.write(uploaded_file.read())

    st.success(f"Uploaded `{filename}` successfully.")

    if st.button("Convert to Python (OOP)"):
        with st.spinner("Running migration pipeline..."):

            # Run the backend pipeline
            result = subprocess.run(
                ["python", "run.py", str(c_file_path.resolve())],
                cwd=PYTHON_DIR,
                capture_output=True,
                text=True
            )

            if result.returncode != 0:
                st.error("❌ Conversion failed.")
                st.text(result.stderr)
            else:
                st.success("✅ Conversion completed!")

                # Show the AST graph
                graph_img_path = PYTHON_DIR / "code_graph.png"
                if graph_img_path.exists():
                    st.subheader("Abstract Syntax Tree:")
                    st.image(str(graph_img_path))

                # Show the Python code
                if py_file_path.exists():
                    col1, col2 = st.columns(2)

                    with col1:
                        st.subheader("Uploaded C Code:")
                        with open(c_file_path, "r") as f:
                            st.code(f.read(), language="c")

                    with col2:
                        st.subheader("Generated Python Code:")
                        with open(py_file_path, "r") as f:
                            st.code(f.read(), language="python")

                    # Offer download
                    with open(py_file_path, "rb") as py_file:
                        st.download_button(
                            label="Download Python File",
                            data=py_file,
                            file_name=py_file_path.name,
                            mime="text/x-python"
                        )
                else:
                    st.warning("⚠️ No Python output file found.")

