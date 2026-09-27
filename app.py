import tempfile

import streamlit as st

from rag import create_vector_database, ask_question


# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="AI Research & Study Assistant",
    page_icon="🤖",
    layout="wide"
)


# --------------------------------------------------
# TITLE
# --------------------------------------------------

st.title("🤖 AI Research & Study Assistant")

st.write(
    "Upload a PDF and ask questions about it using RAG."
)


# --------------------------------------------------
# PDF UPLOAD
# --------------------------------------------------

uploaded_file = st.file_uploader(
    "📄 Upload your PDF",
    type=["pdf"]
)


if uploaded_file:

    # Save uploaded PDF temporarily
    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".pdf"
    ) as temp_file:

        temp_file.write(
            uploaded_file.getvalue()
        )

        pdf_path = temp_file.name


    # --------------------------------------------------
    # PROCESS PDF
    # --------------------------------------------------

    if st.button("Process PDF"):

        with st.spinner(
            "Processing PDF and creating embeddings..."
        ):

            try:

                vector_db = create_vector_database(
                    pdf_path
                )

                st.session_state["vector_db"] = vector_db

                st.success(
                    "✅ PDF processed successfully!"
                )

            except Exception as e:

                st.error(
                    f"Error processing PDF: {e}"
                )


# --------------------------------------------------
# QUESTION SECTION
# --------------------------------------------------

if "vector_db" in st.session_state:

    st.divider()

    st.header("💬 Ask a question")

    question = st.text_input(
        "What would you like to know about the document?"
    )


    # --------------------------------------------------
    # ASK QUESTION
    # --------------------------------------------------

    if st.button("Ask"):

        if not question:

            st.warning(
                "Please enter a question."
            )

        else:

            with st.spinner(
                "Searching the document and generating an answer..."
            ):

                try:

                    answer, sources = ask_question(
                        st.session_state["vector_db"],
                        question
                    )


                    # --------------------------------------------------
                    # ANSWER
                    # --------------------------------------------------

                    st.subheader("💡 Answer")

                    st.write(answer)


                    # --------------------------------------------------
                    # SOURCES
                    # --------------------------------------------------

                    st.subheader("📚 Sources")


                    for i, document in enumerate(
                        sources,
                        start=1
                    ):

                        page = document.metadata.get(
                            "page",
                            None
                        )


                        if page is not None:

                            page_number = page + 1

                        else:

                            page_number = "Unknown"


                        st.markdown(
                            f"**[{i}] 📄 Page {page_number}**"
                        )


                        preview = (
                            document.page_content[:500]
                        )


                        if len(
                            document.page_content
                        ) > 500:

                            preview += "..."


                        st.caption(
                            preview
                        )


                except Exception as e:

                    st.error(
                        f"Error answering question: {e}"
                    )