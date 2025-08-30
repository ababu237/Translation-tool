import pandas as pd
from deep_translator import GoogleTranslator
import streamlit as st
from io import BytesIO

# Translating Tool


def translate_xlsx_with_deep_translator(df, target_languages):
    """
    Translates a DataFrame to multiple target languages using deep-translator.
    """
    translations = {}

    for target_language in target_languages:
        translator = GoogleTranslator(source='auto', target=target_language)
        translated_df = df.applymap(
            lambda x: translator.translate(str(x)) if pd.notnull(x) else "")
        translations[target_language] = translated_df

    return translations


def process_xlsx(file, target_languages):
    """
    Processes an Excel file, translates it, and outputs the translated data.
    """
    try:
        df = pd.read_excel(file)
    except Exception as e:
        st.error(f"Error processing file: {str(e)}")
        return None

    translations = translate_xlsx_with_deep_translator(df, target_languages)

    # Display and combine translations
    combined_translations = []
    for target_language, translated_df in translations.items():
        st.write(f"Translated File ({target_language.upper()})")
        st.dataframe(translated_df)

        # Combine original and translated data
        combined_df = pd.concat(
            [df.add_prefix('Original_'), translated_df.add_prefix(
                f'Translated_{target_language}_')],
            axis=1
        )
        combined_translations.append(combined_df)

    return combined_translations


def export_to_excel(combined_translations):
    """
    Exports the translated DataFrame to an Excel file.
    """
    output = BytesIO()
    with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
        for i, combined_df in enumerate(combined_translations):
            combined_df.to_excel(writer, index=False, sheet_name=f'File_{i+1}')
    output.seek(0)
    return output


# Streamlit App
st.title("Excel Translation Tool Using Deep Translator")
st.write("Upload an Excel file to translate its content into multiple languages.")

# File Upload
uploaded_file = st.file_uploader("Upload your Excel file", type=["xlsx"])

# Target Language Selection
target_languages = st.multiselect(
    "Select Target Languages",
    options=["de", "fr", "es", "it", "zh", "ja", "pl"],
    default=["de"]
)

if uploaded_file and target_languages:
    st.write("Processing the uploaded file...")
    combined_translations = process_xlsx(uploaded_file, target_languages)

    if combined_translations is not None:
        st.success("Translation completed!")

        # Export translated data as Excel file
        output_excel = export_to_excel(combined_translations)
        st.download_button(
            label="Download Translated Excel File",
            data=output_excel,
            file_name="Polish_translation_27_Aug.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
