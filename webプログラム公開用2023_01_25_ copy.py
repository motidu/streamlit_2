import datetime
import random

import streamlit as st


# データをテキストファイルに保存する
def save_variable_to_text_file(variable, file_name):
    # file_name のファイルを開く
    with open(file_name, "a", encoding="UTF-8") as f:
        f.write("\n")
        f.write(str(datetime.datetime.now()) + "\n")
        for j in range(len(variable)):
            f.write(variable[j])
            f.write("\n")
        f.close()


# タイトル
st.title("掃除当番アプリ")

# フォーム画面
with st.form(key="profile_form"):
    # セレクトボックス
    user_names: list = st.multiselect(
        "名前",
        (
            "利用者A",
            "利用者B",
            "利用者C",
            "利用者D",
            "利用者E",
            "利用者F",
            "利用者G",
            "利用者H",
            "利用者I",
            "利用者J",
            "利用者K",
            "利用者L",
            "利用者M",
            "利用者N",
            "利用者O",
            "利用者P",
            "利用者Q",
            "利用者R",
            "利用者S",
            "利用者T",
            "利用者U",
            "利用者V",
            "利用者W",
            "利用者X",
            "利用者Y",
            "利用者Z",
        ),
    )
    name_tc: list = st.multiselect(
        "職員名", ("職員a", "職員b", "職員c", "職員d", "職員e", "職員f")
    )

    user_names.extend(name_tc)
    name2: list = user_names
    number_of_left: int = len(user_names) - 7
    # リストの名前をシャッフル
    random.shuffle(name2)
    # 当番の辞書を作る max_value_dic =　{当番名：最大数}
    max_value_dic: dict = {
        "掃除機": 2,
        "ぞうきん": 4,
        "はたき": 1,
        "ごみ捨て(さらに支援員1人。必要ない場合は除菌)": 1,
        "みずやり:月曜(または除菌)": 1,
        "除菌": 1,
        "休み": number_of_left,
    }
    # 辞書の値から当番の最大数をリストへ格納
    max_value_list: list = list(max_value_dic.values())
    # 辞書のkeyから当番名をリストに入れる
    keys_list: list = list(max_value_dic.keys())

    # それぞれの初期値
    list2: list = []  # 最終的に入れるリスト
    i: int = 0  # for文で使う
    j: int = 0  # for文で使う
    separator: str = ", "  # 下のfor文内で名前のリストから要素を一つずつ取り出す時の分割の目印

    for n in max_value_list:
        # スライスでname のリストをmax_value_listごとに分け、新たなリストに入れる
        sub_list: list = user_names[i : i + n]
        # 当番名のリストから一つずつとりだしてdutynameに入れる
        dutyname: str = keys_list[j]
        second_list: str = dutyname + ":" + separator.join(map(str, sub_list))
        list2.append(second_list)
        i += n
        j += 1

    # ボタン部分
    submit_btn_1: bool = st.form_submit_button("送信")
    submit_btn_2: bool = st.form_submit_button("名前保存")
    cancel_btn: bool = st.form_submit_button("取り消し")

    # ボタンが押されたあとの表示
    if submit_btn_1:
        for i in range(len(list2)):
            st.write(f"### {list2[i]}")

        if st.session_state != 0:
            st.session_state.foo = list2
    if submit_btn_2:
        save_variable_to_text_file(name2, "今日の出席簿.txt")
        st.success("保存できました")
    if cancel_btn:
        st.session_state.foo = 0

# 注意書き表示
st.write(
    """
   ## ・職員や利用者の方が持ち込まれたPCには触らない。
   ## ・掃除の前には、なるべく机の上は整理し、かばんを椅子の上へ。
   ## ・個人が借りたPCの返却時は自分で除菌を行う。
"""
)
if st.button("名前保存"):
    save_variable_to_text_file(name2, "今日の出席簿.txt")
    st.success("保存できました")
if st.button("保存"):
    save_variable_to_text_file(st.session_state.foo, "掃除当番表.txt")
    st.success("保存できました")
    for i in range(len(st.session_state.foo)):
        st.write(f"### {st.session_state.foo[i]}")
