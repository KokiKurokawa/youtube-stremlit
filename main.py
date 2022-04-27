import streamlit as st
import time

st.title("Streamlit 超f入門")
st.write("Progress")

"Start!!"

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f"Itaration{i+1}")
    bar.progress(i+1)
    time.sleep(0.1)
"Done"

# df = pd.DataFrame(
#     np.random.rand(20, 3),
#     columns=["a", "b", "c"]
# )
# st.line_chart(df)
#
# df2 = pd.DataFrame(
#     np.random.rand(100, 2)/[50, 50]+[35.69, 139.70],
#     columns=["lat", "lon"]
#)
#st.map(df2)

st.write('Interactive widgets')

left_column, right_column = st.columns(2)
button = left_column.button("左")
if button:
    right_column.write("右")

expander = st.expander("問い合わせ")
expander.write("問い合わせ内容を書く")

# text = st.text_input("Your favorite Culture")
# condition = st.slider("調子は？", 0, 100, 50)
# option = st.selectbox(
#     "Your Like Number",
#     list(range(1, 11))
# # )
# "文化：",text
# "調子：", condition

# if st.checkbox("Show Image"):
#     img = Image.open("sample.JPG")
#     st.image(img, caption="壁紙", use_column_width=True)


